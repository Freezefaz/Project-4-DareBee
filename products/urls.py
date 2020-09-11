from django.urls import path
import products.views

urlpatterns = [
    path("", products.views.index, name="view_all_products"),
    path("exercise/", products.views.show_exercise, name="view_all_exercise"),
    path("exercise/create/", products.views.create_exercise,
         name="create_exercise_route"),
    #  it is _id NOT .id!!
    path("exercise/update/<exercise_id>", products.views.update_exercise,
         name="update_exercise_route"),
    path("exercise/delete/<exercise_id>", products.views.delete_exercise,
         name="delete_exercise_route"),
    path("mealplans/", products.views.show_mealplans,
         name="view_all_mealplans_route"),
    path("mealplans/create/", products.views.create_mealplan,
         name="create_mealplan_route"),
    path("mealplans/update/<mealplan_id>", products.views.update_mealplan,
         name="update_mealplan_route"),
    path("mealplans/delete/<mealplan_id>", products.views.delete_mealplan,
         name="delete_mealplan_route")

]
