# Week 8 Resources – Final Project: Design & Build

Curated resources for Week 8: Building a complete Django application.

---

## Project Planning Resources

### Requirements & User Stories

- **User Story Template:** "As a [user], I want to [action] so that [benefit]"
- **MoSCoW Prioritization:** Must have, Should have, Could have, Won't have
- **Agile User Stories Guide** - https://www.atlassian.com/agile/project-management/user-stories

### Wireframing Tools

- **Excalidraw** - https://excalidraw.com/ (Simple, free)
- **Figma** - https://www.figma.com/ (Professional, free tier)
- **Balsamiq** - https://balsamiq.com/ (Quick wireframes)
- **Paper & Pen** - Still the fastest!

---

## Django Documentation

### Essential References

1. **Models** - https://docs.djangoproject.com/en/stable/topics/db/models/
2. **Views** - https://docs.djangoproject.com/en/stable/topics/http/views/
3. **Templates** - https://docs.djangoproject.com/en/stable/topics/templates/
4. **Forms** - https://docs.djangoproject.com/en/stable/topics/forms/
5. **Authentication** - https://docs.djangoproject.com/en/stable/topics/auth/
6. **Class-Based Views** - https://docs.djangoproject.com/en/stable/topics/class-based-views/

---

## Quick Reference Cheat Sheets

### Model Field Types

```python
# Text
CharField(max_length=100)
TextField()
EmailField()
URLField()
SlugField()

# Numbers
IntegerField()
FloatField()
DecimalField(max_digits=10, decimal_places=2)

# Boolean
BooleanField(default=False)

# Date/Time
DateField()
DateTimeField()
TimeField()
DateField(auto_now_add=True)  # Set on create
DateTimeField(auto_now=True)  # Set on every save

# Relationships
ForeignKey(Model, on_delete=models.CASCADE)
ManyToManyField(Model)
OneToOneField(Model, on_delete=models.CASCADE)

# Files
FileField(upload_to='uploads/')
ImageField(upload_to='images/')
```

### Model Meta Options

```python
class Meta:
    ordering = ['-created_at']
    verbose_name = 'Task'
    verbose_name_plural = 'Tasks'
    unique_together = ['user', 'title']
```

### View Patterns

```python
# Function-based view
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

### Class-Based Views

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

### Form Widgets

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

### URL Patterns

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

### Template Tags

```html
<!-- URL -->
<a href="{% url 'item_detail' item.pk %}">View</a>

<!-- Static files -->
{% load static %}
<link href="{% static 'css/style.css' %}" rel="stylesheet">

<!-- Conditionals -->
{% if user.is_authenticated %}
    Welcome, {{ user.username }}
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}

<!-- Loops -->
{% for item in items %}
    <p>{{ item.title }}</p>
{% empty %}
    <p>No items found.</p>
{% endfor %}

<!-- Filters -->
{{ item.created_at|date:"M d, Y" }}
{{ item.description|truncatewords:20 }}
{{ item.status|default:"Unknown" }}
```

---

## Bootstrap Quick Reference

### Basic Layout

```html
<div class="container">
    <div class="row">
        <div class="col-md-6">Half width on medium+</div>
        <div class="col-md-6">Half width on medium+</div>
    </div>
</div>
```

### Cards

```html
<div class="card">
    <div class="card-header">Title</div>
    <div class="card-body">
        <h5 class="card-title">Card Title</h5>
        <p class="card-text">Content here.</p>
        <a href="#" class="btn btn-primary">Action</a>
    </div>
</div>
```

### Alerts

```html
<div class="alert alert-success">Success message!</div>
<div class="alert alert-danger">Error message!</div>
<div class="alert alert-warning">Warning message!</div>
<div class="alert alert-info">Info message!</div>
```

### Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Delete</button>
<button class="btn btn-outline-primary">Outline</button>
<button class="btn btn-sm">Small</button>
<button class="btn btn-lg">Large</button>
```

### Forms

```html
<form method="post">
    {% csrf_token %}
    <div class="mb-3">
        <label class="form-label">Title</label>
        <input type="text" class="form-control" name="title">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

### Navigation

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="#">Brand</a>
        <div class="navbar-nav ms-auto">
            <a class="nav-link" href="#">Link</a>
        </div>
    </div>
</nav>
```

---

## Project Examples

### Task Manager

```python
# Models
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

### Student Management

```python
# Models
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

### Support Tickets

```python
# Models
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

## Security Checklist

- [ ] Use {% csrf_token %} in all POST forms
- [ ] Filter querysets by user
- [ ] Check ownership before edit/delete
- [ ] Use @login_required on protected views
- [ ] Don't expose sensitive data in templates
- [ ] Validate all form input
- [ ] Use Django's authentication system

---

## Debugging Tips

### Common Errors

**TemplateDoesNotExist:**
- Check template path
- Check TEMPLATES['DIRS'] in settings
- Verify APP_DIRS is True

**NoReverseMatch:**
- Check URL name exists
- Check you're passing required arguments
- Check for typos

**AttributeError: 'NoneType':**
- Check if object exists before accessing
- Use get_object_or_404()

**IntegrityError:**
- Check required fields
- Check unique constraints
- Check foreign key references

### Debugging Techniques

```python
# Print in views
print("DEBUG:", variable)

# Print in templates
{{ variable|pprint }}

# Django Debug Toolbar
pip install django-debug-toolbar

# Shell debugging
python manage.py shell
```

---

## Additional Resources

- **Two Scoops of Django** - Best practices book
- **Django Girls Tutorial** - Beginner-friendly
- **Simple is Better than Complex** - Blog with tutorials
- **Real Python** - Django tutorials
- **Stack Overflow** - Q&A for specific issues

---

**Good luck with your project!**
