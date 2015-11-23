# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20151101_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='group_name',
            field=models.CharField(max_length=200, default='public'),
        ),
    ]
