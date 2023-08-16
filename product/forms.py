from django.forms import ModelForm, forms
from django import forms

from product.models import ColorModel


class ColorModelAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = ColorModel
        fields = ('name',)
