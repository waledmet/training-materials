# Week 6 Exercises – Forms, Validation & Authentication Practice

Practice exercises for Week 6: Django forms, form validation, user authentication, and class-based views.

---

## Table of Contents

1. [Day 1: Django Forms Basics](#day-1-django-forms-basics)
2. [Day 2: Form Validation & Processing](#day-2-form-validation--processing)
3. [Day 3: User Authentication](#day-3-user-authentication)
4. [Day 4: Class-Based Views](#day-4-class-based-views)
5. [Day 5: Complete Project with Authentication](#day-5-complete-project-with-authentication)
6. [Challenge Exercises](#challenge-exercises)

---

## Day 1: Django Forms Basics

### Exercise 1: Create a Contact Form

**Task:**
1. Create a Django project called `contact_site`
2. Create an app called `contact`
3. Create a `ContactForm` with these fields:
   - name (CharField, max_length=100)
   - email (EmailField)
   - subject (CharField, max_length=200)
   - message (CharField with Textarea widget)

<details>
<summary>Solution</summary>

```bash
django-admin startproject contact_site
cd contact_site
python manage.py startapp contact
```

```python
# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
```

```python
# contact_site/settings.py
INSTALLED_APPS = [
    # ...
    'contact',
]
```
</details>

---

### Exercise 2: Create a View to Display the Form

**Task:**
1. Create a view that displays the ContactForm
2. Configure URLs to access the form at `/contact/`
3. Create a template to render the form

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
```

```python
# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
]
```

```python
# contact_site/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
]
```

```html
<!-- contact/templates/contact/contact.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Send</button>
    </form>
</body>
</html>
```
</details>

---

### Exercise 3: Add Custom Widgets and Attributes

**Task:**
Update the ContactForm to:
- Add placeholder text to all fields
- Set the message textarea to 5 rows
- Add CSS class 'form-control' to all fields

<details>
<summary>Solution</summary>

```python
# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'form-control'
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-control'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message here...',
            'class': 'form-control',
            'rows': 5
        })
    )
```
</details>

---

### Exercise 4: Create a ModelForm

**Task:**
1. Create a `Feedback` model with fields: name, email, rating (1-5), comment
2. Create a ModelForm for the Feedback model
3. Create a view to display the form

<details>
<summary>Solution</summary>

```python
# contact/models.py
from django.db import models

class Feedback(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}/5"
```

```python
# contact/forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }
```

```bash
python manage.py makemigrations
python manage.py migrate
```

```python
# contact/views.py
from .forms import FeedbackForm

def feedback_view(request):
    form = FeedbackForm()
    return render(request, 'contact/feedback.html', {'form': form})
```
</details>

---

### Exercise 5: Customize ModelForm

**Task:**
Customize the FeedbackForm to:
- Change field labels
- Add help text
- Customize widgets with CSS classes

<details>
<summary>Solution</summary>

```python
# contact/forms.py
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comment']

        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'rating': 'How would you rate us?',
            'comment': 'Additional Comments',
        }

        help_texts = {
            'rating': 'Select a rating from 1 (Poor) to 5 (Excellent)',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
```
</details>

---

## Day 2: Form Validation & Processing

### Exercise 6: Process Form Submission

**Task:**
Update the contact_view to:
1. Handle POST requests
2. Validate the form
3. Print form data to console if valid
4. Display success message

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print(f"Contact from: {name} ({email})")
            print(f"Subject: {subject}")
            print(f"Message: {message}")

            # In real app, send email here
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
```

```html
<!-- contact/templates/contact/success.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Success</title>
</head>
<body>
    <h1>Thank You!</h1>
    <p>Your message has been sent successfully.</p>
    <a href="{% url 'contact' %}">Send another message</a>
</body>
</html>
```
</details>

---

### Exercise 7: Save ModelForm to Database

**Task:**
Update feedback_view to:
1. Save valid feedback to database
2. Redirect to success page
3. Show all submitted feedback

<details>
<summary>Solution</summary>

```python
# contact/views.py
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()

    return render(request, 'contact/feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'contact/feedback_success.html')

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'contact/feedback_list.html', {'feedbacks': feedbacks})
```

```python
# contact/urls.py
urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    path('feedback/list/', views.feedback_list, name='feedback_list'),
]
```
</details>

---

### Exercise 8: Add Custom Validation

**Task:**
Add validation to ContactForm:
1. Name must be at least 3 characters
2. Message must be at least 10 characters
3. Subject cannot contain the word "spam" (case-insensitive)

<details>
<summary>Solution</summary>

```python
# contact/forms.py
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long")
        return message

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if 'spam' in subject.lower():
            raise forms.ValidationError("Subject cannot contain 'spam'")
        return subject
```
</details>

---

### Exercise 9: Display Form Errors

**Task:**
Update the contact template to:
1. Display field-specific errors
2. Display non-field errors
3. Highlight fields with errors

<details>
<summary>Solution</summary>

```html
<!-- contact/templates/contact/contact.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <style>
        .error { color: red; }
        .errorlist { list-style: none; padding: 0; }
        .field-error { border: 1px solid red; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>

    {% if form.non_field_errors %}
        <div class="error">
            {{ form.non_field_errors }}
        </div>
    {% endif %}

    <form method="post">
        {% csrf_token %}

        <div>
            <label>{{ form.name.label }}:</label>
            {{ form.name }}
            {% if form.name.errors %}
                <div class="error">{{ form.name.errors }}</div>
            {% endif %}
        </div>

        <div>
            <label>{{ form.email.label }}:</label>
            {{ form.email }}
            {% if form.email.errors %}
                <div class="error">{{ form.email.errors }}</div>
            {% endif %}
        </div>

        <div>
            <label>{{ form.subject.label }}:</label>
            {{ form.subject }}
            {% if form.subject.errors %}
                <div class="error">{{ form.subject.errors }}</div>
            {% endif %}
        </div>

        <div>
            <label>{{ form.message.label }}:</label>
            {{ form.message }}
            {% if form.message.errors %}
                <div class="error">{{ form.message.errors }}</div>
            {% endif %}
        </div>

        <button type="submit">Send</button>
    </form>
</body>
</html>
```
</details>

---

### Exercise 10: Form-level Validation

**Task:**
Create a BookingForm with:
- start_date (DateField)
- end_date (DateField)
- Add validation: end_date must be after start_date

<details>
<summary>Solution</summary>

```python
# contact/forms.py
from datetime import date

class BookingForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date must be after start date")

            if start_date < date.today():
                raise forms.ValidationError("Start date cannot be in the past")

        return cleaned_data
```
</details>

---

## Day 3: User Authentication

### Exercise 11: Create Login View

**Task:**
1. Create a login view
2. Create login template
3. Configure URL at `/login/`
4. Test login functionality

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'contact/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'contact/login.html')
```

```html
<!-- contact/templates/contact/login.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>

    {% if error %}
        <div style="color: red;">{{ error }}</div>
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

    <p>Don't have an account? <a href="{% url 'register' %}">Register</a></p>
</body>
</html>
```

```python
# contact/urls.py
urlpatterns = [
    # ...
    path('login/', views.login_view, name='login'),
]
```
</details>

---

### Exercise 12: Create Logout View

**Task:**
1. Create logout view
2. Add logout link to navigation
3. Test logout functionality

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

```python
# contact/urls.py
urlpatterns = [
    # ...
    path('logout/', views.logout_view, name='logout'),
]
```

```html
<!-- In your base template or navigation -->
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
{% endif %}
```
</details>

---

### Exercise 13: Create Registration Form and View

**Task:**
1. Create a registration form (username, email, password, confirm password)
2. Add validation to ensure passwords match
3. Create registration view
4. Create user upon successful registration

<details>
<summary>Solution</summary>

```python
# contact/forms.py
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

```python
# contact/views.py
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'contact/register.html', {'form': form})
```

```html
<!-- contact/templates/contact/register.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>

    <p>Already have an account? <a href="{% url 'login' %}">Login</a></p>
</body>
</html>
```
</details>

---

### Exercise 14: Protect Views with @login_required

**Task:**
1. Create a profile view (must be logged in)
2. Protect it with @login_required decorator
3. Set LOGIN_URL in settings
4. Test by accessing without login

<details>
<summary>Solution</summary>

```python
# contact_site/settings.py
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
```

```python
# contact/views.py
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'contact/profile.html')
```

```html
<!-- contact/templates/contact/profile.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Profile</title>
</head>
<body>
    <h1>Profile</h1>
    <p>Username: {{ user.username }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Date Joined: {{ user.date_joined }}</p>
</body>
</html>
```

```python
# contact/urls.py
urlpatterns = [
    # ...
    path('profile/', views.profile_view, name='profile'),
]
```
</details>

---

### Exercise 15: Add Messages Framework

**Task:**
1. Add success message after login
2. Add success message after registration
3. Add info message after logout
4. Display messages in base template

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'contact/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, 'Welcome! Your account has been created.')
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'contact/register.html', {'form': form})
```

```html
<!-- contact/templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        {% if user.is_authenticated %}
            <a href="{% url 'profile' %}">Profile</a>
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
</details>

---

## Day 4: Class-Based Views

### Exercise 16: Convert to ListView

**Task:**
Convert the feedback_list view to use ListView

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.views.generic import ListView
from .models import Feedback

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'contact/feedback_list.html'
    context_object_name = 'feedbacks'
    ordering = ['-created_at']
    paginate_by = 10
```

```python
# contact/urls.py
from .views import FeedbackListView

urlpatterns = [
    # ...
    path('feedback/list/', FeedbackListView.as_view(), name='feedback_list'),
]
```
</details>

---

### Exercise 17: Create DetailView

**Task:**
Create a DetailView to display individual feedback

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.views.generic import DetailView

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'contact/feedback_detail.html'
    context_object_name = 'feedback'
```

```html
<!-- contact/templates/contact/feedback_detail.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Feedback Detail</title>
</head>
<body>
    <h1>Feedback from {{ feedback.name }}</h1>
    <p><strong>Email:</strong> {{ feedback.email }}</p>
    <p><strong>Rating:</strong> {{ feedback.rating }}/5</p>
    <p><strong>Comment:</strong> {{ feedback.comment }}</p>
    <p><strong>Submitted:</strong> {{ feedback.created_at }}</p>
    <a href="{% url 'feedback_list' %}">Back to list</a>
</body>
</html>
```

```python
# contact/urls.py
urlpatterns = [
    # ...
    path('feedback/<int:pk>/', FeedbackDetailView.as_view(), name='feedback_detail'),
]
```
</details>

---

### Exercise 18: Create CreateView

**Task:**
Convert feedback_view to use CreateView

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.views.generic import CreateView
from django.urls import reverse_lazy

class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact/feedback_form.html'
    success_url = reverse_lazy('feedback_success')
```

```python
# contact/urls.py
urlpatterns = [
    # ...
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
```
</details>

---

### Exercise 19: Create UpdateView and DeleteView

**Task:**
1. Create UpdateView to edit feedback
2. Create DeleteView to delete feedback
3. Both should require login

<details>
<summary>Solution</summary>

```python
# contact/views.py
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class FeedbackUpdateView(LoginRequiredMixin, UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact/feedback_form.html'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('feedback_detail', kwargs={'pk': self.object.pk})

class FeedbackDeleteView(LoginRequiredMixin, DeleteView):
    model = Feedback
    template_name = 'contact/feedback_confirm_delete.html'
    success_url = reverse_lazy('feedback_list')
    login_url = '/login/'
```

```html
<!-- contact/templates/contact/feedback_confirm_delete.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Delete Feedback</title>
</head>
<body>
    <h1>Delete Feedback</h1>
    <form method="post">
        {% csrf_token %}
        <p>Are you sure you want to delete this feedback from {{ feedback.name }}?</p>
        <button type="submit">Yes, delete</button>
        <a href="{% url 'feedback_detail' feedback.pk %}">Cancel</a>
    </form>
</body>
</html>
```

```python
# contact/urls.py
urlpatterns = [
    # ...
    path('feedback/<int:pk>/edit/', FeedbackUpdateView.as_view(), name='feedback_edit'),
    path('feedback/<int:pk>/delete/', FeedbackDeleteView.as_view(), name='feedback_delete'),
]
```
</details>

---

### Exercise 20: Complete CRUD with CBVs

**Task:**
Create a simple Note app with full CRUD using only class-based views:
- Model: Note (title, content, author, created_at)
- List, Detail, Create, Update, Delete views
- Only authenticated users can create/edit/delete
- Users can only edit/delete their own notes

<details>
<summary>Solution</summary>

```python
# contact/models.py
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```python
# contact/views.py
class NoteListView(ListView):
    model = Note
    template_name = 'contact/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created_at']

class NoteDetailView(DetailView):
    model = Note
    template_name = 'contact/note_detail.html'
    context_object_name = 'note'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'contact/note_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'contact/note_form.html'
    login_url = '/login/'

    def get_queryset(self):
        # Users can only edit their own notes
        return Note.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('note_detail', kwargs={'pk': self.object.pk})

class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'contact/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
    login_url = '/login/'

    def get_queryset(self):
        # Users can only delete their own notes
        return Note.objects.filter(author=self.request.user)
```
</details>

---

## Day 5: Complete Project with Authentication

### Exercise 21: Build Complete Blog with Authentication

**Task:**
Create a complete blog application with:
1. User registration, login, logout
2. Create posts (authenticated users only)
3. Edit posts (author only)
4. Delete posts (author only)
5. View posts (everyone)
6. Messages for all actions
7. Use class-based views where appropriate

**Requirements:**
- Post model: title, content, author, created_at, updated_at
- All CRUD operations
- Proper authentication and authorization
- User-friendly messages
- Clean navigation
- Error handling

<details>
<summary>Solution Structure</summary>

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

```python
# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    login_url = '/login/'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = '/login/'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)
```

Continue with authentication views, templates, and URLs following the patterns from earlier exercises.

</details>

---

## Challenge Exercises

### Challenge 1: Password Reset

Implement password reset functionality:
- Password reset request form
- Email with reset link (mock or real)
- Reset password form
- Confirmation page

### Challenge 2: User Profile

Create user profile functionality:
- Profile model (bio, avatar URL, website)
- Profile page showing user info and posts
- Edit profile form
- Profile picture upload

### Challenge 3: Advanced Forms

Create a multi-step registration form:
- Step 1: Username and email
- Step 2: Password
- Step 3: Profile information
- Use sessions to store data between steps

### Challenge 4: Search Form

Add search functionality:
- Search form (keyword)
- Filter posts by title and content
- Display search results
- Highlight search terms

### Challenge 5: Comment System

Add comments to blog posts:
- Comment model (post, author, content, created_at)
- Display comments on post detail
- Add comment form (authenticated users only)
- Delete own comments

---

## Testing Your Knowledge

After completing these exercises, you should be able to:
- ✓ Create Django forms and ModelForms
- ✓ Add validation to forms
- ✓ Process form submissions
- ✓ Implement user authentication
- ✓ Protect views with decorators and mixins
- ✓ Use class-based views
- ✓ Display messages to users
- ✓ Build complete CRUD applications with authentication

---

## Next Steps

1. Complete all exercises in order
2. Build your own project with authentication
3. Experiment with custom user models
4. Explore Django's built-in auth views
5. Learn about permissions and groups
