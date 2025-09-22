from rest_framework import serializers
from .models import Task
from accounts.models import User

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model"""
    assigned_to_inactive = serializers.ReadOnlyField()
    assigned_to_email = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'assigned_to', 
                 'assigned_to_email', 'assigned_to_inactive', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_assigned_to_email(self, obj):
        return obj.assigned_to.email if obj.assigned_to else None

class TaskStatusUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating task status"""
    class Meta:
        model = Task
        fields = ('status',)
