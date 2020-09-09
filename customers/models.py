from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    # columns in the table
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)
    password = models.CharField(blank=False, max_length=255)

    # make to string
    def __str__(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    # columns in the table
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=False)
    height = models.PositiveIntegerField(blank=False)
    weight = models.PositiveIntegerField(blank=False)
    goals = models.CharField(blank=False, max_length=255)

    # make to string
    def __str__(self):
        return self.customer

