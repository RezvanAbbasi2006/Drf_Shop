from django.contrib.auth import get_user_model
from django.db import models

from apps.core.models import BaseModel
from apps.models.product.models import Product

User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    is_active = models.BooleanField(default=True)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.__str__()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    total_price = models.FloatField(max_length=50, blank=True)
    count = models.IntegerField(default=1)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cart.customer} - {self.product}"

    def get_total_price(self):
        return self.count * self.product.price


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transaction')
    cart_id = models.CharField(max_length=120)
    token = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=100)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cart_id} is transacting.'

    class Meta:
        ordering = ['-timestamp']


class MetaNew(BaseModel):
    pass


