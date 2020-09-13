from django.urls import path
import customers.views

urlpatterns = [    
    path("", customers.views.show_profiles,
         name="show_profile_route"),
    path("create/", customers.views.create_profile,
         name="create_profile_route")

]