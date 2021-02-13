from django.urls import path
import customers.views

urlpatterns = [
    path("", customers.views.show_profiles,
         name="show_profiles_route"),
    path("create/", customers.views.create_profile,
         name="create_profile_route"),
    path("update/", customers.views.update_profile,
         name="update_profile_route"),
    path("delete/<profile_id>", customers.views.delete_profile,
         name="delete_profile_route"),
    path("view/", customers.views.view_user_profile,
         name="view_user_profile_route"),
]