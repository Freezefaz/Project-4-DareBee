from django.urls import path
import reviews.views

urlpatterns = [
    path("exercise/", reviews.views.show_exercise_reviews,
         name="view_all_exercise_review_route"),
    path("exercise/create/<exercise_id>", reviews.views.create_exercise_review,
         name="create_exercise_review_route"),
    path("exercise/<exercise_id>/update/",
         reviews.views.update_exercise_review,
         name="update_exercise_review_route")
    # path("exercise/<exercise_id>/update/<exercise_review_id>",
    #      reviews.views.update_exercise_review,
    #      name="update_exercise_review_route")
]
