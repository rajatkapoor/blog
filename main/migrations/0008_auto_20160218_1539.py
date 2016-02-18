# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 10:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160218_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 18, 15, 39, 53, 437000)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.Blog'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 18, 15, 39, 53, 437000)),
        ),
    ]
