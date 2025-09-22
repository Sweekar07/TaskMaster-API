from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Comment
from tasks.models import Task
from .serializers import CommentSerializer
from permissions import IsCommentAuthorOrAdmin

class CommentListCreateView(generics.ListCreateAPIView):
    """List and create comments for a specific task"""
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrAdmin]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        if self.request.user.is_admin:
            return Comment.objects.filter(task_id=task_id)
        return Comment.objects.filter(task_id=task_id, task__assigned_to=self.request.user)

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']

        # Verify task exists and user has permission
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {'error': 'Task not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Check if user can comment on this task
        if not self.request.user.is_admin and task.assigned_to != self.request.user:
            return Response(
                {'error': 'You can only comment on tasks assigned to you'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer.save(author=self.request.user, task_id=task_id)
