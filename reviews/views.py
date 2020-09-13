from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import ExerciseReview
# Create your views here.


def show_exercise_reviews(request):
    all_exercises_reviews = ExerciseReview.objects.all()
    return render(request, "reviews/show_exercise_reviews.template.html", {
        "all_exercises_reviews": all_exercises_reviews
    })
