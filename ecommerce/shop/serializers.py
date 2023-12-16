from rest_framework import serializers

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
