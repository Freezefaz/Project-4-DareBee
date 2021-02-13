from django.test import TestCase

# Create your tests here.


class HomeTestViews(TestCase):
    def test_home_page(self):
        # simulate browswer going to URL
        response = self.client.get("/")
        # check if the it goes exactly to "/"
        self.assertEqual(response.status_code, 200)
        # check that it goes exactly to template
        self.assertTemplateUsed(response, "home/welcome.template.html")
