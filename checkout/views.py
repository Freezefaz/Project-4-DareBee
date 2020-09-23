from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.conf import settings
import stripe
from products.models import Exercise
from django.contrib.auth.models import User
from .models import Purchase
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
import json
from uuid import UUID

# Create your views here.
class UUIDEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,UUID):
            return obj.hex
        return json.JSONEncoder.default(self,obj)

def checkout(request):
    # tell stripe what api key is
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # retrieve my shopping cart
    cart = request.session.get("shopping_cart", {})

    line_items = []
    all_exercise_ids = []

    # go through each line in cart
    for key, item in cart.items():
        # retrieve exercise by id
        exercise_model = get_object_or_404(Exercise, pk=item["id"])

        # create line item for stripe
        item = {
            "name": exercise_model.title,
            "amount": int(exercise_model.price * 100),
            "quantity": item["qty"],
            "currency": "sgd",
        }

        line_items.append(item)
        all_exercise_ids.append({
            "exercise_id": exercise_model.id,
            # "qty": item["qty"]
        })

    # get current website
    current_site = Site.objects.get_current()
    # get the domain name
    domain = current_site.domain

    # create a payment session for current transaction
    session = stripe.checkout.Session.create(
        # take credit cards
        payment_method_types=["card"],
        line_items=line_items,
        # customer id
        client_reference_id=request.user.id,
        mode='payment',
        success_url=domain + reverse("checkout_success_route"),
        cancel_url=domain + reverse("checkout_cancelled_route"),
        metadata={
            "all_exercise_ids": json.dumps(all_exercise_ids, cls=UUIDEncoder)
        }
    )
    print(session)
    # render the template which will redirect to stripe
    return render(request, "checkout/checkout.template.html", {
        'session_id': session.id,
        'public_key': settings.STRIPE_PUBLISHABLE_KEY
    })

def checkout_success(request):
    # empty the shopping cart
    # request.session['shopping_cart'] = {}
    return HttpResponse("Payment is successful")

def checkout_cancelled(request):
    return HttpResponse("Payment is cancelled")

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
    # print(session)
    customer = get_object_or_404(User, pk=session["client_reference_id"])
    print(customer)

    # change the metadata from string back to array
    
    # all_exercise_ids = session["metadata"]["all_exercise_ids"].split(",")
    all_exercise_ids = json.loads(session["metadata"]["all_exercise_ids"])
    print("hi")
    print(all_exercise_ids)
    for exercise in all_exercise_ids:
        exercise_model = get_object_or_404(Exercise, pk=exercise["exercise_id"])
        print(exercise_model)

    # go through each book id
    # for exercise_id in all_exercise_ids:
    #     exercise_model = get_object_or_404(Exercise, pk=exercise_id)

        # create the purchase model
        purchase = Purchase()
        purchase.exercise = exercise_model
        purchase.customer = customer
        purchase.save()
        print(purchase)

