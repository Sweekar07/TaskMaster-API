from django.db import models

# Create your models here.
from django.conf import settings

class Comment(models.Model):
    """Comment model for task comments"""
    
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author.email} on {self.task.title}"
