from django import forms

from kitchen.models import Kitchen, Food, FoodItem


class KitchenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KitchenForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Kitchen
        exclude = ('food',)


class FoodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Food
        widgets = {'is_in': forms.widgets.HiddenInput(),
                   'used_in': forms.widgets.HiddenInput()}


class FoodItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FoodItem