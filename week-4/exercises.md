# Week 4 Exercises – Django Basics Practice

Practice exercises for Week 4: Django project setup, apps, views, templates, and static files.

---

## Table of Contents

1. [Day 1: Django Setup & First Views](#day-1-django-setup--first-views)
2. [Day 2: Templates & Template Tags](#day-2-templates--template-tags)
3. [Day 3: Template Inheritance & URLs](#day-3-template-inheritance--urls)
4. [Day 4: Static Files & Styling](#day-4-static-files--styling)
5. [Day 5: Complete Multi-Page Project](#day-5-complete-multi-page-project)
6. [Challenge Exercises](#challenge-exercises)

---

## Day 1: Django Setup & First Views

### Exercise 1: Install Django and Create Project

**Task:**
1. Create a virtual environment called `venv`
2. Activate the virtual environment
3. Install Django
4. Verify Django installation
5. Create a Django project called `portfolio`

**Commands to use:**
```bash
python -m venv venv
# activate venv (depends on OS)
pip install django
django-admin --version
django-admin startproject portfolio
```

**Expected outcome:**
- Virtual environment created and activated
- Django installed successfully
- New `portfolio` project folder created

<details>
<summary>Solution</summary>

```bash
# Windows
python -m venv venv
venv\Scripts\activate
pip install django
django-admin --version
django-admin startproject portfolio
cd portfolio
python manage.py runserver

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
pip install django
django-admin --version
django-admin startproject portfolio
cd portfolio
python manage.py runserver
```

Visit `http://localhost:8000` to verify it works!
</details>

---

### Exercise 2: Create Your First App

**Task:**
1. Create an app called `pages`
2. Register the app in `settings.py`
3. Verify the app folder was created with all necessary files

**Expected folder structure:**
```
portfolio/
├── pages/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── portfolio/
│   └── settings.py
└── manage.py
```

<details>
<summary>Solution</summary>

```bash
# Create app
python manage.py startapp pages
```

**Edit `portfolio/settings.py`:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # ← Add this
]
```
</details>

---

### Exercise 3: Create Simple Views

**Task:**
Create three simple views that return plain text responses:

1. `home` view → Returns "Welcome to my portfolio!"
2. `about` view → Returns "About me: I'm a Django learner"
3. `projects` view → Returns "My projects coming soon!"

**File:** `pages/views.py`

<details>
<summary>Solution</summary>

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my portfolio!")

def about(request):
    return HttpResponse("About me: I'm a Django learner")

def projects(request):
    return HttpResponse("My projects coming soon!")
```
</details>

---

### Exercise 4: Configure URLs

**Task:**
1. Create `pages/urls.py`
2. Map the three views to URLs:
   - `/` → home view
   - `/about/` → about view
   - `/projects/` → projects view
3. Include app URLs in the project's `urls.py`

<details>
<summary>Solution</summary>

**Create `pages/urls.py`:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
]
```

**Edit `portfolio/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

**Test:**
- `http://localhost:8000/` → "Welcome to my portfolio!"
- `http://localhost:8000/about/` → "About me: I'm a Django learner"
- `http://localhost:8000/projects/` → "My projects coming soon!"
</details>

---

### Exercise 5: Add URL with Parameter

**Task:**
Create a view that displays a greeting with a name from the URL.

**Requirements:**
- URL pattern: `/greet/<name>/`
- Example: `/greet/Ahmed/` → "Hello, Ahmed!"
- Example: `/greet/Sara/` → "Hello, Sara!"

<details>
<summary>Solution</summary>

**Add to `pages/views.py`:**

```python
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
```

**Add to `pages/urls.py`:**

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('greet/<str:name>/', views.greet, name='greet'),  # ← Add this
]
```

**Test:**
- `/greet/Ahmed/` → "Hello, Ahmed!"
- `/greet/Sara/` → "Hello, Sara!"
</details>

---

## Day 2: Templates & Template Tags

### Exercise 6: Create First Template

**Task:**
1. Create the templates folder structure: `pages/templates/pages/`
2. Create `home.html` with basic HTML structure
3. Update the `home` view to render the template

**Template content:**
- Page title: "Home"
- Heading: "Welcome to My Portfolio"
- Paragraph: "This is my Django learning project"

<details>
<summary>Solution</summary>

**Create `pages/templates/pages/home.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to My Portfolio</h1>
    <p>This is my Django learning project</p>
</body>
</html>
```

**Update `pages/views.py`:**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
```
</details>

---

### Exercise 7: Pass Variables to Template

**Task:**
Update the home view to pass the following data to the template:

- `title`: "Django Portfolio"
- `name`: "Your Name"
- `year`: 2025
- `description`: "Learning Django web development"

Display all these variables in the template.

<details>
<summary>Solution</summary>

**Update `pages/views.py`:**

```python
def home(request):
    context = {
        'title': 'Django Portfolio',
        'name': 'Your Name',
        'year': 2025,
        'description': 'Learning Django web development'
    }
    return render(request, 'pages/home.html', context)
```

**Update `pages/templates/pages/home.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to My Portfolio</h1>
    <p>Name: {{ name }}</p>
    <p>{{ description }}</p>
    <p>Year: {{ year }}</p>
</body>
</html>
```
</details>

---

### Exercise 8: Use Template Logic (if/else)

**Task:**
Create an `about.html` template that displays different content based on whether the user is logged in.

**Requirements:**
- Pass a variable `is_logged_in` (boolean) from the view
- If `True`: Display "Welcome back!"
- If `False`: Display "Please log in to see more"

<details>
<summary>Solution</summary>

**Create `pages/templates/pages/about.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>About Page</h1>

    {% if is_logged_in %}
        <p>Welcome back!</p>
        <p>You have full access to this page.</p>
    {% else %}
        <p>Please log in to see more</p>
    {% endif %}
</body>
</html>
```

**Update `pages/views.py`:**

```python
def about(request):
    context = {
        'is_logged_in': False  # Try changing to True
    }
    return render(request, 'pages/about.html', context)
```
</details>

---

### Exercise 9: Loop Through List in Template

**Task:**
Create a `projects.html` template that displays a list of projects.

**Requirements:**
- Pass a list of project names from the view
- Use a `{% for %}` loop to display each project
- Display them in an unordered list (`<ul>`)

**Project list:**
- "Calculator App"
- "To-Do List"
- "Weather Dashboard"
- "Blog Website"

<details>
<summary>Solution</summary>

**Create `pages/templates/pages/projects.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projects</title>
</head>
<body>
    <h1>My Projects</h1>

    <ul>
        {% for project in projects %}
            <li>{{ project }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Update `pages/views.py`:**

```python
def projects(request):
    context = {
        'projects': [
            'Calculator App',
            'To-Do List',
            'Weather Dashboard',
            'Blog Website'
        ]
    }
    return render(request, 'pages/projects.html', context)
```
</details>

---

### Exercise 10: Loop Through Dictionary

**Task:**
Create a `skills.html` template that displays skills with proficiency levels.

**Requirements:**
- Pass a dictionary of skills with proficiency percentages
- Display each skill with its level
- Format: "Python: 80%"

**Skills data:**
```python
{
    'Python': 80,
    'HTML': 90,
    'CSS': 75,
    'Django': 60
}
```

<details>
<summary>Solution</summary>

**Create `pages/templates/pages/skills.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skills</title>
</head>
<body>
    <h1>My Skills</h1>

    <ul>
        {% for skill, level in skills.items %}
            <li>{{ skill }}: {{ level }}%</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**Add to `pages/views.py`:**

```python
def skills(request):
    context = {
        'skills': {
            'Python': 80,
            'HTML': 90,
            'CSS': 75,
            'Django': 60
        }
    }
    return render(request, 'pages/skills.html', context)
```

**Add to `pages/urls.py`:**

```python
path('skills/', views.skills, name='skills'),
```
</details>

---

## Day 3: Template Inheritance & URLs

### Exercise 11: Create Base Template

**Task:**
Create a `base.html` template with:
- A header with site title
- A navigation menu (Home, About, Projects, Skills)
- A content block for child templates
- A footer with copyright

<details>
<summary>Solution</summary>

**Create `pages/templates/pages/base.html`:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Portfolio{% endblock %}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
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
            margin: 0 15px;
            text-decoration: none;
        }
        nav a:hover {
            color: #4CAF50;
        }
        .container {
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
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
        <h1>My Django Portfolio</h1>
    </header>

    <nav>
        <a href="/">Home</a>
        <a href="/about/">About</a>
        <a href="/projects/">Projects</a>
        <a href="/skills/">Skills</a>
    </nav>

    <div class="container">
        {% block content %}
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2025 Django Portfolio. All rights reserved.</p>
    </footer>
</body>
</html>
```
</details>

---

### Exercise 12: Extend Base Template

**Task:**
Update all your existing templates (home, about, projects, skills) to extend `base.html`.

**Requirements:**
- Use `{% extends 'pages/base.html' %}`
- Set custom title for each page
- Put page content in `{% block content %}`

<details>
<summary>Solution</summary>

**Update `pages/templates/pages/home.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}Home - My Portfolio{% endblock %}

{% block content %}
    <h2>Welcome to My Portfolio</h2>
    <p>Name: {{ name }}</p>
    <p>{{ description }}</p>
    <p>Year: {{ year }}</p>
{% endblock %}
```

**Update `pages/templates/pages/about.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}About - My Portfolio{% endblock %}

{% block content %}
    <h2>About Page</h2>

    {% if is_logged_in %}
        <p>Welcome back!</p>
        <p>You have full access to this page.</p>
    {% else %}
        <p>Please log in to see more</p>
    {% endif %}
{% endblock %}
```

**Update `pages/templates/pages/projects.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}Projects - My Portfolio{% endblock %}

{% block content %}
    <h2>My Projects</h2>

    <ul>
        {% for project in projects %}
            <li>{{ project }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

**Update `pages/templates/pages/skills.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}Skills - My Portfolio{% endblock %}

{% block content %}
    <h2>My Skills</h2>

    <ul>
        {% for skill, level in skills.items %}
            <li>{{ skill }}: {{ level }}%</li>
        {% endfor %}
    </ul>
{% endblock %}
```
</details>

---

### Exercise 13: Use URL Names

**Task:**
Update the navigation links in `base.html` to use `{% url %}` tag instead of hardcoded paths.

**Requirements:**
- Use `{% url 'home' %}` instead of `/`
- Use `{% url 'about' %}` instead of `/about/`
- Same for all navigation links

<details>
<summary>Solution</summary>

**Update navigation in `pages/templates/pages/base.html`:**

```html
<nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
    <a href="{% url 'projects' %}">Projects</a>
    <a href="{% url 'skills' %}">Skills</a>
</nav>
```

**Benefit:** If you change URL patterns, links automatically update!
</details>

---

### Exercise 14: Add URL Namespace

**Task:**
1. Add a namespace to your app URLs
2. Update all `{% url %}` tags to use the namespace

<details>
<summary>Solution</summary>

**Update `pages/urls.py`:**

```python
from django.urls import path
from . import views

app_name = 'pages'  # ← Add namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
]
```

**Update navigation in `base.html`:**

```html
<nav>
    <a href="{% url 'pages:home' %}">Home</a>
    <a href="{% url 'pages:about' %}">About</a>
    <a href="{% url 'pages:projects' %}">Projects</a>
    <a href="{% url 'pages:skills' %}">Skills</a>
</nav>
```
</details>

---

## Day 4: Static Files & Styling

### Exercise 15: Set Up Static Files

**Task:**
1. Create static folder structure: `pages/static/pages/css/`
2. Create a `style.css` file
3. Load it in `base.html`

<details>
<summary>Solution</summary>

**Create folder structure:**
```
pages/
└── static/
    └── pages/
        └── css/
            └── style.css
```

**Create `pages/static/pages/css/style.css`:**

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f4f4f4;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px;
    text-align: center;
}

nav {
    background-color: #333;
    padding: 15px;
    text-align: center;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 20px;
    transition: color 0.3s;
}

nav a:hover {
    color: #667eea;
}

.container {
    max-width: 900px;
    margin: 30px auto;
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 15px;
    margin-top: 50px;
}
```

**Update `pages/templates/pages/base.html`:**

```html
{% load static %}  <!-- ← Add at top -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Portfolio{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'pages/css/style.css' %}">
</head>
<!-- rest of template -->
```

Remove the inline `<style>` tags from the template.
</details>

---

### Exercise 16: Add More CSS Styling

**Task:**
Enhance your `style.css` with:
- Styled headings with colors
- Better list styling
- Hover effects on links
- Rounded corners and shadows

<details>
<summary>Solution</summary>

**Add to `pages/static/pages/css/style.css`:**

```css
h2 {
    color: #667eea;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

h3 {
    color: #764ba2;
    margin-top: 20px;
}

.container ul {
    list-style: none;
    padding: 0;
}

.container li {
    background: #f9f9f9;
    margin: 10px 0;
    padding: 15px;
    border-left: 4px solid #667eea;
    border-radius: 5px;
    transition: transform 0.2s;
}

.container li:hover {
    transform: translateX(5px);
    background: #e9e9ff;
}

.container a {
    color: #667eea;
    text-decoration: none;
}

.container a:hover {
    text-decoration: underline;
}
```
</details>

---

### Exercise 17: Add Images

**Task:**
1. Create `pages/static/pages/images/` folder
2. Add a profile image
3. Display it on the About page

<details>
<summary>Solution</summary>

**Folder structure:**
```
pages/static/pages/
├── css/
│   └── style.css
└── images/
    └── profile.jpg  # Add your image here
```

**Update `pages/templates/pages/about.html`:**

```html
{% extends 'pages/base.html' %}
{% load static %}

{% block title %}About - My Portfolio{% endblock %}

{% block content %}
    <h2>About Me</h2>

    <img src="{% static 'pages/images/profile.jpg' %}"
         alt="Profile Picture"
         style="width: 200px; border-radius: 50%; display: block; margin: 20px auto;">

    <p>I'm a Django learner building web applications with Python.</p>
{% endblock %}
```
</details>

---

### Exercise 18: Create Responsive Navigation

**Task:**
Make the navigation menu responsive:
- Stack links vertically on small screens
- Keep horizontal on larger screens

<details>
<summary>Solution</summary>

**Add to `pages/static/pages/css/style.css`:**

```css
nav {
    background-color: #333;
    padding: 15px;
    text-align: center;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 10px 20px;
    display: inline-block;
    transition: color 0.3s;
}

nav a:hover {
    color: #667eea;
}

/* Responsive design */
@media (max-width: 600px) {
    nav a {
        display: block;
        margin: 10px 0;
    }

    .container {
        padding: 15px;
        margin: 15px;
    }

    header h1 {
        font-size: 1.5em;
    }
}
```
</details>

---

## Day 5: Complete Multi-Page Project

### Exercise 19: Build a Personal Blog (Homepage)

**Task:**
Create a blog homepage that displays:
- List of blog post titles
- Publication dates
- Short descriptions
- Link to read more (dummy links for now)

**Pass this data from the view:**
```python
posts = [
    {
        'title': 'My First Django Project',
        'date': '2025-01-01',
        'description': 'Learning Django has been an amazing experience...'
    },
    {
        'title': 'Understanding Templates',
        'date': '2025-01-05',
        'description': 'Django templates make it easy to build dynamic pages...'
    },
    {
        'title': 'Working with Static Files',
        'date': '2025-01-10',
        'description': 'CSS and images bring our site to life...'
    }
]
```

<details>
<summary>Solution</summary>

**Add to `pages/views.py`:**

```python
def blog(request):
    posts = [
        {
            'title': 'My First Django Project',
            'date': '2025-01-01',
            'description': 'Learning Django has been an amazing experience...'
        },
        {
            'title': 'Understanding Templates',
            'date': '2025-01-05',
            'description': 'Django templates make it easy to build dynamic pages...'
        },
        {
            'title': 'Working with Static Files',
            'date': '2025-01-10',
            'description': 'CSS and images bring our site to life...'
        }
    ]
    context = {'posts': posts}
    return render(request, 'pages/blog.html', context)
```

**Create `pages/templates/pages/blog.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}Blog - My Portfolio{% endblock %}

{% block content %}
    <h2>My Blog</h2>

    {% for post in posts %}
        <article style="margin-bottom: 30px; padding: 20px; background: #f9f9f9; border-radius: 8px;">
            <h3>{{ post.title }}</h3>
            <p style="color: #666; font-size: 0.9em;">Published: {{ post.date }}</p>
            <p>{{ post.description }}</p>
            <a href="#">Read more →</a>
        </article>
    {% endfor %}
{% endblock %}
```

**Add to `pages/urls.py`:**

```python
path('blog/', views.blog, name='blog'),
```

**Update navigation in `base.html`:**

```html
<a href="{% url 'pages:blog' %}">Blog</a>
```
</details>

---

### Exercise 20: Create a Contact Page with Information

**Task:**
Create a contact page that displays:
- Your email
- Phone number
- Social media links (GitHub, LinkedIn)
- A contact form (just the HTML, non-functional)

<details>
<summary>Solution</summary>

**Add to `pages/views.py`:**

```python
def contact(request):
    context = {
        'email': 'your.email@example.com',
        'phone': '+123 456 7890',
        'github': 'https://github.com/yourusername',
        'linkedin': 'https://linkedin.com/in/yourusername'
    }
    return render(request, 'pages/contact.html', context)
```

**Create `pages/templates/pages/contact.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}Contact - My Portfolio{% endblock %}

{% block content %}
    <h2>Contact Me</h2>

    <h3>Get in Touch</h3>
    <p><strong>Email:</strong> <a href="mailto:{{ email }}">{{ email }}</a></p>
    <p><strong>Phone:</strong> {{ phone }}</p>

    <h3>Find Me Online</h3>
    <p>
        <a href="{{ github }}" target="_blank">GitHub</a> |
        <a href="{{ linkedin }}" target="_blank">LinkedIn</a>
    </p>

    <h3>Send a Message</h3>
    <form>
        <p>
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" style="width: 100%; padding: 8px; margin-top: 5px;">
        </p>
        <p>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" style="width: 100%; padding: 8px; margin-top: 5px;">
        </p>
        <p>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="5" style="width: 100%; padding: 8px; margin-top: 5px;"></textarea>
        </p>
        <p>
            <button type="submit" style="padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
        </p>
    </form>
    <p style="font-size: 0.9em; color: #666;"><em>Note: Form is not functional yet (we'll learn this in Week 6)</em></p>
{% endblock %}
```

**Add to `pages/urls.py`:**

```python
path('contact/', views.contact, name='contact'),
```
</details>

---

## Challenge Exercises

### Challenge 1: Create a Services Page

**Task:**
Create a services page that displays a list of services you offer. Each service should have:
- Service name
- Description
- Icon or emoji
- Price (or "Free")

Display them in a grid layout using CSS.

<details>
<summary>Hint</summary>

Use CSS Grid or Flexbox for layout:
```css
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```
</details>

---

### Challenge 2: Add a Dark Mode Toggle (CSS Only)

**Task:**
Create two CSS themes (light and dark) and allow the user to switch between them using a CSS file.

**Requirements:**
- Create `dark.css` in addition to `style.css`
- Use different colors for dark mode
- (Advanced: use JavaScript to toggle - optional)

<details>
<summary>Hint</summary>

Create `dark.css` with:
```css
body {
    background: #1a1a1a;
    color: #f0f0f0;
}

.container {
    background: #2a2a2a;
}
```

Link it conditionally or create a toggle button.
</details>

---

### Challenge 3: Create a 404 Error Page

**Task:**
Create a custom 404 error page.

**Requirements:**
1. Create `404.html` template
2. Style it nicely
3. Include a link back to home
4. Configure Django to use your custom 404 page

<details>
<summary>Solution</summary>

**Create `pages/templates/404.html`:**

```html
{% extends 'pages/base.html' %}

{% block title %}Page Not Found{% endblock %}

{% block content %}
    <div style="text-align: center; padding: 50px;">
        <h1 style="font-size: 5em; color: #667eea;">404</h1>
        <h2>Page Not Found</h2>
        <p>The page you're looking for doesn't exist.</p>
        <a href="{% url 'pages:home' %}" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #667eea; color: white; text-decoration: none; border-radius: 5px;">Go Home</a>
    </div>
{% endblock %}
```

**In `portfolio/settings.py`:**

```python
DEBUG = False  # Set to False to see custom 404
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

**Note:** In development, set `DEBUG = True` to see detailed errors.
</details>

---

### Challenge 4: Build a Timeline Page

**Task:**
Create a timeline page showing your learning journey.

**Data structure:**
```python
timeline = [
    {'date': 'Week 1', 'event': 'Started learning Python'},
    {'date': 'Week 2', 'event': 'Mastered Python data structures'},
    {'date': 'Week 3', 'event': 'Built first HTML/CSS website'},
    {'date': 'Week 4', 'event': 'Created Django project'},
]
```

**Requirements:**
- Display as a vertical timeline
- Use CSS to create a visual timeline effect
- Add icons or emojis for each event

<details>
<summary>Hint</summary>

CSS for timeline:
```css
.timeline {
    position: relative;
    padding-left: 40px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 10px;
    top: 0;
    bottom: 0;
    width: 3px;
    background: #667eea;
}

.timeline-item {
    position: relative;
    margin-bottom: 30px;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -35px;
    top: 5px;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background: #667eea;
}
```
</details>

---

### Challenge 5: Create an Interactive Gallery

**Task:**
Create an image gallery page with:
- Grid layout
- Hover effects
- Image captions
- Responsive design

**Requirements:**
- At least 6 images
- CSS Grid for layout
- Hover effects (scale, shadow, overlay)
- Works on mobile devices

<details>
<summary>Hint</summary>

```css
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 10px;
}

.gallery-item img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    transition: transform 0.3s;
}

.gallery-item:hover img {
    transform: scale(1.1);
}
```
</details>

---

## Solutions Summary

All exercises have been completed. Here's what you should have now:

**Project Structure:**
```
portfolio/
├── pages/
│   ├── static/
│   │   └── pages/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── images/
│   ├── templates/
│   │   └── pages/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── projects.html
│   │       ├── skills.html
│   │       ├── blog.html
│   │       └── contact.html
│   ├── views.py
│   └── urls.py
├── portfolio/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

**Skills Practiced:**
- ✓ Django project and app creation
- ✓ Views and URL routing
- ✓ Templates and template tags
- ✓ Template inheritance
- ✓ Static files (CSS, images)
- ✓ Passing context data to templates
- ✓ Using loops and conditionals in templates
- ✓ URL naming and namespaces
- ✓ Basic responsive design

**Next Steps:**
- Complete the mini-project (Exercise 19-20)
- Try the challenge exercises
- Experiment with more styling
- Add your own creative pages
- Push your project to GitHub

---

**Great job completing Week 4 exercises! You're now ready to move on to Week 5: Models and Databases! 🚀**
