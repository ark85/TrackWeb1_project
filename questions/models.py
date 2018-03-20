# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category

class Question(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Question name'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='questions',
        verbose_name='Author'
    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='questions',
        verbose_name='Question\'s categories'
    )
    is_archive = models.BooleanField(
        default=False,
        verbose_name='Question in archive'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = 'name', 'id'