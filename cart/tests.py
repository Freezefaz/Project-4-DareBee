from django.test import TestCase
from products.models import Exercise, ExerciseType

# Create your tests here.

class TestCartView(TestCase):
    def setUp(self):
        self.exercise_type = ExerciseType(type="beginner")
        self.exercise_type.save()
        # self.exercise = Exercise(title="Foundation", description="Easy",
        #                     price="20", exercise_type=self.exercise_type)
        # self.exercise.save()
    
    def test_cart_view_page(self):
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "cart/view_cart.template.html"
        )

    def test_add_to_cart_page(self):
        exercise = Exercise(title="Foundation", description="Easy",
                            price="20", exercise_type=self.exercise_type)
        exercise.save()
        response = self.client.get(f"/cart/add/{exercise.id}")
        self.assertEqual(response.status_code, 200)
        self.client.session.get("shopping_cart")
        for k, e in session.items():
            exercise_added = e
        self.assertEqual(exercise_added["id"], str(exercise.id))
        self.assertEqaual(exercise_added["title"], str(exercise.title))
        self.assertEqual(exercise_added["description"], str(exercise.description))
        self.assertEqual(exercise_added["price"], '${:.2f}'.format(int(exercise.price/100)))
        self.assertEqual(exercise_added["exercise_type"], str(exercise.exercise_type))

        # self.assertTemplateUsed(
        #     response, "cart/add_to_cart.template.html")
