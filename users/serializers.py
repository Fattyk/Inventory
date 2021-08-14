"""
This serializer file contain classes that helps to serializer and deserialize data into required formats
"""

from products.models import Product
from rest_framework import serializers
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name','middle_name','last_name','email','password','mobile','birth_date']

    def create(self, validated_data):
        """
        Overide the create instance to hash the password
        """
        
        user = User.objects.create(**validated_data)
        password = validated_data.get("password")
        user.set_password(password)
        user.save()
        return user
        

class UserDetailSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ['username', 'first_name','middle_name','last_name','email','mobile','birth_date', 'products']