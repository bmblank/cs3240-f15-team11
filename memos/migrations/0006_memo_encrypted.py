# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0005_auto_20151123_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='encrypted',
            field=models.BooleanField(default=False),
        ),
    ]
