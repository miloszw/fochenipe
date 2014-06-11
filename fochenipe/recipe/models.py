from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField()

    def can_make(self, kitchen):
        for item in self.ingredients.all():
            try:
                if kitchen.food.get(food_item=item.food_item).amount < item.amount:
                    return False
            except ObjectDoesNotExist:
                return False
        return True

    def __unicode__(self):
        return "%s - %s" % (self.name, self.type)