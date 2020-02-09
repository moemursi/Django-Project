# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-09 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0019_auto_20190906_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationintake',
            name='end_of_timeslot',
        ),
        migrations.RemoveField(
            model_name='medicationintake',
            name='start_of_timeslot',
        ),
        migrations.AddField(
            model_name='medicationintake',
            name='time',
            field=models.DateTimeField(default='2000-01-01T00:00+0300', verbose_name='Start of medication intake time'),
            preserve_default=False,
        ),
    ]