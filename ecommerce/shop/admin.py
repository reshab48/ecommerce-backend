from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
