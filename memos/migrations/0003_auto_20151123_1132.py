# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0002_memo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
