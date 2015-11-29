# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_folder_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='Attachment_is_Encrypted',
            field=models.BooleanField(default=False),
        ),
    ]
