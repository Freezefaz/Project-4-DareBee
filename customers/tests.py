from django.test import TestCase
from .models import Customer, Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestView(TestCase):
    def test_create_profile_page(self):
        response = self.client.get("/profiles/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "customers/create_profile.template.html")
