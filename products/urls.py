from django.conf.urls import url, include
from .views import all_products, product_showcase

urlpatterns = [
    url(r'^all_products$', all_products, name='products'),
    url(r'^product_showcase/(?P<id>\d+)',
        product_showcase,
        name='product_showcase'),
]
