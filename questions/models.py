# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category
from answers.models import Answer

class Question(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Question name'
    )
    content = models.CharField(
        max_length=500,
        verbose_name='Question content'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='questions',
        verbose_name='Author'
    )
    categories = models.ManyToManyField(
        Category,
        # Update faster than remove
        blank=True,
        related_name='questions',
        verbose_name='Question\'s categories'
    )
    answers = models.ManyToManyField(
        Answer,
        related_name='answers',
        blank=True,
        verbose_name="Question\'s answers"
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="question_likes"
    )
    is_archive = models.BooleanField(
        default=False,
        verbose_name='Question in archive'
    )

    # Add answers and comments

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = 'name', 'id'