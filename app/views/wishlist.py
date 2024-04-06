from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.models.billing import Wishlist
from app.models.other import Product


# @login_required(login_url='login')
# def add_wishlist_view(request, product_id):
#     if request.method == "POST":
#         pro_id = int(request.POST.get('product_id'))
#         product = Product.objects.filter(id=pro_id).first()
#         if product:
#             if Wishlist.objects.filter(user=request.user, product=pro_id):
#                 messages.error(request=request,
#                                message="Product already in wishlist")
#                 return redirect('shop-details', product_id)
#             else:
#                 Wishlist.objects.create(user=request.user, product=pro_id)
#                 return redirect('wishlist')
#         else:
#             messages.error(request=request,
#                            message="Product is not found")
#             return redirect('shop-details', product_id)


@login_required(login_url='login')
def add_wishlist_view(request, product_id):
    # product = Product.objects.get(pk=product_id)
    product = get_object_or_404(klass=Product, pk=product_id)
    user = request.user # Agar foydalanuvchilar uchun autentifikatsiya muvaffaqiyatli bo'lsa

    # Wishlist obyektini foydalanuvchiga mos kelishiga tekshirish (mumkin)
    wishlist, created = Wishlist.objects.get_or_create(user=user)

    wishlist.product.add(product)
    return redirect('wishlist')


@login_required(login_url='login')
def wishlist_view(request):
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        products = wishlist.products.all()  # Assuming 'products' is the related name for the ManyToManyField or ForeignKey

    except Wishlist.DoesNotExist:
        products = []  # If wishlist doesn't exist for the user, return an empty list of products

    return render(request=request,
                  template_name='app/wishlist.html',
                  context={'products': products})

def delete_from_wishlist(request, product_id):
    user = request.user # Agar foydalanuvchilar uchun autentifikatsiya muvaffaqiyatli bo'lsa

    try:
        wishlist = Wishlist.objects.filter(user=user).first()
        product = Product.objects.get(pk=product_id)
        wishlist.product.remove(product)
    except (Wishlist.DoesNotExist, Product.DoesNotExist):
        pass

    return redirect('wishlist')