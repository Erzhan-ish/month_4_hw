from django.urls import  path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name='all_books'),
    path('children/', views.children_books, name='children_books'),
    path('teenager/', views.teenager_books, name='teenager_books'),
    path('youth/', views.youth_books, name='youth_books'),
    path('pensioner/', views.pensioner_books, name='pensioner_books'),
]
