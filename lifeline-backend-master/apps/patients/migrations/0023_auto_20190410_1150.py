# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-10 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0022_auto_20190404_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='language',
            field=models.CharField(blank=True, choices=[('E', 'English'), ('F', 'French'), ('G', 'German'), ('S', 'Spanish'), ('I', 'Italian'), ('D', 'Dutch')], max_length=7, null=True, verbose_name='Language'),
        ),
    ]