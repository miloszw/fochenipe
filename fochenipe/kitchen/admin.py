from django.contrib import admin

from kitchen.models import Kitchen, Food, FoodItem

# Register your models here.
admin.site.register(Kitchen)
admin.site.register(Food)
admin.site.register(FoodItem)
