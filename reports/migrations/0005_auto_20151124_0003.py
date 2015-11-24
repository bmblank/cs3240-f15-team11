# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_report_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='group_name',
            field=models.CharField(max_length=200, default='Public'),
        ),
    ]
