"""
This model maintain information about products
"""

from django.db import models
from users.models import User


# Create your models here.

class Product(models.Model):
    """Product is the model that contains items' fields"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, verbose_name='user id', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"