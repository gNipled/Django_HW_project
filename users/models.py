from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    is_active = models.BooleanField(verbose_name='active', default=False)

    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='phone number', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='country', **NULLABLE)
    verification_key = models.CharField(max_length=15, verbose_name='verification key', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
