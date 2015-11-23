# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sender', models.CharField(max_length=200)),
                ('recepient', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=1000)),
            ],
        ),
    ]
