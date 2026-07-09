from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    """A tiny form for choosing how many of a product to add to the cart."""
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, initial=1,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
