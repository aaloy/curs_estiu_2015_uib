# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apuestas', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Apuesta',
                'verbose_name_plural': 'Apuestas',
            },
        ),
    ]
