from django.urls import path
from . import views

urlpatterns = [
    path('create_review/', views.CreateReviewView.as_view(), name='createReview'),
    path('', views.BookListView.as_view(), name='books'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('about/', views.AboutMeView.as_view(), name='about'),
    path('about_pets/', views.AboutPetsView.as_view(), name='about_pets'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]