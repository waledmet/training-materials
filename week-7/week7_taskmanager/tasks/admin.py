"""
Admin Registration – Week 7 Demo
Register Task with a custom ModelAdmin so the admin panel is useful during lecture.
"""

from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display  = ('title', 'priority', 'completed', 'created_at')
    list_filter   = ('completed', 'priority')
    search_fields = ('title', 'description')
    list_editable = ('completed',)
    ordering      = ('-created_at',)
