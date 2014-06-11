from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField()

    def can_make(self, kitchen):
        for item in self.ingredients.all():
            try:
                if kitchen.food.get(food_item=item.food_item).amount == None:
                    continue
                if kitchen.food.get(food_item=item.food_item).amount < item.amount:
                    return False
            except ObjectDoesNotExist:
                return False
        return True

    def can_definitely_make(self, kitchen):
        for item in self.ingredients.all():
            try:
                if kitchen.food.get(food_item=item.food_item).amount < item.amount:
                    return False
            except ObjectDoesNotExist:
                return False
        return True

    def get_missing_ingredients(self, kitchen, ingredients=None):
        missing = {}
        if ingredients == None:
            ingredients = self.ingredients.all()

        # First collate items
        dict_ingredients = {}
        for item in ingredients:
            if item.food_item in dict_ingredients:
                dict_ingredients[item.food_item] += item.amount
            else:
                dict_ingredients[item.food_item] = item.amount

        # Then check missing amount
        for food_item, item_amount in dict_ingredients.items():
            try:
                amount_missing = item_amount - kitchen.food.get(food_item=food_item).amount
            except (ObjectDoesNotExist, TypeError):
                amount_missing = item_amount
            if amount_missing > 0:
                missing[food_item] = amount_missing
        return missing


    def __unicode__(self):
        return "%s - %s" % (self.name, self.type)