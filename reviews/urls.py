from django.urls import path
import reviews.views

urlpatterns = [
    path("exercise/create/<exercise_id>", reviews.views.create_exercise_review,
         name="create_exercise_review_route"),
    path("mealplan/create/<mealplan_id>", reviews.views.create_mealplan_review,
         name="create_mealplan_review_route"),

]
