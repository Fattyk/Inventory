from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateListItems.as_view(), name='index'),
    path('myitem/<int:pk>/', views.UserItem.as_view(), name='add_item'),
    path('<int:pk>/', views.Detail.as_view(), name='add_item')
]