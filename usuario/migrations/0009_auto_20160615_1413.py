# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20160615_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rg',
            field=models.CharField(blank=True, db_column='RG', max_length=9, null=True, unique=True),
        ),
    ]