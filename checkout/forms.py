from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2041)]

    credit_card_number = forms.CharField(label='Credit card number',
                                         required=False)
    cvv = forms.CharField(label='Security code (CVV)',
                          required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month',
                                     choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year',
                                    choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name',
            'street_address_1',
            'street_address_2',
            'city',
            'postcode',
            'county',
            'country',
            'phone_number',
            )
