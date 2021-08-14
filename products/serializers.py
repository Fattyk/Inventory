from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'user']