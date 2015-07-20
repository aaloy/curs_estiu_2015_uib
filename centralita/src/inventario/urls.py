#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.conf.urls import include, url
from inventario import views

urlpatterns = [
    url(r'^$', views.TelefonoListView.as_view(), name="telefono-list"),
    url(r'^primarios/$', views.PrimariosListView.as_view(), name="primario-list"),
    url(r'^primario/(?P<numero>\w+)/$', views.NumeroPrimarioListView.as_view(), name="numero-primario-list"),
    url(r'^virtuales/$', views.VirtualListView.as_view(), name="virtual-list"),
]
