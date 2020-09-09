from django.contrib import admin
from .models import ExerciseType, Exercise, MealplanType, Mealplan

# Register your models here.
admin.site.register(ExerciseType)
admin.site.register(Exercise)
admin.site.register(MealplanType)
admin.site.register(Mealplan)
