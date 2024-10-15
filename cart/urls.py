
from django.contrib import admin
from django.urls import include, path

from cart import views

urlpatterns = [
    path('<int:id>/', views.cart, name="cart"),
]
