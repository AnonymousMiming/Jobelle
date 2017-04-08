# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170405_1331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Blog',
        ),
    ]
