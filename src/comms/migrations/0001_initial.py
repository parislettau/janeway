# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_display', models.DateField(default=django.utils.timezone.now)),
                ('end_display', models.DateField(blank=True, null=True)),
                ('sequence', models.PositiveIntegerField(default=0)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_content_type', to='contenttypes.ContentType')),
                ('large_image_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_file', to='core.File')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-posted', 'title'),
            },
        ),
    ]
