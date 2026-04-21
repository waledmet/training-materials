"""
Task URLs – Week 7 Demo

Shows the URL evolution across days:

  Day 1: Manual JsonResponse endpoint
  Day 2: @api_view function-based endpoints
  Day 3: Router auto-generates all /api/tasks/ URLs from the ViewSet
  Day 4/5: Home page served to the JavaScript frontend

Trainer Note:
  Point out that the Router replaces all the manual path() entries
  students saw on Day 2. One register() call = 6+ endpoints.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


# ─── Lesson 8 / Day 3: Router + ViewSet ──────────────────────────────────────
# Registering TaskViewSet creates these URLs automatically:
#   GET/POST  /api/tasks/
#   GET/PUT/PATCH/DELETE  /api/tasks/<pk>/
#   POST      /api/tasks/<pk>/toggle/
#   GET       /api/tasks/stats/
#   POST      /api/tasks/clear-completed/
#   GET       /api/tasks/?completed=true  (filtered)
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')


urlpatterns = [
    # ── Home page (Day 4/5 JavaScript frontend) ───────────────────────────────
    path('', views.home, name='home'),

    # ── Day 1: Manual JSON endpoint (before DRF) ──────────────────────────────
    path('api/tasks-json/', views.api_tasks_json, name='tasks_json'),

    # ── Day 2: @api_view function-based endpoints ─────────────────────────────
    path('api/v1/tasks/',       views.api_task_list,   name='task_list_fbv'),
    path('api/v1/tasks/<int:pk>/', views.api_task_detail, name='task_detail_fbv'),

    # ── Day 3: ViewSet via Router (main API used by the frontend) ─────────────
    path('api/', include(router.urls)),
]
