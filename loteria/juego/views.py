#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PrimitivaForm

import random

class DadoView(TemplateView):
    template_name = "loteria/dado.html"

    def get_context_data(self, **kwargs):
        context = super(DadoView, self).get_context_data(**kwargs)
        numero = random.randint(1, 6)
        context['numero'] = numero
        return context

class PrimitivaFormView(FormView):
    """
    Solicita cuántos números de primitiva
    queremos
    """

    template_name = "loteria/primitiva_form.html"
    success_url = reverse_lazy("loteria-primitiva-list")
    form_class = PrimitivaForm

    def get_initial(self):
        initial = super(PrimitivaFormView, self).get_initial()        
        initial['numero'] = self.request.GET.get('numero', 6)
        return initial

class PrimitivaFormCleverView(PrimitivaFormView):
    def _genera_numeros(self, num=6):
        """Devuelve una lista de <num> de la tabla
        de números permitidos de la primitiva"""
        import random
        numeros = range(1, 50)
        random.shuffle(numeros)
        return numeros[:num]

    def form_valid(self, form):
        num = form.cleaned_data['numero']
        self.request.session['numeros'] = self._genera_numeros(num)
        return super(PrimitivaFormCleverView, self).form_valid(form)

class PrimitivaListView(TemplateView):
    template_name ="loteria/primitiva_list.html"

    def get_context_data(self, **kwargs):
        context = super(PrimitivaListView, self).get_context_data(**kwargs)
        try:
            numeros = self.request.session.get('numeros', [])
            numeros.sort()
            context['generados'] = len(numeros)
            context['numeros'] = numeros
            del self.request.session['numeros']
        except KeyError:
            context['error'] = 'Por favor vaya al formulario'
        return context
