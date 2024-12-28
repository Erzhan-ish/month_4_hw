from audioop import reverse

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import RecipeForm, IngredientForm, CollectionForm
from django.views import generic
from .models import RecipeModel, IngredientModel, CollectionModel


class CreateRecipeView(generic.CreateView):
    template_name = 'recipe/create_recipe.html'
    form_class = RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateRecipeView, self).form_valid(form=form)

class CreateIngredientView(generic.CreateView):
    template_name = 'recipe/create_ingredient.html'
    form_class = IngredientForm
    success_url = '/ingredient_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateIngredientView, self).form_valid(form=form)


class IngredientListView(generic.ListView):
    template_name = 'recipe/list_ingredient.html'
    context_object_name = 'ingredient_list'
    model = IngredientModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class UpdateIngredientView(generic.UpdateView):
    template_name = 'recipe/ingredient_update.html'
    form_class = IngredientForm
    success_url = '/ingredient_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateIngredientView, self).form_valid(form=form)

    def get_object(self, **kwargs):
        ingredient_id = self.kwargs.get['id']
        return get_object_or_404(IngredientModel, id=ingredient_id)


class CollectionView(generic.CreateView):
    template_name = 'recipe/create_collection.html'
    form_class = CollectionForm
    success_url = '/collection_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CollectionView, self).form_valid(form=form)

class CollectionListView(generic.ListView):
    template_name = 'recipe/list_collection.html'
    context_object_name = 'collection_list'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class RecipeListView(generic.ListView):
    template_name = 'recipe/list_recipe.html'
    context_object_name = 'recipe_list'
    model = RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RecipeDetailView(generic.DetailView):
    template_name = 'recipe/recipe_detail.html'
    context_object_name = 'recipe_id'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(IngredientModel, id=recipe_id)

class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipe/confirm_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(RecipeModel, id=recipe_id)

class AllCollectionView(generic.ListView):
    template_name = 'recipe/all_collection.html'
    context_object_name = 'recipe'
    model = RecipeModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class SweetRecipeView(generic.ListView):
    template_name = 'recipe/recipe_sweet.html'
    context_object_name = 'sweet_recipe'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.filter(recipes__name='сладкое').order_by('-id')

class SaltyRecipeView(generic.ListView):
    template_name = 'recipe/recipe_salty.html'
    context_object_name = 'salty_recipe'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.filter(recipes__name='соленое').order_by('-id')

class FlourRecipeView(generic.ListView):
    template_name = 'recipe/recipe_flour.html'
    context_object_name = 'flour_recipe'
    model = CollectionModel

    def get_queryset(self):
        return self.model.objects.filter(recipes__name='мучное').order_by('-id')

