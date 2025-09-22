from django.urls import path
from .views import RegisterView, LoginView, UserListView, UserSoftDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/soft-delete/', UserSoftDeleteView.as_view(), name='user-soft-delete'),
]
