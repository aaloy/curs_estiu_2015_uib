# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20150626_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saltos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orden', models.IntegerField(default=0)),
                ('telefono', models.ForeignKey(to='inventario.Telefono')),
            ],
        ),
    ]
