from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import User
from .models import UserProfile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
    
    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class EditUserForm(UserChangeForm):
    username = forms.CharField(max_length=20)
    
    class Meta:
       model = User
       fields = (
            'username',
            'password'
        )

class EditUserProfileForm(forms.ModelForm):
    description = forms.CharField(max_length=600, widget=forms.Textarea, required=False)
    experience = forms.CharField(max_length=600, widget=forms.Textarea, required=False)
    image = forms.ImageField()
    
    class Meta:
       model = UserProfile
       fields = (
            'description',
            'experience',
            'image'
        )
