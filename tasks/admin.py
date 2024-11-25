from django.contrib import admin
from allauth.socialaccount.models import SocialApp
from .models import Task  

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model
    """
    list_display = ('title', 'description', 'completed', 'created_at', 'updated_at')  
    list_filter = ('completed', 'created_at')  
    search_fields = ('title', 'description')  
    ordering = ('-created_at',)  
    readonly_fields = ('created_at', 'updated_at')  

