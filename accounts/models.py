from django.contrib.auth.models import User
from django.db import models


class BillingAddress(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=42)
    street_address_1 = models.CharField(max_length=32)
    street_address_2 = models.CharField(max_length=32)
    city = models.CharField(max_length=24)
    postcode = models.CharField(max_length=12)
    county = models.CharField(max_length=24)
    country = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=16)

    def __str__(self):
        return self.user.email
