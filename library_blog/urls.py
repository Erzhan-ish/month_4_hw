from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_me, name='about'),
    path('about_pets/', views.about_pets, name='about_pets'),
    path('system_time/', views.system_time, name='system_time'),
]