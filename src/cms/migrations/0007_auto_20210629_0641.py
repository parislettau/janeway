# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-29 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20210618_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationitem',
            name='link_name_nl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='content_nl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='display_name_nl',
            field=models.CharField(help_text='Name of the page, max 100 chars, displayed in the nav and on the header of the page eg. About or Contact', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='submissionitem',
            name='text_nl',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='submissionitem',
            name='title_nl',
            field=models.CharField(max_length=255, null=True),
        ),
    ]