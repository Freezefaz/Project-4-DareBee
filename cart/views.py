from django.shortcuts import render, get_object_0r_404, redirect, reverse

# Create your views here.
def view_cart(request):
    # retrieve the cart
    cart  = request.session.get("shopping_cart", {})
    return render(request, "cart/view_cart.template.html", {
        "shopping_cart": cart
    })