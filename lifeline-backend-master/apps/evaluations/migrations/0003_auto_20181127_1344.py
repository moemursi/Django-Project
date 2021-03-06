# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-27 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluations', '0002_auto_20181124_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='edited_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Editor'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]
