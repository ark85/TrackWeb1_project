# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, "core/index.html", {})

def signup(request):
    return render(request, "core/signup.html", {})

def login(request):
    return render(request, "core/login.html", {})

def logout(request):
    return render(request, "core/logout.html", {})

def profile(request):
    return render(request, "core/profile.html", {})