# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from models import Answer
from django.views.generic import UpdateView, CreateView
from forms import AnswerViewsForm
from questions.views import question_views


def answer_details(request, answer_id):
    context = {
        'answer': get_object_or_404(Answer, id=answer_id)
    }

    return render(request, "answers/answer_details.html", context)

def answer_views(request):
    answers = Answer.objects.all()

    form = AnswerViewsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            answers = answers.order_by(data['sort'])
        if data['search']:
            answers = answers.filter(name__icontains=data['search'])
    context = {
        'answers': answers,
        'answer_form': form
    }

    return render(request, "answers/answer_views.html", context)


class AnswerEdit(UpdateView):
    model = Answer
    fields = 'content'
    context_object_name = 'answer'
    template_name = 'answer/answer_edit.html'

    def get_queryset(self):
        queryset = super(AnswerEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('answers:answer_details', kwargs={'answer_id': self.object.pk})


class AnswerCreate(CreateView):

    def dispatch(self, request, *args, **kwargs):
        # if user auth
        return super(AnswerCreate, self).dispatch(request, *args, **kwargs)

    model = Answer
    fields = 'content', 'question'
    context_object_name = 'answer'
    template_name = 'answers/answer_create.html'

    #

    def get(self, request):
        form = self.get_form()
        return render(request, 'answers/answer_create.html', {'form': form})

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.save()
            # return redirect('answers:answer_details', answer_id=answer.pk)
            return redirect('questions:questions')
        else:
            return render(request, 'answers/answer_create.html', {'form': form})

    def get_success_url(self):
        return reverse('answers:answer_details', kwargs={'answer_id': self.object.pk})
