# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from models import Question
from django.views.generic import UpdateView, CreateView, View
from forms import QuestionViewsForm


def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    context = {
        'question': question,
        'answers': question.answers.all().filter(is_archive=False)
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

    # @login_required()
    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('questions:question_details', kwargs={'question_id': self.object.pk})


class QuestionCreate(CreateView):

    # @login_required
    def dispatch(self, request, *args, **kwargs):
        # if user auth
        return super(QuestionCreate, self).dispatch(request, *args, **kwargs)

    model = Question
    fields = 'name', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_create.html'

    #

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


class QuestionLikesCount(View):
    question = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=pk)
        return super(QuestionLikesCount, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(self.question.likes.count())
