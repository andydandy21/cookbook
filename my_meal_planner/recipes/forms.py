from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient

IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name', 'quantity', 'measurement'), extra=1)
