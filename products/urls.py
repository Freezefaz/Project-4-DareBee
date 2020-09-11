from django.urls import path
import products.views

urlpatterns = [
    path("", products.views.index, name="view_all_products"),
    path("exercise/", products.views.show_exercise, name="view_all_exercise"),
    path("exercise/create/", products.views.create_exercise,
         name="create_exercise"),
    #  it is _id NOT .id!!
    path("exercise/update/<exercise_id>", products.views.update_exercise,
         name="update_exercise_route"),
    path("exercise/delete/<exercise_id>", products.views.delete_exercise,
         name="delete_exercise_route"),
    path("mealplans/", products.views.show_mealplans,
         name="view_all_mealplans")

]
