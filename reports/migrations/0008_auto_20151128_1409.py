# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20151128_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Folder_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='folder',
            field=models.ForeignKey(related_name='author', to='reports.Folder', null=True, default=None),
        ),
    ]
