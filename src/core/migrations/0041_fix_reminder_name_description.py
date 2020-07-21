# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-21 16:07
from __future__ import unicode_literals

from django.db import migrations


EMAILS_TO_FIX = [
    {
        'name': 'accepted_review_reminder',
        'pretty_name': 'Accepted Review Reminder',
        'description': 'Notify reviewer of accepted request and remind them to review submission.',
    },
    {
        'name': 'author_publication',
        'pretty_name': 'Author Publication Notification',
        'description': 'Notify the author of their publication date and time.',
    },
    {
        'name': 'review_decline_acknowledgement',
        'pretty_name': 'Review Decline Acknowledgement',
    },
    {
        'name': 'editor_digest',
        'description': 'Digest email sent to editors.',
    },
    {
        'name': 'notify_proofreader_assignment',
        'description': 'Email sent to a proofreader when they are given an assignment.'
    },
    {
        'name': 'review_request_sent',
        'pretty_name': 'Review Request Update',
        'description': 'Email sent when a review assignment is updated.',
    },
]

def fix_email_names_descriptions(apps, schema_editor):
    Setting = apps.get_model('core', 'Setting')

    for fix in EMAILS_TO_FIX:
        settings = Setting.objects.filter(name=fix.get('name'))

        for setting in settings:
            if fix.get('pretty_name'):
                setting.pretty_name = fix.get('pretty_name')

            if fix.get('description'):
                setting.description = fix.get('description')

            setting.save()


def move_from_address_to_general(apps, schema_editor):
    Setting = apps.get_model('core', 'Setting')
    Group = apps.get_model('core', 'SettingGroup')

    group = Group.objects.get(name='general')

    Setting.objects.filter(
        name='from_address'
    ).update(
        group=group
    )


def move_from_address_to_email(apps, schema_editor):
    Setting = apps.get_model('core', 'Setting')
    Group = apps.get_model('core', 'SettingGroup')

    group = Group.objects.get(name='email')

    Setting.objects.filter(
        name='from_address'
    ).update(
        group=group
    )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20200529_1415'),
    ]

    operations = [
        migrations.RunPython(
            fix_email_names_descriptions,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunPython(
            move_from_address_to_general,
            reverse_code=move_from_address_to_email,
        )
    ]