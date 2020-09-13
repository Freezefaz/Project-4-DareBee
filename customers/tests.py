from django.test import TestCase
from .models import Customer, Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestView(TestCase):
    def test_show_profile_page(self):
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "customers/show_profiles.template.html")

    def test_create_profile_page(self):
        response = self.client.get("/profiles/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "customers/create_profile.template.html")

    # To create a dummy user

    def setUp(self):
        self.customer = User(
            username="test", email="test@test.com", password="test123")
        self.customer.save()

    def test_update_profile_page(self):
        # to create a dummy profile to retrieve id
        profile = Profile(customer=self.customer, first_name="Herb",
                          last_name="Dean", dob="2020-10-09", height="182",
                          weight="60", goals="best")
        profile.save()
        response = self.client.get(f"/profiles/update/{profile.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "customers/update_profile.template.html")
