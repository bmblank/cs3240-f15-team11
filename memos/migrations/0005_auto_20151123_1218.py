# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0004_auto_20151123_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='recipient_username',
            field=models.CharField(max_length=100, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memo',
            name='subject',
            field=models.CharField(max_length=100, default=None),
        ),
    ]
