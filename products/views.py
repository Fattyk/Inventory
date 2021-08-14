from users import serializers
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

class CreateListItems(generics.CreateAPIView):
    """This create and list all items"""
    models: Product.objects.all()
    serializer_class: ProductSerializer


class UserItem(generics.RetrieveUpdateDestroyAPIView):
    """This item can be retrieve, updated and deleted by the owner"""
    models: Product.objects.all()
    serializer_class: ProductSerializer

    def get_queryset(self):
        """Ensure that user cannot get, edit or delete other users' item"""
        qs = super().get_queryset() 
        return qs.filter(user=self.request.user)


class Detail(generics.RetrieveAPIView):
    """This item can be retrieve only"""
    models: Product.objects.all()
    serializer_class: ProductSerializer