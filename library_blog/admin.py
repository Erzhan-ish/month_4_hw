from django.contrib import admin
from .models import BookModel, Review

admin.site.register(BookModel)
admin.site.register(Review)

