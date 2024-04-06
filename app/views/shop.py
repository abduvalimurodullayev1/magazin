from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from app.forms.shop_form import ProductModelForm
from app.models.auth import User
from app.models.other import Product, Category, Comment


def index_view(request):
    products = Product.objects.order_by('-created_at')
    laptops = Product.objects.filter(category__title='laptop').all()
    tvs = Product.objects.filter(category__title='TV').all()
    best_products = Product.objects.order_by('-price')
    return render(request=request,
                  template_name='app/index.html',
                  context={"products":products,
                           "laptops":laptops,
                           "tvs":tvs,
                           "best_products":best_products},)


def shop_view(request):
    categories = Category.objects.all()
    # Pagination start
    products_sort_created = Product.objects.order_by('-created_at')
    paginator = Paginator(products_sort_created, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    # Pagination end
    query = request.GET.get("query")
    if request.GET.get('sort_by') == 'title':
        products = Product.objects.order_by('title')[:9]
    elif request.GET.get('sort_by') == 'price':
        products = Product.objects.order_by('price')[:9]
    if query:
        products = products_sort_created.filter(Q(title__icontains=query))
    return render(request=request,
                  template_name='app/shop/shop_list.html',
                  context={"products":products,
                           "categories":categories})


def shop_details_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    comments = Comment.objects.filter(product_id=product.id).all()
    return render(request=request,
                  template_name='app/shop/shop_details.html',
                  context={"product": product,
                           "comments":comments})


def add_product(request):
    users = User.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop-list')
    form = ProductModelForm()
    return render(request=request,
                  template_name='app/shop/add_product.html',
                  context={"form":form,
                           "users":users,
                           "categories":categories})


def edit_product(request, product_id):
    users = User.objects.all()
    categories = Category.objects.all()
    product = Product.objects.filter(id=product_id).first()
    if product.user == request.user:
        
        if request.method == "POST":
            form = ProductModelForm(data=request.POST,
                                    files=request.FILES,
                                    instance=product)
            if form.is_valid():
                form.save()
                return redirect("shop-details", product.id)
    else:
        messages.error(request=request,
                       message="Iltimos o'zingiz")
    form = ProductModelForm(instance=product)
    return render(request=request,
                  template_name='app/shop/edit_product.html',
                  context={"form":form,
                           "users":users,
                           "categories":categories})


def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if product:
        product.delete()
        return redirect('shop-list')

