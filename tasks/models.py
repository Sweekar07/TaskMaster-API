from django.db import models

# Create your models here.
from django.conf import settings

class Task(models.Model):
    """Task model for the task management system"""
    
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'
    
    STATUS_CHOICES = [
        (TODO, 'To-Do'),
        (IN_PROGRESS, 'In-Progress'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=TODO)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.PROTECT,
        related_name='assigned_tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"

    @property
    def assigned_to_inactive(self):
        """Check if the assigned user is inactive (soft deleted)"""
        return not self.assigned_to.is_active
