from django.urls import path
import customers.views

urlpatterns = [    
    path("create/", customers.views.create_profile,
         name="create_profile_route")

]