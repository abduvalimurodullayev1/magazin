from django import forms
from app.models.other import Product


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ()



