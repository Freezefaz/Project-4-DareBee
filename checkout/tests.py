from django.test import TestCase

# Create your tests here.
class TestCheckoutView(TestCase):
    def test_checkout_view_page(self):
        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "checkout/checkout.template.html"
        )