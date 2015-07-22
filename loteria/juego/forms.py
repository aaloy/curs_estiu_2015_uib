#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django import forms

class PrimitivaForm(forms.Form):
    numero = forms.IntegerField(max_value=12, min_value=5,
                                label='Numeros:')
