# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-30 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onroad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkdetails',
            name='checked_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 31, 1, 15, 18, 268991)),
        ),
    ]
