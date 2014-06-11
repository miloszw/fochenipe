from django.shortcuts import render

from recipe.forms import RecipeForm


def home(request):
    return render(request, 'recipe/recipe.html')


def add(request):
    form = RecipeForm()
    return render(request, 'kitchen/add.html', {'form': form, 'subject': 'recept'})