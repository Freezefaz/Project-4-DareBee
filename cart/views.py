from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404

# Create your views here.
def view_cart(request):
    # retrieve the cart
    cart  = request.session.get("shopping_cart", {})
    return render(request, "cart/view_cart.template.html", {
        "shopping_cart": cart
    })