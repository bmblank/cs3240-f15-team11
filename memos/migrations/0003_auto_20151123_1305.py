# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0002_auto_20151123_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='encrypt',
            field=models.BooleanField(default=False, verbose_name='Encrypt Message'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memo',
            name='body',
            field=models.TextField(max_length=1000, verbose_name='Message Body'),
        ),
        migrations.AlterField(
            model_name='memo',
            name='cc_myself',
            field=models.BooleanField(verbose_name='CC Myself'),
        ),
        migrations.AlterField(
            model_name='memo',
            name='recipient',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, max_length=200, null=True, blank=True),
        ),
    ]
