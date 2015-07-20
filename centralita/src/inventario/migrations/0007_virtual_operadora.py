# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_auto_20150626_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtual',
            name='operadora',
            field=models.ForeignKey(default=1, to='inventario.Operadora'),
            preserve_default=False,
        ),
    ]
