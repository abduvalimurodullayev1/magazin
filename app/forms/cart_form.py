from django import forms

from app.models.billing import ShoppingCart


class ShoppingCartModelForm(forms.ModelForm):

    class Meta:
        model = ShoppingCart
        exclude = ()