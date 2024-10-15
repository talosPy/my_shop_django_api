from rest_framework import serializers
from products.models import Product
from products.serializers import ProductSerializer
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Nested serializer
    # products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    
    class Meta:
        model = Cart
        fields = '__all__'