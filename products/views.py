from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def product_showcase(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product-showcase.html", {"product": product})
