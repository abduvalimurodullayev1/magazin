from django.db import models


class Wishlist(models.Model):
    user = models.ForeignKey(to='app.User',
                             on_delete=models.CASCADE,
                             related_name='wishlist')
    product = models.ManyToManyField(to='app.Product',
                                     related_name='products')


class ShoppingCart(models.Model):
    user = models.ForeignKey(to='app.User',
                             on_delete=models.CASCADE,
                             related_name='shoppings')
    product = models.ManyToManyField(to='app.Product',
                                     related_name='shoppings')


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey('app.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity