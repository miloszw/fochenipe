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

    def get_missing_ingredients(self, kitchen):
        missing = {}
        for item in self.ingredients.all():
            try:
                amount_missing = item.amount - kitchen.food.get(food_item=item.food_item).amount
            except (ObjectDoesNotExist, TypeError):
                amount_missing = item.amount
            if amount_missing > 0:
                missing[item.food_item] = amount_missing
        return missing


    def __unicode__(self):
        return "%s - %s" % (self.name, self.type)