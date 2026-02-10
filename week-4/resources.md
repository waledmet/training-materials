# Week 4 Resources – Django Learning Materials

Curated learning resources for Django basics: tutorials, documentation, videos, and practice platforms.

---

## Table of Contents

1. [Official Documentation](#official-documentation)
2. [Video Tutorials](#video-tutorials)
3. [Interactive Tutorials](#interactive-tutorials)
4. [Books and Guides](#books-and-guides)
5. [Practice Platforms](#practice-platforms)
6. [Django Tools](#django-tools)
7. [Community and Support](#community-and-support)
8. [Cheat Sheets](#cheat-sheets)

---

## Official Documentation

### Django Documentation

**Django Official Docs**
- URL: https://docs.djangoproject.com/
- Best for: Reference, in-depth explanations
- Recommended sections for Week 4:
  - Getting Started Tutorial (Parts 1-3)
  - Templates Guide
  - URL Dispatcher
  - Managing Static Files

**Django Tutorial (Official)**
- URL: https://docs.djangoproject.com/en/stable/intro/tutorial01/
- A 7-part tutorial building a polling app
- Covers: Projects, apps, views, templates, URLs
- Excellent for beginners

**Django Template Language**
- URL: https://docs.djangoproject.com/en/stable/ref/templates/language/
- Complete reference for template tags and filters
- Use when you need specific template syntax

**URL Dispatcher Reference**
- URL: https://docs.djangoproject.com/en/stable/topics/http/urls/
- Everything about URL routing
- Includes advanced patterns

---

## Video Tutorials

### YouTube Channels

**Corey Schafer - Django Tutorial Series**
- URL: https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
- 17-part series, beginner-friendly
- Covers Django from scratch
- Highly recommended for Week 4-6
- Topics: Setup, views, templates, static files, database

**Programming with Mosh - Python Django Tutorial**
- URL: https://www.youtube.com/watch?v=rHux0gMZ3Eg
- 1-hour crash course
- Great overview of Django basics
- Good for visual learners

**Traversy Media - Django Crash Course**
- URL: https://www.youtube.com/watch?v=e1IyzVyrLSU
- Fast-paced introduction
- Build a simple app from scratch
- 1 hour 30 minutes

**Dennis Ivy - Django for Beginners**
- URL: https://www.youtube.com/c/DennisIvy
- Multiple Django tutorials
- Clear explanations
- Project-based learning

### Udemy Courses (Paid)

**Django for Beginners** by Nick Walter
- Comprehensive Django course
- Projects included
- Good for structured learning

**Python Django - The Practical Guide** by Maximilian Schwarzmüller
- In-depth Django course
- Modern Django practices
- Includes deployment

---

## Interactive Tutorials

### Django Girls Tutorial

**Django Girls**
- URL: https://tutorial.djangogirls.org/
- Free, beginner-friendly tutorial
- Build a blog from scratch
- Covers: Setup, models, views, templates, deployment
- Excellent for self-paced learning
- Available in multiple languages

### Real Python

**Real Python - Django Tutorials**
- URL: https://realpython.com/tutorials/django/
- High-quality written tutorials
- Mix of free and premium content
- Topics: Django basics, best practices, testing

### Mozilla Developer Network (MDN)

**Django Web Framework**
- URL: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
- Complete Django tutorial series
- Build a library website
- Excellent explanations
- Free and comprehensive

---

## Books and Guides

### Free Books

**Django for Beginners** by William S. Vincent
- Available online (paid book, but samples available)
- Build 3 projects
- Clear explanations
- Modern Django practices

**Two Scoops of Django** by Daniel Roy Greenfeld & Audrey Roy Greenfeld
- Best practices book
- More advanced (save for later)
- Industry-standard recommendations

### Online Guides

**Simple is Better Than Complex**
- URL: https://simpleisbetterthancomplex.com/
- Excellent Django tutorials
- Beginner to advanced
- Practical examples

**Django Central**
- URL: https://djangocentral.com/
- Tutorials and guides
- Good for specific topics
- Clear code examples

**Full Stack Python**
- URL: https://www.fullstackpython.com/django.html
- Django section of larger guide
- Links to best resources
- Deployment guides

---

## Practice Platforms

### Django Practice

**Django Projects on GitHub**
- Search: "django beginner projects"
- Clone and study existing projects
- Learn from real code
- Examples:
  - Blog applications
  - Portfolio sites
  - To-do apps

**Coding Challenges**

1. **Build a Blog**
   - Posts, categories, comments
   - Perfect for practicing templates

2. **Create a Portfolio**
   - Projects showcase
   - About page, contact form
   - Practice static files

3. **To-Do List App**
   - CRUD operations
   - User interface
   - List management

4. **Personal Library**
   - Book tracking
   - Reading lists
   - Category organization

---

## Django Tools

### Development Tools

**Django Extensions**
- pip install django-extensions
- Useful management commands
- Enhanced shell
- Graph models

**Django Debug Toolbar**
- pip install django-debug-toolbar
- Debugging in development
- See SQL queries
- Performance profiling

**Django Crispy Forms**
- pip install django-crispy-forms
- Better form rendering
- Bootstrap integration
- (For Week 6)

### VS Code Extensions

**Python Extension**
- By Microsoft
- Essential for Python development
- Linting, formatting, IntelliSense

**Django Extension**
- By Baptiste Darthenay
- Django template syntax highlighting
- Snippets for Django code

**SQLite Viewer**
- View database in VS Code
- Inspect tables and data
- Useful for Week 5+

**HTML CSS Support**
- Better HTML/CSS in templates
- Auto-completion

### Browser Tools

**Django Debug Toolbar**
- Shows database queries
- Request/response info
- Template rendering time

**Browser DevTools**
- F12 in browser
- Inspect HTML from templates
- Debug CSS from static files
- Network tab for requests

---

## Community and Support

### Forums and Q&A

**Stack Overflow**
- URL: https://stackoverflow.com/questions/tagged/django
- Ask and answer questions
- Search before asking
- Tag your questions with `django`

**Reddit - r/django**
- URL: https://www.reddit.com/r/django/
- Community discussions
- Share projects
- Get feedback

**Django Forum**
- URL: https://forum.djangoproject.com/
- Official Django community forum
- Helpful community
- Best practices discussions

**Discord Servers**
- Python Discord
- Django developers
- Real-time help
- Study groups

### Social Media

**Twitter**
- Follow: @djangoproject
- Follow: @DjangoTricks
- Django news and updates
- Community tips

**Dev.to**
- URL: https://dev.to/t/django
- Django articles and tutorials
- Community content
- Share your learning

---

## Cheat Sheets

### Django Quick Reference

**Django Template Tags**

```django
{# Comments #}

{{ variable }}                  {# Display variable #}
{{ variable|filter }}           {# Apply filter #}

{% if condition %}              {# If statement #}
    ...
{% elif other %}
    ...
{% else %}
    ...
{% endif %}

{% for item in list %}          {# For loop #}
    {{ item }}
{% empty %}
    No items
{% endfor %}

{% url 'name' %}                {# URL by name #}
{% url 'namespace:name' %}      {# With namespace #}

{% extends 'base.html' %}       {# Template inheritance #}
{% block name %}...{% endblock %} {# Define block #}

{% include 'partial.html' %}    {# Include template #}

{% load static %}               {# Load static files #}
{% static 'path/file' %}        {# Static file URL #}
```

**Common Template Filters**

```django
{{ name|lower }}                # Lowercase
{{ name|upper }}                # Uppercase
{{ name|title }}                # Title Case
{{ text|truncatewords:10 }}     # Limit words
{{ value|default:"N/A" }}       # Default if empty
{{ date|date:"Y-m-d" }}         # Format date
{{ number|floatformat:2 }}      # Format decimal
{{ list|length }}               # Length of list
{{ text|safe }}                 # Mark as safe HTML
```

**Django Management Commands**

```bash
# Project & Apps
django-admin startproject name          # Create project
python manage.py startapp name          # Create app

# Development Server
python manage.py runserver              # Start server
python manage.py runserver 8001         # Custom port

# Database (Week 5)
python manage.py makemigrations         # Create migrations
python manage.py migrate                # Apply migrations
python manage.py createsuperuser        # Create admin user

# Other Useful
python manage.py shell                  # Python shell
python manage.py check                  # Check for errors
python manage.py collectstatic          # Collect static files
```

**URL Patterns**

```python
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),              # /
    path('about/', views.about, name='about'),      # /about/
    path('post/<int:id>/', views.post, name='post'), # /post/5/
    path('user/<str:username>/', views.user),        # /user/ahmed/
]
```

**Views Patterns**

```python
from django.shortcuts import render
from django.http import HttpResponse

# Simple text response
def home(request):
    return HttpResponse("Hello")

# Render template
def home(request):
    return render(request, 'app/home.html')

# With context
def home(request):
    context = {'name': 'Ahmed'}
    return render(request, 'app/home.html', context)

# With URL parameter
def detail(request, id):
    context = {'id': id}
    return render(request, 'app/detail.html', context)
```

---

## Week 4 Specific Resources

### For Day 1: Django Setup

**Installation Guides:**
- Official: https://docs.djangoproject.com/en/stable/topics/install/
- Real Python: https://realpython.com/django-setup/

**Virtual Environments:**
- Python venv docs: https://docs.python.org/3/library/venv.html
- Guide: https://docs.python-guide.org/dev/virtualenvs/

### For Day 2-3: Templates

**Template Documentation:**
- Built-in tags: https://docs.djangoproject.com/en/stable/ref/templates/builtins/
- Template language: https://docs.djangoproject.com/en/stable/topics/templates/
- Template inheritance: https://docs.djangoproject.com/en/stable/ref/templates/language/#template-inheritance

### For Day 4: Static Files

**Static Files Guide:**
- How to manage: https://docs.djangoproject.com/en/stable/howto/static-files/
- Deploying static files: https://docs.djangoproject.com/en/stable/howto/static-files/deployment/

### For Day 5: Complete Project

**Project Structure:**
- Best practices: https://docs.djangoproject.com/en/stable/misc/design-philosophies/
- Common project structure patterns
- Code organization tips

---

## Troubleshooting Resources

### Common Errors

**"No module named 'django'"**
- Solution: Activate virtual environment, then `pip install django`
- Guide: Check installation section in lessons.md

**"TemplateDoesNotExist"**
- Solution: Check INSTALLED_APPS, verify template path
- Debug: https://docs.djangoproject.com/en/stable/ref/templates/api/

**"Page not found (404)"**
- Solution: Check URL patterns, ensure urls.py is configured
- Debug guide in lessons.md troubleshooting section

**Error Pages:**
- Django error pages explained: https://docs.djangoproject.com/en/stable/ref/views/#error-views

---

## Additional Learning Paths

### After Week 4

**Week 5 Preview: Models & Databases**
- Django ORM tutorial
- Database relationships
- Migrations guide

**Week 6 Preview: Forms & Authentication**
- Django forms documentation
- User authentication
- Form validation

**Future Topics:**
- Django REST Framework (Week 7)
- Deployment (Week 9)
- Testing best practices
- Django security

---

## Recommended Learning Path

### For Week 4

**Day 1:**
1. Read Django official tutorial part 1
2. Watch Corey Schafer's first 2 Django videos
3. Complete exercises 1-5

**Day 2:**
1. Read Django template documentation
2. Watch template tutorial videos
3. Complete exercises 6-10

**Day 3:**
1. Study template inheritance examples
2. Read URL dispatcher docs
3. Complete exercises 11-14

**Day 4:**
1. Read static files guide
2. Review CSS from Week 3
3. Complete exercises 15-18

**Day 5:**
1. Review all previous lessons
2. Start mini-project
3. Complete exercises 19-20

---

## Study Tips

**Effective Learning:**
1. **Type the code yourself** - Don't copy/paste
2. **Break things intentionally** - Learn from errors
3. **Read error messages carefully** - They tell you what's wrong
4. **Use the documentation** - Official docs are your best friend
5. **Build projects** - Apply what you learn immediately
6. **Join communities** - Ask questions, help others
7. **Review regularly** - Revisit concepts

**When Stuck:**
1. Read the error message
2. Check your code for typos
3. Review the lesson/documentation
4. Google the error
5. Check Stack Overflow
6. Ask in community forums
7. Ask your trainer

---

## Useful Websites

**Development:**
- Django Packages: https://djangopackages.org/ (Find Django packages)
- PyPI: https://pypi.org/ (Python packages)
- GitHub: https://github.com/ (Code examples, templates)

**Design:**
- Bootstrap: https://getbootstrap.com/ (CSS framework)
- Tailwind: https://tailwindcss.com/ (Utility CSS)
- Google Fonts: https://fonts.google.com/ (Free fonts)
- Unsplash: https://unsplash.com/ (Free images)

**Tools:**
- DB Browser for SQLite: https://sqlitebrowser.org/
- Postman: https://www.postman.com/ (API testing - Week 7)
- Git: https://git-scm.com/doc (Version control)

---

## Keep Learning

Django is vast! Week 4 is just the beginning.

**What's Next:**
- Week 5: Models and databases
- Week 6: Forms and authentication
- Week 7: APIs and AJAX
- Week 8-9: Final project and deployment

**Long-term:**
- Advanced Django features
- Django REST Framework
- Django channels (WebSockets)
- Django deployment
- Django with Docker
- Django testing

---

**Remember: You don't need to read everything at once. Use these resources as you need them. Focus on Week 4 topics first, then explore deeper as you progress. Happy learning! 🚀**
