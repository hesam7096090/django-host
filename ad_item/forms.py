from django import forms
from .models import *

# forms.py
from django import forms
from django.forms.models import inlineformset_factory

from .models import *

class ItemForm(forms.ModelForm):
    collateral_types = forms.ModelMultipleChoiceField(
        queryset=Collateral.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )

    class Meta:
        model = Item
        fields = [
            'category', 'title', 'description', 'quantity_available',
            'province', 'city', 'address', 'collateral_required',
            'collateral_types', 'price_per_day',
            'item_value',


        ]
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'quantity_available': forms.NumberInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'collateral_required': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_value': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']


