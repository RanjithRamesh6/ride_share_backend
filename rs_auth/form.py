from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class login_form(UserCreationForm):
  email = forms.CharField(widget=forms.EmailField())
  password = forms.CharField(widget=forms.PasswordInput())
  confirmPassword = forms.CharField(widget=forms.PasswordInput())
  
  class Meta:
    model = User
    fields = ['email', 'password', 'confirmPassword']
