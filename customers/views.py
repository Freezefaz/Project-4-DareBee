from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Customer, Profile
from django.contrib.auth.models import User
from .forms import ProfileForm

import products.views
# Create your views here.

def show_profiles(request):
    all_profiles = Profile.objects.all()
    return render(request, "customers/show_profiles.template.html", {
        "all_profiles": all_profiles
    })


def create_profile(request):
    # return HttpResponse("Your Profile")
    if request.method == "POST":
        create_form = ProfileForm(request.POST)
        # check if created form have valid values
        if create_form.is_valid():
            profile_model = create_form.save(commit=False)
            profile_model.customer = request.user
            profile_model.save()
            return redirect(reverse(show_profiles))
        else:
            # if does not have any valid values and re-render the form
            return render(request, "customers/create_profile.template.html", {
                "form": create_form
            })
    else:
        create_form = ProfileForm()
        return render(request, "customers/create_profile.template.html", {
            "form": create_form
        })

   