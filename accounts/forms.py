from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    """
    Extends Django's built-in UserCreationForm to also collect an email
    address. UserCreationForm already handles username + password +
    password confirmation + validation for us.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        # Add Bootstrap's 'form-control' class to every field so the
        # form looks styled when we render it with {{ field }} in the
        # template, without having to redefine every widget manually.
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    """Lets a logged-in user edit their extra profile details."""

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'avatar':
                field.widget.attrs.update({'class': 'form-control'})


class UserUpdateForm(forms.ModelForm):
    """Lets a logged-in user edit basic account info (name/email)."""

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
