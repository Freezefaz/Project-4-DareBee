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
        # to save the user
        u.save()
        # test if can save by id
        # check if id is not zero
        self.assertTrue(u.id > 0)
        # get user base on model and the primary key
        saved_user = get_object_or_404(User, pk=u.id)
        # correct if the user exist
        self.assertTrue(saved_user is not None)
