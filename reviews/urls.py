from django.urls import path
import reviews.views

urlpatterns = [
    path("exercise/", reviews.views.show_exercise_reviews,
         name="view_all_exercise_review_route"),
    path("exercise/create/<exercise_id>", reviews.views.create_exercise_review,
         name="create_exercise_review_route"),
    # path("exercise/<exercise_id>/update/<exercisereview_id>",
    #      reviews.views.update_exercise_review,
    #      name="update_exercise_review_route"),
    path("exercise/update/<exercisereview_id>",
         reviews.views.update_exercise_review,
         name="update_exercise_review_route"),
    path("exercise/delete/<exercisereview_id",
         reviews.views.delete_exercise_review,
         name="delete_exercise_review_route"),
    path("mealplan/create/<mealplan_id>", reviews.views.create_mealplan_review,
         name="create_mealplan_review_route")
]
