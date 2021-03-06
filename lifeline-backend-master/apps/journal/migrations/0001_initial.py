# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-14 08:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0012_emergencycontact'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Note header')),
                ('category', models.CharField(blank=True, default='default', max_length=255, null=True, verbose_name='Category slug')),
                ('content', models.TextField(verbose_name='Content')),
                ('type', models.CharField(choices=[('comment', 'Comment'), ('event', 'Event')], default='comment', max_length=10, verbose_name='Note type')),
                ('tag', models.CharField(blank=True, choices=[('medical', 'Medical info'), ('nursing', 'Nursing info'), ('caregiver', 'Caregiver info'), ('psycho', 'Psychotherapy'), ('physio', 'Physiotherapy'), ('social', 'Social info'), ('staff', 'Staff meeting'), ('night', 'Nightshift'), ('fall', 'Fall'), ('confusion', 'Confusion'), ('disorient', 'Disorientation'), ('run', 'Runaway'), ('behavior', 'Behavior disorder'), ('agressive', 'Agressiveness'), ('agitate', 'Agitation'), ('drug', 'Drug use')], max_length=10, null=True, verbose_name='Note tag')),
                ('action', models.CharField(choices=[('create', 'Created'), ('add', 'Added'), ('edit', 'Edited'), ('delete', 'Deleted'), ('status', 'Status changed'), ('cured', 'Cured')], max_length=10, null=True, verbose_name='User Action')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.File', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journal',
                'db_table': 'journal',
                'ordering': ('-created',),
            },
        ),
    ]
