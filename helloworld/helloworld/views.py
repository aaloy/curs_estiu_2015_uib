#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.views.generic import TemplateView
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html', {"foo": "bar"})


class HelloWorld(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HelloWorld, self).get_context_data(**kwargs)
        context['foo'] = "bar"
        return context
