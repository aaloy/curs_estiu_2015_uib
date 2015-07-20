# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_saltos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'L\xednea de salto',
                'verbose_name_plural': 'L\xedneas de salto',
            },
        ),
        migrations.CreateModel(
            name='Virtual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(help_text='Tel\xe9fono, sin espacios, s\xf3lo n\xfameros', unique=True, max_length=9)),
                ('descripcion', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'verbose_name': 'Tel\xe9fono virtual',
                'verbose_name_plural': 'Tel\xe9fonos virtuales',
            },
        ),
        migrations.RemoveField(
            model_name='saltos',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='es_virtual',
        ),
        migrations.DeleteModel(
            name='Saltos',
        ),
        migrations.AddField(
            model_name='salto',
            name='telefono',
            field=models.ForeignKey(to='inventario.Telefono'),
        ),
        migrations.AddField(
            model_name='salto',
            name='virtual',
            field=models.ForeignKey(to='inventario.Virtual'),
        ),
    ]
