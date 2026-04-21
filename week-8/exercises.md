# Week 8 Exercises – Final Project: Design & Build

Practice exercises for Week 8: Building a complete Django application from scratch.

---

## Table of Contents

1. [Day 1: Project Planning & Database Design](#day-1-project-planning--database-design)
2. [Day 2: Models & Admin](#day-2-models--admin)
3. [Day 3: Views & Templates](#day-3-views--templates)
4. [Day 4: Authentication & Forms](#day-4-authentication--forms)
5. [Day 5: Polish & Presentation](#day-5-polish--presentation)
6. [Project Milestones](#project-milestones)

---

## Day 1: Project Planning & Database Design

### Exercise 1: Choose Your Project

**Task:**
Choose one of these projects (or propose your own):

1. **Task Manager** - Personal task tracking with categories
2. **Student Management** - Students, courses, and enrollments
3. **Support Tickets** - Help desk ticket system
4. **Personal Blog** - Posts with categories and comments

Write down:
- Why you chose this project
- What features you want to include
- Who will use it

<details>
<summary>Example Response</summary>

**Project:** Task Manager

**Why:** I want to track my daily tasks and stay organized. This is practical and I'll actually use it.

**Features:**
- Create, edit, delete tasks
- Mark tasks as complete
- Organize by categories
- See statistics on dashboard
- Due dates with overdue warnings

**Users:** Myself and other people who want to organize their work
</details>

---

### Exercise 2: Write User Stories

**Task:**
Write at least 8 user stories for your project.

Format: "As a [user], I want to [action] so that [benefit]."

<details>
<summary>Example: Task Manager User Stories</summary>

1. As a user, I want to register an account so that I can have my own task list
2. As a user, I want to login so that I can access my tasks
3. As a user, I want to create tasks so that I can track my work
4. As a user, I want to set due dates so that I know when tasks are due
5. As a user, I want to mark tasks complete so that I can track my progress
6. As a user, I want to edit tasks so that I can update details
7. As a user, I want to delete tasks so that I can remove items I no longer need
8. As a user, I want to filter tasks by status so that I can focus on what needs attention
9. As a user, I want to see statistics so that I know my overall progress
10. As a user, I want to organize tasks by category so that I can group related work
</details>

---

### Exercise 3: Plan Your URLs

**Task:**
List all the URLs/pages your application will have.

<details>
<summary>Example: Task Manager URLs</summary>

```
Authentication:
/login/         - Login page
/logout/        - Logout (redirect)
/register/      - Registration page

Dashboard:
/               - Home/Dashboard

Tasks:
/tasks/         - List all tasks
/tasks/create/  - Create new task
/tasks/<id>/    - Task detail
/tasks/<id>/edit/   - Edit task
/tasks/<id>/delete/ - Delete task
/tasks/<id>/toggle/ - Toggle complete status

Categories:
/categories/        - List categories
/categories/create/ - Create category
/categories/<id>/delete/ - Delete category

API (optional):
/api/tasks/     - Task API endpoints
/api/categories/ - Category API endpoints
```
</details>

---

### Exercise 4: Design Your Database

**Task:**
Draw your database design (ERD) with:
- All models
- All fields with types
- Relationships between models

<details>
<summary>Example: Task Manager ERD</summary>

```
User (Django built-in)
├── id (auto)
├── username
├── email
├── password (hashed)
└── date_joined

Category
├── id (auto)
├── name (CharField, max=100)
├── user (ForeignKey → User)
└── created_at (DateTimeField)

Task
├── id (auto)
├── title (CharField, max=200)
├── description (TextField, blank=True)
├── status (CharField, choices)
├── priority (CharField, choices)
├── due_date (DateField, null=True)
├── created_at (DateTimeField)
├── updated_at (DateTimeField)
├── user (ForeignKey → User)
└── category (ForeignKey → Category, null=True)

Relationships:
- User (1) → (N) Task
- User (1) → (N) Category
- Category (1) → (N) Task
```
</details>

---

### Exercise 5: Create Project Structure

**Task:**
1. Create the Django project
2. Create your main app
3. Configure settings
4. Create the folder structure

```bash
# Commands to run
mkdir final_project
cd final_project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install django djangorestframework
django-admin startproject config .
python manage.py startapp tasks
```

<details>
<summary>Solution: Settings Configuration</summary>

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        # ...
    },
]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

**Folder Structure:**
```
final_project/
├── config/
├── tasks/
│   ├── templates/
│   │   └── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── registration/
├── static/
├── manage.py
└── requirements.txt
```
</details>

---

## Day 2: Models & Admin

### Exercise 6: Create Your Models

**Task:**
Implement all your models based on your database design from Day 1.

<details>
<summary>Example: Task Manager Models</summary>

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
</details>

---

### Exercise 7: Run Migrations

**Task:**
1. Create migrations
2. Apply migrations
3. Create superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### Exercise 8: Register Models in Admin

**Task:**
Register your models in admin with customization:
- list_display
- search_fields
- list_filter

<details>
<summary>Example: Task Manager Admin</summary>

```python
# tasks/admin.py
from django.contrib import admin
from .models import Task, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']
    search_fields = ['name']
    list_filter = ['user']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'user', 'due_date', 'created_at']
    list_filter = ['status', 'priority', 'category']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
    list_editable = ['status', 'priority']
```
</details>

---

### Exercise 9: Add Sample Data

**Task:**
Using Django admin, add:
- At least 3 categories
- At least 10 tasks with various statuses

Or use Django shell:
```python
python manage.py shell
```

<details>
<summary>Example: Shell Commands</summary>

```python
from django.contrib.auth.models import User
from tasks.models import Category, Task

# Get user
user = User.objects.first()

# Create categories
work = Category.objects.create(name='Work', user=user)
personal = Category.objects.create(name='Personal', user=user)
learning = Category.objects.create(name='Learning', user=user)

# Create tasks
Task.objects.create(
    title='Complete Django project',
    description='Finish the final project',
    status='in_progress',
    priority='high',
    user=user,
    category=learning
)

Task.objects.create(
    title='Buy groceries',
    status='new',
    priority='medium',
    user=user,
    category=personal
)

# ... add more tasks
```
</details>

---

### Exercise 10: Test Model Methods

**Task:**
Test your model methods in the shell:
- `__str__` methods
- Any custom properties (like `is_overdue`)

<details>
<summary>Example: Testing</summary>

```python
from tasks.models import Task

task = Task.objects.first()
print(str(task))  # Should show task title
print(task.is_overdue)  # Should show True/False
print(task.get_status_display())  # Should show "New", "In Progress", etc.
```
</details>

---

## Day 3: Views & Templates

### Exercise 11: Create Base Template

**Task:**
Create a base template with:
- Navigation bar
- Main content area
- Messages display
- Footer (optional)

<details>
<summary>Example: base.html</summary>

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Task Manager{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'dashboard' %}">Task Manager</a>
            <div class="navbar-nav ms-auto">
                {% if user.is_authenticated %}
                <a class="nav-link" href="{% url 'task_list' %}">Tasks</a>
                <a class="nav-link" href="{% url 'logout' %}">Logout</a>
                {% else %}
                <a class="nav-link" href="{% url 'login' %}">Login</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <div class="container mt-4">
        {% if messages %}
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
        {% endfor %}
        {% endif %}

        {% block content %}{% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```
</details>

---

### Exercise 12: Create Dashboard View

**Task:**
Create a dashboard that shows:
- Statistics (total, by status)
- Recent items
- Quick actions

<details>
<summary>Example: Dashboard View & Template</summary>

```python
# tasks/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task

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
```

```html
<!-- tasks/templates/tasks/dashboard.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Dashboard</h1>

<div class="row">
    <div class="col-md-3">
        <div class="card bg-secondary text-white">
            <div class="card-body text-center">
                <h2>{{ stats.total }}</h2>
                <p>Total</p>
            </div>
        </div>
    </div>
    <!-- Add more stat cards -->
</div>

<h2 class="mt-4">Recent Tasks</h2>
{% for task in recent_tasks %}
<p>{{ task.title }} - {{ task.get_status_display }}</p>
{% endfor %}
{% endblock %}
```
</details>

---

### Exercise 13: Create List View

**Task:**
Create a list view that shows all items with:
- Filter options
- Status badges
- Action buttons

<details>
<summary>Example: Task List</summary>

```python
# tasks/views.py
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})
```

```html
<!-- tasks/templates/tasks/task_list.html -->
{% extends 'base.html' %}

{% block content %}
<h1>My Tasks</h1>

<div class="mb-3">
    <a href="{% url 'task_list' %}" class="btn btn-outline-secondary">All</a>
    <a href="?status=new" class="btn btn-outline-warning">New</a>
    <a href="?status=in_progress" class="btn btn-outline-info">In Progress</a>
    <a href="?status=done" class="btn btn-outline-success">Done</a>
</div>

{% for task in tasks %}
<div class="card mb-2">
    <div class="card-body">
        <h5>{{ task.title }}</h5>
        <span class="badge bg-{{ task.status }}">{{ task.get_status_display }}</span>
        <a href="{% url 'task_detail' task.pk %}" class="btn btn-sm btn-primary">View</a>
    </div>
</div>
{% empty %}
<p>No tasks found.</p>
{% endfor %}
{% endblock %}
```
</details>

---

### Exercise 14: Create CRUD Views

**Task:**
Implement Create, Read, Update, Delete views for your main model.

<details>
<summary>Example: Task CRUD Views</summary>

```python
# tasks/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm

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
            messages.success(request, 'Task created!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Create Task'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('task_detail', pk=pk)
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Edit Task'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```
</details>

---

### Exercise 15: Configure URLs

**Task:**
Configure all URLs for your views.

<details>
<summary>Example: Task URLs</summary>

```python
# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
```

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
```
</details>

---

## Day 4: Authentication & Forms

### Exercise 16: Create Forms

**Task:**
Create ModelForms for your models with proper widgets and validation.

<details>
<summary>Example: Task Form</summary>

```python
# tasks/forms.py
from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
```
</details>

---

### Exercise 17: Add Login/Logout

**Task:**
Implement login and logout functionality using Django's built-in views.

<details>
<summary>Solution</summary>

```python
# config/urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ...
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

```html
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-4">
        <h2>Login</h2>
        <form method="post">
            {% csrf_token %}
            <div class="mb-3">
                <label>Username</label>
                <input type="text" name="username" class="form-control" required>
            </div>
            <div class="mb-3">
                <label>Password</label>
                <input type="password" name="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </div>
</div>
{% endblock %}
```
</details>

---

### Exercise 18: Add Registration

**Task:**
Create a user registration view with a custom form.

<details>
<summary>Solution</summary>

```python
# tasks/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

```python
# tasks/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

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
```
</details>

---

### Exercise 19: Protect All Views

**Task:**
Ensure all views (except login/register) require authentication.

Check:
- [ ] Dashboard requires login
- [ ] List view requires login
- [ ] Detail view requires login
- [ ] Create view requires login
- [ ] Update view requires login
- [ ] Delete view requires login
- [ ] Users can only see their own data

---

### Exercise 20: Add Messages Feedback

**Task:**
Add success/error messages for all actions:
- Create success
- Update success
- Delete success
- Errors

<details>
<summary>Example</summary>

```python
from django.contrib import messages

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            # ...
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    # ...
```
</details>

---

## Day 5: Polish & Presentation

### Exercise 21: Add API Endpoints (Optional)

**Task:**
Add REST API endpoints for your main model.

<details>
<summary>Example</summary>

```python
# tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```

```python
# tasks/api_views.py
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```
</details>

---

### Exercise 22: Final Testing

**Task:**
Test all features thoroughly:

- [ ] Register new user
- [ ] Login with new user
- [ ] Create item
- [ ] View item list
- [ ] Filter items
- [ ] View item detail
- [ ] Edit item
- [ ] Delete item
- [ ] Logout
- [ ] Login with different user
- [ ] Verify user isolation (can't see other's data)

---

### Exercise 23: Code Cleanup

**Task:**
Review and clean up your code:

- [ ] Remove debug print statements
- [ ] Remove commented-out code
- [ ] Add docstrings to complex functions
- [ ] Ensure consistent formatting
- [ ] Check for security issues

---

### Exercise 24: Prepare Presentation

**Task:**
Prepare a 5-minute presentation covering:

1. **Introduction** (30 seconds)
   - What is your application?
   - Who is it for?

2. **Demo** (3 minutes)
   - Show registration/login
   - Show main features
   - Show dashboard/statistics

3. **Technical Overview** (1 minute)
   - Models and relationships
   - Key views/features
   - Challenges faced

4. **Future Improvements** (30 seconds)
   - What would you add next?
   - What would you change?

---

### Exercise 25: Present Your Project!

**Task:**
Present your completed project to the trainer and peers.

Be prepared to:
- Demo all features live
- Answer technical questions
- Explain your code decisions
- Discuss what you learned

---

## Project Milestones

Track your progress:

### Day 1: Planning ✓
- [ ] Project chosen
- [ ] User stories written
- [ ] URLs planned
- [ ] Database designed
- [ ] Project created

### Day 2: Models ✓
- [ ] Models created
- [ ] Migrations run
- [ ] Admin configured
- [ ] Sample data added

### Day 3: Views ✓
- [ ] Base template
- [ ] Dashboard view
- [ ] List view
- [ ] Detail view
- [ ] Create view
- [ ] Update view
- [ ] Delete view

### Day 4: Auth ✓
- [ ] Forms created
- [ ] Login working
- [ ] Logout working
- [ ] Registration working
- [ ] Views protected
- [ ] Messages added

### Day 5: Polish ✓
- [ ] All features tested
- [ ] Code cleaned
- [ ] Presentation ready
- [ ] Project presented!

---

**Congratulations on completing your final project!**
