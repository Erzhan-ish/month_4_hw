from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ITLevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            level = (request.POST.get("level"))
            if level == 'jun':
                request.salary = '700$'
            elif level == 'middle':
                request.salary = '1000$'
            elif level == 'senior':
                request.salary = '2000$'
            else:
                return HttpResponseBadRequest('Пожалуста подтяните ваш уровень')
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, 'salary', 'ЗП не определен')

