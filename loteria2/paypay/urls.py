#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:
#
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'datos/$', views.DatosMFormView.as_view(), name="paypay-datos"),
    url(r'gracias/$', views.GraciasView.as_view(), name="paypay-gracias"),
]
