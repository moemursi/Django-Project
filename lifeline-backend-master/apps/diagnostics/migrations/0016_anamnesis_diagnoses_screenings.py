# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-16 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0015_auto_20181229_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anamnesis',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('diagnostics.diagnostic',),
        ),
        migrations.CreateModel(
            name='Diagnoses',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('diagnostics.diagnostic',),
        ),
        migrations.CreateModel(
            name='Screenings',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('diagnostics.diagnostic',),
        ),
    ]