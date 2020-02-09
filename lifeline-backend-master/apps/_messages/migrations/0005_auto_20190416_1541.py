# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-16 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_messages', '0004_auto_20181211_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpatient',
            name='subject_en',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='aboutpatient',
            name='subject_fr',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Subject'),
        ),
        migrations.AddField(
            model_name='aboutpatient',
            name='subject_nl',
            field=models.CharField(db_index=True, max_length=255, null=True, verbose_name='Subject'),
        ),
    ]