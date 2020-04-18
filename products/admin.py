from django.contrib import admin
from .models import Product, GenderFilter


# Register your models here.
admin.site.register(Product)
admin.site.register(GenderFilter)
