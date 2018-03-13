# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def login(request):
    user_name = request.GET.get('user_name')
    return HttpResponse('Login for {}'.format(user_name))
