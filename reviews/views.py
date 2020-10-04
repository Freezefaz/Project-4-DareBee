from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import ExerciseReview, MealplanReview
from .forms import ExerciseReviewForm, MealplanReviewForm
from products.models import Exercise, Mealplan
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def show_exercise_reviews(request):
    all_exercise_reviews = ExerciseReview.objects.all()
    print(all_exercise_reviews)
    return render(request, "reviews/show_exercise_reviews.template.html", {
        "all_exercise_reviews": all_exercise_reviews
    })


@login_required
def create_exercise_review(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == "POST":
        form = ExerciseReviewForm(request.POST)
        if form.is_valid():
            review_model = form.save(commit=False)
            review_model.exercise = exercise
            review_model.customer = request.user
            review_model.save()
            print(review_model)
            messages.success(request, "Your review has been created!")
            return redirect(reverse("exercise_details_route",
                                    kwargs={"exercise_id": exercise_id}))
    else:
        form = ExerciseReviewForm()
        return render(request,
                      "reviews/create_exercise_review.template.html", {
                          "form": form,
                          "exercise": exercise
                      })


def update_exercise_review(request, exercisereview_id):
    exercise_review_to_update = get_object_or_404(
        ExerciseReview, pk=exercisereview_id)
    if request.method == "POST":
        form = ExerciseReviewForm(request.POST,
                                  instance=exercise_review_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated!")
            return redirect(reverse("exercise_details_route",
                                    kwargs={"exercise_id":
                                            exercise_review_to_update.exercise.id, }))
    else:
        form = ExerciseReviewForm(instance=exercise_review_to_update)
        return render(request,
                      'reviews/update_exercise_review.template.html', {
                          "form": form,
                          "exercise": exercise_review_to_update
                      })


def delete_exercise_review(request, exercisereview_id):
    exercise_review_to_delete = get_object_or_404(
        ExerciseReview, pk=exercisereview_id)
    if request.method == "POST":
        messages.success(request, "Review have been deleted!")
        exercise_review_to_delete.delete()
        return redirect(reverse("exercise_details_route",
                                kwargs={
                                    "exercise_id": exercisereview_id.exercise.id,
                                    "exercisereview_id": exercisereview_id}))
    else:
        return render(request, "reviews/delete_exercise_review.template.html",
                      {
                          "exercisereview": exercise_review_to_delete,
                      })


@login_required
def create_mealplan_review(request, mealplan_id):
    mealplan = get_object_or_404(Mealplan, pk=mealplan_id)
    if request.method == "POST":
        form = MealplanReviewForm(request.POST)
        if form.is_valid():
            review_model = form.save(commit=False)
            review_model.mealplan = mealplan
            review_model.customer = request.user
            review_model.save()
            messages.success(request, "Your review has been created!")
            return redirect(reverse("mealplan_details_route",
                                    kwargs={"mealplan_id": mealplan_id}))
    else:
        form = MealplanReviewForm()
        return render(request,
                      "reviews/create_mealplan_review.template.html", {
                          "form": form,
                          "mealplan": mealplan
                      })


def update_mealplan_review(request, mealplanreview_id):
    mealplan_review_to_update = get_object_or_404(
        MealplanReview, pk=mealplanreview_id)
    if request.method == "POST":
        form = MealplanReviewForm(request.POST,
                                  instance=mealplan_review_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated!")
            return redirect(reverse("mealplan_details_route",
                                    kwargs={"mealplan_id":
                                            mealplan_review_to_update.mealplan.id}))
    else:
        form = MealplanReviewForm(instance=mealplan_review_to_update)
        return render(request,
                      'reviews/update_mealplan_review.template.html', {
                          "form": form,
                          "mealplan": mealplan_review_to_update
                      })


def delete_mealplan_review(request, mealplanreview_id):
    mealplan_review_to_delete = get_object_or_404(
        MealplanReview, pk=mealplanreview_id)
    if request.method == "POST":
        messages.success(request, "Review have been deleted!")
        mealplan_review_to_delete.delete()
        return redirect(reverse("mealplan_details_route",
                                kwargs={"mealplan_id": mealplan_review_to_delete.mealplan.id,
                                        "mealplanreview_id": mealplanreview_id}))
    else:
        return render(request, "reviews/delete_mealplan_review.template.html",
                      {
                          "mealplanreview": mealplan_review_to_delete
                      })
