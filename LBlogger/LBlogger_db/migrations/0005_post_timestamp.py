# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LBlogger_db', '0004_auto_20150406_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 15, 16, 52, 54222, tzinfo=utc), verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4\xe6\x88\xb3', auto_now_add=True),
            preserve_default=False,
        ),
    ]
