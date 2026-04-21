# Week 8 Lessons – Final Project: Design & Build

Welcome to Week 8! This week, you'll design and implement a complete Django application from scratch. You'll apply everything you've learned: models, views, templates, forms, authentication, and APIs.

---

## Table of Contents

1. [Introduction to the Final Project](#1-introduction-to-the-final-project)
2. [Project Options](#2-project-options)
3. [Project Planning](#3-project-planning)
4. [Database Design](#4-database-design)
5. [Setting Up the Project](#5-setting-up-the-project)
6. [Building Models](#6-building-models)
7. [Creating Forms](#7-creating-forms)
8. [Implementing Views](#8-implementing-views)
9. [Building Templates](#9-building-templates)
10. [Adding Authentication](#10-adding-authentication)
11. [Adding API Endpoints](#11-adding-api-endpoints)
12. [Code Review Best Practices](#12-code-review-best-practices)
13. [Project: Task Manager](#13-project-task-manager)

---

## 1. Introduction to the Final Project

### Why a Final Project?

A final project helps you:
- **Apply all skills** learned in previous weeks
- **Build something real** you can show others
- **Experience full development** from planning to deployment
- **Identify gaps** in your knowledge
- **Gain confidence** as a Django developer

### What You'll Build

A complete web application with:
- User registration and authentication
- Database models and relationships
- CRUD operations (Create, Read, Update, Delete)
- Forms with validation
- Clean navigation and UI
- Optional: REST API

### Project Timeline

**Day 1:** Planning and database design
**Day 2:** Models, migrations, and admin
**Day 3:** Views and templates
**Day 4:** Authentication and forms
**Day 5:** Polish, testing, and presentation

---

## 2. Project Options

Choose one of the following projects (or propose your own):

### Option 1: Task Manager

**Description:** Users can manage their personal tasks.

**Features:**
- User registration/login
- Create, edit, delete tasks
- Task status (New, In Progress, Done)
- Due dates
- Task categories
- Dashboard with task counts

**Models:**
- User (built-in)
- Task
- Category

### Option 2: Student Management System

**Description:** Manage students, courses, and enrollments.

**Features:**
- Add/edit/delete students
- Create courses
- Enroll students in courses
- View student grades
- Course roster

**Models:**
- Student
- Course
- Enrollment

### Option 3: Support Ticket System

**Description:** Simple help desk for tracking support requests.

**Features:**
- Users create tickets
- Ticket status (Open, In Progress, Closed)
- Priority levels
- Comments on tickets
- Assigned support agent

**Models:**
- User (built-in)
- Ticket
- Comment

### Option 4: Personal Blog

**Description:** A blog platform with categories and comments.

**Features:**
- Write and publish posts
- Categories for posts
- Comments from users
- Author profiles
- Search functionality

**Models:**
- User (built-in)
- Post
- Category
- Comment

---

## 3. Project Planning

### Step 1: Define Requirements

Write down exactly what your application will do.

**Example for Task Manager:**
```
Functional Requirements:
1. Users can register and login
2. Users can create tasks with title, description, due date
3. Users can assign tasks to categories
4. Users can mark tasks as complete
5. Users can only see their own tasks
6. Dashboard shows task statistics

Non-Functional Requirements:
1. Clean, simple UI
2. Fast page loads
3. Mobile-friendly
```

### Step 2: Define User Stories

User stories describe features from the user's perspective.

**Format:** "As a [user], I want to [action] so that [benefit]."

**Examples:**
```
- As a user, I want to register so that I can use the app
- As a user, I want to create tasks so that I can track my work
- As a user, I want to see my tasks by status so that I know what to work on
- As a user, I want to mark tasks complete so that I can track progress
```

### Step 3: Plan Pages/URLs

List all pages your application will have.

**Example:**
```
/ - Home/Dashboard
/tasks/ - List all tasks
/tasks/create/ - Create new task
/tasks/<id>/ - Task detail
/tasks/<id>/edit/ - Edit task
/tasks/<id>/delete/ - Delete task
/categories/ - List categories
/login/ - Login page
/register/ - Registration page
/logout/ - Logout (redirect)
```

### Step 4: Sketch Wireframes

Draw simple layouts for your main pages.

```
+------------------+
| Task Manager     |
+------------------+
| [+ New Task]     |
+------------------+
| Tasks:           |
| [ ] Task 1       |
| [x] Task 2       |
| [ ] Task 3       |
+------------------+
```

---

## 4. Database Design

### Entity-Relationship Diagram (ERD)

Identify your models and their relationships.

**Task Manager ERD:**
```
User (Django built-in)
  |
  | 1:N (one user has many tasks)
  v
Task
  - id (auto)
  - title
  - description
  - status
  - due_date
  - created_at
  - user (FK to User)
  - category (FK to Category)
  |
  | N:1 (many tasks belong to one category)
  v
Category
  - id (auto)
  - name
  - user (FK to User)
```

### Relationship Types

**One-to-Many (1:N):**
- One user has many tasks
- One category has many tasks

```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

**Many-to-Many (N:N):**
- One student enrolled in many courses
- One course has many students

```python
class Student(models.Model):
    courses = models.ManyToManyField(Course)
```

### Database Design Tips

1. **Start simple** - You can always add fields later
2. **Use appropriate field types** - CharField, TextField, DateField, etc.
3. **Add indexes** for frequently queried fields
4. **Think about cascade behavior** - What happens when parent is deleted?
5. **Normalize** - Don't repeat data unnecessarily

---

## 5. Setting Up the Project

### Initial Setup

```bash
# Create directory
mkdir final_project
cd final_project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install Django
pip install django djangorestframework

# Create project
django-admin startproject config .

# Create main app
python manage.py startapp tasks
```

### Configure Settings

```python
# config/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tasks',
]

# Template directory
TEMPLATES = [
    {
        # ...
        'DIRS': [BASE_DIR / 'templates'],
        # ...
    },
]

# Authentication
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Project Structure

```
final_project/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── static/
│   └── css/
│       └── style.css
├── manage.py
└── requirements.txt
```

---

## 6. Building Models

### Task Manager Models

```python
# tasks/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def is_overdue(self):
        from django.utils import timezone
        if self.due_date and self.status != 'done':
            return self.due_date < timezone.now().date()
        return False
```

### Register in Admin

```python
# tasks/admin.py
from django.contrib import admin
from .models import Task, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'user', 'due_date']
    list_filter = ['status', 'priority', 'category']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 7. Creating Forms

### Task Forms

```python
# tasks/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Task description (optional)'
            }),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show user's categories
        self.fields['category'].queryset = Category.objects.filter(user=user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Category name'
            }),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
```

---

## 8. Implementing Views

### Function-Based Views

```python
# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Task, Category
from .forms import TaskForm, CategoryForm, CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Please login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    stats = {
        'total': tasks.count(),
        'new': tasks.filter(status='new').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'done': tasks.filter(status='done').count(),
    }
    recent_tasks = tasks[:5]
    return render(request, 'tasks/dashboard.html', {
        'stats': stats,
        'recent_tasks': recent_tasks,
    })


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    # Filter by status
    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)

    # Filter by category
    category = request.GET.get('category')
    if category:
        tasks = tasks.filter(category_id=category)

    categories = Category.objects.filter(user=request.user)

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'categories': categories,
        'current_status': status,
        'current_category': category,
    })


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user)
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Create Task'
    })


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'Edit Task'
    })


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if task.status == 'done':
        task.status = 'new'
    else:
        task.status = 'done'
    task.save()
    return redirect('task_list')
```

### Class-Based Views Alternative

```python
# tasks/views.py (using CBVs)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
```

---

## 9. Building Templates

### Base Template

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Task Manager{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .sidebar {
            min-height: calc(100vh - 56px);
            background-color: #f8f9fa;
        }
        .task-card {
            transition: transform 0.2s;
        }
        .task-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .status-new { border-left: 4px solid #ffc107; }
        .status-in_progress { border-left: 4px solid #17a2b8; }
        .status-done { border-left: 4px solid #28a745; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'dashboard' %}">Task Manager</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'dashboard' %}">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_list' %}">Tasks</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_create' %}">+ New Task</a>
                    </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <span class="nav-link">Hello, {{ user.username }}</span>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'login' %}">Login</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'register' %}">Register</a>
                    </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% if messages %}
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
        {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### Dashboard Template

```html
<!-- tasks/templates/tasks/dashboard.html -->
{% extends 'base.html' %}

{% block title %}Dashboard - Task Manager{% endblock %}

{% block content %}
<h1>Dashboard</h1>

<div class="row mt-4">
    <div class="col-md-3">
        <div class="card text-white bg-secondary">
            <div class="card-body text-center">
                <h2>{{ stats.total }}</h2>
                <p class="mb-0">Total Tasks</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-dark bg-warning">
            <div class="card-body text-center">
                <h2>{{ stats.new }}</h2>
                <p class="mb-0">New</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-info">
            <div class="card-body text-center">
                <h2>{{ stats.in_progress }}</h2>
                <p class="mb-0">In Progress</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-white bg-success">
            <div class="card-body text-center">
                <h2>{{ stats.done }}</h2>
                <p class="mb-0">Completed</p>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header d-flex justify-content-between align-items-center">
                <span>Recent Tasks</span>
                <a href="{% url 'task_create' %}" class="btn btn-primary btn-sm">+ New Task</a>
            </div>
            <div class="card-body">
                {% if recent_tasks %}
                <ul class="list-group list-group-flush">
                    {% for task in recent_tasks %}
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <a href="{% url 'task_detail' task.pk %}">{{ task.title }}</a>
                            {% if task.due_date %}
                            <small class="text-muted ms-2">Due: {{ task.due_date }}</small>
                            {% endif %}
                        </div>
                        <span class="badge bg-{% if task.status == 'new' %}warning{% elif task.status == 'in_progress' %}info{% else %}success{% endif %}">
                            {{ task.get_status_display }}
                        </span>
                    </li>
                    {% endfor %}
                </ul>
                {% else %}
                <p class="text-muted">No tasks yet. <a href="{% url 'task_create' %}">Create one!</a></p>
                {% endif %}
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">Quick Actions</div>
            <div class="card-body">
                <a href="{% url 'task_create' %}" class="btn btn-primary w-100 mb-2">Create New Task</a>
                <a href="{% url 'task_list' %}?status=new" class="btn btn-outline-warning w-100 mb-2">View New Tasks</a>
                <a href="{% url 'task_list' %}?status=in_progress" class="btn btn-outline-info w-100 mb-2">View In Progress</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Task List Template

```html
<!-- tasks/templates/tasks/task_list.html -->
{% extends 'base.html' %}

{% block title %}Tasks - Task Manager{% endblock %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h1>My Tasks</h1>
    <a href="{% url 'task_create' %}" class="btn btn-primary">+ New Task</a>
</div>

<!-- Filters -->
<div class="card mb-4">
    <div class="card-body">
        <div class="row">
            <div class="col-md-6">
                <label class="form-label">Filter by Status:</label>
                <div class="btn-group">
                    <a href="{% url 'task_list' %}" class="btn btn-outline-secondary {% if not current_status %}active{% endif %}">All</a>
                    <a href="?status=new" class="btn btn-outline-warning {% if current_status == 'new' %}active{% endif %}">New</a>
                    <a href="?status=in_progress" class="btn btn-outline-info {% if current_status == 'in_progress' %}active{% endif %}">In Progress</a>
                    <a href="?status=done" class="btn btn-outline-success {% if current_status == 'done' %}active{% endif %}">Done</a>
                </div>
            </div>
            <div class="col-md-6">
                <label class="form-label">Filter by Category:</label>
                <select class="form-select" onchange="location = this.value;">
                    <option value="{% url 'task_list' %}">All Categories</option>
                    {% for cat in categories %}
                    <option value="?category={{ cat.id }}" {% if current_category == cat.id|stringformat:"s" %}selected{% endif %}>
                        {{ cat.name }}
                    </option>
                    {% endfor %}
                </select>
            </div>
        </div>
    </div>
</div>

<!-- Task List -->
{% if tasks %}
<div class="row">
    {% for task in tasks %}
    <div class="col-md-6 col-lg-4 mb-3">
        <div class="card task-card status-{{ task.status }}">
            <div class="card-body">
                <h5 class="card-title">{{ task.title }}</h5>
                <p class="card-text text-muted">
                    {{ task.description|truncatewords:20 }}
                </p>
                <div class="d-flex justify-content-between align-items-center">
                    <span class="badge bg-{% if task.status == 'new' %}warning{% elif task.status == 'in_progress' %}info{% else %}success{% endif %}">
                        {{ task.get_status_display }}
                    </span>
                    {% if task.due_date %}
                    <small class="{% if task.is_overdue %}text-danger{% else %}text-muted{% endif %}">
                        Due: {{ task.due_date }}
                    </small>
                    {% endif %}
                </div>
                <div class="mt-3">
                    <a href="{% url 'task_detail' task.pk %}" class="btn btn-sm btn-outline-primary">View</a>
                    <a href="{% url 'task_update' task.pk %}" class="btn btn-sm btn-outline-secondary">Edit</a>
                    <a href="{% url 'task_toggle_status' task.pk %}" class="btn btn-sm btn-outline-{% if task.status == 'done' %}warning{% else %}success{% endif %}">
                        {% if task.status == 'done' %}Reopen{% else %}Complete{% endif %}
                    </a>
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% else %}
<div class="alert alert-info">
    No tasks found. <a href="{% url 'task_create' %}">Create your first task!</a>
</div>
{% endif %}
{% endblock %}
```

---

## 10. Adding Authentication

### URL Configuration

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
```

### Login Template

```html
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login - Task Manager{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6 col-lg-4">
        <div class="card">
            <div class="card-header">
                <h4 class="mb-0">Login</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" name="username" class="form-control" id="username" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" name="password" class="form-control" id="password" required>
                    </div>
                    {% if form.errors %}
                    <div class="alert alert-danger">
                        Invalid username or password.
                    </div>
                    {% endif %}
                    <button type="submit" class="btn btn-primary w-100">Login</button>
                </form>
            </div>
            <div class="card-footer text-center">
                Don't have an account? <a href="{% url 'register' %}">Register</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### Registration Template

```html
<!-- templates/registration/register.html -->
{% extends 'base.html' %}

{% block title %}Register - Task Manager{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6 col-lg-4">
        <div class="card">
            <div class="card-header">
                <h4 class="mb-0">Create Account</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {% for field in form %}
                    <div class="mb-3">
                        <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
                        {{ field }}
                        {% if field.errors %}
                        <div class="text-danger small">{{ field.errors|join:", " }}</div>
                        {% endif %}
                        {% if field.help_text %}
                        <small class="text-muted">{{ field.help_text }}</small>
                        {% endif %}
                    </div>
                    {% endfor %}
                    <button type="submit" class="btn btn-primary w-100">Register</button>
                </form>
            </div>
            <div class="card-footer text-center">
                Already have an account? <a href="{% url 'login' %}">Login</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 11. Adding API Endpoints

### Serializers

```python
# tasks/serializers.py
from rest_framework import serializers
from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        read_only_fields = ['created_at']


class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    is_overdue = serializers.BooleanField(read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'due_date', 'category', 'category_name', 'is_overdue',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
```

### API Views

```python
# tasks/api_views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        task = self.get_object()
        task.status = 'new' if task.status == 'done' else 'done'
        task.save()
        return Response(TaskSerializer(task).data)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        tasks = self.get_queryset()
        return Response({
            'total': tasks.count(),
            'new': tasks.filter(status='new').count(),
            'in_progress': tasks.filter(status='in_progress').count(),
            'done': tasks.filter(status='done').count(),
        })


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

### API URLs

```python
# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

router = DefaultRouter()
router.register(r'tasks', api_views.TaskViewSet, basename='api-task')
router.register(r'categories', api_views.CategoryViewSet, basename='api-category')

urlpatterns = [
    # Web views
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/toggle/', views.task_toggle_status, name='task_toggle_status'),

    # API views
    path('api/', include(router.urls)),
]
```

---

## 12. Code Review Best Practices

### Code Review Checklist

When reviewing code (yours or others'), check:

**Functionality:**
- [ ] Does the code work as expected?
- [ ] Are all requirements implemented?
- [ ] Are edge cases handled?

**Security:**
- [ ] Is user input validated?
- [ ] Are permissions checked?
- [ ] No SQL injection vulnerabilities?
- [ ] CSRF protection in place?

**Code Quality:**
- [ ] Is the code readable?
- [ ] Are variable names descriptive?
- [ ] Is there code duplication?
- [ ] Are functions small and focused?

**Django Best Practices:**
- [ ] Using appropriate HTTP methods?
- [ ] Models have proper field types?
- [ ] Views check user ownership?
- [ ] Templates use inheritance?

### Common Issues to Watch For

**1. Missing User Filtering**
```python
# Bad - shows all tasks
tasks = Task.objects.all()

# Good - shows only user's tasks
tasks = Task.objects.filter(user=request.user)
```

**2. N+1 Query Problem**
```python
# Bad - one query per task for category
for task in tasks:
    print(task.category.name)

# Good - single query
tasks = Task.objects.select_related('category').filter(user=request.user)
```

**3. Hardcoded URLs**
```html
<!-- Bad -->
<a href="/tasks/create/">Create</a>

<!-- Good -->
<a href="{% url 'task_create' %}">Create</a>
```

---

## 13. Project: Task Manager

### Complete Implementation

Follow these steps to build the complete Task Manager:

1. **Setup** (Day 1 Morning)
   - Create project and app
   - Configure settings
   - Plan database design

2. **Models** (Day 1 Afternoon - Day 2 Morning)
   - Create Task and Category models
   - Run migrations
   - Register in admin
   - Add sample data

3. **Views** (Day 2 Afternoon - Day 3)
   - Dashboard view
   - Task list with filters
   - Task CRUD views
   - Category management

4. **Templates** (Day 3)
   - Base template with navigation
   - Dashboard template
   - Task list template
   - Form templates

5. **Authentication** (Day 4)
   - Login/logout
   - Registration
   - Protected views

6. **Polish** (Day 5)
   - Add API endpoints
   - Improve styling
   - Test all features
   - Fix bugs

### Final Checklist

Before presenting your project:

- [ ] User can register new account
- [ ] User can login and logout
- [ ] User can create tasks
- [ ] User can edit tasks
- [ ] User can delete tasks
- [ ] User can mark tasks complete
- [ ] Dashboard shows statistics
- [ ] Task list has filters
- [ ] Only own tasks are visible
- [ ] Navigation works correctly
- [ ] No obvious bugs
- [ ] Code is clean and organized

---

## Summary

This week you learned how to:

1. **Plan a project** - Requirements, user stories, wireframes
2. **Design databases** - Models, relationships, migrations
3. **Build complete CRUD** - Create, Read, Update, Delete
4. **Implement authentication** - Registration, login, protection
5. **Create APIs** - DRF viewsets with custom actions
6. **Review code** - Best practices and common issues

**Congratulations!** You're now ready to build Django applications from scratch!

**Next Week:** Testing, Settings Management & Deployment
