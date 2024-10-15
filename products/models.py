from django.db import models
from cart.models import Cart

class Category(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.popularity}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category,related_name="products")
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    cart = models.ManyToManyField(Cart,related_name="products")


    def __str__(self):
        return f"{self.name} - {self.price}"