from django.urls import path

from shop.views import ProductListView


urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='products-list'),
]
