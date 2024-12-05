from django.shortcuts import render
from django.http import HttpResponse
import datetime

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