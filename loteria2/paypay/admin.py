#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.contrib import admin
from .models import Apuesta

class ApuestaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nombre', 'apuestas', 'fecha_juego')
    list_filter = ('fecha', 'fecha_juego')
    search_fields = ('nombre',)


admin.site.register(Apuesta, ApuestaAdmin)
