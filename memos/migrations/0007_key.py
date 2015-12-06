# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('memos', '0006_memo_encrypted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('privateKey', models.TextField(null=True, blank=True)),
                ('publicKey', models.TextField(null=True, blank=True)),
                ('rKey', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
