# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_report_attachment_is_encrypted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='Report_is_Public',
        ),
    ]
