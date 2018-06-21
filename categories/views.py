# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from models import Category
from forms import CategoryViewsForm, CategoryForm
from django.views.generic import UpdateView


def category_details(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False)
    }

    return render(request, "categories/category_details.html", context)


def category_views(request):

    categories = Category.objects.all()

    form = CategoryViewsForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            categories = categories.order_by(data['sort'])
        if data['search']:
            categories = categories.filter(name__icontains=data['search'])
    context = {
        'categories': categories,
        'categories_form': form
    }

    return render(request, "categories/category_views.html", context)



def category_create(request):

    category = Category()

    if request.method == 'GET':
        form = CategoryForm(instance=category)
        return render(request, 'categories/category_create.html', {'form': form})
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user
            category.save()
            return redirect('categories:categories')
        else:
            return render(request, 'categories/category_create.html', {'form': form})

class CategoryEdit(UpdateView):

    model = Category
    fields = 'name',
    context_object_name = 'category'
    template_name = 'categories/category_edit.html'

    def get_queryset(self):
        queryset = super(CategoryEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('categories:category_details', kwargs={'category_id': self.object.pk})

    def form_valid(self, form):
        response = super(CategoryEdit, self).form_valid(form)
        return HttpResponse('valid')