from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from cart.models import Cart
from cart.serializers import CartSerializer

@api_view(['GET'])
def cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    serializer = CartSerializer(cart)
    return Response(serializer.data)