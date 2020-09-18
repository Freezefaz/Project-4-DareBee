from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Exercise

# Create your views here.

def add_to_cart(request, exercise_id):
    cart = request.session.get("shopping_cart", {})
    # exercise = get_object_or_404(Exercise, pk=exercise_id)
    # check if book is not in the cart, then add
    if exercise_id not in cart:
        exercise = get_object_or_404(Exercise, pk=exercise_id)
        # book found add to cart
        cart[exercise_id] = {
            "id": exercise_id,
            "title": exercise.title,
            "price": "${:.2f}".format(int(exercise.price/100)),
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

def view_cart(request):
    # retrieve the cart
    cart = request.session.get("shopping_cart", {})
    return render(request, "cart/view_cart.template.html", {
        "cart": cart
    })


