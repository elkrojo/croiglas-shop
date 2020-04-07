from django.db import models
import products.choices as choices

BRAND_CHOICES = choices.BRAND_CHOICES
PRODUCT_CATEGORY_CHOICES = choices.PRODUCT_CATEGORY_CHOICES
SIZE_CHOICES = choices.SIZE_CHOICES


# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=6,
                             choices=BRAND_CHOICES,
                             default='LABONE')

    category = models.CharField(max_length=7,
                                choices=PRODUCT_CATEGORY_CHOICES,
                                default='MJACPAR')

    title = models.CharField(max_length=100, blank=False)

    description = models.TextField(blank=False)

    size = models.CharField(max_length=3,
                            choices=SIZE_CHOICES,
                            default='NA')

    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                blank=False)

    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
