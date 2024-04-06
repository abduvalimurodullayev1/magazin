from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginModelForm(AuthenticationForm):
    username = forms.CharField(required=False)
    email = forms.EmailField()
    password = forms.CharField(max_length=128)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(self.request,
                         email=email,
                         password=password)
            if self.user_cache:
                self.confirm_login_allowed(self.user_cache)
            else:
                raise self.get_invalid_login_error()

        return self.cleaned_data