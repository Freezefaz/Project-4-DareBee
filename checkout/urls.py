from django.urls import path

from .views import checkout, checkout_success, checkout_cancelled

urlpatterns = [
    path("", checkout, name="checkout_route"),
    path("success", checkout_success, name="checkout_success_route"),
    path("cancelled", checkout_cancelled, name="checkout_cancelled_route")
]