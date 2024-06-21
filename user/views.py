from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account has been successfully created for {username}. Continue to log in')
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)

def profile(request):
    return render(request, 'user/profile.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'user/login.html', context)

def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'user_form':user_form,
        'profile_form':profile_form,
    }

    return render(request, 'user/profile_update.html', context)