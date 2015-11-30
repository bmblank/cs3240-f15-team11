# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20151130_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='user',
        ),
        migrations.DeleteModel(
            name='Key',
        ),
    ]
