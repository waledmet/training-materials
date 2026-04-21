"""
Task Model – Week 7 Demo

Demonstrates:
  - Simple model suitable for a REST API            (Lesson 1)
  - BooleanField for task completion status         (Day 1)
  - Priority choices                                (shown on Day 3)
  - Meta ordering and __str__                       (recap from Week 5)

Trainer Note: Keep the model simple so students focus on DRF, not Django ORM.
"""

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    A single to-do task.
    Exposed as a full REST API via DRF ViewSet (Lesson 8).
    """

    PRIORITY_LOW    = 'low'
    PRIORITY_MEDIUM = 'medium'
    PRIORITY_HIGH   = 'high'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW,    'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_HIGH,   'High'),
    ]

    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    completed   = models.BooleanField(default=False)
    priority    = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=PRIORITY_MEDIUM,
    )
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        status = '✓' if self.completed else '○'
        return f"[{status}] {self.title} ({self.priority})"
