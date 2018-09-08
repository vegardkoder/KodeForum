from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import RegisterUserForm, EditUserForm, EditUserProfileForm

def index(request):

    if(request.user.is_authenticated):
        return redirect('profile')
    
    return render(request, 'personal/start.html')

def register(request):
    if(request.method == "POST"):
        form = RegisterUserForm(request.POST)

        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterUserForm()
        
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def profile(request):
    return render(request, 'personal/profile.html')

def LogoutView(request):
    logout(request)
    return redirect('index')

def Rules(request):
    return render(request, 'personal/rules.html')

def edit_profile(request):
    if(request.method == "POST"):
        UserForm = EditUserForm(request.POST, instance=request.user)
        UserProfileForm = EditUserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if(UserForm.is_valid() and UserProfileForm.is_valid()):
            UserForm.save()
            UserProfileForm.save()
            
            return redirect('profile')
    else:
        UserForm = EditUserForm(instance=request.user)
        UserProfileForm = EditUserProfileForm(instance=request.user.userprofile)

    return render(request, 'personal/edit_profile.html', {
        'UserForm' : UserForm,
        'UserProfileForm' : UserProfileForm
    })
