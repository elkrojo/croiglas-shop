from django.conf.urls import url, include
from .views import (all_products,
                    mens_products,
                    womens_products,
                    product_showcase
                    )

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^men', mens_products, name='mens_products'),
    url(r'^women', womens_products, name='womens_products'),
    url(r'^product_showcase/(?P<id>\d+)',
        product_showcase,
        name='product_showcase'),
]
