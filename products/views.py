from django.shortcuts import render, HttpResponse

# Create your views here.

# show product pages
def index(request):
    # return HttpResponse("Products")
    return render(request, "products/index_product.template.html")

# show only all exercise page
def show_exercise(request):
    return HttpResponse("Exercise")
    # return render(request, "products/index_product.template.html")
