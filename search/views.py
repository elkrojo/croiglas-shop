from django.shortcuts import render
from django.contrib import messages
from products.models import Product


# Create your views here.
def do_search(request):
    products = Product.objects.filter(title__icontains=request.GET['q'])
    if products:
        return render(request, "products.html", {"products": products})
    else:
        return render(request, "index.html")
