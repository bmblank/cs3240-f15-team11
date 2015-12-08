# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('privateKey', models.TextField(blank=True, null=True)),
                ('publicKey', models.TextField(blank=True, null=True)),
                ('rKey', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('recipient_username', models.CharField(max_length=100)),
                ('subject', models.CharField(default=None, max_length=100)),
                ('body', models.TextField(max_length=1000)),
                ('created', models.DateTimeField(default=None)),
                ('encrypted', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='recipient', null=True)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender', null=True)),
            ],
        ),
    ]
