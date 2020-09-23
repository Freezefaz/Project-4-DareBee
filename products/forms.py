from django import forms
from .models import Exercise, Mealplan


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ("type",)
    cover = CloudinaryJsFileField()


class MealplanForm(forms.ModelForm):
    class Meta:
        model = Mealplan
        exclude = ("type",)
