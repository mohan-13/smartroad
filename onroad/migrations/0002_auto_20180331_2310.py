# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-31 17:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkdetails',
            name='fine_reason',
            field=models.CharField(default='NILL', max_length=500),
        ),
        migrations.AlterField(
            model_name='checkdetails',
            name='checked_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 23, 10, 7, 803695)),
        ),
    ]