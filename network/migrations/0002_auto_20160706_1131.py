# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switch',
            name='status',
            field=models.CharField(default='product', max_length=255, verbose_name='\u72b6\u6001'),
        ),
    ]
