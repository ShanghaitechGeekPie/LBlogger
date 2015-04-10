# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LBlogger_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=0, verbose_name=b'\xe5\xae\xa1\xe6\xa0\xb8'),
            preserve_default=False,
        ),
    ]
