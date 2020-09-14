from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import ExerciseReview
from .forms import ExerciseReviewForm
from products.models import Exercise
# Create your views here.


def show_exercise_reviews(request):
    all_exercise_reviews = ExerciseReview.objects.all()
    print(all_exercise_reviews)
    return render(request, "reviews/show_exercise_reviews.template.html", {
        "all_exercise_reviews": all_exercise_reviews
    })


def create_exercise_review(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == "POST":
        form = ExerciseReviewForm(request.POST)
        if form.is_valid():
            review_model = form.save(commit=False)
            review_model.exercise = exercise
            review_model.customer = request.user
            review_model.save()
            return redirect(reverse("exercise_details_route", kwargs={"exercise_id": exercise_id}))
    else:
        form = ExerciseReviewForm()
        return render(request, 'reviews/create_exercise_review.template.html', {
            "form": form,
            "exercise": exercise
        })
