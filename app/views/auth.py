from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms.login_form import LoginModelForm
from app.forms.register_form import RegisterModelForm
from app.forms.send_email_form import send_email, send_forget_password_mail
from app.models.auth import User


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            form = RegisterModelForm(request.POST)
            if form.is_valid():
                form.save()
                send_email(email=form.data.get('email'),
                           request=request,
                           _type='register')
                messages.add_message(
                    request=request,
                    level=messages.WARNING,
                    message="Successfully send your email, please activate your profile"
                )
                return redirect('register')
        else:
            form = RegisterModelForm()
    return render(request=request,
                  template_name='app/auth/register.html',
                  context={"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginModelForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request=request,
                      user=user)
                return redirect('index')
        else:
            form = LoginModelForm()
    return render(request=request,
                  template_name='app/auth/login.html',
                  context={"form":form})


@login_required(login_url='login')
def confirm_email_password_view(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email')

            if not User.objects.filter(email=email).first():
                messages.success(request=request, message='Bunaqa email bazada yo\'q')
                return redirect('confirm-email-password')

            user = User.objects.get(email=email)
            send_forget_password_mail(email=user, request=request)
            messages.success(request=request,
                             message="xabar emailingiz bordi, iltimos tasdiqlab yuboring")
            return redirect('confirm-email-password')
    except Exception as e:
        print(e)

    return render(request=request,
                  template_name='app/auth/confirm_password_email.html')


@login_required(login_url='login')
def change_password(request):
    user_id = request.user.id
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if user_id is None:
            messages.success(request, 'User is not found')
            return redirect('confirm-email-password')

        if new_password != confirm_password:
            messages.success(request, 'both should be equal')
            return redirect('change-password')

        user = User.objects.get(id=user_id)
        user.set_password(new_password)
        user.save()
        return redirect('login')
    return render(request, 'app/auth/change_password.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request=request)
    return redirect('index')
