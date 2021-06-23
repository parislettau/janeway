# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-18 16:19
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

from utils import setting_handler


settings_to_migrate = [
    {'group': 'general', 'name': 'journal_description', 'title': 'About'},
    {'group': 'general', 'name': 'focus_and_scope', 'title': 'Focus and Scope'},
    {'group': 'general', 'name': 'submission_checklist', 'title': 'Submission Checklist'},
    {'group': 'general', 'name': 'copyright_notice', 'title': 'Copyright Notice'},
    {'group': 'general', 'name': 'peer_review_info', 'title': 'Peer Review'},
    {'group': 'special', 'name': 'licences', 'title': 'licences'},
    {'group': 'general', 'name': 'publication_fees', 'title': 'Publication Fees'},
    {'group': 'general', 'name': 'publication_cycle', 'title': 'Publication Cycle'},
    {'group': 'special', 'name': 'sections', 'title': 'sections'},
]


def setup_submission_items(apps, schema_editor):
    SubmissionItem = apps.get_model('cms', 'SubmissionItem')
    Journal = apps.get_model('journal', 'Journal')
    Setting = apps.get_model('core', 'Setting')

    journals = Journal.objects.all()

    for journal in journals:
        for i, setting in enumerate(settings_to_migrate):
            if not setting.get('group') == 'special':
                setting_obj = Setting.objects.get(
                    group__name=setting.get('group'),
                    name=setting.get('name'),
                )
            else:
                setting_obj = None

            obj, c = SubmissionItem.objects.get_or_create(
                journal=journal,
                order=i,
                existing_setting=setting_obj,
            )

            setattr(obj, 'title_{}'.format(settings.LANGUAGE_CODE), setting.get('title'))
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_submissionitem'),
    ]

    operations = [
        migrations.RunPython(
            setup_submission_items,
            reverse_code=migrations.RunPython.noop,
        )
    ]
