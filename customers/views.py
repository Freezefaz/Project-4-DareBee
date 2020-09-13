from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Customer, Profile
from .forms import ProfileForm

import products.views
# Create your views here.



def create_profile(request):
    # return HttpResponse("Your Profile")
        create_form = ProfileForm()
        return render(request, "customers/create_profile.template.html", {
            "form": create_form
        })

   