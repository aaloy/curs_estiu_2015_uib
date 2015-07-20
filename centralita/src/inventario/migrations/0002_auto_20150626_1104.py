# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='numero',
            field=models.CharField(help_text='Tel\xe9fono, sin espacios, s\xf3lo n\xfameros', unique=True, max_length=9),
        ),
    ]
