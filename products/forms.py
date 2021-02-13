from django import forms
from .models import Exercise, Mealplan, ExerciseType, MealplanType
from cloudinary.forms import CloudinaryJsFileField


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ("type",)
    cover = CloudinaryJsFileField()


class MealplanForm(forms.ModelForm):
    class Meta:
        model = Mealplan
        exclude = ("type",)
    cover = CloudinaryJsFileField()


class Exercise_SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    exercise_type = forms.ModelChoiceField(
        queryset=ExerciseType.objects.all(), required=False
    )
    price = forms.CharField(max_length=100, required=False)


class Mealplan_SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    mealplan_type = forms.ModelChoiceField(
        queryset=MealplanType.objects.all(), required=False
    )
    price = forms.CharField(max_length=100, required=False)
