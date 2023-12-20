from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass



class UserRole(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('seller', 'Seller')
    ]

    role = models.CharField(choices=ROLE_CHOICES, max_length=100, null=True)


    def __str__(self):
        return self.role

