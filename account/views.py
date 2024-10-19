from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from .forms import LoginForm, RegistrationForm  # Ensure you import the RegistrationForm
from .models import User
from posts import *
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email_or_contact = form.cleaned_data['username_or_email_or_contact']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username_or_email_or_contact, password=password)

            if user is not None:
                if user.is_active:  # Check if the user is active
                    auth_login(request, user)
                    return redirect('posts:home')  # Redirect to your desired URL
                else:
                    messages.error(request, 'Your account is not active. Please contact an admin for approval.')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Set the user as inactive
            user.save()
            messages.success(request, 'Registration successful! Please wait for admin approval.')
            return redirect('account:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'account/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)  # Log the user out
    messages.success(request, 'You have been logged out successfully.')
    return redirect('account:login')  # Redirect to the login page after logout
