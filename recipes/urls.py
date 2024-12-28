from django.urls import path
from . import views

urlpatterns = [
    path('all_collection/', views.AllCollectionView.as_view(), name='all_collection'),
    path('sweet/', views.SweetRecipeView.as_view(), name='sweet_recipe'),
    path('salty/', views.SaltyRecipeView.as_view(), name='salty_recipe'),
    path('flour/', views.FlourRecipeView.as_view(), name='flour_recipe'),
    path('create_collection/', views.CollectionView.as_view(), name='createCollection'),

    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('create_recipe/', views.CreateRecipeView.as_view(), name='createRecipe'),
    path('create_ingredient/', views.CreateIngredientView.as_view(), name='createIngredient'),
    path('recipe_list/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe_list/<int:id>/delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]