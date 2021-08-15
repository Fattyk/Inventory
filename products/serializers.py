from rest_framework import serializers
from products.models import Product, SearchHistory


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'user']

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['history', 'created']