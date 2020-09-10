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
    return render(request, "products/show_exercise.template.html")

# create exercise
def create_exercise(request):
    if request.method == "POST":
        create_form = ExerciseForm(request.POST)
        # check if created form have valid values
        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
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
    return HttpResponse("Update Exercise")