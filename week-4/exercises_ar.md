# تمارين الأسبوع الرابع – ممارسة أساسيات Django

تمارين عملية للأسبوع الرابع: إعداد مشروع Django، التطبيقات، العروض، القوالب، والملفات الثابتة.

---

## جدول المحتويات

1. [اليوم 1: إعداد Django وأولى العروض](#اليوم-1-إعداد-django-وأولى-العروض)
2. [اليوم 2: القوالب ووسوم القوالب](#اليوم-2-القوالب-ووسوم-القوالب)
3. [اليوم 3: وراثة القوالب وعناوين URL](#اليوم-3-وراثة-القوالب-وعناوين-url)
4. [اليوم 4: الملفات الثابتة والتنسيق](#اليوم-4-الملفات-الثابتة-والتنسيق)
5. [اليوم 5: مشروع كامل متعدد الصفحات](#اليوم-5-مشروع-كامل-متعدد-الصفحات)
6. [تمارين التحدي](#تمارين-التحدي)

---

## اليوم 1: إعداد Django وأولى العروض

### التمرين 1: تثبيت Django وإنشاء مشروع

**المهمة:**
1. أنشئ بيئة افتراضية باسم `venv`
2. فعّل البيئة الافتراضية
3. ثبّت Django
4. تحقق من تثبيت Django
5. أنشئ مشروع Django باسم `portfolio`

**الأوامر المطلوبة:**
```bash
python -m venv venv
# فعّل venv (يعتمد على نظام التشغيل)
pip install django
django-admin --version
django-admin startproject portfolio
```

**النتيجة المتوقعة:**
- البيئة الافتراضية تم إنشاؤها وتفعيلها
- Django تم تثبيته بنجاح
- مجلد مشروع `portfolio` الجديد تم إنشاؤه

<details>
<summary>اضغط لعرض الحل</summary>

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

زر `http://localhost:8000` للتحقق من أنه يعمل!
</details>

---

### التمرين 2: إنشاء أول تطبيق

**المهمة:**
1. أنشئ تطبيقًا باسم `pages`
2. سجّل التطبيق في `settings.py`
3. تحقق أن مجلد التطبيق تم إنشاؤه مع جميع الملفات الضرورية

**هيكل المجلدات المتوقع:**
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
<summary>اضغط لعرض الحل</summary>

```bash
# إنشاء التطبيق
python manage.py startapp pages
```

**عدّل `portfolio/settings.py`:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # ← أضف هذا
]
```
</details>

---

### التمرين 3: إنشاء عروض بسيطة

**المهمة:**
أنشئ ثلاثة عروض بسيطة تُرجع استجابات نصية:

1. عرض `home` → يُرجع "Welcome to my portfolio!"
2. عرض `about` → يُرجع "About me: I'm a Django learner"
3. عرض `projects` → يُرجع "My projects coming soon!"

**الملف:** `pages/views.py`

<details>
<summary>اضغط لعرض الحل</summary>

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

### التمرين 4: إعداد عناوين URL

**المهمة:**
1. أنشئ `pages/urls.py`
2. اربط العروض الثلاثة بعناوين URL:
   - `/` → عرض home
   - `/about/` → عرض about
   - `/projects/` → عرض projects
3. ضمّن عناوين URL الخاصة بالتطبيق في `urls.py` الخاص بالمشروع

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/urls.py`:**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
]
```

**عدّل `portfolio/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

**اختبر:**
- `http://localhost:8000/` → "Welcome to my portfolio!"
- `http://localhost:8000/about/` → "About me: I'm a Django learner"
- `http://localhost:8000/projects/` → "My projects coming soon!"
</details>

---

### التمرين 5: إضافة URL بمعامل

**المهمة:**
أنشئ عرضًا يعرض تحية باسم من عنوان URL.

**المتطلبات:**
- نمط URL: `/greet/<name>/`
- مثال: `/greet/Ahmed/` → "Hello, Ahmed!"
- مثال: `/greet/Sara/` → "Hello, Sara!"

<details>
<summary>اضغط لعرض الحل</summary>

**أضف إلى `pages/views.py`:**

```python
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
```

**أضف إلى `pages/urls.py`:**

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('greet/<str:name>/', views.greet, name='greet'),  # ← أضف هذا
]
```

**اختبر:**
- `/greet/Ahmed/` → "Hello, Ahmed!"
- `/greet/Sara/` → "Hello, Sara!"
</details>

---

## اليوم 2: القوالب ووسوم القوالب

### التمرين 6: إنشاء أول قالب

**المهمة:**
1. أنشئ هيكل مجلد القوالب: `pages/templates/pages/`
2. أنشئ `home.html` بهيكل HTML أساسي
3. حدّث عرض `home` ليعرض القالب

**محتوى القالب:**
- عنوان الصفحة: "Home"
- عنوان رئيسي: "Welcome to My Portfolio"
- فقرة: "This is my Django learning project"

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/templates/pages/home.html`:**

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

**حدّث `pages/views.py`:**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')
```
</details>

---

### التمرين 7: تمرير متغيرات إلى القالب

**المهمة:**
حدّث عرض home لتمرير البيانات التالية إلى القالب:

- `title`: "Django Portfolio"
- `name`: "Your Name"
- `year`: 2025
- `description`: "Learning Django web development"

اعرض جميع هذه المتغيرات في القالب.

<details>
<summary>اضغط لعرض الحل</summary>

**حدّث `pages/views.py`:**

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

**حدّث `pages/templates/pages/home.html`:**

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

### التمرين 8: استخدام المنطق في القوالب (if/else)

**المهمة:**
أنشئ قالب `about.html` يعرض محتوى مختلف بناءً على ما إذا كان المستخدم مسجلاً دخوله.

**المتطلبات:**
- مرّر متغير `is_logged_in` (منطقي) من العرض
- إذا `True`: اعرض "Welcome back!"
- إذا `False`: اعرض "Please log in to see more"

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/templates/pages/about.html`:**

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

**حدّث `pages/views.py`:**

```python
def about(request):
    context = {
        'is_logged_in': False  # جرّب تغييرها إلى True
    }
    return render(request, 'pages/about.html', context)
```
</details>

---

### التمرين 9: التكرار في قائمة داخل القالب

**المهمة:**
أنشئ قالب `projects.html` يعرض قائمة بالمشاريع.

**المتطلبات:**
- مرّر قائمة بأسماء المشاريع من العرض
- استخدم حلقة `{% for %}` لعرض كل مشروع
- اعرضها في قائمة غير مرتبة (`<ul>`)

**قائمة المشاريع:**
- "Calculator App"
- "To-Do List"
- "Weather Dashboard"
- "Blog Website"

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/templates/pages/projects.html`:**

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

**حدّث `pages/views.py`:**

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

### التمرين 10: التكرار في قاموس

**المهمة:**
أنشئ قالب `skills.html` يعرض المهارات مع مستويات الإتقان.

**المتطلبات:**
- مرّر قاموسًا بالمهارات مع نسب الإتقان
- اعرض كل مهارة مع مستواها
- الصيغة: "Python: 80%"

**بيانات المهارات:**
```python
{
    'Python': 80,
    'HTML': 90,
    'CSS': 75,
    'Django': 60
}
```

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/templates/pages/skills.html`:**

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

**أضف إلى `pages/views.py`:**

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

**أضف إلى `pages/urls.py`:**

```python
path('skills/', views.skills, name='skills'),
```
</details>

---

## اليوم 3: وراثة القوالب وعناوين URL

### التمرين 11: إنشاء قالب أساسي

**المهمة:**
أنشئ قالب `base.html` يحتوي على:
- رأس بعنوان الموقع
- قائمة تنقل (Home, About, Projects, Skills)
- كتلة محتوى للقوالب الفرعية
- تذييل بحقوق النشر

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/templates/pages/base.html`:**

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

### التمرين 12: توسيع القالب الأساسي

**المهمة:**
حدّث جميع قوالبك الحالية (home, about, projects, skills) لتوسيع `base.html`.

**المتطلبات:**
- استخدم `{% extends 'pages/base.html' %}`
- حدد عنوانًا مخصصًا لكل صفحة
- ضع محتوى الصفحة في `{% block content %}`

<details>
<summary>اضغط لعرض الحل</summary>

**حدّث `pages/templates/pages/home.html`:**

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

**حدّث `pages/templates/pages/about.html`:**

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

**حدّث `pages/templates/pages/projects.html`:**

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

**حدّث `pages/templates/pages/skills.html`:**

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

### التمرين 13: استخدام أسماء URL

**المهمة:**
حدّث روابط التنقل في `base.html` لاستخدام وسم `{% url %}` بدلاً من المسارات الثابتة.

**المتطلبات:**
- استخدم `{% url 'home' %}` بدلاً من `/`
- استخدم `{% url 'about' %}` بدلاً من `/about/`
- نفس الشيء لجميع روابط التنقل

<details>
<summary>اضغط لعرض الحل</summary>

**حدّث التنقل في `pages/templates/pages/base.html`:**

```html
<nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
    <a href="{% url 'projects' %}">Projects</a>
    <a href="{% url 'skills' %}">Skills</a>
</nav>
```

**الفائدة:** إذا غيّرت أنماط URL، تتحدث الروابط تلقائيًا!
</details>

---

### التمرين 14: إضافة مساحة اسمية لعناوين URL

**المهمة:**
1. أضف مساحة اسمية لعناوين URL في تطبيقك
2. حدّث جميع وسوم `{% url %}` لاستخدام المساحة الاسمية

<details>
<summary>اضغط لعرض الحل</summary>

**حدّث `pages/urls.py`:**

```python
from django.urls import path
from . import views

app_name = 'pages'  # ← أضف مساحة اسمية

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
]
```

**حدّث التنقل في `base.html`:**

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

## اليوم 4: الملفات الثابتة والتنسيق

### التمرين 15: إعداد الملفات الثابتة

**المهمة:**
1. أنشئ هيكل مجلد الملفات الثابتة: `pages/static/pages/css/`
2. أنشئ ملف `style.css`
3. حمّله في `base.html`

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ هيكل المجلدات:**
```
pages/
└── static/
    └── pages/
        └── css/
            └── style.css
```

**أنشئ `pages/static/pages/css/style.css`:**

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

**حدّث `pages/templates/pages/base.html`:**

```html
{% load static %}  <!-- ← أضف في الأعلى -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Portfolio{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'pages/css/style.css' %}">
</head>
<!-- باقي القالب -->
```

احذف وسوم `<style>` المضمنة من القالب.
</details>

---

### التمرين 16: إضافة المزيد من تنسيق CSS

**المهمة:**
حسّن ملف `style.css` مع:
- عناوين منسقة بألوان
- تنسيق أفضل للقوائم
- تأثيرات عند التمرير على الروابط
- حواف مستديرة وظلال

<details>
<summary>اضغط لعرض الحل</summary>

**أضف إلى `pages/static/pages/css/style.css`:**

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

### التمرين 17: إضافة صور

**المهمة:**
1. أنشئ مجلد `pages/static/pages/images/`
2. أضف صورة شخصية
3. اعرضها في صفحة About

<details>
<summary>اضغط لعرض الحل</summary>

**هيكل المجلدات:**
```
pages/static/pages/
├── css/
│   └── style.css
└── images/
    └── profile.jpg  # أضف صورتك هنا
```

**حدّث `pages/templates/pages/about.html`:**

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

### التمرين 18: إنشاء تنقل متجاوب

**المهمة:**
اجعل قائمة التنقل متجاوبة:
- رتّب الروابط عموديًا على الشاشات الصغيرة
- ابقِها أفقية على الشاشات الكبيرة

<details>
<summary>اضغط لعرض الحل</summary>

**أضف إلى `pages/static/pages/css/style.css`:**

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

/* التصميم المتجاوب */
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

## اليوم 5: مشروع كامل متعدد الصفحات

### التمرين 19: بناء صفحة رئيسية لمدونة شخصية

**المهمة:**
أنشئ صفحة رئيسية لمدونة تعرض:
- قائمة بعناوين المقالات
- تواريخ النشر
- أوصاف مختصرة
- رابط لقراءة المزيد (روابط وهمية حاليًا)

**مرّر هذه البيانات من العرض:**
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
<summary>اضغط لعرض الحل</summary>

**أضف إلى `pages/views.py`:**

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

**أنشئ `pages/templates/pages/blog.html`:**

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

**أضف إلى `pages/urls.py`:**

```python
path('blog/', views.blog, name='blog'),
```

**حدّث التنقل في `base.html`:**

```html
<a href="{% url 'pages:blog' %}">Blog</a>
```
</details>

---

### التمرين 20: إنشاء صفحة تواصل بمعلومات

**المهمة:**
أنشئ صفحة تواصل تعرض:
- بريدك الإلكتروني
- رقم الهاتف
- روابط وسائل التواصل الاجتماعي (GitHub, LinkedIn)
- نموذج تواصل (HTML فقط، غير وظيفي)

<details>
<summary>اضغط لعرض الحل</summary>

**أضف إلى `pages/views.py`:**

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

**أنشئ `pages/templates/pages/contact.html`:**

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
    <p style="font-size: 0.9em; color: #666;"><em>ملاحظة: النموذج غير وظيفي حاليًا (سنتعلم هذا في الأسبوع 6)</em></p>
{% endblock %}
```

**أضف إلى `pages/urls.py`:**

```python
path('contact/', views.contact, name='contact'),
```
</details>

---

## تمارين التحدي

### التحدي 1: إنشاء صفحة خدمات

**المهمة:**
أنشئ صفحة خدمات تعرض قائمة بالخدمات التي تقدمها. كل خدمة تحتوي على:
- اسم الخدمة
- الوصف
- رمز أو إيموجي
- السعر (أو "مجاني")

اعرضها بتخطيط شبكي باستخدام CSS.

<details>
<summary>تلميح</summary>

استخدم CSS Grid أو Flexbox للتخطيط:
```css
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```
</details>

---

### التحدي 2: إضافة وضع داكن (CSS فقط)

**المهمة:**
أنشئ سمتين CSS (فاتحة وداكنة) واسمح للمستخدم بالتبديل بينهما.

**المتطلبات:**
- أنشئ `dark.css` بالإضافة إلى `style.css`
- استخدم ألوانًا مختلفة للوضع الداكن
- (متقدم: استخدم JavaScript للتبديل - اختياري)

<details>
<summary>تلميح</summary>

أنشئ `dark.css` مع:
```css
body {
    background: #1a1a1a;
    color: #f0f0f0;
}

.container {
    background: #2a2a2a;
}
```

اربطه بشكل شرطي أو أنشئ زر تبديل.
</details>

---

### التحدي 3: إنشاء صفحة خطأ 404

**المهمة:**
أنشئ صفحة خطأ 404 مخصصة.

**المتطلبات:**
1. أنشئ قالب `404.html`
2. نسّقه بشكل جميل
3. أضف رابطًا للعودة إلى الرئيسية
4. أعِد Django لاستخدام صفحة 404 المخصصة

<details>
<summary>اضغط لعرض الحل</summary>

**أنشئ `pages/templates/404.html`:**

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

**في `portfolio/settings.py`:**

```python
DEBUG = False  # اضبطها على False لرؤية صفحة 404 المخصصة
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

**ملاحظة:** في التطوير، اضبط `DEBUG = True` لرؤية الأخطاء المفصلة.
</details>

---

### التحدي 4: بناء صفحة خط زمني

**المهمة:**
أنشئ صفحة خط زمني تعرض رحلة تعلمك.

**هيكل البيانات:**
```python
timeline = [
    {'date': 'Week 1', 'event': 'Started learning Python'},
    {'date': 'Week 2', 'event': 'Mastered Python data structures'},
    {'date': 'Week 3', 'event': 'Built first HTML/CSS website'},
    {'date': 'Week 4', 'event': 'Created Django project'},
]
```

**المتطلبات:**
- اعرضه كخط زمني عمودي
- استخدم CSS لإنشاء تأثير خط زمني بصري
- أضف أيقونات أو إيموجي لكل حدث

<details>
<summary>تلميح</summary>

CSS للخط الزمني:
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

### التحدي 5: إنشاء معرض صور تفاعلي

**المهمة:**
أنشئ صفحة معرض صور مع:
- تخطيط شبكي
- تأثيرات عند التمرير
- تعليقات على الصور
- تصميم متجاوب

**المتطلبات:**
- 6 صور على الأقل
- CSS Grid للتخطيط
- تأثيرات عند التمرير (تكبير، ظل، طبقة فوقية)
- يعمل على الأجهزة المحمولة

<details>
<summary>تلميح</summary>

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

## ملخص الحلول

تم إكمال جميع التمارين. إليك ما يجب أن يكون لديك الآن:

**هيكل المشروع:**
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

**المهارات التي تمّت ممارستها:**
- ✓ إنشاء مشروع وتطبيق Django
- ✓ العروض وتوجيه URL
- ✓ القوالب ووسوم القوالب
- ✓ وراثة القوالب
- ✓ الملفات الثابتة (CSS، الصور)
- ✓ تمرير بيانات السياق إلى القوالب
- ✓ استخدام الحلقات والشروط في القوالب
- ✓ تسمية URL والمساحات الاسمية
- ✓ أساسيات التصميم المتجاوب

**الخطوات التالية:**
- أكمل المشروع المصغّر (التمارين 19-20)
- جرّب تمارين التحدي
- جرّب المزيد من التنسيق
- أضف صفحاتك الإبداعية الخاصة
- ارفع مشروعك إلى GitHub

---

**أحسنت في إكمال تمارين الأسبوع الرابع! أنت الآن جاهز للانتقال إلى الأسبوع 5: النماذج وقواعد البيانات!**
