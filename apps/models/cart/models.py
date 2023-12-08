from __future__ import unicode_literals

from django.db import models

from apps.models.product.models import Product
from apps.user.models import User


class CartItem(models.Model):
    """
    Select items for shopping cart
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        related_name='product'
    )
    count = models.IntegerField(default=1, null=True)
    is_ordered = models.BooleanField(default=False, null=True)
    date_added = models.DateTimeField(auto_now=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    """
    Making a shopping cart with all the selected products
    """
    ref_code = models.CharField(max_length=15, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='user'
    )
    is_ordered = models.BooleanField(default=False, null=True)
    items = models.ForeignKey(
        CartItem,
        related_name='cart_item',
        on_delete=models.CASCADE,
        null=True
    )
    date_ordered = models.DateTimeField(auto_now=True, null=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price * item.count for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


class Transaction(models.Model):
    """
    Save customer order information
    """
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transaction_user',
        null=True
    )
    token = models.CharField(max_length=120, null=True)
    order_id = models.CharField(max_length=120, null=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

    def __str__(self):
        return self.order_id

    class Meta:
        ordering = ['-timestamp']
