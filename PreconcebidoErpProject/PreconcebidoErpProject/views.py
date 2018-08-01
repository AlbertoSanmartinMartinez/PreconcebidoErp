#!/usr/local/bin/python
# coding: utf-8

from django.shortcuts import render

# General views
def home(request):

    return render(request, 'home.html', {})
