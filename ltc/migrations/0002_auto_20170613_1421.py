# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ltc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='count',
            field=models.IntegerField(default=0, verbose_name='fetch times'),
        ),
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.IntegerField(db_index=True, verbose_name='date of record'),
        ),
    ]
