from django import forms
from django.core.exceptions import ValidationError
from django.db.transaction import atomic

from app.models.auth import User


class RegisterModelForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=128)
    confirm_password = forms.CharField(max_length=128)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email already exists')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Confirm password is wrong")
        return password

    @atomic
    def save(self):
        user = User.objects.create_user(
            email=self.cleaned_data.get('email'),
            is_active=False
        )
        user.set_password(self.cleaned_data.get('password'))
        user.save()




