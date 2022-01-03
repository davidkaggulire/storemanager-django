from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    price = MoneyField(max_digits=19, decimal_places=2, null=True, default_currency='UGX')
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
