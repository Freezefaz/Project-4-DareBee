from django.urls import path
import products.views

urlpatterns = [
    path("", products.views.index, name="view_all_products")
]
