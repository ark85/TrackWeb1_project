# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import Question

def question_details(request, question_id):
    context = {
        'question': get_object_or_404(Question, id=question_id)
    }

    return render(request, "questions/question_details.html", context)


def question_views(request):
    context = {
        'questions': Question.objects.all()
    }

    return render(request, "questions/question_views.html", context)
