from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        exclude = ("type",)
