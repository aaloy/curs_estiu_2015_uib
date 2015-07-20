#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:

from django.db import models
from django.core.exceptions import ValidationError

class Operadora(models.Model):
    """
    Operadores telefónicos. De momento guardamos
    únicamente el nombre
    """
    
    nombre = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nombre


class Telefono(models.Model):
    """Define el model de teléfono. Un teléfono puede
    ser a su vez un primario, lo que significa que es cabecera
    de varios teléfonos"""

    numero = models.CharField(max_length=9, unique=True,
                              help_text=u'Teléfono, sin espacios, sólo números')
    descripcion = models.CharField(max_length=100, blank=True) 
    
    operadora = models.ForeignKey(Operadora)
    es_primario = models.BooleanField(default=False)

    primario = models.ForeignKey("self", related_name='primarios', 
                                 limit_choices_to={'es_primario': True},
                                 blank=True, null=True,
                                 help_text=u"Si no es primario indica a quién pertenece")
    
    class Meta:
        verbose_name = u"Telefono"
        verbose_name_plural = u"Teléfonos"
    
    def __unicode__(self):
        return self.numero


    def clean(self):
        if self.es_primario and self.primario:
            raise ValidationError(u'Un número no puede ser primario y a la vez estar asociado a un primario')
    
class Virtual(models.Model):
    """
    Definición de un teléfono virtual.
    """
    numero = models.CharField(max_length=9, unique=True,
                              help_text=u'Teléfono, sin espacios, sólo números')
    descripcion = models.CharField(max_length=100, blank=True) 
    
    operadora = models.ForeignKey(Operadora)
    def __unicode__(self):
        return self.numero


    def saltos(self):
        return self.salto_set.all().order_by('orden')

    class Meta:
        verbose_name = u'Teléfono virtual'
        verbose_name_plural = u'Teléfonos virtuales'

class Salto(models.Model):
    """
    Líneas de salto pertenecientes a un teléfono
    virtual
    """
    virtual = models.ForeignKey(Virtual)
    orden = models.IntegerField(default=0)
    telefono = models.ForeignKey(Telefono,
                                 limit_choices_to={'es_primario': False},
                                 )
    #destino = models.ForeignKey(Telefono, related_name='telefono_destino')

    class Meta:
        verbose_name = u'Línea de salto'
        verbose_name_plural = u'Líneas de salto'
        unique_together = ('virtual', 'telefono')

    def __unicode__(self):
        return u"%s -> %s" % (self.virtual, self.telefono)
    #@models.permalink
    #def get_absolute_url(self):
    #    return ('view_or_url_name' )
