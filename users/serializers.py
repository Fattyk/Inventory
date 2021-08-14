"""
This serializer file contain classes that helps to serializer and deserialize data into required formats
"""

from rest_framework import serializers
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','middle_name','last_name','email','password','mobile','birth_date']
        

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','middle_name','last_name','email','mobile','birth_date']