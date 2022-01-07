from rest_framework import serializers
from .models import Product
from category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'image', 'price', 'price_currency', 'quantity']
