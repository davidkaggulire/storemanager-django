from django.db import models
from store.products.models import Product

# Create your models here.
class Sale(models.Model):
    product = models.ForeignKey(
        Product, null=False, on_delete=models.CASCADE)
    total = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
