# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-19 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20181219_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='t_wound',
            new_name='wound',
        ),
    ]
