# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 11:29
from __future__ import unicode_literals

import core.models
import django.core.files.storage
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170829_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ajrbyers/Code/janeway/src/media'), upload_to=core.models.profile_images_upload_path),
        ),
    ]
