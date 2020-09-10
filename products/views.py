from django.shortcuts import render, HttpResponse
from .forms import ExerciseForm

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
    create_form = ExerciseForm()
    return render(request, "products/create_exercise.template.html", {
        "form": create_form
    })
    # return HttpResponse("Create Exercise")
