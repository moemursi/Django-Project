# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-28 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0011_add_result_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='results_id',
            field=models.IntegerField(default=1, verbose_name='Evaluation id by type'),
        ),
    ]