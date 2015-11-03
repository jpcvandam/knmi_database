# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knmi_database', '0002_meteodata'),
    ]

    operations = [
        migrations.AddField(
            model_name='meteodata',
            name='station',
            field=models.ForeignKey(blank=True, to='knmi_database.Station', null=True),
        ),
    ]
