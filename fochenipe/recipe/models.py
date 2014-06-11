from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField()

    def __unicode__(self):
        return "%s - %s" % (self.name, self.type)