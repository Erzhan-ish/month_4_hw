from django.shortcuts import render
from . import models
from django.views import generic
from .models import Books


class AllBooksView(generic.ListView):
    template_name = 'tags/all_books.html'
    context_object_name = 'books'
    model = Books

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class ChildrenBooksView(generic.ListView):
    template_name = 'tags/children_books.html'
    context_object_name = 'books_children'
    model = Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Детей').order_by('-id')


class TeenagerBooksView(generic.ListView):
    template_name = 'tags/teenager_books.html'
    context_object_name = 'books_teenager'
    model = Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Подростков').order_by('-id')


class YouthBooksView(generic.ListView):
    template_name = 'tags/youth_books.html'
    context_object_name = 'books_youth'
    model = Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Молодежи').order_by('-id')


class PensionerBooksView(generic.ListView):
    template_name = 'tags/pensioner_books.html'
    context_object_name = 'books_pensioner'
    model = Books

    def get_queryset(self):
        return self.model.objects.filter(tags__name='Пенсионеров').order_by('-id')

