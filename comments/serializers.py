from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model"""
    author_email = serializers.SerializerMethodField()
    task_id = serializers.ReadOnlyField(source='task.id')

    class Meta:
        model = Comment
        fields = ('id', 'task_id', 'author', 'author_email', 'text', 'created_at')
        read_only_fields = ('id', 'task_id', 'author', 'created_at')

    def get_author_email(self, obj):
        return obj.author.email
