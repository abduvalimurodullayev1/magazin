from django.contrib import admin

from app.models.auth import User
from app.models.billing import Wishlist, ShoppingCart, ShoppingCartItem
from app.models.other import Product, Category, Contact, Blog, Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Wishlist)
admin.site.register(User)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)