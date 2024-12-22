from django.urls import path
from . import views

urlpatterns = [
    path('kinoogo_film_list/', views.KinoogoListView.as_view(), name='kinoogo_list'),
    path('form_parser_kinoogo/', views.KinoogoFormView.as_view()),
]