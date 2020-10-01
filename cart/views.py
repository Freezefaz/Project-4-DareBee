from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Exercise, Mealplan

# Create your views here.


def add_to_exercise_cart(request, exercise_id):
    cart = request.session.get("shopping_cart", {})
    # exercise = get_object_or_404(Exercise, pk=exercise_id)
    # check if exercise is not in the cart, then add
    if exercise_id not in cart:
        exercise = get_object_or_404(Exercise, pk=exercise_id)
        # exercise found add to cart
        cart[exercise_id] = {
            "id": exercise_id,
            "title": exercise.title,
            # "price": "${:.2f}".format(int(exercise.price/100)),
            "price": f"{exercise.price:.2f}",
            "qty": 1
        }
        # save the cart back to sessions
        request.session["shopping_cart"] = cart
        messages.success(request, f"{exercise.title} added to your cart!")
        # return redirect(reverse("view_all_exercise_route", kwargs={"exercise_id": exercise_id}))
        return redirect(reverse("view_all_exercise_route"))
    else:
        cart[exercise_id]["qty"] += 1
        request.session["shopping_cart"] = cart
        # return redirect(reverse("view_all_exercise_route", kwargs={"exercise_id": exercise_id}))
        return redirect(reverse("view_all_exercise_route"))

def add_to_mealplan_cart(request, mealplan_id):
    cart = request.session.get("mealplan_shopping_cart", {})
    if mealplan_id not in cart:
        mealplan = get_object_or_404(Mealplan, pk=mealplan_id)
        # book found add to cart
        cart[mealplan_id] = {
            "id": mealplan_id,
            "title": mealplan.title,
            "price": f"{mealplan.price:.2f}",
        }
        # save the cart back to sessions
        request.session["mealplan_shopping_cart"] = cart
        messages.success(request, f"{mealplan.title} added to your cart!")
        return redirect(reverse("view_all_mealplans_route"))
    else:
        messages.success(request, f"{mealplan.title} already added to your cart!")
        return redirect(reverse("view_all_mealplans_route"))


def view_cart(request):
    # retrieve the cart
    exercise_cart = request.session.get("shopping_cart", {})
    mealplan_cart = request.session.get("mealplan_shopping_cart", {})
    total = 0
    for key, item in exercise_cart.items():
        total += (float(item["price"]) * float(item["qty"]))
    for key, item in mealplan_cart.items():
        total += float(item["price"])

    return render(request, "cart/view_cart.template.html", {
        "cart": exercise_cart,
        "mealplan_cart": mealplan_cart,
        "total": f"{total:.2f}"
    })


def remove_from_exercise_cart(request, exercise_id):
    cart = request.session.get("shopping_cart", {})

    # if exercise is in cart
    if exercise_id in cart:
        # remove from cart
        del cart[exercise_id]
        # save back to the session
        request.session["shopping_cart"] = cart
        messages.success(request, "Exercise removed from cart successfully!")
        return redirect(reverse("view_all_exercise_route"))

def remove_from_mealplan_cart(request, mealplan_id):
    cart = request.session.get("mealplan_shopping_cart", {})

    # if exercise is in cart
    if mealplan_id in cart:
        # remove from cart
        del cart[mealplan_id]
        # save back to the session
        request.session["mealplan_shopping_cart"] = cart
        messages.success(request, "Mealplan removed from cart successfully!")
        return redirect(reverse("view_all_mealplans_route"))

def update_exercise_cart_quantity(request, exercise_id):
    cart = request.session.get("shopping_cart", {})
    quantity = request.POST["qty"]
    if exercise_id in cart:
        # cart[exercise_id]["qty"] = request.POST["qty"]
        cart[exercise_id]["qty"] = quantity
        print(quantity)
        messages.success(request, "Quantity has been updated!")

        # update the session
        request.session["shopping_cart"] = cart
    else:
        messages.success(request, "Failed to update")
    return redirect(reverse('view_cart_route'))
