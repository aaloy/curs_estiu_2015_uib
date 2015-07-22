#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:
#
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dado/$', views.DadoView.as_view(), name="juego-dado"),
    url(r'primitiva/$', views.PrimitivaFormCleverView.as_view(), name="loteria-primitiva"),
    url(r'primitiva-list/$', views.PrimitivaListView.as_view(), name="loteria-primitiva-list"),
]
