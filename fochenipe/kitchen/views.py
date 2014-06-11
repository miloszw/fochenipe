#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from kitchen.models import Kitchen, FoodItem, Food
from kitchen.forms import FoodForm, KitchenForm, FoodItemForm


def home(request):
    try:
        food = (Kitchen.objects.get(id=request.session.get('kitchen', -1))
                .food.all())
        context = {'food': food}
    except ObjectDoesNotExist:
        # None of wrong kitchen id
        kitchens = Kitchen.objects.all()
        context = {'kitchens': kitchens}
    return render(request, 'kitchen/index.html', context)


def add(request, subject, id=0):
    # Create corresponding form
    if subject == 'kitchen':
        form = KitchenForm
        subject = 'kök'
    elif subject == 'food':
        form = FoodForm
        obj = Food
        subject = 'vara'
    elif subject == 'fooditem':
        form = FoodItemForm
        obj = FoodItem
        subject = 'vara'    

    # Handle form request
    if request.method == "POST":
        if id > 0:
            obj = obj.objects.get(pk=id)
            form = form(request.POST, instance=obj)
        else:
            form = form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.GET.get('next', 'home'))
    else:
        if id > 0:
            obj = obj.objects.get(pk=id)
            form = form(instance=obj)
        else:
            # Instantize with correct kitchen (only in case of model = food)
            try:
                kitchen = Kitchen.objects.get(id=request.session['kitchen'])
                form = form(initial={'is_in':kitchen})
            except KeyError:
                # In case of model = kitchen
                form = form()
    return render(request, 'kitchen/add.html', {'form': form, 'subject': subject})


def select(request, kitchen_id):
    if not kitchen_id == '0':
        request.session['kitchen'] = kitchen_id
    else:
        del request.session['kitchen']
    return redirect('home')


def catalog(request):
    food = FoodItem.objects.all()
    return render (request, 'kitchen/catalog.html', {'food': food})