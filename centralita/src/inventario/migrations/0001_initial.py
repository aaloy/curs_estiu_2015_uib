# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(help_text='Tel\xe9fono, sin espacios, s\xf3lo n\xfameros', max_length=9)),
                ('descripcion', models.CharField(max_length=100, blank=True)),
                ('es_primario', models.BooleanField(default=False)),
                ('primario', models.ForeignKey(related_name='primarios', blank=True, to='inventario.Telefono', help_text='Si no es primario indica a qui\xe9n pertenece', null=True)),
            ],
            options={
                'verbose_name': 'Telefono',
                'verbose_name_plural': 'Tel\xe9fonos',
            },
        ),
    ]
