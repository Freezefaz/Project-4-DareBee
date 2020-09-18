from django.urls import path
import cart.views

urlpatterns = [
    path("", cart.views.view_cart, name="view_cart_route"),
    path("add/<exercise_id>", cart.views.add_to_cart, name="add_to_cart_route"),
]