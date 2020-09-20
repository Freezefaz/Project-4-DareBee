def cart_contents(request):
    # make cart content available on  all templates
    cart = request.session.get("shopping_cart", {})
    return {
        "cart": cart,
        "number_of_items": len(cart)
    }