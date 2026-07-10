from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """The billing details form shown on the checkout page."""

    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'postal_code']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal code'}),
        }
