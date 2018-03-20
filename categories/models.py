# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Category name'
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = 'name', 'id'