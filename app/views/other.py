from django.shortcuts import render


def about_us_view(request):
    return render(request=request,
                  template_name='app/about-us.html')


def contact_view(request):
    return render(request=request,
                  template_name='app/contact.html')


def checkout_view(request):
    return render(request=request,
                  template_name='app/checkout.html')


def view_404(request):
    return render(request=request,
                  template_name='app/404.html')