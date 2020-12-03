from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=12)

    def clean(self):
        print("inside the clean")
