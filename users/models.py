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