#!/usr/local/bin/python
# coding: utf-8

from django.contrib import admin
from django.conf.urls import include, url
from PreconcebidoErpProject import views as general_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Admin Urls
    url('administracion/', admin.site.urls),

    # General Urls
    url(r'^$', general_views.home, name='home'),

    # Log in/out and register Urls
    url(r'^acceso/$', general_views.custom_login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^registro/$', general_views.custom_register, name='register'),

    # Facturacion Views
    url(r'^facturacion/', include('facturacion.urls', namespace='facturacion')),

    # Contabilidad Views
    url(r'^contabilidad/', include('contabilidad.urls', namespace='contabilidad')),

    # Fiscalidad Views
    url(r'^fiscalidad/', include('fiscalidad.urls', namespace='fiscalidad')),

    # Fiscalidad Views
    url(r'^laboral/', include('laboral.urls', namespace='laboral')),

    # Fiscalidad Views
    # url(r'^tesoreria/', include('tesoreria.urls', namespace='tesoreria')),

    # Fiscalidad Views
    url(r'^proyectos/', include('proyectos.urls', namespace='proyectos')),

    # Fiscalidad Views
    url(r'^marketing/', include('marketing.urls', namespace='marketing')),
]
