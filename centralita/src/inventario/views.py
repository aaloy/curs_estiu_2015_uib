#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.shortcuts import render
from django.views.generic import ListView
from .models import Telefono, Virtual


class PrimariosListView(ListView):
    template_name = 'inventario/primario_list.html'
    model = Telefono

    def get_queryset(self):
        queryset = queryset = super(PrimariosListView, self).get_queryset()
        queryset = queryset.filter(es_primario=True)
        return queryset


class NumeroPrimarioListView(ListView):
    template_name = 'inventario/numero_primario_list.html'
    model = Telefono

    def get_queryset(self):
        queryset = super(NumeroPrimarioListView, self).get_queryset()
        queryset = queryset.filter(es_primario=False)
        queryset = queryset.filter(primario__numero=self.kwargs['numero'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NumeroPrimarioListView, self).get_context_data(**kwargs)
        primario = self.model.objects.get(numero=self.kwargs['numero'])
        context['primario'] = primario
        return context

class VirtualListView(ListView):
    template_name = 'inventario/virtual_list.html'
    model = Virtual

class TelefonoListView(ListView):
    template_name = 'inventario/telefono_list.html'
    model = Telefono
