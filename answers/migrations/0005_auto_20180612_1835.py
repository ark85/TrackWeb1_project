# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-12 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0004_auto_20180612_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.Question', verbose_name="Answer's question"),
        ),
    ]
