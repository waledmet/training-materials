"""
Blog Models – Week 6 Demo

Demonstrates:
- ForeignKey to the built-in User model (Lesson 7)
- Status choices (used in ModelForm ChoiceField)
- Meta class with ordering
- __str__ method
"""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    A blog post.
    Used with ModelForm (Lesson 3) and Class-Based Views (Lesson 11).
    """

    STATUS_DRAFT     = 'draft'
    STATUS_PUBLISHED = 'published'
    STATUS_CHOICES = [
        (STATUS_DRAFT,     'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    title      = models.CharField(max_length=200)
    content    = models.TextField()
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Newest first

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    def is_published(self):
        return self.status == self.STATUS_PUBLISHED
