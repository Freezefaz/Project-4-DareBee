from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.
class UserModelTestCase(TestCase):

    def test_create_user_model(self):
        first_name = "John"
        last_name = "Doe"
        contact_number = "90009000"
        email = "jd@email.com"
        password = "jd1234"