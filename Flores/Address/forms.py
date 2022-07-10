from django.forms import ModelForm
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'line1', 'line2', 'city', 'region', 'country', 'zip', 'reference'
        ]

        labels = {
            'line1': 'Dirección 1', 
            'line2': 'Dirección 2',
            'city': 'Ciudad',
            'region': 'Región', 
            'country': 'País',
            'zip': 'Codigo Postal',
            'reference': 'Referencias'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['line1'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['line2'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['city'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['region'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['country'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['zip'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '0000'
        })

        self.fields['reference'].widget.attrs.update({
            'class': 'form-control'
        })