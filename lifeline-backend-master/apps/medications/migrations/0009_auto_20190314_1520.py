# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-14 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0008_prescription_max_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(default='code', max_length=64, verbose_name='Code'),
        ),
    ]