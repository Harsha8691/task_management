from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    """
    Represents a task associated with a user.
    """
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    completed = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
    )  # Associate task with a user

    class Meta:
        ordering = ['-created_at']  # Order tasks by newest first

    def __str__(self):
        return self.title  