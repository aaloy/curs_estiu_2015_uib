#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.contrib import admin
from .models import Telefono, Operadora, Salto, Virtual



@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descripcion', 'es_primario', 'primario', 'operadora')
    search_fields = ('numero', 'descripcion', 'primario')
    list_filter = ('es_primario', 'primario', 'operadora')
    list_editable = ('descripcion',)

@admin.register(Operadora)
class OperadoraAdmin(admin.ModelAdmin):
    pass

class SaltoInline(admin.TabularInline):
    model = Salto

@admin.register(Virtual)
class VirtualAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descripcion', 'operadora')
    list_filter = ('operadora', )
    inlines = [SaltoInline, ]

