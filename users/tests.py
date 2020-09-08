from django.test import TestCase
from .models import User
from django.shortcuts import get_object_or_404

# Create your tests here.
class UserModelTestCase(TestCase):

    def test_create_user_model(self):
        u = User()
        u.first_name = "John"
        u.last_name = "Doe"
        u.contact_number = "90009000"
        u.email = "jd@email.com"
        u.password = "jd1234"
        # u.save()