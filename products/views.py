from django.shortcuts import render
from .models import Product, GenderFilter


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def mens_products(request):
    category = GenderFilter.objects.filter(category="M")
    products = Product.objects.filter(person_category=category)
    return render(request, "products.html", {"products": products})


def womens_products(request):
    category = GenderFilter.objects.filter(category="W")
    products = Product.objects.filter(person_category=category)
    return render(request, "products.html", {"products": products})


def product_showcase(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product-showcase.html", {"product": product})
