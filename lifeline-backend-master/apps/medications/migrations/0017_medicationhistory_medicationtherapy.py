# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-16 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0016_auto_20190513_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationHistory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('medications.prescription',),
        ),
        migrations.CreateModel(
            name='MedicationTherapy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('medications.prescription',),
        ),
    ]
