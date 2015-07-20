# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20150626_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='es_virtual',
            field=models.BooleanField(default=False),
        ),
    ]
