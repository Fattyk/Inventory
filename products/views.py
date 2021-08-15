from rest_framework import generics
from products.models import Product, SearchHistory
from products.serializers import ProductSerializer, SearchHistorySerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.

class ItemHistory(generics.ListAPIView):
    """List search item history"""
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer

    def get_queryset(self):
        """Ensure that history of user are return"""
        qs = super().get_queryset() 
        return qs.filter(searcher=self.request.user)


class Products(generics.ListAPIView):
    """List all items and enable search with 'search' parameter"""
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Queryset to search"""
        query = self.request.GET.get('search')
        quantity = self.request.GET.get('quantity')

        if query:
            # Search for item and capture user search if user is authenticated
            if self.request.user.is_authenticated:
                data={'history':query}
                s = SearchHistorySerializer(data=data)
                if s.is_valid():
                    SearchHistory.objects.create(searcher=self.request.user, history=query)
            object_list = Product.objects.filter(
                Q(name__icontains=query) #| Q(price__icontains=query)
            )
            return object_list

        elif quantity:
            # Filter item based on quantity and capture user search if user is authenticated
            if self.request.user.is_authenticated:
                data={'history':quantity}
                s = SearchHistorySerializer(data=data)
                if s.is_valid():
                    SearchHistory.objects.create(searcher=self.request.user, history=quantity)
            object_list = Product.objects.filter(quantity=quantity)
            return object_list
        return Product.objects.all()



@method_decorator(login_required, name='dispatch')
class CreateItems(generics.CreateAPIView):
    """This create an item"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class UserItem(generics.RetrieveUpdateDestroyAPIView):
    """This item can be retrieve, updated and deleted by the owner
    name, price and quantity of this item can be modified by the owner
    """
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