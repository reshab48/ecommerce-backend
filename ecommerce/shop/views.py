from rest_framework import generics, viewsets

from shop.models import Product, Order
from shop.serializers import ProductSerializer, OrderSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
