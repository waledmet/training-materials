# تمارين الأسبوع الثامن – المشروع النهائي: التصميم والبناء

تمارين عملية للأسبوع الثامن: بناء تطبيق Django متكامل من الصفر.

---

## جدول المحتويات

1. [اليوم الأول: تخطيط المشروع وتصميم قاعدة البيانات](#اليوم-الأول-تخطيط-المشروع-وتصميم-قاعدة-البيانات)
2. [اليوم الثاني: النماذج والإدارة](#اليوم-الثاني-النماذج-والإدارة)
3. [اليوم الثالث: العروض والقوالب](#اليوم-الثالث-العروض-والقوالب)
4. [اليوم الرابع: المصادقة والنماذج](#اليوم-الرابع-المصادقة-والنماذج)
5. [اليوم الخامس: التلميع والعرض](#اليوم-الخامس-التلميع-والعرض)
6. [مراحل المشروع](#مراحل-المشروع)

---

## اليوم الأول: تخطيط المشروع وتصميم قاعدة البيانات

### تمرين 1: اختر مشروعك

**المهمة:**
اختر أحد هذه المشاريع (أو اقترح مشروعًا من اختيارك):

1. **مدير المهام** – تتبع المهام الشخصية مع التصنيفات
2. **إدارة الطلاب** – الطلاب والمقررات والتسجيلات
3. **تذاكر الدعم الفني** – نظام مكتب المساعدة
4. **مدونة شخصية** – مقالات مع تصنيفات وتعليقات

اكتب:
- لماذا اخترت هذا المشروع
- الميزات التي تريد تضمينها
- من سيستخدم التطبيق

<details>
<summary>مثال على الإجابة</summary>

**المشروع:** مدير المهام

**السبب:** أريد تتبع مهامي اليومية والبقاء منظمًا. هذا المشروع عملي وسأستخدمه فعلًا.

**الميزات:**
- إنشاء المهام وتعديلها وحذفها
- تعليم المهام كمكتملة
- تنظيم المهام حسب التصنيفات
- عرض إحصائيات على لوحة التحكم
- تواريخ الاستحقاق مع تحذيرات التأخر

**المستخدمون:** أنا وغيري ممن يريدون تنظيم عملهم
</details>

---

### تمرين 2: اكتب قصص المستخدم

**المهمة:**
اكتب ما لا يقل عن 8 قصص مستخدم لمشروعك.

الصيغة: "بوصفي [مستخدمًا]، أريد أن [الإجراء] حتى [الفائدة]."

<details>
<summary>مثال: قصص مستخدم مدير المهام</summary>

1. بوصفي مستخدمًا، أريد تسجيل حساب حتى يكون لديّ قائمة مهامي الخاصة
2. بوصفي مستخدمًا، أريد تسجيل الدخول حتى أتمكن من الوصول إلى مهامي
3. بوصفي مستخدمًا، أريد إنشاء مهام حتى أتتبع عملي
4. بوصفي مستخدمًا، أريد تحديد تواريخ استحقاق حتى أعرف موعد انتهاء المهام
5. بوصفي مستخدمًا، أريد تعليم المهام كمكتملة حتى أتابع تقدمي
6. بوصفي مستخدمًا، أريد تعديل المهام حتى أحدّث التفاصيل
7. بوصفي مستخدمًا، أريد حذف المهام حتى أزيل ما لم أعد بحاجة إليه
8. بوصفي مستخدمًا، أريد تصفية المهام حسب الحالة حتى أركز على ما يحتاج اهتمامًا
9. بوصفي مستخدمًا، أريد رؤية الإحصائيات حتى أعرف تقدمي الإجمالي
10. بوصفي مستخدمًا، أريد تنظيم المهام حسب التصنيف حتى أجمّع الأعمال المتشابهة
</details>

---

### تمرين 3: خطط لمسارات URL

**المهمة:**
اعرض جميع مسارات URL/الصفحات التي سيحتوي عليها تطبيقك.

<details>
<summary>مثال: مسارات URL لمدير المهام</summary>

```
المصادقة:
/login/         - صفحة تسجيل الدخول
/logout/        - تسجيل الخروج (إعادة توجيه)
/register/      - صفحة التسجيل

لوحة التحكم:
/               - الرئيسية/لوحة التحكم

المهام:
/tasks/         - قائمة جميع المهام
/tasks/create/  - إنشاء مهمة جديدة
/tasks/<id>/    - تفاصيل المهمة
/tasks/<id>/edit/   - تعديل المهمة
/tasks/<id>/delete/ - حذف المهمة
/tasks/<id>/toggle/ - تبديل حالة الاكتمال

التصنيفات:
/categories/        - قائمة التصنيفات
/categories/create/ - إنشاء تصنيف
/categories/<id>/delete/ - حذف تصنيف

API (اختياري):
/api/tasks/     - نقاط نهاية API للمهام
/api/categories/ - نقاط نهاية API للتصنيفات
```
</details>

---

### تمرين 4: صمّم قاعدة بياناتك

**المهمة:**
ارسم تصميم قاعدة البيانات (ERD) ليشمل:
- جميع النماذج
- جميع الحقول مع أنواعها
- العلاقات بين النماذج

<details>
<summary>مثال: ERD لمدير المهام</summary>

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

العلاقات:
- User (1) → (N) Task
- User (1) → (N) Category
- Category (1) → (N) Task
```
</details>

---

### تمرين 5: أنشئ هيكل المشروع

**المهمة:**
1. أنشئ مشروع Django
2. أنشئ التطبيق الرئيسي
3. اضبط الإعدادات
4. أنشئ هيكل المجلدات

```bash
# الأوامر التي يجب تشغيلها
mkdir final_project
cd final_project
python -m venv venv
source venv/bin/activate  # أو venv\Scripts\activate على ويندوز
pip install django djangorestframework
django-admin startproject config .
python manage.py startapp tasks
```

<details>
<summary>الحل: إعداد الإعدادات</summary>

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

**هيكل المجلدات:**
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

## اليوم الثاني: النماذج والإدارة

### تمرين 6: أنشئ نماذجك

**المهمة:**
طبّق جميع نماذجك بناءً على تصميم قاعدة البيانات من اليوم الأول.

<details>
<summary>مثال: نماذج مدير المهام</summary>

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

### تمرين 7: شغّل الترحيلات

**المهمة:**
1. أنشئ الترحيلات
2. طبّق الترحيلات
3. أنشئ مستخدم المدير (superuser)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### تمرين 8: سجّل النماذج في لوحة الإدارة

**المهمة:**
سجّل نماذجك في لوحة الإدارة مع التخصيص التالي:
- `list_display`
- `search_fields`
- `list_filter`

<details>
<summary>مثال: إدارة مدير المهام</summary>

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

### تمرين 9: أضف بيانات تجريبية

**المهمة:**
باستخدام لوحة إدارة Django، أضف:
- ما لا يقل عن 3 تصنيفات
- ما لا يقل عن 10 مهام بحالات مختلفة

أو استخدم Django shell:
```python
python manage.py shell
```

<details>
<summary>مثال: أوامر Shell</summary>

```python
from django.contrib.auth.models import User
from tasks.models import Category, Task

# الحصول على المستخدم
user = User.objects.first()

# إنشاء التصنيفات
work = Category.objects.create(name='Work', user=user)
personal = Category.objects.create(name='Personal', user=user)
learning = Category.objects.create(name='Learning', user=user)

# إنشاء المهام
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

# ... أضف المزيد من المهام
```
</details>

---

### تمرين 10: اختبر دوال النماذج

**المهمة:**
اختبر دوال نماذجك في shell:
- دوال `__str__`
- أي خصائص مخصصة (مثل `is_overdue`)

<details>
<summary>مثال: الاختبار</summary>

```python
from tasks.models import Task

task = Task.objects.first()
print(str(task))          # يجب أن يعرض عنوان المهمة
print(task.is_overdue)    # يجب أن يعرض True أو False
print(task.get_status_display())  # يجب أن يعرض "New" أو "In Progress" ...
```
</details>

---

## اليوم الثالث: العروض والقوالب

### تمرين 11: أنشئ القالب الأساسي

**المهمة:**
أنشئ قالبًا أساسيًا يحتوي على:
- شريط تنقل
- منطقة المحتوى الرئيسي
- عرض رسائل التنبيه
- تذييل الصفحة (اختياري)

<details>
<summary>مثال: base.html</summary>

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

### تمرين 12: أنشئ عرض لوحة التحكم

**المهمة:**
أنشئ لوحة تحكم تعرض:
- إحصائيات (الإجمالي، حسب الحالة)
- العناصر الأخيرة
- إجراءات سريعة

<details>
<summary>مثال: عرض لوحة التحكم والقالب</summary>

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
    <!-- أضف المزيد من بطاقات الإحصائيات -->
</div>

<h2 class="mt-4">Recent Tasks</h2>
{% for task in recent_tasks %}
<p>{{ task.title }} - {{ task.get_status_display }}</p>
{% endfor %}
{% endblock %}
```
</details>

---

### تمرين 13: أنشئ عرض القائمة

**المهمة:**
أنشئ عرض قائمة يعرض جميع العناصر مع:
- خيارات التصفية
- شارات الحالة
- أزرار الإجراءات

<details>
<summary>مثال: قائمة المهام</summary>

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

### تمرين 14: أنشئ عروض CRUD

**المهمة:**
نفّذ عروض الإنشاء والقراءة والتحديث والحذف للنموذج الرئيسي.

<details>
<summary>مثال: عروض CRUD للمهام</summary>

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

### تمرين 15: اضبط مسارات URL

**المهمة:**
اضبط جميع مسارات URL لعروضك.

<details>
<summary>مثال: مسارات URL للمهام</summary>

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

## اليوم الرابع: المصادقة والنماذج

### تمرين 16: أنشئ النماذج (Forms)

**المهمة:**
أنشئ `ModelForm` لنماذجك مع عناصر واجهة مناسبة والتحقق من الصحة.

<details>
<summary>مثال: نموذج المهمة</summary>

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

### تمرين 17: أضف تسجيل الدخول والخروج

**المهمة:**
نفّذ وظيفتَي تسجيل الدخول والخروج باستخدام عروض Django المدمجة.

<details>
<summary>الحل</summary>

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

### تمرين 18: أضف التسجيل

**المهمة:**
أنشئ عرض تسجيل المستخدم مع نموذج مخصص.

<details>
<summary>الحل</summary>

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

### تمرين 19: احمِ جميع العروض

**المهمة:**
تأكد من أن جميع العروض (عدا تسجيل الدخول والتسجيل) تستلزم المصادقة.

تحقق من:
- [ ] لوحة التحكم تستلزم تسجيل الدخول
- [ ] عرض القائمة يستلزم تسجيل الدخول
- [ ] عرض التفاصيل يستلزم تسجيل الدخول
- [ ] عرض الإنشاء يستلزم تسجيل الدخول
- [ ] عرض التحديث يستلزم تسجيل الدخول
- [ ] عرض الحذف يستلزم تسجيل الدخول
- [ ] يرى كل مستخدم بياناته فقط

---

### تمرين 20: أضف رسائل التغذية الراجعة

**المهمة:**
أضف رسائل نجاح/خطأ لجميع الإجراءات:
- نجاح الإنشاء
- نجاح التحديث
- نجاح الحذف
- الأخطاء

<details>
<summary>مثال</summary>

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

## اليوم الخامس: التلميع والعرض

### تمرين 21: أضف نقاط نهاية API (اختياري)

**المهمة:**
أضف نقاط نهاية REST API للنموذج الرئيسي.

<details>
<summary>مثال</summary>

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

### تمرين 22: الاختبار النهائي

**المهمة:**
اختبر جميع الميزات بشكل شامل:

- [ ] تسجيل مستخدم جديد
- [ ] تسجيل الدخول بالمستخدم الجديد
- [ ] إنشاء عنصر
- [ ] عرض قائمة العناصر
- [ ] تصفية العناصر
- [ ] عرض تفاصيل العنصر
- [ ] تعديل عنصر
- [ ] حذف عنصر
- [ ] تسجيل الخروج
- [ ] تسجيل الدخول بمستخدم آخر
- [ ] التحقق من عزل البيانات (لا يرى مستخدم بيانات الآخر)

---

### تمرين 23: تنظيف الكود

**المهمة:**
راجع كودك ونظّفه:

- [ ] أزل جمل `print` التصحيحية
- [ ] أزل الكود المعلّق
- [ ] أضف توثيقًا للدوال المعقدة
- [ ] تأكد من التنسيق المتسق
- [ ] تحقق من مشكلات الأمان

---

### تمرين 24: أعدّ العرض التقديمي

**المهمة:**
أعدّ عرضًا تقديميًا مدته 5 دقائق يغطي:

1. **المقدمة** (30 ثانية)
   - ما هو تطبيقك؟
   - لمن هو؟

2. **العرض التجريبي** (3 دقائق)
   - أظهر التسجيل وتسجيل الدخول
   - أظهر الميزات الرئيسية
   - أظهر لوحة التحكم والإحصائيات

3. **النظرة التقنية** (دقيقة واحدة)
   - النماذج والعلاقات
   - العروض/الميزات الرئيسية
   - التحديات التي واجهتها

4. **التحسينات المستقبلية** (30 ثانية)
   - ما الذي ستضيفه لاحقًا؟
   - ما الذي ستغيّره؟

---

### تمرين 25: قدّم مشروعك!

**المهمة:**
قدّم مشروعك المكتمل للمدرّب وزملائك.

كن مستعدًا لـ:
- عرض جميع الميزات مباشرةً
- الإجابة على الأسئلة التقنية
- شرح قراراتك البرمجية
- مناقشة ما تعلمته

---

## مراحل المشروع

تتبّع تقدمك:

### اليوم الأول: التخطيط ✓
- [ ] اختيار المشروع
- [ ] كتابة قصص المستخدم
- [ ] تخطيط مسارات URL
- [ ] تصميم قاعدة البيانات
- [ ] إنشاء المشروع

### اليوم الثاني: النماذج ✓
- [ ] إنشاء النماذج
- [ ] تشغيل الترحيلات
- [ ] ضبط لوحة الإدارة
- [ ] إضافة البيانات التجريبية

### اليوم الثالث: العروض ✓
- [ ] القالب الأساسي
- [ ] عرض لوحة التحكم
- [ ] عرض القائمة
- [ ] عرض التفاصيل
- [ ] عرض الإنشاء
- [ ] عرض التحديث
- [ ] عرض الحذف

### اليوم الرابع: المصادقة ✓
- [ ] إنشاء النماذج
- [ ] تسجيل الدخول يعمل
- [ ] تسجيل الخروج يعمل
- [ ] التسجيل يعمل
- [ ] العروض محمية
- [ ] الرسائل مضافة

### اليوم الخامس: التلميع ✓
- [ ] اختبار جميع الميزات
- [ ] تنظيف الكود
- [ ] العرض التقديمي جاهز
- [ ] تقديم المشروع!

---

**تهانينا على إتمام مشروعك النهائي!**
