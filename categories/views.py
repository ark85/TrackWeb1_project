# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import Category


def category_details(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False)
    }

    return render(request, "categories/category_details.html", context)


def category_views(request):
    context = {
        'categories': Category.objects.all()
    }

    return render(request, "categories/category_views.html", context)
