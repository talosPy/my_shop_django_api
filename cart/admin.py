from django.contrib import admin
from .models import Cart

class ProductInline(admin.TabularInline):
    model = Cart.products.through  # Use the through model for ManyToManyField
    extra = 1  # Number of empty forms to display

class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInline]

admin.site.register(Cart, CartAdmin)
# admin.site.register(Product)