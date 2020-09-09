from django.db import models

# Create your models here.


class Customer(models.Model):
    # columns in the table
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.CharField(blank=False, max_length=255)
    password = models.CharField(blank=False, max_length=255)

    # make to string

    def __str__(self):
        return self.first_name + " " + self.last_name
