#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from recipe.forms import RecipeForm
from recipe.models import Recipe
from kitchen.models import Kitchen


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe.html', {'recipes': recipes})


def add(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_home')
    return render(request, 'kitchen/add.html', {'form': form, 'subject': 'recept'})


def detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    k_id = request.session['kitchen']
    enough_ingredients = recipe.can_make(Kitchen.objects.get(pk=k_id))
    return render(request, 'recipe/detail.html', {'recipe': recipe,
        'enough_ingredients': enough_ingredients})


def delete(request,id):
    recipe = Recipe.objects.get(pk=id)
    recipe.delete()
    return redirect('recipe_home')


def make(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    kitchen = Kitchen.objects.get(pk=request.session['kitchen'])
    
    if not recipe.can_make(kitchen):
        messages.warning(request, 'Det fattas ingredienser!')
        return redirect('recipe_home')

    for item in recipe.ingredients.all():
        kitchen_item = kitchen.food.get(food_item=item.food_item)
        kitchen_item.amount -= item.amount
        kitchen_item.save()

    messages.success(request, 'Förbrukat respektive ingredienser')
    return redirect('home')
