#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django import forms


class PagoForm(forms.Form):
    nombre = forms.CharField(initial="su nombre")
    apuestas = forms.IntegerField(initial=1)



