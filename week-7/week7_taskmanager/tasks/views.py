"""
Task Views – Week 7 Demo

Demonstrates the FULL progression of API views (one per day):

  Day 1 – Manual JsonResponse (Lesson 4)
    api_tasks_json        – GET list with plain JsonResponse

  Day 2 – DRF @api_view (Lesson 7)
    api_task_list         – GET + POST with @api_view
    api_task_detail       – GET + PUT + DELETE with @api_view

  Day 3 – DRF ViewSet + Router (Lesson 8)
    TaskViewSet           – full CRUD in 5 lines + custom actions

  Day 4 / 5 – Template view served to JavaScript frontend
    home                  – renders the SPA-style page (Day 4-5)

Trainer Note:
  Walk through each style in order.
  The final product uses TaskViewSet + the home() template.
  Keep older views in the file so students can compare.
"""

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 4 / Day 1 – Manual JsonResponse (before DRF)
# Show this first to illustrate why DRF is needed.
# ═════════════════════════════════════════════════════════════════════════════

def api_tasks_json(request):
    """
    GET /api/tasks-json/
    Returns tasks as JSON without any DRF.
    Lesson 4: JsonResponse, manual serialization.
    Problem: tedious, no validation, no browsable API.
    """
    tasks = Task.objects.all()
    data = []
    for task in tasks:
        data.append({
            'id':          task.id,
            'title':       task.title,
            'description': task.description,
            'completed':   task.completed,
            'priority':    task.priority,
            'created_at':  task.created_at.isoformat(),
        })
    return JsonResponse({'tasks': data, 'count': len(data)})


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 7 / Day 2 – @api_view (Function-Based API Views)
# Introduce DRF here. Show the browsable API instantly.
# ═════════════════════════════════════════════════════════════════════════════

@api_view(['GET', 'POST'])
def api_task_list(request):
    """
    GET  /api/v1/tasks/   → list all tasks
    POST /api/v1/tasks/   → create a new task

    Lesson 7: @api_view decorator, request.data, Response, status codes.
    """
    if request.method == 'GET':
        tasks      = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_task_detail(request, pk):
    """
    GET    /api/v1/tasks/<pk>/  → retrieve one task
    PUT    /api/v1/tasks/<pk>/  → full update
    PATCH  /api/v1/tasks/<pk>/  → partial update
    DELETE /api/v1/tasks/<pk>/  → delete

    Lesson 7: HTTP method dispatch, 404 handling, partial=True.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        partial    = request.method == 'PATCH'
        serializer = TaskSerializer(task, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ═════════════════════════════════════════════════════════════════════════════
# Lesson 8 / Day 3 – ModelViewSet + Routers  ← the star of the show
# Compare to the 50+ lines above: this does the same with 5 lines!
# ═════════════════════════════════════════════════════════════════════════════

class TaskViewSet(viewsets.ModelViewSet):
    """
    Full CRUD API for Task, registered with a Router in urls.py.
    Lesson 8: ModelViewSet, queryset, serializer_class.

    Auto-generated endpoints (via DefaultRouter):
      GET    /api/tasks/          list
      POST   /api/tasks/          create
      GET    /api/tasks/<id>/     retrieve
      PUT    /api/tasks/<id>/     update
      PATCH  /api/tasks/<id>/     partial update
      DELETE /api/tasks/<id>/     destroy

    Plus browsable API at each URL!
    """
    queryset         = Task.objects.all()
    serializer_class = TaskSerializer

    # ── Lesson 8: Filtering via query params ─────────────────────────────────
    def get_queryset(self):
        """
        Optional query params:
          ?completed=true   → filter completed tasks
          ?completed=false  → filter pending tasks
          ?priority=high    → filter by priority
        """
        qs = Task.objects.all()

        completed = self.request.query_params.get('completed')
        if completed is not None:
            qs = qs.filter(completed=(completed.lower() == 'true'))

        priority = self.request.query_params.get('priority')
        if priority:
            qs = qs.filter(priority=priority)

        return qs

    # ── Lesson 8: Custom Action ───────────────────────────────────────────────
    @action(detail=True, methods=['post'], url_path='toggle')
    def toggle_complete(self, request, pk=None):
        """
        POST /api/tasks/<id>/toggle/
        Toggles the completed status of a task.
        Lesson 8: @action decorator, detail=True, custom URL path.
        """
        task           = self.get_object()
        task.completed = not task.completed
        task.save()

        serializer = self.get_serializer(task)
        return Response({
            'message':   f"Task {'completed' if task.completed else 'reopened'}.",
            'task':      serializer.data,
        })

    # ── Lesson 8: Custom list action ─────────────────────────────────────────
    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        """
        GET /api/tasks/stats/
        Returns a summary of task counts.
        Lesson 8: detail=False custom action (operates on the collection).
        """
        qs        = self.get_queryset()
        total     = qs.count()
        completed = qs.filter(completed=True).count()
        pending   = qs.filter(completed=False).count()

        by_priority = {}
        for p, label in Task.PRIORITY_CHOICES:
            by_priority[p] = qs.filter(priority=p).count()

        return Response({
            'total':       total,
            'completed':   completed,
            'pending':     pending,
            'by_priority': by_priority,
        })

    # ── Lesson 8: Bulk action ─────────────────────────────────────────────────
    @action(detail=False, methods=['post'], url_path='clear-completed')
    def clear_completed(self, request):
        """
        POST /api/tasks/clear-completed/
        Deletes all completed tasks.
        Lesson 8: Another custom collection action.
        """
        deleted_count, _ = Task.objects.filter(completed=True).delete()
        return Response({
            'message': f"Deleted {deleted_count} completed task(s).",
            'deleted': deleted_count,
        })


# ═════════════════════════════════════════════════════════════════════════════
# Template view – served to the JavaScript frontend (Day 4 / 5)
# ═════════════════════════════════════════════════════════════════════════════

def home(request):
    """
    Renders the Task Manager SPA page.
    Day 4-5: The JavaScript on this page calls /api/tasks/ via fetch().
    """
    return render(request, 'home.html')
