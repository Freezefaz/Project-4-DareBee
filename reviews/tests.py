from django.test import TestCase
from .models import ExerciseReview, MealplanReview
from products.models import Exercise, ExerciseType
from django.contrib.auth.models import User

# Create your tests here.


class ExerciseReviewTestView(TestCase):
    def test_exercise_review_page(self):
        # simulate going to products page
        response = self.client.get("/reviews/exercise/")
        # check if it goes to the exact page
        self.assertEqual(response.status_code, 200)
        # check if it goes to the template
        self.assertTemplateUsed(
            response, "reviews/show_exercise_reviews.template.html")

    # To create a dummy exercise type
    def setUp(self):
        self.exercise_type = ExerciseType(type="beginner")
        self.exercise_type.save()

    # def test_create_exercise_review_page(self):
    #     exercise = Exercise(title="Foundation", description="Easy",
    #                         price="20", exercise_type=self.exercise_type)
    #     response = self.client.get(f"/reviews/exercise/create/{exercise.id}")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response, "customers/create_exercise_review.template.html")
    
    # def test_update_exercise_review_page(self):
    #     exercise = Exercise(title="Foundation", description="Easy",
    #                         price="20", exercise_type=self.exercise_type)
    #     response = self.client.get(f"/reviews/exercise/update/{exercise.id}")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response, "customers/update_exercise_review.template.html")

