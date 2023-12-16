from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=512)
    image_url = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        User,
        related_name='orders',
        related_query_name='order',
        on_delete=models.CASCADE
    )
    total_amount = models.DecimalField(
        max_digits=20, decimal_places=2
    )
    shipping_address = models.TextField()
    billing_address = models.TextField()

    def __str__(self) -> str:
        return f'Order #{self.id}, User: {str(self.user)}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='order_items',
        related_query_name='order_item',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        related_query_name='order_item',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f'{str(self.order)}, quantity: {self.quantity}'
