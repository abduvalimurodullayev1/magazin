from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models
from app.models.base import BaseModel


class Category(models.Model):
    title = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    image = models.ImageField(upload_to='product/%Y/%m/%d')
    title = models.CharField(max_length=155)
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE, related_name='product')
    review = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    category = models.ForeignKey(to='app.Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class Blog(BaseModel):
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    title = models.CharField(max_length=155)
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE, related_name="blogs")
    text = models.TextField()

    def __str__(self):
        return self.title


class Comment(BaseModel):
    text = models.TextField()
    user = models.ForeignKey(to='app.User', on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(to='app.Product', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Telefon raqamini to'g'ri formatda kiriting."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=13,
        verbose_name='Telefon raqami',
        help_text='Ishonchli telefon raqami'
    )
    subject = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.phone_number




