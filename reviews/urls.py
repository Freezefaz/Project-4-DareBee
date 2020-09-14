from django.urls import path
import reviews.views

urlpatterns = [
    path("exercise/", reviews.views.show_exercise_reviews,
         name="view_all_exercise_review_route"),
    path("exercise/create/<exercise_id>", reviews.views.create_exercise_review,
         name="create_exercise_review_route")
]
