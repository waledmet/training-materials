"""
Week 7 URL Configuration

Shows three URL namespaces side by side:
  /          → Django template home page (Day 1 - baseline)
  /api/      → DRF REST API endpoints   (Day 2-3)
  /admin/    → Django admin
  /api-auth/ → DRF browsable API login  (Lesson 5 bonus)
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # DRF browsable API login/logout (Lesson 5)
    # Visit /api-auth/login/ to log in within the browsable API
    path('api-auth/', include('rest_framework.urls')),

    # All task routes (API + template views)
    path('', include('tasks.urls')),
]
