# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def signup(request):
    new_user = request.GET.get('new_user')
    return HttpResponse('Hello {}'.format(new_user))