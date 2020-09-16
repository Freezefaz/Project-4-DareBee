from django.urls import path

urlpatterns = [
    path("/add/exercise/<exercise_id>", cart.views.add_exercise_to_cart,
    name="add_exercise_to_cart_route")
]