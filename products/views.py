from .forms import ExerciseForm, MealplanForm
from .models import Exercise, Mealplan
from reviews.models import ExerciseReview
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages

# Create your views here.

# show product pages


def index(request):
    # return HttpResponse("Products")
    return render(request, "products/index_product.template.html")

# Start of Exercise
# show only all exercise page


def show_exercise(request):
    # return HttpResponse("Exercise")
    all_exercises = Exercise.objects.all()
    return render(request, "products/show_exercise.template.html", {
        "all_exercises": all_exercises
    })

# create exercise


def create_exercise(request):
    if request.method == "POST":
        create_form = ExerciseForm(request.POST)
        # check if created form have valid values
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"{create_form.cleaned_data['title']} has been created")
            return redirect(reverse(show_exercise))
        else:
            # if does not have any valid values and re-render the form
            messages.errors(request, f"{create_form.cleaned_data['title']} has not been created")
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
            messages.success(request, f"{exercise_form.cleaned_data['title']} has been updated")
            return redirect(reverse(show_exercise))
    else:
        # create form and fill it with data
        exercise_form = ExerciseForm(instance=exercise_to_update)
        return render(request, "products/update_exercise.template.html", {
            "form": exercise_form
        })


def delete_exercise(request, exercise_id):
    # return HttpResponse("Delete Exercise")
    exercise_to_delete = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == "POST":
        messages.success(request, f"{exercise_to_delete.title} has been deleted")
        exercise_to_delete.delete()
        return redirect(show_exercise)
    else:
        return render(request, "products/delete_exercise.template.html", {
            "exercise": exercise_to_delete
        })


def view_exercise_details(request, exercise_id):
    exercise_model = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, 'products/exercise_details.template.html', {
        "exercise": exercise_model
    })

# End of Exercise


# Start of Mealplans
# show all mealplans
def show_mealplans(request):
    # return HttpResponse("Mealplans")
    all_mealplans = Mealplan.objects.all()
    return render(request, "products/show_mealplans.template.html", {
        "all_mealplans": all_mealplans
    })

# create mealplan


def create_mealplan(request):
    # return HttpResponse("Create Mealplan")
    if request.method == "POST":
        create_form = MealplanForm(request.POST)
        # check if form have valid values
        if create_form.is_valid():
            create_form.save()
            messages.success(request, f"{create_form.cleaned_data['title']} has been created")
            return redirect(reverse(show_mealplans))
        else:
            # if no valid values, re-render form
            return render(request, "products/create_mealplan.template.html", {
                "form": create_form
            })
    else:
        create_form = MealplanForm()
        return render(request, "products/create_mealplan.template.html", {
            "form": create_form
        })

# update mealplan


def update_mealplan(request, mealplan_id):
    # return HttpResponse("Update Mealplan")
    mealplan_to_update = get_object_or_404(Mealplan, pk=mealplan_id)
    if request.method == "POST":
        mealplan_form = MealplanForm(request.POST, instance=mealplan_to_update)
        if mealplan_form.is_valid():
            mealplan_form.save()
            messages.success(request, f"{mealplan_form.cleaned_data['title']} has been updated")
            return redirect(reverse(show_mealplans))
        else:
            return render(request, "products/update_mealplan.template.html", {
                "form": mealplan_form
            })
    else:
        mealplan_form = MealplanForm(instance=mealplan_to_update)
        return render(request, "products/update_mealplan.template.html", {
            "form": mealplan_form
        })


def delete_mealplan(request, mealplan_id):
    # return HttpResponse("Delete")
    mealplan_to_delete = get_object_or_404(Mealplan, pk=mealplan_id)
    if request.method == "POST":
        messages.success(request, f"{mealplan_to_delete.title} has been deleted")
        mealplan_to_delete.delete()
        return redirect(show_mealplans)
    else:
        return render(request, "products/delete_mealplan.template.html", {
            "mealplan": mealplan_to_delete
        })


def view_mealplan_details(request, mealplan_id):
    mealplan_model = get_object_or_404(Mealplan, pk=mealplan_id)
    return render(request, 'products/mealplan_details.template.html', {
        "mealplan": mealplan_model
    })
