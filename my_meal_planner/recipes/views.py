from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView, 
    UpdateView,
    DeleteView,
)
from django.forms import inlineformset_factory
from django.db import transaction

from .models import Recipe, Ingredient, Tag
from .forms import IngredientFormSet



class HomeView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipe_list'
    ordering = 'name'
    paginate_by = 12

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['name','description','image','tags','instructions']
    
    
    def get_context_data(self, **kwargs):
        data = super(RecipeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST)
        else:
            data['ingredients'] = IngredientFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()

        return super(RecipeCreateView, self).form_valid(form)

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['name','description','image','tags','instructions']
    
    
    def get_context_data(self, **kwargs):
        data = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = IngredientFormSet(self.request.POST, instance=self.object)
        else:
            data['ingredients'] = IngredientFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        with transaction.atomic():
            self.object = form.save()

            if ingredients.is_valid():
                ingredients.instance = self.object
                ingredients.save()

        return super(RecipeUpdateView, self).form_valid(form)

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = '/'

class TagListView(ListView):
    model = Tag
    template_name = 'recipes/tag_list.html'
    context_object_name = 'tag_list'
    ordering = 'name'
    paginate_by = 12

    
    def get_queryset(self):
        result = super(TagListView, self).get_queryset()
        query = self.request.GET.get('tag')
        q_tag_recipes = Tag.objects.get(name=query)
        if query:
            result = Recipe.objects.filter(tags=q_tag_recipes)
        else:
            result = None
        return result
    
    def get_context_data(self, **kwargs):
        data = super(TagListView, self).get_context_data(**kwargs)
        query = self.request.GET.get('tag')
        data['q_tag'] = Tag.objects.get(name=query)
        return data

class SearchView(ListView):
    model = Recipe
    template_name = 'recipes/search.html'
    context_object_name = 'search_results'
    ordering = ['name']
    paginate_by = 12

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = Recipe.objects.filter(name__contains=query)
        else:
            result = None
        return result
    
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context