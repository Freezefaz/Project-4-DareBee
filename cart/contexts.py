def cart_contents(request):
    # make cart content available on  all templates
    cart = request.session.get("shopping_cart", {})
    mealplan_cart = request.session.get("mealplan_shopping_cart", {})
    return {
        "cart": cart,
        "mealplan_cart": mealplan_cart,
        "number_of_items": int(len(cart) + len(mealplan_cart))
    }