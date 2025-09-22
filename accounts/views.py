from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserRegistrationSerializer, UserSerializer, LoginSerializer
from permissions import IsAdminOrReadOnly

class RegisterView(generics.CreateAPIView):
    """User registration view"""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    """User login view"""
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })

class UserListView(generics.ListAPIView):
    """Admin-only view to list all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]

class UserSoftDeleteView(generics.UpdateAPIView):
    """Admin-only view to soft delete users"""
    queryset = User.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        user.soft_delete()
        return Response({'message': 'User soft deleted successfully'}, status=status.HTTP_200_OK)
