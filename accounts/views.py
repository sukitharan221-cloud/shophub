from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ProfileUpdateForm, UserUpdateForm
from orders.models import Order


def register(request):
    """
    Handles new user sign-up.
    GET  -> show a blank registration form
    POST -> validate the submitted data; if valid, create the user,
            log them in immediately, and redirect to the home page.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the new user in automatically
            messages.success(request, f'Welcome to ShopHub, {user.username}! Your account was created.')
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """
    Shows and lets the user edit their profile details, and shows
    their past order history.
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'orders': orders,
    }
    return render(request, 'registration/profile.html', context)
