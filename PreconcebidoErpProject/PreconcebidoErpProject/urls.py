#!/usr/local/bin/python
# coding: utf-8

from django.contrib import admin
from django.conf.urls import include, url
from PreconcebidoErpProject import views as general_views

urlpatterns = [

    # Admin Urls
    url('admin/', admin.site.urls),

    # General Urls
    url(r'^$', general_views.home, name='home'),

    # Facturacion Views
    url(r'^facturacion/', include('facturacion.urls', namespace='facturacion')),

    # Contabilidad Views

    # Fiscalidad Views
]
