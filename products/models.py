from django.db import models

# Create your models here.


class ExerciseType(models.Model):
    # columns in the table
    type = models.CharField(blank=False, max_length=100)

    # to make string
    def __str__(self):
        return self.type


class Exercise(models.Model):
    # columns in the table
    title = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=False, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

    # to make string
    def __str__(self):
        return self.title
