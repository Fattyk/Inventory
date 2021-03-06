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
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='user id', on_delete=models.CASCADE, related_name='products')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"

    def __unique_code__(self):
        return hash(self.user.password)

class SearchHistory(models.Model):
    searcher = models.ForeignKey(User, blank=True, null=True, verbose_name='searcher id', on_delete=models.CASCADE, related_name='search_history')
    history = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.history} {self.created}"
