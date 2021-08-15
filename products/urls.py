from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Products.as_view(), name='index'),
    path('create/', views.CreateItems.as_view(), name='create'),
    path('myitem/<int:pk>/', views.UserItem.as_view(), name='add_item'),
    path('<int:pk>/', views.Detail.as_view(), name='add_item')
]