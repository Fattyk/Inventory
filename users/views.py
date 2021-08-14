from django.http import request
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import RegistrationSerializer, UserDetailSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


@method_decorator(login_required, name='dispatch')
class UserDetails(generics.RetrieveUpdateAPIView):
    """Retrieve and Update Profile Information of the User and not of others"""
    queryset  = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        """Ensure that user cannot get or edit other users' info"""
        qs = super().get_queryset() 
        return qs.filter(pk=self.request.user.pk)


@api_view(['POST'])
@login_required
def change_password(request):
    """Update User's password"""

    if request.method == 'POST':
        # get the requirements to change password
        try:
            username = request.data['username']
            password = request.data['password']
            new_password = request.data['new_password']
            confirm_password = request.data['confirm_password']
        except:
            return Response({'error':'Wrong input'}, status=status.HTTP_400_BAD_REQUEST)

        # get the user from database
        user_to_change = authenticate(username=username, password=password)
        if not user_to_change:
            return Response({'error':'Wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)


        # check if the user match the request.user
        check = request.user == user_to_change
        if not check:
            return Response({'error':'Wrong username or password'}, status=status.HTTP_400_BAD_REQUEST)
        
        # check that new pasword and confirm_password are thesame
        if new_password != confirm_password:
            return Response({'error':'Password not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Change the password
        user_to_change.set_password(new_password)
        user_to_change.save()
        return Response({'message':'Password changed successfully'}, status=status.HTTP_200_OK)
