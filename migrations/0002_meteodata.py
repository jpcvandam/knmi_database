# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knmi_database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeteoData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nummer', models.IntegerField()),
                ('datum', models.DateTimeField()),
                ('rh', models.IntegerField()),
                ('ev24', models.IntegerField()),
            ],
        ),
    ]
