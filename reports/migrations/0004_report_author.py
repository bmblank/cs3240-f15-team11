# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0003_report_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='author'),
        ),
    ]
