# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_telefono_es_virtual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operadora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='telefono',
            name='operadora',
            field=models.ForeignKey(default=1, to='inventario.Operadora'),
            preserve_default=False,
        ),
    ]
