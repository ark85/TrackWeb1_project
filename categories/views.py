# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def category_details(request, category_id):
    return HttpResponse("This is category {}".format(category_id))