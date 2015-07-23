# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('paypay', '0002_apuesta_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta',
            name='fecha_juego',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 24, 3, 389511, tzinfo=utc), help_text='Cu\xe1ndo quiere jugar?'),
            preserve_default=False,
        ),
    ]
