from django.test import TestCase

# for testing cases
# 1st test will fail as no write up
# Commit first
# Then go settings.py to add url
# then go urls to add path


# Create your tests here.
class ProductsTestView(TestCase):
    def test_products_page(self):
        # simulate going to products page
        response = self.client.get("/products/")
        # check if it goes to the exact page
        self.assertEqual(response.status_code, 200)
        # check if it goes to the template
        self.assertTemplateUsed(
            response, "products/index_product.template.html")


class ExerciseTestView(TestCase):
    def test_exercise_page(self):
        response = self.client.get("/products/exercise/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "products/show_exercise.template.html")

    def test_create_exercise_page(self):
        response = self.client.get("products/exercise/create/")
        self.assertEqual(response.status_code, 200)
