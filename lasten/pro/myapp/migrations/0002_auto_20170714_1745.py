# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='PositionWeight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
