#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.db import models


class Apuesta(models.Model):
    """Tabla para guardar las apuestas"""
    nombre = models.CharField(max_length=50)
    apuestas = models.IntegerField(default=1)
    fecha_juego = models.DateTimeField(help_text=u"Cuándo quiere jugar?")
    fecha = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = u"Apuesta"
        verbose_name_plural = u"Apuestas"
    
    def __unicode__(self):
        return self.nombre
