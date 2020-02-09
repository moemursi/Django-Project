# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-10 07:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import lifeline.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0031_auto_20190619_1213'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('file', models.FileField(storage=lifeline.storage_backends.PrivateMediaStorage(), upload_to='')),
                ('name', models.CharField(max_length=64, verbose_name='documents name')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('document_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='documents.DocumentType')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'db_table': 'documents',
            },
        ),
    ]