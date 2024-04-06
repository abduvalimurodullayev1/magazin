from django.urls import path
from app.views.activate_mail_view import ActivateEmailView, ActivatePasswordEmailView
from app.views.auth import register_view, login_view, logout_view, confirm_email_password_view, change_password
from app.views.shopping_cart import add_shopping_view, shopping_cart_view, delete_shopping_view
from app.views.wishlist import wishlist_view, add_wishlist_view, delete_from_wishlist
from app.views.blog import blog_list_view, blog_details_view
from app.views.comment import new_comment, delete_comment
from app.views.other import about_us_view, contact_view, checkout_view, view_404
from app.views.shop import index_view, shop_view, shop_details_view, add_product, edit_product, delete_product

urlpatterns = [
    path('', index_view, name='index'),
    path('shop-list/', shop_view, name='shop-list'),
    path('shop-details/<int:product_id>', shop_details_view, name='shop-details'),
    path('add-product/', add_product, name='add-product'),
    path('edit-product/<int:product_id>', edit_product, name='edit-product'),
    path('delete-product/<int:product_id>', delete_product, name='delete-product'),

    path('<int:product_id>/add-comment', new_comment, name='add-comment'),
    path('<int:product_id>/delete-comment/<int:comment_id>', delete_comment, name='delete-comment'),

    path('blog-list/', blog_list_view, name='blog-list'),
    path('blog-details/<int:blog_id>', blog_details_view, name='blog-details'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<str:uid>/<str:token>', ActivateEmailView.as_view(), name='activate-mail'),
    path('confirm-email-password/', confirm_email_password_view, name='confirm-email-password'),
    path('activate_password/<str:uid>/<str:token>', ActivatePasswordEmailView.as_view(), name='activate-password'),
    path('change-password/', change_password, name='change-password'),

    path('about-us/', about_us_view, name='about-us'),
    path('contact/', contact_view, name='contact'),
    path('checkout/', checkout_view, name='checkout'),
    path('404/', view_404, name='404'),

    path('wishlist/', wishlist_view, name='wishlist'),
    path('add-wishlist/<int:product_id>', add_wishlist_view, name='add-wishlist'),
    path('delete-wishlist/<int:product_id>', delete_from_wishlist, name='delete-wishlist'),

    path('shopping-cart/', shopping_cart_view, name='shopping-cart'),
    path('add-shopping-cart/<int:product_id>', add_shopping_view, name='add-shopping-cart'),
    path('delete-shopping-cart/<int:product_id>', delete_shopping_view, name='delete-shopping-cart'),
]