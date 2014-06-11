from django import forms

from recipe.models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
