# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-21 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoicePdf',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]