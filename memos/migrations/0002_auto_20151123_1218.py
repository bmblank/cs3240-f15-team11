# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='recepient',
            new_name='recipient',
        ),
        migrations.AddField(
            model_name='memo',
            name='cc_myself',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
