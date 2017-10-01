# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('post', models.ForeignKey(to='blog.Post')),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'verbose_name': 'Comment',
            },
        ),
    ]
