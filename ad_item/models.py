from datetime import timezone

from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity_available = models.PositiveIntegerField(default=1)
    item_value = models.PositiveIntegerField(default=0)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    address = models.TextField()
    collateral_required = models.BooleanField(default=False)
    collateral_types = models.ManyToManyField('Collateral', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items', null=True, blank=True , default=1)  # تغییر به null=True
    latitude = models.FloatField(null=True, blank=True)  # عرض جغرافیایی
    longitude = models.FloatField(null=True, blank=True)  # طول جغرافیایی

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', max_length=200)


class Collateral(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
