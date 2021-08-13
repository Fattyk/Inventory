from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """Profile extends the default AbstractUser to add more fields"""
    middle_name = models.CharField(blank=True, max_length=150, verbose_name='middle name')
    mobile = models.CharField(max_length=20, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} {self.mobile}"

class Product(models.Model):
    """Product is the model that contains items' fields"""
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User, verbose_name='user id', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"