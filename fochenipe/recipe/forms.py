from django import forms

from recipe.models import Recipe
from kitchen.models import FoodItem


class RecipeForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(queryset=FoodItem.objects.all())

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Recipe
