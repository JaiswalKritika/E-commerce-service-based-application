from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm,UsernameField ,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class MyPasswordResetForm(PasswordResetForm):
        email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control'}),
    )