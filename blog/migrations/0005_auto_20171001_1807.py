# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171001_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 10, 1, 12, 7, 7, 945429, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
