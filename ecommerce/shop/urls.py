from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shop.views import ProductListView, OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='products-list'),
    path('', include(router.urls)),
]
