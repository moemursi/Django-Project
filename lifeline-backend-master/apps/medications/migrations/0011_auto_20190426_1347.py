# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-26 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0010_auto_20190422_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='unit',
            field=models.CharField(default='mg', max_length=128, verbose_name='Unit'),
            preserve_default=False,
        ),
    ]
