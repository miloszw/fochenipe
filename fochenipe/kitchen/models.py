from django.db import models

from recipe.models import Recipe


class Kitchen(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=20)
    MILLILITERS = 'ml'
    GRAMS = 'g'
    PIECES = 'st'
    MEASURE_CHOICES = (
        (MILLILITERS, 'Milliliter'),
        (GRAMS, 'Gram'),
        (PIECES, 'Styck'),
    )
    measure = models.CharField(max_length=4, choices=MEASURE_CHOICES,
                               default=PIECES)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.measure)


class Food(models.Model):
    food_item = models.ForeignKey(FoodItem)
    amount = models.IntegerField(blank=True, null=True)

    # Relationships
    is_in = models.ForeignKey(Kitchen, related_name='food',
                              blank=True, null=True)
    used_in = models.ForeignKey(Recipe, related_name='ingredients',
                                blank=True, null=True)

    class Meta:
        unique_together = (('food_item', 'is_in'), ('food_item', 'used_in'))

    def save(self, *args, **kwargs):
        try:
            # We want to delete existing model to avoid unique_together update bug
            self.delete()
            print "ok"
        except:
            pass
        if self.amount == 0:
            return
        super(Food, self).save(*args, **kwargs)


    def __unicode__(self):
        return "%s / %s%s" % (self.food_item.name, self.amount,
                              self.food_item.measure)