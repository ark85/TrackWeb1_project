# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-12 18:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20180612_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
    ]
