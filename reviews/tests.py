from django.test import TestCase
from .models import ExerciseReview, MealplanReview
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
