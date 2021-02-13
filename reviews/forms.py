from django import forms
from .models import ExerciseReview, MealplanReview


class ExerciseReviewForm(forms.ModelForm):
    class Meta:
        model = ExerciseReview
        exclude = ('exercise', 'customer')


class MealplanReviewForm(forms.ModelForm):
    class Meta:
        model = MealplanReview
        exclude = ('mealplan', 'customer')
