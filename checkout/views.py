from django.shortcuts import render, HttpResponse, redirect, reverse, \
    get_object_or_404
from django.conf import settings
from products.models import Exercise, Mealplan
from customers.models import Customer
from .models import Exercise_Purchase, Mealplan_Purchase
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from uuid import UUID
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


#  create a unique id for each exercise in array
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)


@login_required
def checkout(request):
    # tell stripe what api key is
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # retrieve my shopping cart

    exercise_cart = request.session.get("shopping_cart", {})
    mealplan_cart = request.session.get("mealplan_shopping_cart", {})

    exercise_line_items = []
    all_exercise_ids = []

    mealplan_line_items = []
    all_mealplan_ids = []

    if exercise_cart is not None or mealplan_cart is not None:
        # go through each line in cart
        for key, exercise_item in exercise_cart.items():
            # retrieve exercise by id
            exercise_model = get_object_or_404(Exercise, pk=exercise_item["id"])

            # create line item for stripe
            exercise_item = {
                "name": exercise_model.title,
                "amount": int(exercise_model.price * 100),
                "quantity": exercise_item["qty"],
                "currency": "sgd",
            }

            exercise_line_items.append(exercise_item)
            all_exercise_ids.append({
                "exercise_id": exercise_model.id,
            })

        # go through each line in cart
        for key, mealplan_item in mealplan_cart.items():
            # retrieve exercise by id
            mealplan_model = get_object_or_404(Mealplan, pk=mealplan_item["id"])

            # create line item for stripe
            mealplan_item = {
                "name": mealplan_model.title,
                "amount": int(mealplan_model.price * 100),
                "quantity": 1,
                "currency": "sgd",
            }
            mealplan_line_items.append(mealplan_item)
            all_mealplan_ids.append({
                "mealplan_id": mealplan_model.id,
            })

        # get current website
        current_site = Site.objects.get_current()
        # get the domain name
        domain = current_site.domain

        all_line_items = exercise_line_items + mealplan_line_items
        # create a payment session for current transaction
        session = stripe.checkout.Session.create(
            # take credit cards
            payment_method_types=["card"],
            line_items=all_line_items,
            # customer id
            client_reference_id=request.user.id,
            mode='payment',
            success_url=domain + reverse("checkout_success_route"),
            cancel_url=domain + reverse("checkout_cancelled_route"),
            metadata={
                "all_exercise_ids": json.dumps(all_exercise_ids, cls=UUIDEncoder),
                "all_mealplan_ids": json.dumps(all_mealplan_ids)
            }
        )
        # render the template which will redirect to stripe
        return render(request, "checkout/checkout.template.html", {
            'session_id': session.id,
            'public_key': settings.STRIPE_PUBLISHABLE_KEY
        })
    else:
        return redirect(reverse("view_cart_route"))


@login_required
def checkout_success(request):
    # empty the shopping cart
    request.session['shopping_cart'] = {}
    request.session['mealplan_shopping_cart'] = {}
    messages.success(request, "Checkout Success!")
    return redirect(reverse('home_route'))


@login_required
def checkout_cancelled(request):
    messages.success(request, "Error in Checkout!")
    return redirect(reverse('home_route'))


@csrf_exempt
def payment_completed(request):
    # data send to us by stripe
    payload = request.body
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    # stripe gives a serial number and need to verify if this stripe
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    # to define event in try
    event = None
    # remember to get the endpoint secret
    # get the secret signature and paste on the settings.py
    # also on .env
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        return HttpResponse(status=400)

    if event["type"] == 'checkout.session.completed':
        session = event["data"]["object"]
        handle_payment(session)
    return HttpResponse(status=200)


def handle_payment(session):
    # get id from meta data to find the id
    customer = get_object_or_404(User, pk=session["client_reference_id"])
    all_exercise_ids = json.loads(session["metadata"]["all_exercise_ids"])
    for exercise in all_exercise_ids:
        exercise_model = get_object_or_404(
            Exercise, pk=exercise["exercise_id"])
        # create the purchase model
        exercise_purchase = Exercise_Purchase()
        exercise_purchase.exercise = exercise_model
        exercise_purchase.customer = customer
        exercise_purchase.price = exercise_model.price
        exercise_purchase.save()

    all_mealplan_ids = json.loads(session["metadata"]["all_mealplan_ids"])
    for mealplan in all_mealplan_ids:
        mealplan_model = get_object_or_404(
            Mealplan, pk=mealplan["mealplan_id"])
        # create the purchase model
        mealplan_purchase = Mealplan_Purchase()
        mealplan_purchase.mealplan = mealplan_model
        mealplan_purchase.customer = customer
        mealplan_purchase.price = mealplan_model.price
        mealplan_purchase.save()


def view_purchases(request):
    #  get all purchase from purchase model to display on purchase template
    exercise_purchase = Exercise_Purchase.objects.filter(customer=request.user)
    mealplan_purchase = Mealplan_Purchase.objects.filter(customer=request.user)
    return render(request, "checkout/user_purchases.template.html", {
        "exercise_purchase": exercise_purchase,
        "mealplan_purchase": mealplan_purchase
    })
