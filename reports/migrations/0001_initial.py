# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('Folder_Name', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='creator', default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('Short_Description', models.CharField(max_length=200)),
                ('Detailed_Description', models.TextField(max_length=1000)),
                ('Location_of_Event', models.CharField(max_length=100)),
                ('Attachments', models.FileField(blank=True, upload_to='report')),
                ('Attachment_is_Encrypted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('group_name', models.CharField(max_length=200, default='Public')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='author', null=True)),
                ('folder', models.ForeignKey(to='reports.Folder', related_name='author', default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensitivity',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sensitivity', models.IntegerField(choices=[(3, 'public'), (2, 'private')])),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='reports.Report'),
        ),
    ]
