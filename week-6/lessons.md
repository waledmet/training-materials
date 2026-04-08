# Week 6 Lessons – Forms, Validation & Authentication

Welcome to Week 6! This week, we'll learn how to handle user input through forms and implement user authentication. By the end of this week, you'll be able to create forms, validate data, and build a complete login/registration system.

---

## Table of Contents

1. [Introduction to Forms](#1-introduction-to-forms)
2. [Django Forms Basics](#2-django-forms-basics)
3. [ModelForm](#3-modelform)
4. [Form Validation](#4-form-validation)
5. [Processing Forms in Views](#5-processing-forms-in-views)
6. [CSRF Protection](#6-csrf-protection)
7. [Django Authentication System](#7-django-authentication-system)
8. [Login and Logout](#8-login-and-logout)
9. [User Registration](#9-user-registration)
10. [Protecting Views](#10-protecting-views)
11. [Class-Based Views](#11-class-based-views)
12. [Messages Framework](#12-messages-framework)
13. [Mini-Project: Blog with Authentication](#13-mini-project-blog-with-authentication)

---

## 1. Introduction to Forms

### Why Forms?

Forms allow users to **interact** with your application by submitting data.

**Common use cases:**
- Login/signup
- Create/edit blog posts
- Contact forms
- Search functionality
- Comments
- Reviews

**Without forms:**
```python
# Hardcoded data
post = Post.objects.create(title="Hardcoded", content="Not flexible")
```

**With forms:**
```html
<!-- User can input their own data -->
<form method="post">
    <input type="text" name="title">
    <textarea name="content"></textarea>
    <button type="submit">Submit</button>
</form>
```

### HTML Forms vs Django Forms

**Plain HTML form:**
```html
<form method="post" action="/submit/">
    <input type="text" name="email">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>
```

**Problems:**
- No validation
- No security (CSRF)
- Repetitive error handling
- Manual HTML writing

**Django Forms solve these:**
- ✅ Automatic HTML generation
- ✅ Built-in validation
- ✅ CSRF protection
- ✅ Error handling
- ✅ Data cleaning

---

## 2. Django Forms Basics

### Creating a Form

**forms.py:**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

**Form fields:**
- `CharField` - text input
- `EmailField` - email validation
- `IntegerField` - numbers
- `BooleanField` - checkboxes
- `ChoiceField` - dropdowns
- `DateField` - date picker

### Field Parameters

```python
class ContactForm(forms.Form):
    # Required field (default)
    name = forms.CharField(max_length=100)

    # Optional field
    phone = forms.CharField(required=False)

    # With help text
    email = forms.EmailField(help_text="We'll never share your email")

    # With initial value
    subject = forms.CharField(initial="Hello")

    # With custom label
    message = forms.CharField(
        label="Your Message",
        widget=forms.Textarea(attrs={'rows': 5})
    )
```

### Widgets

**Widgets control how form fields are rendered:**

```python
from django import forms

class ExampleForm(forms.Form):
    # Text input (default)
    name = forms.CharField()

    # Textarea
    bio = forms.CharField(widget=forms.Textarea)

    # Password input
    password = forms.CharField(widget=forms.PasswordInput)

    # Email input
    email = forms.EmailField(widget=forms.EmailInput)

    # Select dropdown
    country = forms.ChoiceField(choices=[
        ('us', 'United States'),
        ('uk', 'United Kingdom'),
        ('sa', 'Saudi Arabia'),
    ])

    # Checkboxes
    subscribe = forms.BooleanField(widget=forms.CheckboxInput)

    # Radio buttons
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[('m', 'Male'), ('f', 'Female')]
    )
```

### Custom Widget Attributes

```python
class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name',
            'id': 'name-input'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 40,
            'class': 'form-control'
        })
    )
```

---

## 3. ModelForm

### What is ModelForm?

**ModelForm** automatically creates a form from a model.

**Without ModelForm:**
```python
class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.TextField()
    status = forms.ChoiceField(choices=[...])
    # Must manually match model fields
```

**With ModelForm:**
```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
    # Automatically matches model!
```

### Creating a ModelForm

```python
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
```

### ModelForm Meta Options

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # Specify fields to include
        fields = ['title', 'content', 'status']

        # Or use all fields (not recommended)
        # fields = '__all__'

        # Or exclude specific fields
        # exclude = ['created_at', 'author']

        # Custom labels
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }

        # Help texts
        help_texts = {
            'status': 'Choose post visibility',
        }

        # Custom widgets
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
```

### When to Use ModelForm vs Form

**Use ModelForm when:**
- Creating/editing model instances
- Form fields match model fields
- Want automatic validation

**Use Form when:**
- No direct model relationship
- Contact forms
- Search forms
- Login forms (doesn't create/edit model)

---

## 4. Form Validation

### Built-in Validation

Django forms validate automatically:

```python
form = ContactForm(data={'email': 'invalid-email'})
if form.is_valid():
    # Process data
    pass
else:
    # Show errors
    print(form.errors)
```

**Field validators:**
```python
class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20
    )

    email = forms.EmailField()  # Validates email format

    age = forms.IntegerField(
        min_value=18,
        max_value=100
    )

    url = forms.URLField()  # Validates URL format
```

### Custom Field Validation

**Method 1: clean_<fieldname>**

```python
class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")

        # Check if username has spaces
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain spaces")

        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")

        return password_confirm
```

### Form-level Validation

**Method 2: clean()**

```python
class BookingForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError(
                    "End date must be after start date"
                )

        return cleaned_data
```

### Custom Validators

```python
from django.core.exceptions import ValidationError

def validate_even_number(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} is not an even number')

class NumberForm(forms.Form):
    number = forms.IntegerField(validators=[validate_even_number])
```

---

## 5. Processing Forms in Views

### GET vs POST

**GET request:** Display empty form
**POST request:** Process submitted data

### Basic Form View

```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        # Form submitted
        form = ContactForm(request.POST)

        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Do something with the data
            # Send email, save to database, etc.

            return redirect('success')
    else:
        # Display empty form
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

### ModelForm View (Create)

```python
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            # Save to database
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})
```

### ModelForm View (Edit)

```python
from django.shortcuts import get_object_or_404

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'post_form.html', {
        'form': form,
        'post': post
    })
```

### Form Template

```html
<!-- templates/contact.html -->
<form method="post">
    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">Submit</button>
</form>
```

**Form rendering options:**

```html
<!-- As paragraphs (most common) -->
{{ form.as_p }}

<!-- As table -->
<table>{{ form.as_table }}</table>

<!-- As unordered list -->
<ul>{{ form.as_ul }}</ul>

<!-- Manual rendering (full control) -->
<div>
    {{ form.name.label_tag }}
    {{ form.name }}
    {% if form.name.errors %}
        <div class="error">{{ form.name.errors }}</div>
    {% endif %}
</div>
```

### Displaying Form Errors

```html
<form method="post">
    {% csrf_token %}

    <!-- Show all form errors -->
    {% if form.errors %}
        <div class="alert alert-danger">
            Please correct the errors below.
        </div>
    {% endif %}

    <!-- Show field errors -->
    <div>
        {{ form.email.label_tag }}
        {{ form.email }}
        {% if form.email.errors %}
            <div class="error">
                {{ form.email.errors }}
            </div>
        {% endif %}
    </div>

    <button type="submit">Submit</button>
</form>
```

---

## 6. CSRF Protection

### What is CSRF?

**CSRF (Cross-Site Request Forgery):** An attack where a malicious site tricks users into submitting requests to your site.

**Example attack:**
```html
<!-- Malicious site -->
<form action="https://yoursite.com/delete-account" method="post">
    <button>Click for free prize!</button>
</form>
```

### Django's CSRF Protection

**Django protects you automatically:**

1. **In template:**
```html
<form method="post">
    {% csrf_token %}  <!-- Required! -->
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

2. **Django adds hidden token:**
```html
<input type="hidden" name="csrfmiddlewaretoken" value="...long token...">
```

3. **Django verifies token on POST**

**Important:**
- Always use `{% csrf_token %}` in POST forms
- Django rejects forms without valid CSRF token
- GET requests don't need CSRF token

---

## 7. Django Authentication System

### Built-in User Model

Django provides a `User` model:

```python
from django.contrib.auth.models import User

# User fields:
# - username
# - password (hashed)
# - email
# - first_name
# - last_name
# - is_active
# - is_staff
# - is_superuser
# - date_joined
# - last_login
```

### Creating Users

```python
from django.contrib.auth.models import User

# Create regular user
user = User.objects.create_user(
    username='ahmed',
    email='ahmed@example.com',
    password='secure_password'  # Automatically hashed
)

# Create superuser (via shell or createsuperuser command)
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin_password'
)
```

**Never store plain passwords:**
```python
# ❌ WRONG
user.password = 'mypassword'
user.save()

# ✅ CORRECT
user.set_password('mypassword')
user.save()
```

### Checking Passwords

```python
from django.contrib.auth import authenticate

# Authenticate user
user = authenticate(
    username='ahmed',
    password='secure_password'
)

if user is not None:
    # Credentials correct
    print("Login successful")
else:
    # Invalid credentials
    print("Invalid username or password")
```

---

## 8. Login and Logout

### Login View

```python
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')
```

### Login Template

```html
<!-- templates/login.html -->
<h2>Login</h2>

{% if error %}
    <div class="error">{{ error }}</div>
{% endif %}

<form method="post">
    {% csrf_token %}

    <div>
        <label>Username:</label>
        <input type="text" name="username" required>
    </div>

    <div>
        <label>Password:</label>
        <input type="password" name="password" required>
    </div>

    <button type="submit">Login</button>
</form>
```

### Logout View

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

### Using Django's Built-in Views

**Django provides ready-made auth views:**

```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
```

### Accessing Current User

**In views:**
```python
def profile_view(request):
    user = request.user

    if user.is_authenticated:
        username = user.username
        email = user.email
    else:
        # Anonymous user
        pass
```

**In templates:**
```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```

---

## 9. User Registration

### Registration Form

```python
# forms.py
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")

        return cleaned_data
```

### Registration View

```python
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # Create user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Log them in
            login(request, user)

            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
```

### Using UserCreationForm

**Django provides a built-in form:**

```python
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
```

### Custom UserCreationForm

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
```

---

## 10. Protecting Views

### @login_required Decorator

**Require authentication for views:**

```python
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    # Only logged-in users can access
    form = PostForm()
    return render(request, 'post_form.html', {'form': form})
```

**With custom redirect:**
```python
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')
```

**In settings.py:**
```python
LOGIN_URL = '/accounts/login/'  # Default redirect for @login_required
LOGIN_REDIRECT_URL = '/dashboard/'  # Where to go after login
LOGOUT_REDIRECT_URL = '/'  # Where to go after logout
```

### Checking Permissions in Views

```python
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Only author can edit
    if post.author != request.user:
        return redirect('post_detail', post_id=post_id)

    # ... rest of view
```

### Protecting URLs

```python
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create/', login_required(views.post_create), name='post_create'),
]
```

---

## 11. Class-Based Views

### Why Class-Based Views?

**Function-based views:**
```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
```

**Class-based views (CBV):**
```python
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
```

**Benefits:**
- Less code
- Reusable
- Built-in functionality
- Organized

### ListView

**Display list of objects:**

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10  # Optional pagination
```

**URL:**
```python
from .views import PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
]
```

**Template (post_list.html):**
```html
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
```

### DetailView

**Display single object:**

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
```

**URL:**
```python
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
```

### CreateView

**Form to create object:**

```python
from django.views.generic import CreateView
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

### UpdateView

**Form to edit object:**

```python
from django.views.generic import UpdateView

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
```

### DeleteView

**Confirm delete:**

```python
from django.views.generic import DeleteView

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
```

**Template (post_confirm_delete.html):**
```html
<form method="post">
    {% csrf_token %}
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <button type="submit">Yes, delete</button>
    <a href="{% url 'post_detail' post.pk %}">Cancel</a>
</form>
```

### LoginRequiredMixin

**Protect class-based views:**

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = '/login/'
```

---

## 12. Messages Framework

### What is Messages Framework?

Display one-time notifications to users (success, error, warning, info).

**Setup (already enabled by default):**
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.messages',  # Already there
]

MIDDLEWARE = [
    'django.contrib.messages.middleware.MessageMiddleware',  # Already there
]
```

### Adding Messages

```python
from django.contrib import messages

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})
```

### Message Levels

```python
from django.contrib import messages

messages.debug(request, 'Debug info')
messages.info(request, 'For your information')
messages.success(request, 'Success!')
messages.warning(request, 'Warning!')
messages.error(request, 'Error occurred')
```

### Displaying Messages

**base.html:**
```html
{% if messages %}
    <div class="messages">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}
```

**With Bootstrap:**
```html
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="close" data-dismiss="alert">
                <span>&times;</span>
            </button>
        </div>
    {% endfor %}
{% endif %}
```

---

## 13. Mini-Project: Blog with Authentication

### Project Overview

Build a complete blog with:
- User registration and login
- Create/edit posts (authenticated users only)
- View posts (everyone)
- Messages for feedback

### Step 1: Models

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

### Step 2: Forms

```python
# blog/forms.py
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

### Step 3: Views

```python
# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm, RegisterForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, 'You can only edit your own posts.')
        return redirect('post_detail', post_id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'post': post})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('post_list')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('post_list')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('post_list')
```

### Step 4: URLs

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

### Step 5: Templates

**base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Blog{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'post_list' %}">Home</a>
        {% if user.is_authenticated %}
            <a href="{% url 'post_create' %}">New Post</a>
            <span>Hello, {{ user.username }}</span>
            <a href="{% url 'logout' %}">Logout</a>
        {% else %}
            <a href="{% url 'login' %}">Login</a>
            <a href="{% url 'register' %}">Register</a>
        {% endif %}
    </nav>

    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}

    {% block content %}{% endblock %}
</body>
</html>
```

**post_list.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>All Posts</h1>
    {% for post in posts %}
        <article>
            <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
            <p>By {{ post.author.username }} on {{ post.created_at|date:"F j, Y" }}</p>
            <p>{{ post.content|truncatewords:30 }}</p>
        </article>
    {% empty %}
        <p>No posts yet.</p>
    {% endfor %}
{% endblock %}
```

---

## Summary

This week you learned:

1. **Forms** - Django forms and ModelForms
2. **Validation** - Built-in and custom validation
3. **Form Processing** - Handling GET and POST requests
4. **CSRF** - Cross-Site Request Forgery protection
5. **Authentication** - User login, logout, registration
6. **Protection** - @login_required decorator
7. **Class-Based Views** - ListView, DetailView, CreateView, UpdateView, DeleteView
8. **Messages** - User feedback system

### Key Takeaways

- Always use `{% csrf_token %}` in POST forms
- Use ModelForm for model-based forms
- Validate data before processing
- Never store plain passwords
- Protect sensitive views with @login_required
- Use messages for user feedback

### Next Week Preview

Week 7 will cover:
- REST APIs
- Django REST Framework
- JavaScript and AJAX
- Building API endpoints
- Consuming APIs

---

## Additional Resources

- [Django Forms Documentation](https://docs.djangoproject.com/en/stable/topics/forms/)
- [Django Authentication Documentation](https://docs.djangoproject.com/en/stable/topics/auth/)
- [Class-Based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/)
- [Messages Framework](https://docs.djangoproject.com/en/stable/ref/contrib/messages/)
