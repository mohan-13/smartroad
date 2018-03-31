# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-31 18:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleusers', '0002_auto_20180331_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fine_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 23, 47, 45, 452552)),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='licensenum',
            field=models.CharField(default=0, max_length=100, unique=True),
        ),
    ]