from django.db import models
import products.choices as choices

BRAND_CHOICES = choices.BRAND_CHOICES
PRODUCT_CATEGORY_CHOICES = choices.PRODUCT_CATEGORY_CHOICES
PERSON_CATEGORY_CHOICES = choices.PERSON_CATEGORY_CHOICES
SIZE_CHOICES = choices.SIZE_CHOICES


# Create your models here.
class MainFilter(models.Model):
    category = models.CharField(max_length=3)

    def __str__(self):
        return self.category


class Product(models.Model):
    person_category = models.ForeignKey('MainFilter',
                                        blank=True,
                                        null=True,
                                        on_delete=models.SET_NULL)

    brand = models.CharField(max_length=6,
                             choices=BRAND_CHOICES,
                             default='LABONE')

    product_category = models.CharField(max_length=6,
                                        choices=PRODUCT_CATEGORY_CHOICES,
                                        default='JACPAR')

    title = models.CharField(max_length=100,
                             default='',
                             blank=False)

    description = models.TextField(blank=False)

    size = models.CharField(max_length=3,
                            choices=SIZE_CHOICES,
                            default='NA')

    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                blank=False)

    image = models.ImageField(upload_to='images')

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title
