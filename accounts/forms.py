from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={
        'class': 'validate form-control', 'name': 'username', 'placeholder': 'Username'
    }))

    password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'form-control', 'name': 'password', 'placeholder': 'Password'
    }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=PasswordInput(attrs={
        'class': 'validate form-control', 'name': 'old_password', 'placeholder': 'Old Password'
    }))

    new_password1 = forms.CharField(widget=PasswordInput(attrs={
        'class': 'validate form-control', 'name': 'new_password1', 'placeholder': 'New Password'
    }))

    new_password2 = forms.CharField(widget=PasswordInput(attrs={
        'class': 'validate form-control', 'name': 'new_password2', 'placeholder': 'Confirm Password'
    }))
