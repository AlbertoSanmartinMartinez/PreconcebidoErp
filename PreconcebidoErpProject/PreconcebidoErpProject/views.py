#!/usr/local/bin/python
# coding: utf-8

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from PreconcebidoErpProject import forms as general_forms

# General views
@login_required(redirect_field_name='login')
def home(request):
    """
    """

    return render(request, 'home.html', {})


def custom_login(request):
    """
    custom login view
    """
    if request.method == 'POST':
        custom_login_form = general_forms.CustomLoginForm(data=request.POST)
        if custom_login_form.is_valid():
            data = custom_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')

    else:
        custom_login_form = general_forms.CustomLoginForm()

    return render(request, 'custom_login.html', {
        'custom_login_form': custom_login_form,
    })



def custom_register(request):
    """
    custom register view
    """

    if request.method == 'POST':
        custom_register_form = general_forms.CustomRegisterForm(data=request.POST)
        if custom_register_form.is_valid():
            custom_register_form.save()
            return redirect('home')
    else:
        custom_register_form = general_forms.CustomRegisterForm()

    return render(request, 'custom_register.html', {
        'custom_register_form': custom_register_form,
    })


@login_required(redirect_field_name='login')
def profile(request):
    """
    """

    return render(request, 'profile.html', {})


@login_required(redirect_field_name='login')
def help(request):
    """
    """

    return render(request, 'help.html', {})


@login_required(redirect_field_name='login')
def calendar(request):
    """
    """

    return render(request, 'calendar.html', {})


@login_required(redirect_field_name='login')
def settings(request):
    """
    """

    return render(request, 'settings.html', {})


@login_required(redirect_field_name='login')
def costumers(request):
    """
    """

    return render(request, 'costumers.html', {})


@login_required(redirect_field_name='login')
def messages(request):
    """
    """

    return render(request, 'messages.html', {})





# Common Functions
