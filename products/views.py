from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

class CreateListItems(generics.ListCreateAPIView):
    """This create and list all items"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserItem(generics.RetrieveUpdateDestroyAPIView):
    """This item can be retrieve, updated and deleted by the owner"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Ensure that user cannot get, edit or delete other users' item"""
        qs = super().get_queryset() 
        return qs.filter(user=self.request.user)


class Detail(generics.RetrieveAPIView):
    """This item can be retrieve only"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer