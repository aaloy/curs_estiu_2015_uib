#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.contrib import admin
from .models import Apuesta, Juego

class ApuestaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nombre', 'juego', 'apuestas', 'fecha_juego')
    list_filter = ('fecha', 'fecha_juego', 'juego')
    search_fields = ('nombre',)

class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', "activo")
    list_editable = ('activo',)

admin.site.register(Apuesta, ApuestaAdmin)
admin.site.register(Juego, JuegoAdmin)
