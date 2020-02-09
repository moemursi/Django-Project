# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_extensions.db.fields
import lifeline.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('wounds', '0002_wound_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wound',
            options={'ordering': ('-created',), 'verbose_name': 'Wound', 'verbose_name_plural': 'Wounds'},
        ),
        migrations.AddField(
            model_name='evolution',
            name='height_t',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='evolution',
            name='thumbnail',
            field=models.ImageField(max_length=255, null=True, storage=lifeline.storage_backends.PrivateMediaStorage(), upload_to='', verbose_name='Wound photo'),
        ),
        migrations.AddField(
            model_name='evolution',
            name='width_t',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='wound',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wound',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]