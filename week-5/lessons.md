# Week 5 Lessons – Models, ORM, Migrations & Admin

Welcome to Week 5! This week, we dive into the **data layer** of Django. You'll learn how to define database models, perform CRUD operations using Django ORM, and manage data through Django's powerful admin interface.

---

## Table of Contents

1. [Introduction to Databases in Django](#1-introduction-to-databases-in-django)
2. [Django Models](#2-django-models)
3. [Field Types](#3-field-types)
4. [Migrations](#4-migrations)
5. [Django ORM Basics](#5-django-orm-basics)
6. [CRUD Operations](#6-crud-operations)
7. [Django Admin Interface](#7-django-admin-interface)
8. [Customizing the Admin](#8-customizing-the-admin)
9. [Django Shell](#9-django-shell)
10. [Mini-Project: Simple Blog with Database](#10-mini-project-simple-blog-with-database)

---

## 1. Introduction to Databases in Django

### What is a Database?

A **database** is an organized collection of structured data stored electronically.

**Real-world analogy:**
- Think of a database like a **filing cabinet**
- Each **drawer** is a table
- Each **folder** is a row/record
- Each **document field** is a column

### Why Do We Need Databases?

**Without a database:**
```python
# Data stored in variables (lost when program stops)
posts = [
    {"title": "First Post", "content": "Hello World"},
    {"title": "Second Post", "content": "More content"}
]
```

**Problems:**
- Data disappears when the server restarts
- Cannot handle large amounts of data
- No easy way to search or filter
- Multiple users cause conflicts

**With a database:**
- Data persists permanently
- Handle millions of records
- Fast searching and filtering
- Support multiple users simultaneously

### SQLite in Django

Django comes with **SQLite** by default:
- **Lightweight**: No separate server needed
- **File-based**: Database is a single file (`db.sqlite3`)
- **Perfect for development**: Easy to get started
- **Production-ready alternatives**: PostgreSQL, MySQL

**Default database location:**
```
myproject/
├── db.sqlite3  ← Your database file
├── manage.py
└── myapp/
```

### SQL vs ORM

**SQL (Structured Query Language):**
```sql
SELECT * FROM posts WHERE published = TRUE;
```

**Django ORM (Object-Relational Mapping):**
```python
Post.objects.filter(published=True)
```

**ORM Benefits:**
- Write Python instead of SQL
- Database-agnostic (switch databases easily)
- Protection from SQL injection
- More readable and maintainable

---

## 2. Django Models

### What is a Model?

A **model** is a Python class that represents a database table.

**Model = Blueprint for data**

```python
# This Python class...
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

**...Creates this database table:**
```
posts table:
┌────┬──────────────┬────────────────┬─────────────────────┐
│ id │    title     │    content     │     created_at      │
├────┼──────────────┼────────────────┼─────────────────────┤
│ 1  │ First Post   │ Hello World!   │ 2024-01-15 10:30:00 │
│ 2  │ Second Post  │ More content   │ 2024-01-15 11:45:00 │
└────┴──────────────┴────────────────┴─────────────────────┘
```

### Creating Your First Model

**Step 1: Define the model in `models.py`**

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

**Step 2: Run migrations (we'll cover this soon!)**

```bash
python manage.py makemigrations
python manage.py migrate
```

### Model Best Practices

**1. Always include `__str__()` method:**
```python
def __str__(self):
    return self.title  # Shows meaningful text instead of "Post object (1)"
```

**2. Use descriptive field names:**
```python
# Good
published_date = models.DateTimeField()

# Bad
pd = models.DateTimeField()
```

**3. Add related_name for relationships:**
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
```

---

## 3. Field Types

Django provides many field types for different kinds of data.

### Text Fields

#### CharField
For short text (requires `max_length`):
```python
title = models.CharField(max_length=200)
first_name = models.CharField(max_length=50)
```

**Use for:** Titles, names, short descriptions

#### TextField
For long text (no length limit):
```python
content = models.TextField()
bio = models.TextField()
```

**Use for:** Articles, descriptions, long content

#### EmailField
Validates email addresses:
```python
email = models.EmailField()
```

**Use for:** Email addresses

#### URLField
Validates URLs:
```python
website = models.URLField()
```

**Use for:** Website links

### Number Fields

#### IntegerField
Whole numbers:
```python
age = models.IntegerField()
count = models.IntegerField(default=0)
```

#### DecimalField
Precise decimal numbers (for money):
```python
price = models.DecimalField(max_digits=10, decimal_places=2)
# Example: 12345678.99
```

#### FloatField
Floating-point numbers:
```python
rating = models.FloatField()
```

### Boolean Fields

#### BooleanField
True/False values:
```python
is_published = models.BooleanField(default=False)
is_active = models.BooleanField(default=True)
```

### Date and Time Fields

#### DateField
Store dates only:
```python
birth_date = models.DateField()
```

#### DateTimeField
Store date AND time:
```python
created_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
updated_at = models.DateTimeField(auto_now=True)      # Update on every save
```

**Important parameters:**
- `auto_now_add=True`: Set when object is created (never changes)
- `auto_now=True`: Update every time object is saved

### Relationship Fields

#### ForeignKey
Many-to-one relationship:
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Many comments belong to one post
```

**`on_delete` options:**
- `models.CASCADE`: Delete comments when post is deleted
- `models.PROTECT`: Prevent post deletion if comments exist
- `models.SET_NULL`: Set to NULL when post is deleted (requires `null=True`)

#### ManyToManyField
Many-to-many relationship:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')
    # Many students can enroll in many courses
```

### Field Options

Common parameters for all fields:

```python
# Required vs Optional
name = models.CharField(max_length=100)                    # Required
middle_name = models.CharField(max_length=100, blank=True)  # Optional in forms

# Null in database
description = models.TextField(null=True, blank=True)      # Can be NULL in DB

# Default values
status = models.CharField(max_length=20, default='draft')

# Unique values
email = models.EmailField(unique=True)  # No duplicates allowed

# Choices
STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]
status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
```

**Important distinction:**
- `blank=True`: Allows empty values in forms (validation)
- `null=True`: Allows NULL in database (storage)

### Complete Example

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    featured_image = models.URLField(blank=True)
    views = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
```

---

## 4. Migrations

### What are Migrations?

**Migrations** are Django's way of propagating changes you make to your models into your database schema.

**Think of migrations as version control for your database.**

### The Migration Workflow

```
1. Create/modify model → 2. Make migration → 3. Apply migration → 4. Database updated
   (models.py)            (makemigrations)     (migrate)           (db.sqlite3)
```

### Creating Migrations

**Command:**
```bash
python manage.py makemigrations
```

**What it does:**
- Scans your models for changes
- Creates migration files in `migrations/` folder
- Doesn't change the database yet

**Example output:**
```
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

### Applying Migrations

**Command:**
```bash
python manage.py migrate
```

**What it does:**
- Executes all pending migrations
- Updates the database schema
- Creates/modifies tables

**Example output:**
```
Running migrations:
  Applying blog.0001_initial... OK
```

### Migration Files

Migrations are stored in `app/migrations/`:
```
blog/
└── migrations/
    ├── __init__.py
    ├── 0001_initial.py      ← First migration
    ├── 0002_post_author.py  ← Added author field
    └── 0003_auto_20240115.py
```

**Example migration file:**
```python
# blog/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

### Common Migration Commands

```bash
# Check for model changes without creating migrations
python manage.py makemigrations --dry-run

# Show migration status
python manage.py showmigrations

# View SQL for a migration (without running it)
python manage.py sqlmigrate blog 0001

# Undo last migration
python manage.py migrate blog 0001
```

### Migration Best Practices

1. **Always create migrations after model changes**
2. **Commit migrations to version control (Git)**
3. **Never edit applied migrations** (create a new one instead)
4. **Run migrations on all environments** (dev, staging, production)

### Common Migration Issues

**Problem: "No changes detected"**
```bash
# Solution: Make sure app is in INSTALLED_APPS
# settings.py
INSTALLED_APPS = [
    'blog',  # Add your app here
]
```

**Problem: Migration conflicts**
```bash
# Solution: Merge migrations
python manage.py makemigrations --merge
```

---

## 5. Django ORM Basics

### What is ORM?

**ORM (Object-Relational Mapping)** lets you interact with your database using Python objects instead of SQL.

**Without ORM (SQL):**
```sql
SELECT * FROM blog_post WHERE status = 'published';
```

**With ORM (Python):**
```python
Post.objects.filter(status='published')
```

### QuerySets

A **QuerySet** is a collection of database queries.

```python
# Get all posts
posts = Post.objects.all()  # Returns QuerySet

# QuerySets are lazy (query not executed yet)
posts = Post.objects.all()  # No database hit

# Query executed when you iterate
for post in posts:          # Database hit happens here
    print(post.title)
```

### The Objects Manager

Every model has an `objects` manager:

```python
Post.objects  # Manager for Post model
```

**Common methods:**
- `all()` - Get all records
- `filter()` - Get records matching conditions
- `get()` - Get single record
- `create()` - Create new record
- `update()` - Update records
- `delete()` - Delete records

---

## 6. CRUD Operations

### Create - Adding Data

**Method 1: Create and save**
```python
post = Post(title="My First Post", content="Hello World!")
post.save()
```

**Method 2: Using create()**
```python
post = Post.objects.create(
    title="My First Post",
    content="Hello World!"
)
```

**Method 3: Bulk create**
```python
Post.objects.bulk_create([
    Post(title="Post 1", content="Content 1"),
    Post(title="Post 2", content="Content 2"),
    Post(title="Post 3", content="Content 3"),
])
```

### Read - Retrieving Data

**Get all records:**
```python
posts = Post.objects.all()
```

**Filter records:**
```python
# Single condition
published_posts = Post.objects.filter(status='published')

# Multiple conditions (AND)
recent_published = Post.objects.filter(status='published', is_featured=True)

# OR conditions
from django.db.models import Q
posts = Post.objects.filter(Q(status='published') | Q(is_featured=True))

# Exclude records (NOT)
not_drafts = Post.objects.exclude(status='draft')
```

**Get single record:**
```python
# Get by ID
post = Post.objects.get(id=1)

# Get by unique field
post = Post.objects.get(slug='my-first-post')

# Be careful: get() raises exception if not found or multiple found
```

**Ordering:**
```python
# Ascending
posts = Post.objects.order_by('created_at')

# Descending
posts = Post.objects.order_by('-created_at')

# Multiple fields
posts = Post.objects.order_by('-is_featured', '-created_at')
```

**Limiting results:**
```python
# First 5 posts
posts = Post.objects.all()[:5]

# Posts 5-10 (pagination)
posts = Post.objects.all()[5:10]

# First post
first_post = Post.objects.first()

# Last post
last_post = Post.objects.last()
```

**Counting:**
```python
total = Post.objects.count()
published_count = Post.objects.filter(status='published').count()
```

**Check if exists:**
```python
has_posts = Post.objects.filter(status='published').exists()
```

### Update - Modifying Data

**Method 1: Save existing object**
```python
post = Post.objects.get(id=1)
post.title = "Updated Title"
post.save()
```

**Method 2: Update queryset (more efficient)**
```python
# Update single field
Post.objects.filter(status='draft').update(status='published')

# Update multiple fields
Post.objects.filter(id=1).update(
    title="New Title",
    content="New Content"
)
```

**Method 3: Update or create**
```python
post, created = Post.objects.update_or_create(
    slug='my-post',
    defaults={'title': 'My Post', 'content': 'Content'}
)
```

### Delete - Removing Data

**Delete single object:**
```python
post = Post.objects.get(id=1)
post.delete()
```

**Delete multiple objects:**
```python
# Delete all drafts
Post.objects.filter(status='draft').delete()

# Delete all posts (be careful!)
Post.objects.all().delete()
```

### Chaining QuerySet Methods

```python
# Multiple filters
posts = Post.objects.filter(status='published')\
                    .filter(is_featured=True)\
                    .order_by('-created_at')[:5]

# Equivalent to:
SELECT * FROM blog_post
WHERE status = 'published' AND is_featured = TRUE
ORDER BY created_at DESC
LIMIT 5;
```

---

## 7. Django Admin Interface

### What is Django Admin?

Django Admin is a **built-in web interface** for managing your data.

**Features:**
- Automatic CRUD interface
- User authentication
- Search and filtering
- Data validation
- Customizable

**Access:** `http://localhost:8000/admin/`

### Creating a Superuser

**Command:**
```bash
python manage.py createsuperuser
```

**You'll be prompted for:**
- Username
- Email
- Password

**Example:**
```bash
Username: admin
Email: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### Registering Models

**To manage models in admin, register them:**

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

**Now `Post` appears in admin interface!**

### Basic Admin Usage

1. Start server: `python manage.py runserver`
2. Visit: `http://localhost:8000/admin/`
3. Login with superuser credentials
4. Click on model name (e.g., "Posts")
5. Add/edit/delete records

---

## 8. Customizing the Admin

### ModelAdmin Class

Customize how models appear in admin:

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'author')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
```

### Common Customizations

#### list_display
Fields to show in list view:
```python
list_display = ('title', 'author', 'status', 'created_at')
```

#### list_filter
Add filters sidebar:
```python
list_filter = ('status', 'is_featured', 'created_at')
```

#### search_fields
Enable search:
```python
search_fields = ('title', 'content', 'author__username')
```

#### prepopulated_fields
Auto-fill fields (useful for slugs):
```python
prepopulated_fields = {'slug': ('title',)}
```

#### readonly_fields
Make fields read-only:
```python
readonly_fields = ('created_at', 'updated_at', 'views')
```

#### fieldsets
Organize fields into sections:
```python
fieldsets = (
    ('Basic Information', {
        'fields': ('title', 'slug', 'author')
    }),
    ('Content', {
        'fields': ('content', 'excerpt')
    }),
    ('Settings', {
        'fields': ('status', 'is_featured', 'featured_image')
    }),
)
```

### Custom Admin Methods

Display custom columns:

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'word_count', 'created_at')

    @admin.display(description='Word Count')
    def word_count(self, obj):
        return len(obj.content.split())
```

---

## 9. Django Shell

### What is Django Shell?

An interactive Python shell with Django environment loaded.

**Start the shell:**
```bash
python manage.py shell
```

### Using the Shell

```python
# Import model
>>> from blog.models import Post

# Create post
>>> post = Post.objects.create(title="Test", content="Testing")

# Get all posts
>>> Post.objects.all()
<QuerySet [<Post: Test>]>

# Filter posts
>>> Post.objects.filter(status='published')

# Get single post
>>> post = Post.objects.get(id=1)
>>> post.title
'Test'

# Update post
>>> post.title = "Updated"
>>> post.save()

# Delete post
>>> post.delete()

# Count posts
>>> Post.objects.count()
5

# Exit shell
>>> exit()
```

### Shell Best Practices

**Use shell for:**
- Testing queries before writing views
- Debugging data issues
- One-off data operations
- Learning ORM

**Don't use shell for:**
- Regular data entry (use admin interface)
- Production data changes (write scripts instead)

---

## 10. Mini-Project: Simple Blog with Database

### Project Goals

Build a blog application with:
- Post model (title, content, created_at)
- List all posts page
- Single post detail page
- Admin interface to manage posts

### Step 1: Create the Blog App

```bash
python manage.py startapp blog
```

**Add to settings:**
```python
# settings.py
INSTALLED_APPS = [
    # ...
    'blog',
]
```

### Step 2: Create Post Model

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

### Step 3: Create and Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Register in Admin

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
```

### Step 5: Create Views

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
```

### Step 6: Configure URLs

```python
# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
```

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

### Step 7: Create Templates

```html
<!-- blog/templates/blog/post_list.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Blog Posts</title>
</head>
<body>
    <h1>All Blog Posts</h1>
    {% for post in posts %}
        <article>
            <h2>
                <a href="{% url 'blog:post_detail' post.id %}">{{ post.title }}</a>
            </h2>
            <p>Published: {{ post.created_at|date:"F j, Y" }}</p>
            <p>{{ post.content|truncatewords:30 }}</p>
        </article>
        <hr>
    {% empty %}
        <p>No posts yet.</p>
    {% endfor %}
</body>
</html>
```

```html
<!-- blog/templates/blog/post_detail.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ post.title }}</title>
</head>
<body>
    <article>
        <h1>{{ post.title }}</h1>
        <p>Published: {{ post.created_at|date:"F j, Y" }}</p>
        <div>
            {{ post.content|linebreaks }}
        </div>
    </article>
    <a href="{% url 'blog:post_list' %}">← Back to all posts</a>
</body>
</html>
```

### Step 8: Test Everything

1. Create superuser: `python manage.py createsuperuser`
2. Run server: `python manage.py runserver`
3. Add posts via admin: `http://localhost:8000/admin/`
4. View blog: `http://localhost:8000/blog/`
5. Click post to see details

### Step 9: Use Django Shell

```bash
python manage.py shell
```

```python
# Test ORM queries
from blog.models import Post

# Create a post
Post.objects.create(title="Shell Post", content="Created from shell!")

# Get all posts
Post.objects.all()

# Filter posts
Post.objects.filter(title__contains="Shell")

# Count posts
Post.objects.count()
```

---

## Summary

This week you learned:

1. **Databases**: Why we need them and how Django uses SQLite
2. **Models**: Define data structure using Python classes
3. **Field Types**: CharField, TextField, DateTimeField, ForeignKey, etc.
4. **Migrations**: Version control for database schema
5. **ORM**: Query database using Python (CRUD operations)
6. **Admin Interface**: Built-in tool for data management
7. **Django Shell**: Interactive testing environment

### Key Commands

```bash
# Migrations
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations

# Admin
python manage.py createsuperuser

# Shell
python manage.py shell
```

### Next Week Preview

Week 6 will cover:
- Django Forms
- Form validation
- User authentication (login/logout)
- Class-based views
- Messages framework

---

## Additional Resources

- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django QuerySet API](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [Django Admin Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [Database Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)
