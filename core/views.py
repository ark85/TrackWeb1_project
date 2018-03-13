# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('This is homepage')

def signup(request):
    new_user = request.GET.get('new_user')
    return HttpResponse('Hello {}'.format(new_user))

def login(request):
    user_name = request.GET.get('user_name')
    return HttpResponse('Login for {}'.format(user_name))