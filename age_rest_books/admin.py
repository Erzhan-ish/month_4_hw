from django.contrib import admin

from age_rest_books.models import Tag, Books

admin.site.register(Books)
admin.site.register(Tag)
