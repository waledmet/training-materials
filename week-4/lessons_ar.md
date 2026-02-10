# دروس الأسبوع الرابع – أساسيات Django: المشروع، التطبيقات، العروض والقوالب

مرحبًا بك في الأسبوع الرابع! هذا الأسبوع ننتقل من صفحات HTML/CSS الثابتة إلى تطبيقات الويب الديناميكية باستخدام **Django**، إطار عمل Python القوي للويب.

---

## جدول المحتويات

1. [ما هو Django؟](#1-ما-هو-django)
2. [تثبيت Django](#2-تثبيت-django)
3. [إنشاء أول مشروع Django](#3-إنشاء-أول-مشروع-django)
4. [فهم هيكل المشروع](#4-فهم-هيكل-المشروع)
5. [إنشاء تطبيق Django](#5-إنشاء-تطبيق-django)
6. [عناوين URL والعروض (Views)](#6-عناوين-url-والعروض)
7. [قوالب Django](#7-قوالب-django)
8. [وراثة القوالب](#8-وراثة-القوالب)
9. [الملفات الثابتة (CSS، الصور)](#9-الملفات-الثابتة)
10. [مشروع مصغّر: موقع Django من 3 صفحات](#10-مشروع-مصغّر)

---

## 1. ما هو Django؟

### ما هو إطار عمل الويب؟

**إطار عمل الويب** يوفر أدوات وهيكلية لبناء تطبيقات الويب بشكل أسرع وأكثر كفاءة.

**بدون إطار عمل:**
```python
# عليك التعامل مع كل شيء يدويًا
- تحليل طلبات HTTP
- توجيه عناوين URL
- توليد HTML
- التعامل مع قواعد البيانات
- إدارة الجلسات
- التعامل مع الأمان
```

**مع Django:**
```python
# Django يتولى الأجزاء الصعبة
- ✓ توجيه URL مدمج
- ✓ محرك قوالب مضمّن
- ✓ ORM لقواعد البيانات جاهز
- ✓ ميزات الأمان مفعّلة
- ✓ واجهة الإدارة تلقائية
```

### لماذا Django؟

**المميزات:**
- **شامل (Batteries included)**: كل ما تحتاجه يأتي مع Django
- **مبني على Python**: استخدم مهاراتك في Python
- **تطوير سريع**: ابنِ بسرعة مع كود أقل
- **آمن**: حماية مدمجة ضد الهجمات الشائعة
- **قابل للتوسع**: يستخدمه Instagram و Pinterest و Mozilla
- **توثيق ممتاز**: موارد تعليمية رائعة

**مواقع شهيرة تستخدم Django:**
- Instagram
- Pinterest
- Mozilla
- Spotify
- YouTube (أجزاء منه)
- The Washington Post

### فلسفة Django

يتبع Django مبدأ **"لا تكرر نفسك" (DRY)**:
- اكتب الكود مرة واحدة
- أعد استخدامه في كل مكان
- تكرار أقل = أخطاء أقل

يستخدم Django نمط **MTV**:
- **M**odel (النموذج): طبقة قاعدة البيانات (الأسبوع 5)
- **T**emplate (القالب): طبقة العرض (الأسبوع 4)
- **V**iew (العرض): طبقة منطق الأعمال (الأسبوع 4)

مشابه لنمط MVC (Model-View-Controller).

---

## 2. تثبيت Django

### المتطلبات الأساسية

يجب أن يكون لديك:
- Python 3.8+ مثبت
- pip (مدير حزم Python)
- معرفة بالبيئات الافتراضية (الأسبوع 2)
- محرر نصوص (VS Code)

### الخطوة 1: إنشاء بيئة افتراضية

**لماذا نستخدم بيئة افتراضية؟**
- عزل تبعيات المشروع
- تجنب التعارضات بين المشاريع
- الحفاظ على نظافة Python في النظام

**إنشاء وتفعيل:**

**Windows:**
```bash
# انتقل إلى مجلد المشاريع
cd Documents

# أنشئ مجلدًا للأسبوع الرابع
mkdir week-4-django
cd week-4-django

# أنشئ بيئة افتراضية
python -m venv venv

# فعّلها
venv\Scripts\activate

# يجب أن ترى (venv) في الطرفية
```

**Mac/Linux:**
```bash
# انتقل إلى مجلد المشاريع
cd ~/Documents

# أنشئ مجلدًا للأسبوع الرابع
mkdir week-4-django
cd week-4-django

# أنشئ بيئة افتراضية
python3 -m venv venv

# فعّلها
source venv/bin/activate

# يجب أن ترى (venv) في الطرفية
```

### الخطوة 2: تثبيت Django

```bash
# تأكد من تفعيل البيئة الافتراضية (ترى (venv))
pip install django

# تحقق من التثبيت
django-admin --version

# يجب أن يظهر: 5.x.x (أو مشابه)
```

### الخطوة 3: حفظ التبعيات

```bash
# أنشئ ملف requirements.txt
pip freeze > requirements.txt

# هذا الملف يسرد جميع الحزم المثبتة
# مفيد لمشاركة مشروعك
```

---

## 3. إنشاء أول مشروع Django

### ما هو مشروع Django؟

**المشروع** هو تطبيق الويب بالكامل:
- يحتوي على الإعدادات
- يربط عدة تطبيقات
- يتعامل مع توجيه URL
- يدير الإعدادات

فكّر فيه كـ **الحاوية** لموقعك.

### إنشاء مشروع

```bash
# تأكد أنك في مجلد week-4-django مع تفعيل venv

# أنشئ مشروع Django جديد باسم "mysite"
django-admin startproject mysite

# هذا ينشئ هيكل مجلدات
```

**ما تم إنشاؤه:**

```
mysite/
│
├── mysite/
│   ├── __init__.py      # يجعل هذا حزمة Python
│   ├── settings.py      # إعدادات المشروع (مهم)
│   ├── urls.py          # توجيه URL الرئيسي
│   ├── asgi.py          # إعداد الخادم غير المتزامن
│   └── wsgi.py          # إعداد خادم الويب
│
└── manage.py            # أداة سطر الأوامر (مهم)
```

### الدخول إلى المشروع

```bash
cd mysite

# يجب أن تكون الآن في: week-4-django/mysite/
# هذا المجلد يحتوي على manage.py
```

### تشغيل خادم التطوير

```bash
# شغّل خادم التطوير في Django
python manage.py runserver

# يجب أن ترى:
# Starting development server at http://127.0.0.1:8000/
```

**افتح المتصفح:**
- اذهب إلى: `http://127.0.0.1:8000/` أو `http://localhost:8000/`
- يجب أن ترى صفحة **"The install worked successfully!"**

**تهانينا! مشروع Django الأول يعمل!**

**لإيقاف الخادم:**
- اضغط `Ctrl+C` في الطرفية

---

## 4. فهم هيكل المشروع

### شرح الملفات الرئيسية

#### `manage.py`

**أداة سطر الأوامر** الخاصة بـ Django:

```bash
python manage.py runserver      # تشغيل الخادم
python manage.py startapp name   # إنشاء تطبيق
python manage.py migrate         # تطبيق تغييرات قاعدة البيانات
python manage.py createsuperuser # إنشاء مستخدم مدير
```

**لا تعدّل هذا الملف!** يتم إنشاؤه تلقائيًا.

#### `mysite/settings.py`

**قلب مشروعك**. يحتوي على جميع الإعدادات:

```python
# إعدادات مهمة:

DEBUG = True  # عرض أخطاء مفصلة (للتطوير فقط)

ALLOWED_HOSTS = []  # النطاقات المسموح لها بالوصول للموقع

INSTALLED_APPS = [  # تطبيقات Django وتطبيقاتك
    'django.contrib.admin',
    'django.contrib.auth',
    # ... تطبيقاتك ستضاف هنا
]

DATABASES = {  # إعداد قاعدة البيانات
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [  # إعداد محرك القوالب
    # سنقوم بإعداد هذا قريبًا
]

STATIC_URL = 'static/'  # رابط الملفات الثابتة (CSS، الصور)

SECRET_KEY = '...'  # احتفظ بهذا سريًا في الإنتاج!
```

#### `mysite/urls.py`

**موجّه URL الرئيسي**:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # واجهة الإدارة
    # عناوين URL الخاصة بك ستضاف هنا
]
```

فكّر في هذا كـ **جدول المحتويات** لموقعك.

---

## 5. إنشاء تطبيق Django

### ما هو تطبيق Django؟

**التطبيق** هو مكوّن يقوم بعمل معين:
- مدونة
- نظام مصادقة المستخدمين
- نموذج تواصل
- متجر

**مشروع واحد** يمكن أن يحتوي على **عدة تطبيقات**.

**مثال:**
```
mysite (المشروع)
├── blog (تطبيق)       # يتعامل مع المقالات
├── store (تطبيق)      # يتعامل مع المنتجات
└── users (تطبيق)      # يتعامل مع حسابات المستخدمين
```

في الأسبوع 4، سننشئ تطبيقًا واحدًا باسم `core`.

### إنشاء تطبيق

```bash
# تأكد أنك في المجلد الذي يحتوي manage.py
python manage.py startapp core

# هذا ينشئ مجلدًا جديدًا باسم "core"
```

**ما تم إنشاؤه:**

```
core/
├── __init__.py          # علامة حزمة Python
├── admin.py             # تسجيل النماذج للإدارة (الأسبوع 5)
├── apps.py              # إعداد التطبيق
├── models.py            # نماذج قاعدة البيانات (الأسبوع 5)
├── tests.py             # اكتب الاختبارات هنا
├── views.py             # دوال العرض (مهم)
└── migrations/          # ترحيلات قاعدة البيانات (الأسبوع 5)
    └── __init__.py
```

### تسجيل التطبيق

**مهم:** يجب أن تخبر Django عن تطبيقك الجديد!

**عدّل `mysite/settings.py`:**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # ← أضف تطبيقك هنا
]
```

احفظ الملف.

---

## 6. عناوين URL والعروض (Views)

### دورة الطلب والاستجابة

فهم كيفية تعامل Django مع الطلبات:

```
المتصفح → URL → Django → View → الاستجابة → المتصفح
```

**مثال:**
```
المستخدم يزور: http://localhost:8000/about/
↓
Django يفحص urls.py: "ما الذي يتعامل مع /about/؟"
↓
يجد دالة العرض: about_view()
↓
دالة العرض تُرجع HTML
↓
المتصفح يعرض الصفحة
```

### ما هو العرض (View)؟

**العرض** هو دالة Python تقوم بـ:
1. استقبال طلب
2. القيام بشيء ما (جلب بيانات، معالجة نموذج، إلخ)
3. إرجاع استجابة (HTML، JSON، إعادة توجيه، إلخ)

**مثال بسيط:**

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")
```

### إنشاء أول عرض

**عدّل `core/views.py`:**

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django site!")

def about(request):
    return HttpResponse("This is the About page.")

def contact(request):
    return HttpResponse("Contact us at: contact@example.com")
```

**الشرح:**
- كل دالة تأخذ `request` كمعامل
- `HttpResponse` يرسل نصًا إلى المتصفح
- هذه عروض بسيطة (سنستخدم القوالب قريبًا)

### ربط العروض بعناوين URL

الآن نحتاج أن نخبر Django: "عندما يزور شخص ما /about/، استخدم عرض about."

#### الخطوة 1: إنشاء عناوين URL للتطبيق

**أنشئ ملفًا جديدًا: `core/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # localhost:8000/
    path('about/', views.about, name='about'),   # localhost:8000/about/
    path('contact/', views.contact, name='contact'),  # localhost:8000/contact/
]
```

**الشرح:**
- `path('', views.home)` يعني URL الجذر (/)
- `path('about/', views.about)` يعني /about/
- `name='home'` هو اسم URL (سنستخدمه لاحقًا)
- `. import views` يستورد العروض من نفس المجلد

#### الخطوة 2: ربط عناوين URL للتطبيق بعناوين المشروع

**عدّل `mysite/urls.py`:**

```python
from django.contrib import admin
from django.urls import path, include  # ← أضف include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # ← أضف هذا السطر
]
```

**الشرح:**
- `include('core.urls')` تعني "استخدم عناوين URL من تطبيق core"
- `path('', ...)` تعني أن هذه العناوين تبدأ من الجذر
- جميع عناوين URL من `core/urls.py` أصبحت متصلة الآن

### اختبار العروض

```bash
# شغّل الخادم
python manage.py runserver

# افتح المتصفح وزر:
# http://localhost:8000/          → يعرض "Welcome to my Django site!"
# http://localhost:8000/about/    → يعرض "This is the About page."
# http://localhost:8000/contact/  → يعرض "Contact us at: contact@example.com"
```

**تهانينا! لقد أنشأت عروضًا وعناوين URL تعمل!**

---

## 7. قوالب Django

### لماذا القوالب؟

حاليًا، نرجع نصًا عاديًا باستخدام `HttpResponse`.

**المشاكل:**
- لا هيكل HTML
- لا تنسيق
- صعبة الصيانة
- لا يمكن تضمين بيانات ديناميكية بسهولة

**الحل:** استخدام **القوالب** (ملفات HTML مع لغة قوالب Django).

### أساسيات لغة القوالب

قوالب Django تسمح لك بـ:
- عرض المتغيرات: `{{ variable_name }}`
- استخدام المنطق: `{% if condition %} ... {% endif %}`
- التكرار في القوائم: `{% for item in items %} ... {% endfor %}`
- تضمين قوالب أخرى: `{% include 'header.html' %}`
- توسيع القوالب الأساسية: `{% extends 'base.html' %}`

### إعداد القوالب

#### الخطوة 1: إنشاء مجلد القوالب

```bash
# في مجلد التطبيق (core/)، أنشئ مجلد templates
# ثم أنشئ مجلدًا باسم تطبيقك بداخله

mkdir core/templates
mkdir core/templates/core
```

**هيكل المجلدات:**
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

**لماذا المجلد المتداخل؟** Django يبحث في جميع التطبيقات عن القوالب. الهيكل المتداخل يمنع تعارض الأسماء.

#### الخطوة 2: إنشاء ملفات القوالب

**أنشئ `core/templates/core/home.html`:**

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

**أنشئ `core/templates/core/about.html`:**

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

**أنشئ `core/templates/core/contact.html`:**

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

#### الخطوة 3: تحديث العروض لاستخدام القوالب

**عدّل `core/views.py`:**

```python
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
```

**الشرح:**
- `render(request, 'template_name')` يحمّل ويرجع قالب HTML
- `'core/home.html'` يشير إلى `core/templates/core/home.html`
- Django يبحث تلقائيًا في مجلدات `templates`

### تمرير البيانات إلى القوالب

**حدّث `core/views.py`:**

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

**حدّث `core/templates/core/home.html`:**

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

**كيف يعمل:**
- `context` هو قاموس من المتغيرات
- `{{ variable_name }}` يعرض المتغير في القالب
- Django يستبدل `{{ title }}` بـ `'Welcome'`

### المنطق في القوالب

**مثال مع عبارة if:**

```python
# في views.py
def home(request):
    context = {
        'user_logged_in': True,
        'username': 'Ahmed'
    }
    return render(request, 'core/home.html', context)
```

```html
<!-- في home.html -->
{% if user_logged_in %}
    <p>Welcome back, {{ username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

**مثال مع حلقة for:**

```python
# في views.py
def home(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Orange', 'Grape']
    }
    return render(request, 'core/home.html', context)
```

```html
<!-- في home.html -->
<h2>Fruit List:</h2>
<ul>
    {% for fruit in fruits %}
        <li>{{ fruit }}</li>
    {% endfor %}
</ul>
```

---

## 8. وراثة القوالب

### المشكلة

لاحظ كيف أن جميع قوالبنا تحتوي على كود متكرر:
- نفس `<!DOCTYPE html>`، `<head>`، `<meta>`
- نفس روابط التنقل
- نفس الهيكل

**المشكلة:**
- الكثير من التكرار
- صعوبة الصيانة
- تغيير شيء واحد يتطلب تحديث جميع الملفات

**الحل:** وراثة القوالب مع `base.html`

### إنشاء قالب أساسي

**أنشئ `core/templates/core/base.html`:**

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
        <!-- محتوى الصفحة يوضع هنا -->
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2025 My Django Site. All rights reserved.</p>
    </footer>
</body>
</html>
```

**الأجزاء الرئيسية:**
- `{% block title %}...{% endblock %}`: عنصر نائب لعنوان الصفحة
- `{% block content %}...{% endblock %}`: عنصر نائب لمحتوى الصفحة
- كل شيء آخر يُشارك عبر جميع الصفحات

### استخدام القالب الأساسي

**حدّث `core/templates/core/home.html`:**

```html
{% extends 'core/base.html' %}

{% block title %}Home - My Django Site{% endblock %}

{% block content %}
    <h2>Welcome to My Django Site</h2>
    <p>This is the home page built with Django.</p>
    <p>Django makes web development easier and faster!</p>
{% endblock %}
```

**حدّث `core/templates/core/about.html`:**

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

**حدّث `core/templates/core/contact.html`:**

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

**كيف يعمل:**
- `{% extends 'core/base.html' %}` تعني "استخدم base.html كقالب"
- `{% block title %}...{% endblock %}` يستبدل كتلة العنوان في base.html
- `{% block content %}...{% endblock %}` يستبدل كتلة المحتوى
- كل شيء آخر يأتي من base.html

**الفوائد:**
- ✓ لا تكرار في الكود
- ✓ تغيير الرأس مرة واحدة يُحدّث في كل مكان
- ✓ تصميم متناسق عبر الصفحات
- ✓ سهولة الصيانة

---

## 9. الملفات الثابتة (CSS، الصور)

### ما هي الملفات الثابتة؟

**الملفات الثابتة** لا تتغير:
- أوراق أنماط CSS
- ملفات JavaScript
- الصور
- الخطوط
- الأيقونات

على عكس القوالب (التي يمكن أن تحتوي على بيانات ديناميكية)، الملفات الثابتة تُقدَّم كما هي.

### إعداد الملفات الثابتة

#### الخطوة 1: إنشاء مجلد الملفات الثابتة

```bash
# في مجلد التطبيق (core/)، أنشئ مجلد static
mkdir core/static
mkdir core/static/core
mkdir core/static/core/css
mkdir core/static/core/images
```

**هيكل المجلدات:**
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

#### الخطوة 2: إنشاء ملف CSS

**أنشئ `core/static/core/css/style.css`:**

```css
/* أنماط مخصصة لموقع Django */

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

#### الخطوة 3: تحميل الملفات الثابتة في القوالب

**حدّث `core/templates/core/base.html`:**

```html
{% load static %}  <!-- ← أضف هذا في أعلى الملف -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Site{% endblock %}</title>

    <!-- ربط CSS الخارجي -->
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
        <!-- محتوى الصفحة يوضع هنا -->
        {% endblock %}
    </div>

    <footer>
        <p>&copy; 2025 My Django Site. All rights reserved.</p>
    </footer>
</body>
</html>
```

**التغييرات الرئيسية:**
- `{% load static %}` في الأعلى يحمّل نظام الملفات الثابتة في Django
- `{% static 'core/css/style.css' %}` يولّد الرابط الصحيح لملف CSS
- احذف وسوم `<style>` المضمنة (الآن نستخدم CSS خارجي)

#### الخطوة 4: إضافة صورة (اختياري)

إذا كانت لديك صورة باسم `logo.png` في `core/static/core/images/`:

```html
<!-- في رأس base.html -->
<header>
    <img src="{% static 'core/images/logo.png' %}" alt="Logo" style="height: 50px;">
    <h1>My Django Website</h1>
</header>
```

### إعداد الملفات الثابتة في الإعدادات

Django مُعدّ بالفعل للتطوير، لكن تحقق:

**افحص `mysite/settings.py`:**

```python
# الملفات الثابتة (CSS, JavaScript, الصور)
STATIC_URL = 'static/'  # بادئة URL للملفات الثابتة

# للإنتاج، ستحتاج أيضًا:
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# (سنغطي هذا في الأسبوع 9)
```

### اختبار الملفات الثابتة

```bash
# شغّل الخادم
python manage.py runserver

# زر صفحاتك - يجب أن تظهر الآن بالأنماط الجديدة!
```

---

## 10. مشروع مصغّر: موقع Django من 3 صفحات

### متطلبات المشروع

ابنِ موقعًا بسيطًا من 3 صفحات:
- **صفحة الرئيسية**: رسالة ترحيب
- **صفحة حول**: معلومات عنك
- **صفحة التواصل**: معلومات الاتصال

**المتطلبات:**
- استخدام عروض وعناوين URL في Django
- استخدام وراثة القوالب (base.html)
- تضمين قائمة تنقل
- إضافة تنسيق CSS مخصص
- استخدام Git لتتبع التغييرات

### دليل خطوة بخطوة

#### الخطوة 1: خطط لموقعك

**الصفحات:**
1. الرئيسية (`/`)
2. حول (`/about/`)
3. تواصل (`/contact/`)

**التصميم:**
- رأس وتنقل متناسقان
- منطقة محتوى منسقة
- تذييل بحقوق النشر

#### الخطوة 2: إنشاء العروض

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

#### الخطوة 3: إعداد عناوين URL

**`core/urls.py`:**

```python
from django.urls import path
from . import views

app_name = 'core'  # مساحة اسمية لعناوين URL

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

#### الخطوة 4: إنشاء القالب الأساسي

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

**ملاحظة:** `{% url 'core:home' %}` تستخدم أسماء URL بدلاً من المسارات الثابتة. هذا أفضل ممارسة.

#### الخطوة 5: إنشاء قوالب الصفحات

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

#### الخطوة 6: إضافة تنسيق مخصص

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

#### الخطوة 7: اختبر موقعك

```bash
# شغّل خادم التطوير
python manage.py runserver

# زر كل صفحة:
# http://localhost:8000/         (الرئيسية)
# http://localhost:8000/about/   (حول)
# http://localhost:8000/contact/ (تواصل)
```

#### الخطوة 8: استخدم Git

```bash
# تهيئة Git (إذا لم يتم ذلك)
git init

# إنشاء .gitignore
echo "venv/
__pycache__/
*.pyc
db.sqlite3
.env" > .gitignore

# إضافة الملفات
git add .

# الحفظ (Commit)
git commit -m "Week 4: Complete Django 3-page website

- Created Django project and core app
- Implemented home, about, and contact views
- Used template inheritance with base.html
- Added custom CSS styling
- Configured static files"

# الرفع إلى GitHub (إذا كان لديك مستودع بعيد)
git push origin main
```

---

## ملخص

### ما تعلمته هذا الأسبوع

**أساسيات Django:**
- ✓ ما هو Django ولماذا نستخدمه
- ✓ تثبيت Django وإنشاء المشاريع
- ✓ فهم هيكل المشروع
- ✓ إنشاء وتسجيل التطبيقات

**عناوين URL والعروض:**
- ✓ كيف يوجّه Django عناوين URL
- ✓ إنشاء دوال العرض
- ✓ ربط عناوين URL بالعروض
- ✓ إرجاع استجابات HTTP

**القوالب:**
- ✓ إنشاء قوالب HTML
- ✓ تمرير البيانات إلى القوالب
- ✓ استخدام متغيرات ومنطق القوالب
- ✓ وراثة القوالب (extends، blocks)

**الملفات الثابتة:**
- ✓ إعداد الملفات الثابتة
- ✓ إنشاء ملفات CSS
- ✓ تحميل الملفات الثابتة في القوالب
- ✓ تنظيم الأصول الثابتة

### المفاهيم الرئيسية للتذكر

1. **نمط MTV**: Model-Template-View
2. **المشاريع مقابل التطبيقات**: المشاريع تحتوي على التطبيقات
3. **توجيه URL**: URLs → Views → Templates
4. **وراثة القوالب**: مبدأ DRY قيد التطبيق
5. **الملفات الثابتة**: CSS، JS، الصور، الخطوط

### معاينة الأسبوع القادم

**الأسبوع 5 - النماذج، ORM، الترحيلات والإدارة:**
- إنشاء نماذج قاعدة البيانات
- استخدام Django ORM للاستعلام عن البيانات
- إعداد واجهة إدارة Django
- بناء مدونة بمحتوى مدعوم بقاعدة البيانات

### اقتراحات للتمرين

1. **وسّع موقعك**: أضف المزيد من الصفحات (خدمات، معرض أعمال، قائمة مدونة)
2. **حسّن التنسيق**: اجعله متجاوبًا، أضف حركات
3. **جرّب**: جرّب تخطيطات قوالب مختلفة
4. **خصّص**: أضف صورك ومحتواك الخاص
5. **استكشف**: اطلع على توثيق Django

---

## حل المشاكل الشائعة

### المشكلة 1: "ModuleNotFoundError: No module named 'django'"

**الحل:**
```bash
# تأكد من تفعيل البيئة الافتراضية
# يجب أن ترى (venv) في الطرفية

# إذا لم تكن مفعّلة:
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# ثم ثبّت Django:
pip install django
```

### المشكلة 2: "TemplateDoesNotExist at /"

**الحل:**
- تحقق أن `core` موجود في `INSTALLED_APPS` في settings.py
- تحقق من مسار القالب: `core/templates/core/template_name.html`
- تأكد من صحة هيكل المجلدات

### المشكلة 3: الملفات الثابتة لا تُحمَّل

**الحل:**
- أضف `{% load static %}` في أعلى القالب
- افحص `STATIC_URL` في settings.py
- تحقق من هيكل مجلد الملفات الثابتة: `core/static/core/css/style.css`
- حدّث المتصفح بالكامل (Ctrl+F5)

### المشكلة 4: "Page not found (404)"

**الحل:**
- افحص `urls.py` في كل من المشروع والتطبيق
- تأكد أن `include('core.urls')` موجود في urls.py الخاص بالمشروع
- تحقق أن نمط URL يطابق ما تكتبه

### المشكلة 5: الخادم لا يبدأ

**الحل:**
```bash
# المنفذ مستخدم بالفعل
# أوقف العمليات الأخرى أو استخدم منفذًا مختلفًا:
python manage.py runserver 8001

# أو ابحث عن العملية التي تستخدم المنفذ 8000 وأنهِها
```

---

## موارد إضافية

**التوثيق الرسمي:**
- دليل Django التعليمي: https://docs.djangoproject.com/en/stable/intro/tutorial01/
- قوالب Django: https://docs.djangoproject.com/en/stable/topics/templates/
- الملفات الثابتة في Django: https://docs.djangoproject.com/en/stable/howto/static-files/

**دروس فيديو:**
- سلسلة Django لـ Corey Schafer (YouTube)
- Django for Beginners (William Vincent)

**مواقع للتمرين:**
- دليل Django Girls التعليمي: https://tutorial.djangogirls.org/

---

**تهانينا على إكمال الأسبوع الرابع! أنت الآن تعرف كيف تبني مواقع ويب ديناميكية باستخدام Django. استمر في التمرين والبناء!**
