# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-08 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20181005_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='language',
            field=models.CharField(blank=True, choices=[('E', 'English'), ('C', 'Chinese'), ('G', 'German'), ('S', 'Spanish'), ('I', 'Italian'), ('J', 'Japanese'), ('D', 'Dutch')], max_length=7, null=True, verbose_name='Language'),
        ),
    ]
