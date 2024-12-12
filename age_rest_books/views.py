from django.shortcuts import render
from . import models


def all_books(request):
    if request.method == 'GET':
        books = models.Books.objects.all().order_by('-id')
        context = {'books': books}
        return render(request,template_name='tags/all_books.html',context=context)


def children_books(request):
    if request.method == 'GET':
        books_children = models.Books.objects.filter(tags__name='Детей').order_by('-id')
        context = {'books_children': books_children}
        return render(request,template_name='tags/children_books.html',context=context)


def teenager_books(request):
    if request.method == 'GET':
        books_teenager = models.Books.objects.filter(tags__name='Подростков').order_by('-id')
        context = {'books_teenager': books_teenager}
        return render(request,template_name='tags/teenager_books.html',context=context)


def youth_books(request):
    if request.method == 'GET':
        books_youth = models.Books.objects.filter(tags__name='Молодежи').order_by('-id')
        context = {'books_youth': books_youth}
        return render(request,template_name='tags/youth_books.html',context=context)


def pensioner_books(request):
    if request.method == 'GET':
        books_pensioner = models.Books.objects.filter(tags__name='Пенсионеров').order_by('-id')
        context = {'books_pensioner': books_pensioner}
        return render(request,template_name='tags/pensioner_books.html',context=context)

