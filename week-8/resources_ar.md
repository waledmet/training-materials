# موارد الأسبوع الثامن – المشروع النهائي: التصميم والبناء

موارد منتقاة للأسبوع الثامن: بناء تطبيق Django متكامل.

---

## موارد تخطيط المشروع

### المتطلبات وقصص المستخدم

- **قالب قصة المستخدم:** "بوصفي [مستخدمًا]، أريد أن [الإجراء] حتى [الفائدة]"
- **تحديد الأولويات بطريقة MoSCoW:** يجب أن يكون – ينبغي أن يكون – يمكن أن يكون – لن يكون
- **دليل قصص المستخدم في Agile** - https://www.atlassian.com/agile/project-management/user-stories

### أدوات رسم الواجهات

- **Excalidraw** - https://excalidraw.com/ (بسيط ومجاني)
- **Figma** - https://www.figma.com/ (احترافي، نسخة مجانية متاحة)
- **Balsamiq** - https://balsamiq.com/ (رسم سريع للواجهات)
- **الورقة والقلم** – لا يزال الأسرع!

---

## توثيق Django

### مراجع أساسية

1. **النماذج** - https://docs.djangoproject.com/en/stable/topics/db/models/
2. **العروض** - https://docs.djangoproject.com/en/stable/topics/http/views/
3. **القوالب** - https://docs.djangoproject.com/en/stable/topics/templates/
4. **النماذج (Forms)** - https://docs.djangoproject.com/en/stable/topics/forms/
5. **المصادقة** - https://docs.djangoproject.com/en/stable/topics/auth/
6. **العروض المبنية على الفئات** - https://docs.djangoproject.com/en/stable/topics/class-based-views/

---

## أوراق مرجع سريعة

### أنواع حقول النماذج

```python
# النصوص
CharField(max_length=100)
TextField()
EmailField()
URLField()
SlugField()

# الأرقام
IntegerField()
FloatField()
DecimalField(max_digits=10, decimal_places=2)

# القيم المنطقية
BooleanField(default=False)

# التاريخ والوقت
DateField()
DateTimeField()
TimeField()
DateField(auto_now_add=True)      # يُضبط عند الإنشاء
DateTimeField(auto_now=True)      # يُضبط عند كل حفظ

# العلاقات
ForeignKey(Model, on_delete=models.CASCADE)
ManyToManyField(Model)
OneToOneField(Model, on_delete=models.CASCADE)

# الملفات
FileField(upload_to='uploads/')
ImageField(upload_to='images/')
```

### خيارات Meta في النماذج

```python
class Meta:
    ordering = ['-created_at']
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'
    unique_together = ['user', 'title']
```

### أنماط العروض

```python
# العرض المبني على الدوال
@login_required
def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Created!')
            return redirect('list')
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})
```

### العروض المبنية على الفئات

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class MyListView(LoginRequiredMixin, ListView):
    model = MyModel
    template_name = 'list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return MyModel.objects.filter(user=self.request.user)

class MyCreateView(LoginRequiredMixin, CreateView):
    model = MyModel
    form_class = MyForm
    template_name = 'form.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
```

### عناصر واجهة النماذج (Widgets)

```python
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
```

### أنماط مسارات URL

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('items/<int:pk>/edit/', views.item_update, name='item_update'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'),
]
```

### وسوم القوالب

```html
<!-- URL -->
<a href="{% url 'item_detail' item.pk %}">View</a>

<!-- الملفات الثابتة -->
{% load static %}
<link href="{% static 'css/style.css' %}" rel="stylesheet">

<!-- الشروط -->
{% if user.is_authenticated %}
    Welcome, {{ user.username }}
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}

<!-- الحلقات -->
{% for item in items %}
    <p>{{ item.title }}</p>
{% empty %}
    <p>No items found.</p>
{% endfor %}

<!-- المرشّحات -->
{{ item.created_at|date:"M d, Y" }}
{{ item.description|truncatewords:20 }}
{{ item.status|default:"Unknown" }}
```

---

## مرجع سريع لـ Bootstrap

### التخطيط الأساسي

```html
<div class="container">
    <div class="row">
        <div class="col-md-6">نصف العرض على الشاشات المتوسطة فأكبر</div>
        <div class="col-md-6">نصف العرض على الشاشات المتوسطة فأكبر</div>
    </div>
</div>
```

### البطاقات

```html
<div class="card">
    <div class="card-header">العنوان</div>
    <div class="card-body">
        <h5 class="card-title">عنوان البطاقة</h5>
        <p class="card-text">المحتوى هنا.</p>
        <a href="#" class="btn btn-primary">إجراء</a>
    </div>
</div>
```

### التنبيهات

```html
<div class="alert alert-success">رسالة نجاح!</div>
<div class="alert alert-danger">رسالة خطأ!</div>
<div class="alert alert-warning">رسالة تحذير!</div>
<div class="alert alert-info">رسالة معلومات!</div>
```

### الأزرار

```html
<button class="btn btn-primary">أساسي</button>
<button class="btn btn-secondary">ثانوي</button>
<button class="btn btn-success">نجاح</button>
<button class="btn btn-danger">حذف</button>
<button class="btn btn-outline-primary">محدود</button>
<button class="btn btn-sm">صغير</button>
<button class="btn btn-lg">كبير</button>
```

### النماذج

```html
<form method="post">
    {% csrf_token %}
    <div class="mb-3">
        <label class="form-label">العنوان</label>
        <input type="text" class="form-control" name="title">
    </div>
    <button type="submit" class="btn btn-primary">إرسال</button>
</form>
```

### شريط التنقل

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="#">العلامة التجارية</a>
        <div class="navbar-nav ms-auto">
            <a class="nav-link" href="#">رابط</a>
        </div>
    </div>
</nav>
```

---

## أمثلة على المشاريع

### مدير المهام

```python
# النماذج
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    STATUS_CHOICES = [('new', 'New'), ('done', 'Done')]
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
```

### إدارة الطلاب

```python
# النماذج
class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    credits = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    enrollment_date = models.DateField()

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, blank=True)
```

### تذاكر الدعم الفني

```python
# النماذج
class Ticket(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('closed', 'Closed')]
    PRIORITY_CHOICES = [('low', 'Low'), ('high', 'High')]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## قائمة مراجعة الأمان

- [ ] استخدام `{% csrf_token %}` في جميع نماذج POST
- [ ] تصفية querysets حسب المستخدم
- [ ] التحقق من الملكية قبل التعديل أو الحذف
- [ ] استخدام `@login_required` على العروض المحمية
- [ ] عدم كشف البيانات الحساسة في القوالب
- [ ] التحقق من صحة جميع مدخلات النماذج
- [ ] استخدام نظام مصادقة Django

---

## نصائح تصحيح الأخطاء

### الأخطاء الشائعة

**TemplateDoesNotExist:**
- تحقق من مسار القالب
- تحقق من `TEMPLATES['DIRS']` في الإعدادات
- تأكد من أن `APP_DIRS` يساوي `True`

**NoReverseMatch:**
- تحقق من وجود اسم URL
- تحقق من تمرير الوسائط المطلوبة
- تحقق من الأخطاء الإملائية

**AttributeError: 'NoneType':**
- تحقق من وجود الكائن قبل الوصول إليه
- استخدم `get_object_or_404()`

**IntegrityError:**
- تحقق من الحقول المطلوبة
- تحقق من قيود التفرد
- تحقق من مراجع المفاتيح الخارجية

### تقنيات التصحيح

```python
# الطباعة في العروض
print("DEBUG:", variable)

# الطباعة في القوالب
{{ variable|pprint }}

# Django Debug Toolbar
pip install django-debug-toolbar

# التصحيح في Shell
python manage.py shell
```

---

## موارد إضافية

- **Two Scoops of Django** – كتاب أفضل الممارسات
- **Django Girls Tutorial** – مناسب للمبتدئين
- **Simple is Better than Complex** – مدونة بدروس تعليمية
- **Real Python** – دروس Django
- **Stack Overflow** – إجابات للأسئلة التقنية المحددة

---

**حظًا موفقًا في مشروعك!**
