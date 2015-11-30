# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='privateKey',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='publicKey',
            field=models.TextField(blank=True, null=True),
        ),
    ]
