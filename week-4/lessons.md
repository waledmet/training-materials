# Week 4 Lessons – Django Basics: Project, Apps, Views & Templates

Welcome to Week 4! This week, we transition from static HTML/CSS to dynamic web applications using **Django**, a powerful Python web framework.

---

## Table of Contents

1. [What is Django?](#1-what-is-django)
2. [Installing Django](#2-installing-django)
3. [Creating Your First Django Project](#3-creating-your-first-django-project)
4. [Understanding Project Structure](#4-understanding-project-structure)
5. [Creating a Django App](#5-creating-a-django-app)
6. [URLs and Views](#6-urls-and-views)
7. [Django Templates](#7-django-templates)
8. [Template Inheritance](#8-template-inheritance)
9. [Static Files (CSS, Images)](#9-static-files-css-images)
10. [Mini-Project: 3-Page Django Website](#10-mini-project-3-page-django-website)

---

## 1. What is Django?

### What is a Web Framework?

A **web framework** provides tools and structure to build web applications faster and more efficiently.

**Without a framework:**
```python
# You handle everything manually
- Parse HTTP requests
- Route URLs
- Generate HTML
- Handle databases
- Manage sessions
- Handle security
```

**With Django:**
```python
# Django handles the hard parts
- ✓ URL routing built-in
- ✓ Template engine included
- ✓ Database ORM ready
- ✓ Security features enabled
- ✓ Admin interface automatic
```

### Why Django?

**Advantages:**
- **Batteries included**: Everything you need comes with Django
- **Python-based**: Use your Python skills
- **Fast development**: Build quickly with less code
- **Secure**: Built-in protection against common attacks
- **Scalable**: Used by Instagram, Pinterest, Mozilla
- **Great documentation**: Excellent learning resources

**Popular Django Sites:**
- Instagram
- Pinterest
- Mozilla
- Spotify
- YouTube (parts of it)
- The Washington Post

### Django Philosophy

Django follows the **"Don't Repeat Yourself" (DRY)** principle:
- Write code once
- Reuse it everywhere
- Less duplication = fewer bugs

Django uses the **MTV Pattern**:
- **M**odel: Database layer (Week 5)
- **T**emplate: Presentation layer (Week 4)
- **V**iew: Business logic layer (Week 4)

Similar to MVC (Model-View-Controller) pattern.

---

## 2. Installing Django

### Prerequisites

You should have:
- Python 3.8+ installed
- pip (Python package manager)
- Virtual environment knowledge (Week 2)
- A text editor (VS Code)

### Step 1: Create a Virtual Environment

**Why use a virtual environment?**
- Isolate project dependencies
- Avoid conflicts between projects
- Keep your system Python clean

**Create and activate:**

**Windows:**
```bash
# Navigate to your projects folder
cd Documents

# Create a folder for Week 4
mkdir week-4-django
cd week-4-django

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# You should see (venv) in your terminal
```

**Mac/Linux:**
```bash
# Navigate to your projects folder
cd ~/Documents

# Create a folder for Week 4
mkdir week-4-django
cd week-4-django

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) in your terminal
```

### Step 2: Install Django

```bash
# Make sure virtual environment is activated (you see (venv))
pip install django

# Verify installation
django-admin --version

# Should show: 5.x.x (or similar)
```

### Step 3: Save Dependencies

```bash
# Create requirements.txt
pip freeze > requirements.txt

# This file lists all installed packages
# Useful for sharing your project
```

---

## 3. Creating Your First Django Project

### What is a Django Project?

A **project** is the entire web application:
- Contains settings
- Connects multiple apps
- Handles URL routing
- Manages configuration

Think of it as the **container** for your website.

### Create a Project

```bash
# Make sure you're in week-4-django folder with venv activated

# Create a new Django project called "mysite"
django-admin startproject mysite

# This creates a folder structure
```

**What was created:**

```
mysite/
│
├── mysite/
│   ├── __init__.py      # Makes this a Python package
│   ├── settings.py      # Project settings (IMPORTANT)
│   ├── urls.py          # Main URL routing
│   ├── asgi.py          # Async server config
│   └── wsgi.py          # Web server config
│
└── manage.py            # Command-line tool (IMPORTANT)
```

### Navigate into Project

```bash
cd mysite

# You should now be in: week-4-django/mysite/
# This folder contains manage.py
```

### Run the Development Server

```bash
# Start Django's development server
python manage.py runserver

# You should see:
# Starting development server at http://127.0.0.1:8000/
```

**Open your browser:**
- Go to: `http://127.0.0.1:8000/` or `http://localhost:8000/`
- You should see a **"The install worked successfully!"** page

🎉 **Congratulations! Your first Django project is running!**

**To stop the server:**
- Press `Ctrl+C` in the terminal

---

## 4. Understanding Project Structure

### Key Files Explained

#### `manage.py`

Your **command-line tool** for Django:

```bash
python manage.py runserver      # Start server
python manage.py startapp name   # Create app
python manage.py migrate         # Apply database changes
python manage.py createsuperuser # Create admin user
```

**Don't edit this file!** It's automatically generated.

#### `mysite/settings.py`

The **heart of your project**. Contains all configuration:

```python
# Important settings:

DEBUG = True  # Show detailed errors (development only)

ALLOWED_HOSTS = []  # Domains that can access this site

INSTALLED_APPS = [  # Django apps and your apps
    'django.contrib.admin',
    'django.contrib.auth',
    # ... your apps will go here
]

DATABASES = {  # Database configuration
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [  # Template engine configuration
    # We'll configure this soon
]

STATIC_URL = 'static/'  # URL for static files (CSS, images)

SECRET_KEY = '...'  # Keep this secret in production!
```

#### `mysite/urls.py`

The **main URL router**:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    # Your URLs will go here
]
```

Think of this as a **table of contents** for your website.

---

## 5. Creating a Django App

### What is a Django App?

An **app** is a component that does something:
- A blog
- A user authentication system
- A contact form
- A store

**One project** can have **multiple apps**.

**Example:**
```
mysite (project)
├── blog (app)       # Handles blog posts
├── store (app)      # Handles products
└── users (app)      # Handles user accounts
```

For Week 4, we'll create one app called `core`.

### Create an App

```bash
# Make sure you're in the folder with manage.py
python manage.py startapp core

# This creates a new folder called "core"
```

**What was created:**

```
core/
├── __init__.py          # Python package marker
├── admin.py             # Register models for admin (Week 5)
├── apps.py              # App configuration
├── models.py            # Database models (Week 5)
├── tests.py             # Write tests here
├── views.py             # View functions (IMPORTANT)
└── migrations/          # Database migrations (Week 5)
    └── __init__.py
```

### Register the App

**Important:** You must tell Django about your new app!

**Edit `mysite/settings.py`:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # ← Add your app here
]
```

Save the file.

---

## 6. URLs and Views

### The Request-Response Cycle

Understanding how Django handles requests:

```
Browser → URL → Django → View → Response → Browser
```

**Example:**
```
User visits: http://localhost:8000/about/
↓
Django checks urls.py: "What handles /about/?"
↓
Finds view function: about_view()
↓
View function returns HTML
↓
Browser displays the page
```

### What is a View?

A **view** is a Python function that:
1. Takes a request
2. Does something (fetch data, process form, etc.)
3. Returns a response (HTML, JSON, redirect, etc.)

**Simple example:**

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
```

### Creating Your First View

**Edit `core/views.py`:**

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django site!")

def about(request):
    return HttpResponse("This is the About page.")

def contact(request):
    return HttpResponse("Contact us at: contact@example.com")
```

**Explanation:**
- Each function takes `request` as a parameter
- `HttpResponse` sends text back to the browser
- These are simple views (we'll use templates soon)

### Connecting Views to URLs

Now we need to tell Django: "When someone visits /about/, use the about view."

#### Step 1: Create App URLs

**Create a new file: `core/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # localhost:8000/
    path('about/', views.about, name='about'),   # localhost:8000/about/
    path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
]
```

**Explanation:**
- `path('', views.home)` means root URL (/)
- `path('about/', views.about)` means /about/
- `name='home'` is a URL name (we'll use this later)
- `. import views` imports views from the same folder

#### Step 2: Connect App URLs to Project URLs

**Edit `mysite/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include  # ← Add include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # ← Add this line
]
```

**Explanation:**
- `include('core.urls')` means "use URLs from core app"
- `path('', ...)` means these URLs start at the root
- All URLs from `core/urls.py` are now connected

### Test Your Views

```bash
# Run the server
python manage.py runserver

# Open browser and visit:
# http://localhost:8000/          → Shows "Welcome to my Django site!"
# http://localhost:8000/about/    → Shows "This is the About page."
# http://localhost:8000/contact/  → Shows "Contact us at: contact@example.com"
```

🎉 **Congratulations! You've created working views and URLs!**

---

## 7. Django Templates

### Why Templates?

Currently, we're returning plain text with `HttpResponse`.

**Problems:**
- No HTML structure
- No styling
- Hard to maintain
- Can't include dynamic data easily

**Solution:** Use **templates** (HTML files with Django template language).

### Template Language Basics

Django templates let you:
- Display variables: `{{ variable_name }}`
- Use logic: `{% if condition %} ... {% endif %}`
- Loop through lists: `{% for item in items %} ... {% endfor %}`
- Include other templates: `{% include 'header.html' %}`
- Extend base templates: `{% extends 'base.html' %}`

### Setting Up Templates

#### Step 1: Create Templates Folder

```bash
# In your app folder (core/), create a templates folder
# Then create a folder with your app name inside it

mkdir core/templates
mkdir core/templates/core
```

**Folder structure:**
```
core/
├── templates/
│   └── core/
│       ├── home.html
│       ├── about.html
│       └── contact.html
├── views.py
└── urls.py
```

**Why the nested folder?** Django searches all apps for templates. The nested structure prevents naming conflicts.

#### Step 2: Create Template Files

**Create `core/templates/core/home.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to My Django Site</h1>
    <p>This is the home page.</p>
    <nav>
        <a href="/about/">About</a>
        <a href="/contact/">Contact</a>
    </nav>
</body>
</html>
```

**Create `core/templates/core/about.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>About Us</h1>
    <p>We are learning Django!</p>
    <nav>
        <a href="/">Home</a>
        <a href="/contact/">Contact</a>
    </nav>
</body>
</html>
```

**Create `core/templates/core/contact.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <h1>Contact Us</h1>
    <p>Email: contact@example.com</p>
    <p>Phone: +123 456 7890</p>
    <nav>
        <a href="/">Home</a>
        <a href="/about/">About</a>
    </nav>
</body>
</html>
```

#### Step 3: Update Views to Use Templates

**Edit `core/views.py`:**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
```

**Explanation:**
- `render(request, 'template_name')` loads and returns an HTML template
- `'core/home.html'` refers to `core/templates/core/home.html`
- Django automatically looks in `templates` folders

### Passing Data to Templates

**Update `core/views.py`:**

```python
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Welcome',
        'message': 'Hello from Django!',
        'year': 2025
    }
    return render(request, 'core/home.html', context)
```

**Update `core/templates/core/home.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
    <p>Year: {{ year }}</p>
</body>
</html>
```

**How it works:**
- `context` is a dictionary of variables
- `{{ variable_name }}` displays the variable in the template
- Django replaces `{{ title }}` with `'Welcome'`

### Template Logic

**Example with if statement:**

```python
# In views.py
def home(request):
    context = {
        'user_logged_in': True,
        'username': 'Ahmed'
    }
    return render(request, 'core/home.html', context)
```

```html
<!-- In home.html -->
{% if user_logged_in %}
    <p>Welcome back, {{ username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

**Example with for loop:**

```python
# In views.py
def home(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Orange', 'Grape']
    }
    return render(request, 'core/home.html', context)
```

```html
<!-- In home.html -->
<h2>Fruit List:</h2>
<ul>
    {% for fruit in fruits %}
        <li>{{ fruit }}</li>
    {% endfor %}
</ul>
```

---

## 8. Template Inheritance

### The Problem

Notice how all our templates have repeated code:
- Same `<!DOCTYPE html>`, `<head>`, `<meta>` tags
- Same navigation links
- Same structure

**Problem:**
- Lots of duplication
- Hard to maintain
- Change one thing, update all files

**Solution:** Template inheritance with `base.html`

### Creating a Base Template

**Create `core/templates/core/base.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Site{% endblock %}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            background-color: #555;
            padding: 10px;
            text-align: center;
        }
        nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
        }
        nav a:hover {
            color: #4CAF50;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>My Django Website</h1>
    </header>

    <nav>
        <a href="/">Home</a>
        <a href="/about/">About</a>
        <a href="/contact/">Contact</a>
    </nav>

    <div class="container">
        {% block content %}
        <!-- Page-specific content goes here -->
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2025 My Django Site. All rights reserved.</p>
    </footer>
</body>
</html>
```

**Key parts:**
- `{% block title %}...{% endblock %}`: Placeholder for page title
- `{% block content %}...{% endblock %}`: Placeholder for page content
- Everything else is shared across all pages

### Using the Base Template

**Update `core/templates/core/home.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}Home - My Django Site{% endblock %}

{% block content %}
    <h2>Welcome to My Django Site</h2>
    <p>This is the home page built with Django.</p>
    <p>Django makes web development easier and faster!</p>
{% endblock %}
```

**Update `core/templates/core/about.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}About - My Django Site{% endblock %}

{% block content %}
    <h2>About Us</h2>
    <p>We are learning Django web development.</p>
    <p>Django is a powerful Python web framework.</p>
    <h3>What We've Learned:</h3>
    <ul>
        <li>Python basics (Weeks 1-2)</li>
        <li>HTML & CSS (Week 3)</li>
        <li>Django basics (Week 4)</li>
    </ul>
{% endblock %}
```

**Update `core/templates/core/contact.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}Contact - My Django Site{% endblock %}

{% block content %}
    <h2>Contact Us</h2>
    <p>We'd love to hear from you!</p>
    <p><strong>Email:</strong> contact@example.com</p>
    <p><strong>Phone:</strong> +123 456 7890</p>
    <p><strong>Address:</strong> 123 Django Street, Python City</p>
{% endblock %}
```

**How it works:**
- `{% extends 'core/base.html' %}` means "use base.html as the template"
- `{% block title %}...{% endblock %}` replaces the title block in base.html
- `{% block content %}...{% endblock %}` replaces the content block
- Everything else comes from base.html

**Benefits:**
- ✓ No code duplication
- ✓ Change header once, updates everywhere
- ✓ Consistent design across pages
- ✓ Easy to maintain

---

## 9. Static Files (CSS, Images)

### What are Static Files?

**Static files** don't change:
- CSS stylesheets
- JavaScript files
- Images
- Fonts
- Icons

Unlike templates (which can have dynamic data), static files are served as-is.

### Setting Up Static Files

#### Step 1: Create Static Folder

```bash
# In your app folder (core/), create a static folder
mkdir core/static
mkdir core/static/core
mkdir core/static/core/css
mkdir core/static/core/images
```

**Folder structure:**
```
core/
├── static/
│   └── core/
│       ├── css/
│       │   └── style.css
│       └── images/
│           └── logo.png
├── templates/
└── views.py
```

#### Step 2: Create CSS File

**Create `core/static/core/css/style.css`:**

```css
/* Custom styles for our Django site */

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

header {
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 30px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
}

header h1 {
    margin: 0;
    font-size: 2.5em;
}

nav {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 15px;
    text-align: center;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 20px;
    font-size: 1.1em;
    transition: color 0.3s;
}

nav a:hover {
    color: #4CAF50;
}

.container {
    max-width: 900px;
    margin: 30px auto;
    background: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}

.container h2 {
    color: #667eea;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
}

footer {
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    text-align: center;
    padding: 15px;
    position: fixed;
    bottom: 0;
    width: 100%;
}
```

#### Step 3: Load Static Files in Templates

**Update `core/templates/core/base.html`:**

```html
{% load static %}  <!-- ← Add this at the very top -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Site{% endblock %}</title>

    <!-- Link to external CSS -->
    <link rel="stylesheet" href="{% static 'core/css/style.css' %}">
</head>
<body>
    <header>
        <h1>My Django Website</h1>
    </header>

    <nav>
        <a href="/">Home</a>
        <a href="/about/">About</a>
        <a href="/contact/">Contact</a>
    </nav>

    <div class="container">
        {% block content %}
        <!-- Page-specific content goes here -->
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2025 My Django Site. All rights reserved.</p>
    </footer>
</body>
</html>
```

**Key changes:**
- `{% load static %}` at the top loads Django's static files system
- `{% static 'core/css/style.css' %}` generates the correct URL for the CSS file
- Remove the inline `<style>` tags (now using external CSS)

#### Step 4: Add an Image (Optional)

If you have an image called `logo.png` in `core/static/core/images/`:

```html
<!-- In base.html header -->
<header>
    <img src="{% static 'core/images/logo.png' %}" alt="Logo" style="height: 50px;">
    <h1>My Django Website</h1>
</header>
```

### Configure Static Files in Settings

Django is already configured for development, but verify:

**Check `mysite/settings.py`:**

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'  # URL prefix for static files

# For production, you'll also need:
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# (We'll cover this in Week 9)
```

### Test Static Files

```bash
# Run the server
python manage.py runserver

# Visit your pages - they should now have the new styles!
```

---

## 10. Mini-Project: 3-Page Django Website

### Project Requirements

Build a simple 3-page website with:
- **Home page**: Welcome message
- **About page**: Information about yourself
- **Contact page**: Contact information

**Requirements:**
- Use Django views and URLs
- Use template inheritance (base.html)
- Include a navigation menu
- Add custom CSS styling
- Use Git to track changes

### Step-by-Step Guide

#### Step 1: Plan Your Site

**Pages:**
1. Home (`/`)
2. About (`/about/`)
3. Contact (`/contact/`)

**Design:**
- Consistent header and navigation
- Styled content area
- Footer with copyright

#### Step 2: Create Views

**`core/views.py`:**

```python
from django.shortcuts import render

def home(request):
    context = {
        'page_title': 'Home',
        'welcome_message': 'Welcome to my Django website!',
        'description': 'This is my first Django project for Week 4.'
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'page_title': 'About',
        'name': 'Your Name',
        'bio': 'I am learning Django web development.',
        'skills': ['Python', 'HTML', 'CSS', 'Django']
    }
    return render(request, 'core/about.html', context)

def contact(request):
    context = {
        'page_title': 'Contact',
        'email': 'your.email@example.com',
        'phone': '+123 456 7890',
        'social_media': {
            'github': 'https://github.com/yourusername',
            'linkedin': 'https://linkedin.com/in/yourusername'
        }
    }
    return render(request, 'core/contact.html', context)
```

#### Step 3: Configure URLs

**`core/urls.py`:**

```python
from django.urls import path
from . import views

app_name = 'core'  # Namespace for URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```

**`mysite/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

#### Step 4: Create Base Template

**`core/templates/core/base.html`:**

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'core/css/style.css' %}">
</head>
<body>
    <header>
        <h1>{% block header_title %}My Django Portfolio{% endblock %}</h1>
    </header>

    <nav>
        <a href="{% url 'core:home' %}">Home</a>
        <a href="{% url 'core:about' %}">About</a>
        <a href="{% url 'core:contact' %}">Contact</a>
    </nav>

    <main class="container">
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2025 Django Training Project. Week 4 Assignment.</p>
    </footer>
</body>
</html>
```

**Note:** `{% url 'core:home' %}` uses URL names instead of hardcoded paths. This is better practice.

#### Step 5: Create Page Templates

**`core/templates/core/home.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}{{ page_title }} - My Django Site{% endblock %}

{% block content %}
    <h2>{{ welcome_message }}</h2>
    <p>{{ description }}</p>
    <p>This site demonstrates:</p>
    <ul>
        <li>Django views and URLs</li>
        <li>Template inheritance</li>
        <li>Static files (CSS)</li>
        <li>Dynamic content rendering</li>
    </ul>
    <p>Navigate using the menu above to explore!</p>
{% endblock %}
```

**`core/templates/core/about.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}{{ page_title }} - My Django Site{% endblock %}

{% block content %}
    <h2>About Me</h2>
    <p><strong>Name:</strong> {{ name }}</p>
    <p><strong>Bio:</strong> {{ bio }}</p>

    <h3>My Skills</h3>
    <ul>
        {% for skill in skills %}
            <li>{{ skill }}</li>
        {% endfor %}
    </ul>

    <p>I'm currently learning web development with Django as part of a 9-week training program.</p>
{% endblock %}
```

**`core/templates/core/contact.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}{{ page_title }} - My Django Site{% endblock %}

{% block content %}
    <h2>Contact Me</h2>
    <p>Feel free to reach out!</p>

    <p><strong>Email:</strong> <a href="mailto:{{ email }}">{{ email }}</a></p>
    <p><strong>Phone:</strong> {{ phone }}</p>

    <h3>Find Me Online</h3>
    <ul>
        <li><a href="{{ social_media.github }}" target="_blank">GitHub</a></li>
        <li><a href="{{ social_media.linkedin }}" target="_blank">LinkedIn</a></li>
    </ul>
{% endblock %}
```

#### Step 6: Add Custom Styling

**`core/static/core/css/style.css`:**

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding-bottom: 60px;
}

header {
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 30px 0;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
}

header h1 {
    font-size: 2.5em;
    margin: 0;
}

nav {
    background-color: rgba(0, 0, 0, 0.6);
    padding: 15px 0;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 25px;
    font-size: 1.1em;
    transition: all 0.3s ease;
    padding: 8px 15px;
    border-radius: 5px;
}

nav a:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: #4CAF50;
}

.container {
    max-width: 900px;
    margin: 40px auto;
    background: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.3);
}

.container h2 {
    color: #667eea;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

.container h3 {
    color: #764ba2;
    margin-top: 25px;
    margin-bottom: 15px;
}

.container p {
    margin-bottom: 15px;
}

.container ul {
    margin-left: 30px;
    margin-bottom: 20px;
}

.container li {
    margin-bottom: 8px;
}

.container a {
    color: #667eea;
    text-decoration: none;
    transition: color 0.3s;
}

.container a:hover {
    color: #764ba2;
    text-decoration: underline;
}

footer {
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    text-align: center;
    padding: 15px;
    position: fixed;
    bottom: 0;
    width: 100%;
}
```

#### Step 7: Test Your Site

```bash
# Run the development server
python manage.py runserver

# Visit each page:
# http://localhost:8000/         (Home)
# http://localhost:8000/about/   (About)
# http://localhost:8000/contact/ (Contact)
```

#### Step 8: Use Git

```bash
# Initialize Git (if not done)
git init

# Create .gitignore
echo "venv/
__pycache__/
*.pyc
db.sqlite3
.env" > .gitignore

# Add files
git add .

# Commit
git commit -m "Week 4: Complete Django 3-page website

- Created Django project and core app
- Implemented home, about, and contact views
- Used template inheritance with base.html
- Added custom CSS styling
- Configured static files"

# Push to GitHub (if you have a remote repository)
git push origin main
```

---

## Summary

### What You've Learned This Week

**Django Basics:**
- ✓ What Django is and why we use it
- ✓ Installing Django and creating projects
- ✓ Understanding project structure
- ✓ Creating and registering apps

**URLs and Views:**
- ✓ How Django routes URLs
- ✓ Creating view functions
- ✓ Connecting URLs to views
- ✓ Returning HTTP responses

**Templates:**
- ✓ Creating HTML templates
- ✓ Passing data to templates
- ✓ Using template variables and logic
- ✓ Template inheritance (extends, blocks)

**Static Files:**
- ✓ Setting up static files
- ✓ Creating CSS files
- ✓ Loading static files in templates
- ✓ Organizing static assets

### Key Concepts to Remember

1. **MTV Pattern**: Model-Template-View
2. **Projects vs Apps**: Projects contain apps
3. **URL Routing**: URLs → Views → Templates
4. **Template Inheritance**: DRY principle in action
5. **Static Files**: CSS, JS, images, fonts

### Next Week Preview

**Week 5 - Models, ORM, Migrations & Admin:**
- Create database models
- Use Django ORM to query data
- Set up Django admin interface
- Build a blog with database-backed content

### Practice Suggestions

1. **Extend your site**: Add more pages (services, portfolio, blog list)
2. **Improve styling**: Make it responsive, add animations
3. **Experiment**: Try different template layouts
4. **Customize**: Add your own images and content
5. **Explore**: Look at Django documentation

---

## Troubleshooting Common Issues

### Issue 1: "ModuleNotFoundError: No module named 'django'"

**Solution:**
```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal

# If not activated:
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Then install Django:
pip install django
```

### Issue 2: "TemplateDoesNotExist at /"

**Solution:**
- Check that `core` is in `INSTALLED_APPS` in settings.py
- Verify template path: `core/templates/core/template_name.html`
- Make sure folder structure is correct

### Issue 3: Static Files Not Loading

**Solution:**
- Add `{% load static %}` at the top of template
- Check `STATIC_URL` in settings.py
- Verify static folder structure: `core/static/core/css/style.css`
- Hard refresh browser (Ctrl+F5)

### Issue 4: "Page not found (404)"

**Solution:**
- Check `urls.py` in both project and app
- Make sure `include('core.urls')` is in project urls.py
- Verify URL pattern matches what you're typing

### Issue 5: Server Won't Start

**Solution:**
```bash
# Port already in use
# Stop other processes or use different port:
python manage.py runserver 8001

# Or find and kill process using port 8000
```

---

## Additional Resources

**Official Documentation:**
- Django Tutorial: https://docs.djangoproject.com/en/stable/intro/tutorial01/
- Django Templates: https://docs.djangoproject.com/en/stable/topics/templates/
- Django Static Files: https://docs.djangoproject.com/en/stable/howto/static-files/

**Video Tutorials:**
- Corey Schafer's Django Series (YouTube)
- Django for Beginners (William Vincent)

**Practice Sites:**
- Django Girls Tutorial: https://tutorial.djangogirls.org/

---

**Congratulations on completing Week 4! You now know how to build dynamic websites with Django. Keep practicing and building! 🚀**
