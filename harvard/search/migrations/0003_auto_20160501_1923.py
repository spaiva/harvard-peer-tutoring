# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_course_has_tutors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='has_tutors',
            new_name='has_tutor_request',
        ),
    ]
