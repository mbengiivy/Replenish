from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    companyname = forms.CharField()
    category= forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2','companyname','category']