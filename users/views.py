from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users import serializers
from users.models import User
from users.serializers import RegistrationSerializer, PasswordSerializer, UserDetailSerializer
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class UsersRegistration(APIView):
    """Registration of User"""

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.login_user(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error':'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

    def login_user(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

@api_view(['POST'])
def login_view(request):
    """Verify and login user"""

    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error':'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def logout_view(request):
    """Logout User"""
    logout(request)
    return Response(status=status.HTTP_200_OK)


class UserDetails(generics.RetrieveUpdateAPIView):
    """Retrieve and Update Profile Information"""
    queryset  = User.objects.all()
    serializer_class = UserDetailSerializer


# def ChangePassword(request):
#     """Update User's password"""

#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         if password != confirm_password:
#             return Response({'error':'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return Response(status=status.HTTP_200_OK)
#         return Response({'error':'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)    
