# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-30 19:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='checkdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_by', models.CharField(default=0, max_length=12)),
                ('driver', models.CharField(default=0, max_length=12)),
                ('checked_on', models.DateTimeField(default=datetime.datetime(2018, 3, 31, 0, 35, 57, 583647))),
                ('fine_imp', models.IntegerField(default=0)),
            ],
        ),
    ]