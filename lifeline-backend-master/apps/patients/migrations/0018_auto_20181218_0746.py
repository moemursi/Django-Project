# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20181209_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('SI', 'Single'), ('D', 'Divorced'), ('H', 'Co-habitant'), ('U', 'Unknown'), ('SE', 'Separated'), ('W', 'Widowed')], max_length=7, null=True, verbose_name='Marital Status'),
        ),
    ]
