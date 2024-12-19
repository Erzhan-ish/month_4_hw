from django.urls import  path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooksView.as_view(), name='all_books'),
    path('children/', views.ChildrenBooksView.as_view(), name='children_books'),
    path('teenager/', views.TeenagerBooksView.as_view(), name='teenager_books'),
    path('youth/', views.YouthBooksView.as_view(), name='youth_books'),
    path('pensioner/', views.PensionerBooksView.as_view(), name='pensioner_books'),
]
