from django.db import models
from products.models import Exercise, Mealplan
from django.contrib.auth.models import User

# Create your models here.

class Exercise_Purchase(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return f"Purchase made for id:{self.exercise.id} by {self.customer.username} on {self.purchase_date}"

# class Mealplan_Purchase(models.Model):
#     mealplan = models.ForeignKey(mealplan, on_delete=models.CASCADE)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     purchase_date = models.DateTimeField(auto_now=True)
#     quantity = models.PositiveIntegerField(blank=Fa)

#     def __str__(self):
#         return f"Purchase made for id:{self.exercise.id} by {self.customer.username} on {self.purchase_date}"
