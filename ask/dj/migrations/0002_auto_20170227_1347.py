# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='choise',
            new_name='Choice',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='Choice_text',
        ),
    ]
