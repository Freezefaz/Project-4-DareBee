from django.shortcuts import render
from .models import Customer, Profile
from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404

# Create your views here.


def create_profile(request):
    return HttpResponse("Your Profile")
