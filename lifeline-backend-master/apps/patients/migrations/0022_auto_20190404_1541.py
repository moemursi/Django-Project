# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-04 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_auto_20190329_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='status',
            field=models.CharField(blank=True, choices=[('E', 'Emergency'), ('I', 'Inpatient'), ('O', 'Outpatient'), ('P', 'Preadmit'), ('R', 'Recurring patient'), ('B', 'Obstetrics'), ('C', 'Commercial Account'), ('N', 'Not Applicable'), ('U', 'Unknown')], max_length=7, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='file',
            name='temporary_location',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Temporary patients location'),
        ),
    ]