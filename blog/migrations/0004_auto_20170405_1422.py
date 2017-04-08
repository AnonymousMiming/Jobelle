# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170405_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='draft',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=50, default=12),
            preserve_default=False,
        ),
    ]
