# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-21 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0006_eval_preserve_old_res'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='canfor',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='frogs',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='katz',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='result',
        ),
    ]