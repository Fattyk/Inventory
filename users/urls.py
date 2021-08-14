from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.UsersRegistration.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/', views.UserDetails.as_view(), name='user'),
    path('change_password/', views.change_password, name='change_password')
]