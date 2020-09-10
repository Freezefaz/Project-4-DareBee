from .forms import ExerciseForm
from .models import Exercise
from django.shortcuts import render, HttpResponse,redirect, reverse, get_object_or_404

# Create your views here.

# show product pages
def index(request):
    # return HttpResponse("Products")
    return render(request, "products/index_product.template.html")

# show only all exercise page
def show_exercise(request):
    # return HttpResponse("Exercise")
    all_exercises = Exercise.objects.all()
    return render(request, "products/show_exercise.template.html", {
        "all_exercises":all_exercises
    })

# create exercise
def create_exercise(request):
    if request.method == "POST":
        create_form = ExerciseForm(request.POST)
        # check if created form have valid values
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(show_exercise))
        else:
            # if does not have any valid values and re-render the form
            return render(request, "products/create_exercise.template.html", {
                "form": create_form
            })
    else:
        create_form = ExerciseForm()
        return render(request, "products/create_exercise.template.html", {
            "form": create_form
        })
    # return HttpResponse("Create Exercise")

def update_exercise(request, exercise_id):
    # return HttpResponse("Update Exercise")
    # retrieve book that we are updating
    exercise_to_update = get_object_or_404(Exercise, pk=exercise_id)
    # if update form is submitted
    if request.method == "POST":
        # create form and fill in data to existing form
        exercise_form = ExerciseForm(request.POST, instance=exercise_to_update)
        if exercise_form.is_valid():
            exercise_form.save()
            return redirect(reverse(show_exercise))
    else:
        # create form and fill it with data
        exercise_form = ExerciseForm(instance=exercise_to_update)
        return render(request, "products/update_exercise.template.html", {
            "form": exercise_form
        })


def delete_exercise(request, exercise_id):
    # return HttpResponse("Delete Exercise")
    book_to_delete = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == "POST":
        book_to_delete.delete()
        return redirect(show_exercise)
    else:
        return render(request, "products/delete_exercise.template.html", {
            "exercise": book_to_delete
        })
