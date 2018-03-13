# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def question_details(request, question_id):
    return HttpResponse("This is question {}".format(question_id))