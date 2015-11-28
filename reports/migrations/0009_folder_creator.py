# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0008_auto_20151128_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, default=None, related_name='creator'),
        ),
    ]
