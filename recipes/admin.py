from django.contrib import admin
from .models import RecipeModel, IngredientModel, CollectionModel


admin.site.register(RecipeModel)
admin.site.register(IngredientModel)
admin.site.register(CollectionModel)
