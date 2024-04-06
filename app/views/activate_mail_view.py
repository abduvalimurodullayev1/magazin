from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView
from app.forms.token import account_activation_token
from app.models.auth import User


class ActivateEmailView(TemplateView):
    template_name = 'app/auth/register.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('login')
        else:
            return HttpResponse('Activation link is invalid!')


class ActivatePasswordEmailView(TemplateView):
    template_name = 'app/auth/confirm_password_email.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('change-password')
        else:
            return HttpResponse('Activation link is invalid!')