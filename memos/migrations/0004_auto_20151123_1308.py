# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0003_auto_20151123_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='recipient',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, max_length=200, null=True, related_name='recipient'),
        ),
        migrations.AlterField(
            model_name='memo',
            name='sender',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, max_length=200, null=True, related_name='sender'),
        ),
    ]
