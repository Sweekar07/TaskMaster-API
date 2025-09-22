from django.shortcuts import render

# Create your views here.
from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer, TaskStatusUpdateSerializer
from permissions import IsTaskOwnerOrAdmin, IsAdminOrReadOnly

class TaskListCreateView(generics.ListCreateAPIView):
    """List and create tasks"""
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'assigned_to']
    search_fields = ['title', 'description']

    def get_queryset(self):
        if self.request.user.is_admin:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrReadOnly()]
        return [IsTaskOwnerOrAdmin()]

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update and delete tasks"""
    serializer_class = TaskSerializer
    permission_classes = [IsTaskOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_admin:
            return Task.objects.all()
        return Task.objects.filter(assigned_to=self.request.user)

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminOrReadOnly()]
        return [IsTaskOwnerOrAdmin()]

class TaskStatusUpdateView(generics.UpdateAPIView):
    """Update task status (users can only update their own tasks)"""
    serializer_class = TaskStatusUpdateSerializer
    permission_classes = [IsTaskOwnerOrAdmin]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
