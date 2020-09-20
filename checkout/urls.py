from django.urls import path

from .views import checkout, checkout_success, checkout_cancelled

urlpatterns = [
    path("", checkout, name="checkout_route"),
    path("success", checkout_success),
    path("cancelled", checkout_cancelled)
]