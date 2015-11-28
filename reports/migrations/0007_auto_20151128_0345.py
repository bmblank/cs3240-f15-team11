# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='sensitivity',
        ),
        migrations.AddField(
            model_name='report',
            name='Report_is_Public',
            field=models.BooleanField(default=True),
        ),
    ]
