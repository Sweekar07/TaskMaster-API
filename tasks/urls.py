from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TaskStatusUpdateView
from comments.views import CommentListCreateView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/status/', TaskStatusUpdateView.as_view(), name='task-status-update'),
    path('<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
