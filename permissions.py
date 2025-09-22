from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not request.user.is_active:
            return False
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_admin

class IsTaskOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow task owners or admins to view/edit tasks.
    """
    
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return obj.assigned_to == request.user

class IsCommentAuthorOrAdmin(permissions.BasePermission):
    """
    Custom permission for comments.
    """
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not request.user.is_active:
            return False
        
        # For POST requests (creating comments), check if user can access the task
        if request.method == 'POST':
            task_id = view.kwargs.get('task_id')
            if task_id:
                from tasks.models import Task
                try:
                    task = Task.objects.get(id=task_id)
                    # Admin can comment on any task, users only on their assigned tasks
                    return request.user.is_admin or task.assigned_to == request.user
                except Task.DoesNotExist:
                    return False
        
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        # Users can only view/edit comments on their own tasks
        return obj.task.assigned_to == request.user
