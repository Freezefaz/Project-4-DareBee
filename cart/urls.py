from django.urls import path, re_path
import cart.views

urlpatterns = [
    path("", cart.views.view_cart, name="view_cart_route"),
    path("add/<exercise_id>", cart.views.add_to_exercise_cart,
         name="add_to_exercise_cart_route"),
    path("remove/<exercise_id>", cart.views.remove_from_exercise_cart,
         name="remove_from_exercise_cart_route"),
    path('update/quantity/exercise/<exercise_id>',
         cart.views.update_exercise_cart_quantity,
         name="update_exercise_cart_quantity_route"),
    path(r"^add/(?P<mealplan_id>[^/]+$", cart.views.add_to_mealplan_cart,
         name="add_to_mealplan_cart_route"),
    path(r"^remove/(?P<mealplan_id>[^/]+$",
         cart.views.remove_from_mealplan_cart,
         name="remove_from_mealplan_cart_route"),
]
