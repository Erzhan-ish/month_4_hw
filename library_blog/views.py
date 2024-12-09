from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import datetime
from . import models

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {
            'book_id': book_id,
            }
        return render(request, template_name='book_detail.html', context=context)


def book_list_view(request):
    if request.method == 'GET':
        book_list = models.BookModel.objects.all().order_by('-id')
        context = {
            'book_list': book_list
        }
        return render(request,template_name='book.html', context=context)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Привет это мое первое дз на django')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse("У меня собака породы лайка возраста 3 лет, зовут барсик")

def system_time(request):
    time = datetime.datetime.now()
    if request.method == 'GET':
        return HttpResponse(f'Текущее время: {time}')