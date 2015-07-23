#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.views.generic import TemplateView, FormView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PagoForm
from .models import Apuesta

class GraciasView(TemplateView):
    template_name = 'paypay/gracias.html'


class DatosFormView(FormView):
    template_name = 'paypay/datos_form.html'
    form_class = PagoForm
    success_url = reverse_lazy('paypay-gracias')


class DatosMFormView(CreateView):
    model = Apuesta
    fields = ('nombre', 'juego', 'apuestas', 'fecha_juego')
    success_url = reverse_lazy('paypay-gracias')
    template_name = 'paypay/datos_form.html'
