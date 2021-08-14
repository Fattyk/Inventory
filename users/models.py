"""
This model maintain information about users
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """Profile extends the default AbstractUser to add more fields"""
    middle_name = models.CharField(blank=True, max_length=150, null=True, verbose_name='middle name')
    mobile = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username}"