from django.urls import path
import cart.views

urlpatterns = [
    path("", cart.views.view_cart, name="view_cart"),
    path("add/<exercise_id>", add_to_cart, name="add_to_cart")
]