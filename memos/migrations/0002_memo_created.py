# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='created',
            field=models.DateTimeField(default=None),
        ),
    ]
