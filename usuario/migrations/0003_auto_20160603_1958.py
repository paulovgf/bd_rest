# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20160602_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='matricula',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
