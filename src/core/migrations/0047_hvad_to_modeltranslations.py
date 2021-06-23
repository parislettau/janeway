# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-17 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_delete_review_request_sent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settingvaluetranslation',
            old_name='value',
            new_name='hvad_value',
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_cy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settingvalue',
            name='value_fr',
            field=models.TextField(blank=True, null=True),
        ),
    ]
