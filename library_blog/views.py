from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
import datetime
from . import models
from .forms import ReviewForm
from django.views import generic

from .models import BookModel

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 3

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self,* ,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class CreateReviewView(generic.CreateView):
    template_name = 'book_detail.html'
    form_class = ReviewForm
    success_url = '/book_detail/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(BookModel, id=book_id)

@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = BookModel

    def get_queryset(self):
        books = cache.get('books')
        if not books:
            books = self.model.objects.all().order_by('-id')
            cache.set('books', books, 60 * 15)
        return books

def clear_todo_cache(sender, **kwargs):
    cache.delete('books')

class AboutMeView(generic.TemplateView):
    def get(self,request):
        return HttpResponse('Привет это мое первое дз на django')

class AboutPetsView(generic.TemplateView):
    def get(self,request):
        return HttpResponse("У меня собака породы лайка возраста 3 лет, зовут барсик")

class SystemTimeView(generic.TemplateView):
    def get(self,request):
        time = datetime.datetime.now()
        return HttpResponse(f'Текущее время: {time}')
