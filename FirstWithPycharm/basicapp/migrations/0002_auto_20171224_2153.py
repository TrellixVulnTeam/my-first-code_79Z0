# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='users',
        ),
    ]
