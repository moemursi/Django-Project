# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-10 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wounds', '0010_auto_20181120_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evolution',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='wound',
            old_name='created_by',
            new_name='user',
        ),
    ]