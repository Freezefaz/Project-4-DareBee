from django.test import TestCase

# Create your tests here.
class HomeTestViews(TestCase):
    def test_home_page(self):
        # simulate browswer going to URL
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
