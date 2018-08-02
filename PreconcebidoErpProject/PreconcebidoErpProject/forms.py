# coding: utf-8

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Login Form
class CustomLoginForm(AuthenticationForm):
    """
    """
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario o email', 'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))


# Register Form
class CustomRegisterForm(UserCreationForm):
    """
    """
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'}))
    email =  forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}))
    password1 = forms.CharField(required=True, help_text='8 carácteres mínimo', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'class': 'form-control'}))
    # help_text
    # error_message
    # validators
