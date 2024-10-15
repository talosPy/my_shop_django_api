from django.db import models

class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

