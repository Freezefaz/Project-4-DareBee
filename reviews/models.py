from django.db import models
from products.models import Exercise, Mealplan

# Create your models here.


class ExerciseReview(models.Model):
    # columns in the table
    title = models.CharField(blank=False, max_length=255)
    content = models.CharField(blank=False, max_length=255)
    datetime = models.DateTimeField(auto_now=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    # to make string
    def __str__(self):
        return self.title


class MealplanReview(models.Model):
    # columns in the table
    title = models.CharField(blank=False, max_length=255)
    content = models.CharField(blank=False, max_length=255)
    datetime = models.DateTimeField(auto_now=False)
    mealplan = models.ForeignKey(Mealplan, on_delete=models.CASCADE)

    # to make string
    def __str__(self):
        return self.title
