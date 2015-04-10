# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LBlogger_db', '0002_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.NullBooleanField(verbose_name=b'\xe5\xae\xa1\xe6\xa0\xb8'),
        ),
    ]
