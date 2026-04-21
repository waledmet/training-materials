# دروس الأسبوع الثامن – المشروع النهائي: التصميم والبناء

مرحبًا بك في الأسبوع الثامن! هذا الأسبوع ستقوم بتصميم وبناء تطبيق Django متكامل من الصفر. ستطبّق كل ما تعلّمته: النماذج، العروض، القوالب، النماذج (Forms)، المصادقة، وواجهات برمجة التطبيقات.

---

## جدول المحتويات

1. [مقدمة إلى المشروع النهائي](#1-مقدمة-إلى-المشروع-النهائي)
2. [خيارات المشروع](#2-خيارات-المشروع)
3. [تخطيط المشروع](#3-تخطيط-المشروع)
4. [تصميم قاعدة البيانات](#4-تصميم-قاعدة-البيانات)
5. [إعداد المشروع](#5-إعداد-المشروع)
6. [بناء النماذج (Models)](#6-بناء-النماذج-models)
7. [إنشاء النماذج (Forms)](#7-إنشاء-النماذج-forms)
8. [تنفيذ العروض (Views)](#8-تنفيذ-العروض-views)
9. [بناء القوالب (Templates)](#9-بناء-القوالب-templates)
10. [إضافة المصادقة](#10-إضافة-المصادقة)
11. [إضافة نقاط نهاية API](#11-إضافة-نقاط-نهاية-api)
12. [أفضل ممارسات مراجعة الكود](#12-أفضل-ممارسات-مراجعة-الكود)
13. [المشروع: مدير المهام](#13-المشروع-مدير-المهام)

---

## 1. مقدمة إلى المشروع النهائي

### لماذا مشروع نهائي؟

المشروع النهائي يساعدك على:
- **تطبيق جميع المهارات** التي تعلّمتها في الأسابيع السابقة
- **بناء شيء حقيقي** يمكنك إظهاره للآخرين
- **تجربة التطوير الكامل** من التخطيط إلى التسليم
- **اكتشاف الثغرات** في معرفتك
- **اكتساب الثقة** كمطوّر Django

### ما الذي ستبنيه

تطبيق ويب متكامل يشمل:
- تسجيل المستخدمين والمصادقة
- نماذج قاعدة البيانات والعلاقات
- عمليات CRUD (إنشاء، قراءة، تحديث، حذف)
- نماذج (Forms) مع التحقق
- واجهة تنقل واضحة وأنيقة
- اختياري: REST API

### الجدول الزمني للمشروع

**اليوم الأول:** التخطيط وتصميم قاعدة البيانات
**اليوم الثاني:** النماذج والتهجيرات وواجهة الإدارة
**اليوم الثالث:** العروض والقوالب
**اليوم الرابع:** المصادقة والنماذج (Forms)
**اليوم الخامس:** الصقل والاختبار والعرض التقديمي

---

## 2. خيارات المشروع

اختر أحد المشاريع التالية (أو اقترح مشروعًا خاصًا بك):

### الخيار الأول: مدير المهام

**الوصف:** يمكن للمستخدمين إدارة مهامهم الشخصية.

**المميزات:**
- تسجيل/تسجيل دخول المستخدم
- إنشاء المهام وتعديلها وحذفها
- حالة المهمة (جديدة، قيد التنفيذ، منجزة)
- تواريخ الاستحقاق
- تصنيفات المهام
- لوحة تحكم مع إحصائيات المهام

**النماذج:**
- User (مدمج)
- Task
- Category

### الخيار الثاني: نظام إدارة الطلاب

**الوصف:** إدارة الطلاب والمقررات والتسجيلات.

**المميزات:**
- إضافة/تعديل/حذف الطلاب
- إنشاء المقررات
- تسجيل الطلاب في المقررات
- عرض درجات الطلاب
- قائمة المقرر

**النماذج:**
- Student
- Course
- Enrollment

### الخيار الثالث: نظام تذاكر الدعم

**الوصف:** مكتب مساعدة بسيط لتتبع طلبات الدعم.

**المميزات:**
- المستخدمون ينشئون تذاكر
- حالة التذكرة (مفتوحة، قيد المعالجة، مغلقة)
- مستويات الأولوية
- تعليقات على التذاكر
- وكيل دعم مخصص

**النماذج:**
- User (مدمج)
- Ticket
- Comment

### الخيار الرابع: مدونة شخصية

**الوصف:** منصة مدونة مع تصنيفات وتعليقات.

**المميزات:**
- كتابة المنشورات ونشرها
- تصنيفات للمنشورات
- تعليقات من المستخدمين
- ملفات المؤلفين الشخصية
- وظيفة البحث

**النماذج:**
- User (مدمج)
- Post
- Category
- Comment

---

## 3. تخطيط المشروع

### الخطوة الأولى: تحديد المتطلبات

اكتب بالضبط ما سيفعله تطبيقك.

**مثال لمدير المهام:**
```
المتطلبات الوظيفية:
1. يمكن للمستخدمين التسجيل وتسجيل الدخول
2. يمكن للمستخدمين إنشاء مهام بعنوان ووصف وتاريخ استحقاق
3. يمكن للمستخدمين تعيين المهام لتصنيفات
4. يمكن للمستخدمين تحديد المهام كمنجزة
5. يرى المستخدمون مهامهم الخاصة فقط
6. لوحة التحكم تعرض إحصائيات المهام

المتطلبات غير الوظيفية:
1. واجهة مستخدم بسيطة ونظيفة
2. تحميل سريع للصفحات
3. متوافق مع الهاتف المحمول
```

### الخطوة الثانية: تحديد قصص المستخدم

قصص المستخدم تصف المميزات من منظور المستخدم.

**الصيغة:** "بصفتي [مستخدم]، أريد أن [إجراء] حتى [الفائدة]."

**أمثلة:**
```
- بصفتي مستخدمًا، أريد التسجيل حتى أتمكن من استخدام التطبيق
- بصفتي مستخدمًا، أريد إنشاء مهام حتى أتتبع عملي
- بصفتي مستخدمًا، أريد رؤية مهامي حسب الحالة حتى أعرف ما يجب العمل عليه
- بصفتي مستخدمًا، أريد تحديد المهام كمنجزة حتى أتتبع التقدم
```

### الخطوة الثالثة: تخطيط الصفحات/الروابط

اسرد جميع صفحات تطبيقك.

**مثال:**
```
/                   - الرئيسية/لوحة التحكم
/tasks/             - قائمة جميع المهام
/tasks/create/      - إنشاء مهمة جديدة
/tasks/<id>/        - تفاصيل المهمة
/tasks/<id>/edit/   - تعديل المهمة
/tasks/<id>/delete/ - حذف المهمة
/categories/        - قائمة التصنيفات
/login/             - صفحة تسجيل الدخول
/register/          - صفحة التسجيل
/logout/            - تسجيل الخروج (إعادة توجيه)
```

### الخطوة الرابعة: رسم النماذج الأولية (Wireframes)

ارسم تصميمات بسيطة لصفحاتك الرئيسية.

```
+------------------+
| مدير المهام      |
+------------------+
| [+ مهمة جديدة]  |
+------------------+
| المهام:          |
| [ ] المهمة 1     |
| [x] المهمة 2     |
| [ ] المهمة 3     |
+------------------+
```

---

## 4. تصميم قاعدة البيانات

### مخطط علاقات الكيانات (ERD)

حدّد نماذجك وعلاقاتها.

**ERD لمدير المهام:**
```
User (مدمج في Django)
  |
  | 1:N (مستخدم واحد له مهام كثيرة)
  v
Task
  - id (تلقائي)
  - title
  - description
  - status
  - due_date
  - created_at
  - user (FK إلى User)
  - category (FK إلى Category)
  |
  | N:1 (مهام كثيرة تنتمي لتصنيف واحد)
  v
Category
  - id (تلقائي)
  - name
  - user (FK إلى User)
```

### أنواع العلاقات

**واحد إلى متعدد (1:N):**
- مستخدم واحد لديه مهام كثيرة
- تصنيف واحد لديه مهام كثيرة

```python
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

**متعدد إلى متعدد (N:N):**
- طالب واحد مسجّل في مقررات كثيرة
- مقرر واحد لديه طلاب كثيرون

```python
class Student(models.Model):
    courses = models.ManyToManyField(Course)
```

### نصائح تصميم قاعدة البيانات

1. **ابدأ بشكل بسيط** - يمكنك دائمًا إضافة حقول لاحقًا
2. **استخدم أنواع الحقول المناسبة** - CharField، TextField، DateField، إلخ
3. **أضف فهارس** للحقول التي يتم الاستعلام عنها كثيرًا
4. **فكّر في سلوك الحذف المتسلسل** - ماذا يحدث عند حذف الأصل؟
5. **نظّم البيانات** - لا تكرّر البيانات بدون داعٍ

---

## 5. إعداد المشروع

### الإعداد الأولي

```bash
# إنشاء المجلد
mkdir final_project
cd final_project

# إنشاء البيئة الافتراضية
python -m venv venv
source venv/bin/activate  # أو venv\Scripts\activate على Windows

# تثبيت Django
pip install django djangorestframework

# إنشاء المشروع
django-admin startproject config .

# إنشاء التطبيق الرئيسي
python manage.py startapp tasks
```

### إعداد الإعدادات

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

# مجلد القوالب
TEMPLATES = [
    {
        # ...
        'DIRS': [BASE_DIR / 'templates'],
        # ...
    },
]

# المصادقة
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### هيكل المشروع

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

## 6. بناء النماذج (Models)

### نماذج مدير المهام

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

### التسجيل في الإدارة

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

### تشغيل التهجيرات

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 7. إنشاء النماذج (Forms)

### نماذج المهام

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
                'placeholder': 'عنوان المهمة'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'وصف المهمة (اختياري)'
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
        # عرض تصنيفات المستخدم فقط
        self.fields['category'].queryset = Category.objects.filter(user=user)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'اسم التصنيف'
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

## 8. تنفيذ العروض (Views)

### العروض القائمة على الدوال

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
            messages.success(request, 'تم إنشاء الحساب! يرجى تسجيل الدخول.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    stats = {
        'total':       tasks.count(),
        'new':         tasks.filter(status='new').count(),
        'in_progress': tasks.filter(status='in_progress').count(),
        'done':        tasks.filter(status='done').count(),
    }
    recent_tasks = tasks[:5]
    return render(request, 'tasks/dashboard.html', {
        'stats': stats,
        'recent_tasks': recent_tasks,
    })


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    status = request.GET.get('status')
    if status:
        tasks = tasks.filter(status=status)

    category = request.GET.get('category')
    if category:
        tasks = tasks.filter(category_id=category)

    categories = Category.objects.filter(user=request.user)

    return render(request, 'tasks/task_list.html', {
        'tasks':            tasks,
        'categories':       categories,
        'current_status':   status,
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
            messages.success(request, 'تم إنشاء المهمة بنجاح!')
            return redirect('task_list')
    else:
        form = TaskForm(request.user)
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'إنشاء مهمة'
    })


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث المهمة بنجاح!')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'title': 'تعديل المهمة'
    })


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'تم حذف المهمة!')
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

### العروض القائمة على الفئات (بديل)

```python
# tasks/views.py (باستخدام CBVs)
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
```

---

## 9. بناء القوالب (Templates)

### القالب الأساسي

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}مدير المهام{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'dashboard' %}">مدير المهام</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav me-auto">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'dashboard' %}">لوحة التحكم</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'task_list' %}">المهام</a>
                    </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                    <li class="nav-item">
                        <span class="nav-link">مرحبًا، {{ user.username }}</span>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'logout' %}">تسجيل الخروج</a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'login' %}">تسجيل الدخول</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'register' %}">إنشاء حساب</a>
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

### قالب لوحة التحكم

راجع ملف الدروس الإنجليزي للاطلاع على كود القالب الكامل.

### قالب قائمة المهام

راجع ملف الدروس الإنجليزي للاطلاع على كود القالب الكامل.

---

## 10. إضافة المصادقة

### إعداد الروابط

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

### قالب تسجيل الدخول

```html
<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}تسجيل الدخول - مدير المهام{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6 col-lg-4">
        <div class="card">
            <div class="card-header">
                <h4 class="mb-0">تسجيل الدخول</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="username" class="form-label">اسم المستخدم</label>
                        <input type="text" name="username" class="form-control" id="username" required>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">كلمة المرور</label>
                        <input type="password" name="password" class="form-control" id="password" required>
                    </div>
                    {% if form.errors %}
                    <div class="alert alert-danger">
                        اسم المستخدم أو كلمة المرور غير صحيحة.
                    </div>
                    {% endif %}
                    <button type="submit" class="btn btn-primary w-100">تسجيل الدخول</button>
                </form>
            </div>
            <div class="card-footer text-center">
                ليس لديك حساب؟ <a href="{% url 'register' %}">سجّل الآن</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### قالب التسجيل

```html
<!-- templates/registration/register.html -->
{% extends 'base.html' %}

{% block title %}إنشاء حساب - مدير المهام{% endblock %}

{% block content %}
<div class="row justify-content-center">
    <div class="col-md-6 col-lg-4">
        <div class="card">
            <div class="card-header">
                <h4 class="mb-0">إنشاء حساب جديد</h4>
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
                    <button type="submit" class="btn btn-primary w-100">إنشاء الحساب</button>
                </form>
            </div>
            <div class="card-footer text-center">
                لديك حساب بالفعل؟ <a href="{% url 'login' %}">تسجيل الدخول</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

---

## 11. إضافة نقاط نهاية API

### المسلسلات

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
    is_overdue    = serializers.BooleanField(read_only=True)

    class Meta:
        model  = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'due_date', 'category', 'category_name', 'is_overdue',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
```

### عروض الـ API

```python
# tasks/api_views.py
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class   = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def toggle_status(self, request, pk=None):
        task        = self.get_object()
        task.status = 'new' if task.status == 'done' else 'done'
        task.save()
        return Response(TaskSerializer(task).data)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        tasks = self.get_queryset()
        return Response({
            'total':       tasks.count(),
            'new':         tasks.filter(status='new').count(),
            'in_progress': tasks.filter(status='in_progress').count(),
            'done':        tasks.filter(status='done').count(),
        })


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class   = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

### روابط الـ API

```python
# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import api_views

router = DefaultRouter()
router.register(r'tasks',      api_views.TaskViewSet,     basename='api-task')
router.register(r'categories', api_views.CategoryViewSet, basename='api-category')

urlpatterns = [
    # العروض الاعتيادية
    path('',                         views.dashboard,          name='dashboard'),
    path('tasks/',                   views.task_list,           name='task_list'),
    path('tasks/create/',            views.task_create,         name='task_create'),
    path('tasks/<int:pk>/',          views.task_detail,         name='task_detail'),
    path('tasks/<int:pk>/edit/',     views.task_update,         name='task_update'),
    path('tasks/<int:pk>/delete/',   views.task_delete,         name='task_delete'),
    path('tasks/<int:pk>/toggle/',   views.task_toggle_status,  name='task_toggle_status'),

    # عروض الـ API
    path('api/', include(router.urls)),
]
```

---

## 12. أفضل ممارسات مراجعة الكود

### قائمة تدقيق مراجعة الكود

عند مراجعة الكود (خاصتك أو كود الآخرين)، تحقق من:

**الوظيفية:**
- [ ] هل يعمل الكود كما هو متوقع؟
- [ ] هل تم تنفيذ جميع المتطلبات؟
- [ ] هل تمت معالجة الحالات الطرفية؟

**الأمان:**
- [ ] هل تم التحقق من مدخلات المستخدم؟
- [ ] هل تم التحقق من الصلاحيات؟
- [ ] لا توجد ثغرات SQL injection؟
- [ ] حماية CSRF في مكانها؟

**جودة الكود:**
- [ ] هل الكود مقروء؟
- [ ] هل أسماء المتغيرات وصفية؟
- [ ] هل يوجد تكرار في الكود؟
- [ ] هل الدوال صغيرة ومحددة الهدف؟

**أفضل ممارسات Django:**
- [ ] استخدام طرق HTTP المناسبة؟
- [ ] النماذج لها أنواع حقول صحيحة؟
- [ ] العروض تتحقق من ملكية المستخدم؟
- [ ] القوالب تستخدم الوراثة؟

### المشكلات الشائعة التي يجب الانتباه لها

**1. عدم تصفية البيانات حسب المستخدم**
```python
# خطأ - يعرض جميع المهام
tasks = Task.objects.all()

# صحيح - يعرض مهام المستخدم فقط
tasks = Task.objects.filter(user=request.user)
```

**2. مشكلة N+1 في الاستعلامات**
```python
# خطأ - استعلام واحد لكل مهمة للحصول على التصنيف
for task in tasks:
    print(task.category.name)

# صحيح - استعلام واحد فقط
tasks = Task.objects.select_related('category').filter(user=request.user)
```

**3. روابط مكتوبة بشكل ثابت في الكود**
```html
<!-- خطأ -->
<a href="/tasks/create/">إنشاء</a>

<!-- صحيح -->
<a href="{% url 'task_create' %}">إنشاء</a>
```

---

## 13. المشروع: مدير المهام

### التنفيذ الكامل

اتبع هذه الخطوات لبناء مدير المهام الكامل:

1. **الإعداد** (صباح اليوم الأول)
   - إنشاء المشروع والتطبيق
   - ضبط الإعدادات
   - التخطيط لتصميم قاعدة البيانات

2. **النماذج** (مساء اليوم الأول - صباح اليوم الثاني)
   - إنشاء نموذجي Task وCategory
   - تشغيل التهجيرات
   - التسجيل في الإدارة
   - إضافة بيانات تجريبية

3. **العروض** (مساء اليوم الثاني - اليوم الثالث)
   - عرض لوحة التحكم
   - قائمة المهام مع التصفية
   - عروض CRUD للمهام
   - إدارة التصنيفات

4. **القوالب** (اليوم الثالث)
   - القالب الأساسي مع التنقل
   - قالب لوحة التحكم
   - قالب قائمة المهام
   - قوالب النماذج (Forms)

5. **المصادقة** (اليوم الرابع)
   - تسجيل الدخول/الخروج
   - التسجيل
   - حماية العروض

6. **الصقل** (اليوم الخامس)
   - إضافة نقاط نهاية API
   - تحسين التصميم
   - اختبار جميع المميزات
   - إصلاح الأخطاء

### قائمة التدقيق النهائية

قبل تقديم مشروعك:

- [ ] يمكن للمستخدم تسجيل حساب جديد
- [ ] يمكن للمستخدم تسجيل الدخول والخروج
- [ ] يمكن للمستخدم إنشاء المهام
- [ ] يمكن للمستخدم تعديل المهام
- [ ] يمكن للمستخدم حذف المهام
- [ ] يمكن للمستخدم تحديد المهام كمنجزة
- [ ] لوحة التحكم تعرض الإحصائيات
- [ ] قائمة المهام تحتوي على فلاتر
- [ ] المهام المرئية لمستخدمها فقط
- [ ] التنقل يعمل بشكل صحيح
- [ ] لا توجد أخطاء واضحة
- [ ] الكود نظيف ومنظّم

---

## الملخص

هذا الأسبوع تعلّمت كيفية:

1. **تخطيط المشروع** - المتطلبات، قصص المستخدم، النماذج الأولية
2. **تصميم قاعدة البيانات** - النماذج، العلاقات، التهجيرات
3. **بناء CRUD متكامل** - إنشاء، قراءة، تحديث، حذف
4. **تنفيذ المصادقة** - التسجيل، تسجيل الدخول، الحماية
5. **إنشاء APIs** - ViewSets في DRF مع إجراءات مخصصة
6. **مراجعة الكود** - أفضل الممارسات والمشكلات الشائعة

**تهانينا!** أنت الآن جاهز لبناء تطبيقات Django من الصفر!

**الأسبوع القادم:** الاختبارات وإدارة الإعدادات والنشر
