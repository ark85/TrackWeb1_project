# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse, redirect
from models import Question
from django.views.generic import UpdateView, CreateView
from forms import QuestionViewsForm


def question_details(request, question_id):
    context = {
        'question': get_object_or_404(Question, id=question_id)
    }

    return render(request, "questions/question_details.html", context)


def question_views(request):
    questions = Question.objects.all()

    form = QuestionViewsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            questions = questions.order_by(data['sort'])
        if data['search']:
            questions = questions.filter(name__icontains=data['search'])
    context = {
        'questions': questions,
        'questions_form': form
    }

    return render(request, "questions/question_views.html", context)


class QuestionEdit(UpdateView):
    model = Question
    fields = 'name', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_edit.html'

    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('questions:question_details', kwargs={'question_id': self.object.pk})


class QuestionCreate(CreateView):
    model = Question
    fields = 'name', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_create.html'

    def get(self, request):
        form = self.get_form()
        return render(request, 'questions/question_create.html', {'form': form})

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('questions:question_details', question_id=question.pk)
        else:
            return render(request, 'questions/question_create.html', {'form': form})

    def get_success_url(self):
        return reverse('questions:question_details', kwargs={'question_id': self.object.pk})
