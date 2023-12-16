from rest_framework import serializers
from django.contrib.auth.models import User

from shop.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'image_url', 'description', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'total_amount',
            'shipping_address',
            'billing_address',
            'order_items'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')

        user = User.objects.get(id=1)

        order = Order.objects.create(user=user, **validated_data)

        for item in items_data:
            product = Product.objects.get(id=item.get('product_id'))
            OrderItem.objects.create(order=order, product=product, quantity=item.get('quantity'))

        return order

    def update(self, instance, validated_data):
        user = User.objects.get(id=1)

        items_data = validated_data.pop('order_items')
        instance.user = validated_data.get('user', user)
        instance.shipping_address = validated_data.get(
            'shipping_address',
            instance.shipping_address
        )
        instance.billing_address = validated_data.get(
            'billing_address',
            instance.billing_address
        )
        instance.save()

        instance.order_items.delete()
        for item in items_data:
            product = Product.objects.get(id=item.get('product_id'))
            OrderItem.objects.create(order=instance, product=product, quantity=item.get('quantity'))

        return instance
