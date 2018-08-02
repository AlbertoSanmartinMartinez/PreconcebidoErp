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

    # Urls
    url(r'^perfil/$', general_views.profile, name='profile'),
    url(r'^ayuda/$', general_views.help, name='help'),
    url(r'^perfil/$', general_views.profile, name='profile'),
    url(r'^configuracion/$', general_views.settings, name='settings'),
    url(r'^calendario/$', general_views.calendar, name='calendar'),
    url(r'^clientes/$', general_views.costumers, name='costumers'),
    url(r'^mensajes/$', general_views.messages, name='messages'),

    # Facturacion Views
    url(r'^facturacion/', include('facturacion.urls', namespace='facturacion')),
    # Contabilidad Views
    url(r'^contabilidad/', include('contabilidad.urls', namespace='contabilidad')),
    # Fiscalidad Views
    url(r'^fiscalidad/', include('fiscalidad.urls', namespace='fiscalidad')),
    # Laboral Views
    url(r'^laboral/', include('laboral.urls', namespace='laboral')),
    # Proyectos Views
    url(r'^proyectos/', include('proyectos.urls', namespace='proyectos')),
    # Marketing Views
    url(r'^marketing/', include('marketing.urls', namespace='marketing')),
]
