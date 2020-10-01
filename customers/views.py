from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Customer, Profile
from django.contrib.auth.models import User
from .forms import ProfileForm
import products.views
# Create your views here.


def show_profiles(request):
    all_customers = User.objects.all()
    all_profiles = Profile.objects.all()
    return render(request, "customers/show_profiles.template.html", {
        "all_profiles": all_profiles,
        "all_customers": all_customers
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
            messages.success(request, "Your profile have been created!")
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


def update_profile(request, profile_id):
    profile_to_update = get_object_or_404(Profile, pk=profile_id)
    # if update form is submitted
    if request.method == "POST":
        # create form and fill in data to existing form
        profile_form = ProfileForm(request.POST, instance=profile_to_update)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Your profile have been updated!")
            return redirect(reverse(show_profiles))
    else:
        # create form and fill it with data
        profile_form = ProfileForm(instance=profile_to_update)
        return render(request, "customers/update_profile.template.html", {
            "form": profile_form
        })


def delete_profile(request, profile_id):
    # return HttpResponse("Delete Exercise")
    profile_to_delete = get_object_or_404(Profile, pk=profile_id)
    if request.method == "POST":
        messages.success(request, "Profile have been deleted!")
        profile_to_delete.delete()
        return redirect(show_profiles)
    else:
        return render(request, "customers/delete_profile.template.html", {
            "profile": profile_to_delete
        })

    # <h1>All Profiles</h1>
    #     <ul>
    #         {% for each_profile in all_profiles %}
    #         <li>
    #             {{each_profile.first_name}} {{each_profile.last_name}}
    #             <a href="{% url 'update_profile_route' profile_id=each_profile.id%}">Edit</a>
    #             <a href="{% url 'delete_profile_route' profile_id=each_profile.id%}">Delete</a>
    #         </li>
    #     </ul>
        # {% endfor %}
