# دروس الأسبوع الخامس – النماذج، ORM، التهجيرات وواجهة الإدارة

مرحبًا بك في الأسبوع الخامس! هذا الأسبوع نتعمق في **طبقة البيانات** في Django. ستتعلم كيفية تعريف نماذج قواعد البيانات، وتنفيذ عمليات CRUD باستخدام Django ORM، وإدارة البيانات عبر واجهة الإدارة القوية في Django.

---

## جدول المحتويات

1. [مقدمة لقواعد البيانات في Django](#1-مقدمة-لقواعد-البيانات-في-django)
2. [نماذج Django](#2-نماذج-django)
3. [أنواع الحقول](#3-أنواع-الحقول)
4. [التهجيرات](#4-التهجيرات)
5. [أساسيات Django ORM](#5-أساسيات-django-orm)
6. [عمليات CRUD](#6-عمليات-crud)
7. [واجهة إدارة Django](#7-واجهة-إدارة-django)
8. [تخصيص الإدارة](#8-تخصيص-الإدارة)
9. [Django Shell](#9-django-shell)
10. [مشروع مصغّر: مدونة بسيطة مع قاعدة بيانات](#10-مشروع-مصغّر)

---

## 1. مقدمة لقواعد البيانات في Django

### ما هي قاعدة البيانات؟

**قاعدة البيانات** هي مجموعة منظّمة من البيانات المهيكلة المخزّنة إلكترونيًا.

**تشبيه من الواقع:**
- فكّر في قاعدة البيانات كـ**خزانة ملفات**
- كل **درج** هو جدول
- كل **مجلد** هو صف/سجل
- كل **حقل في الوثيقة** هو عمود

### لماذا نحتاج إلى قواعد البيانات؟

**بدون قاعدة بيانات:**
```python
# البيانات مخزّنة في متغيرات (تُفقد عند إيقاف البرنامج)
posts = [
    {"title": "First Post", "content": "Hello World"},
    {"title": "Second Post", "content": "More content"}
]
```

**المشكلات:**
- تختفي البيانات عند إعادة تشغيل الخادم
- لا يمكن التعامل مع كميات كبيرة من البيانات
- لا توجد طريقة سهلة للبحث أو التصفية
- يتسبب المستخدمون المتعددون في تعارضات

**مع قاعدة بيانات:**
- تُحفظ البيانات بشكل دائم
- التعامل مع ملايين السجلات
- بحث وتصفية سريعان
- دعم مستخدمين متعددين في آنٍ واحد

### SQLite في Django

يأتي Django مع **SQLite** كإعداد افتراضي:
- **خفيفة الوزن**: لا يلزم خادم منفصل
- **قائمة على ملف**: قاعدة البيانات ملف واحد (`db.sqlite3`)
- **مثالية للتطوير**: سهلة البدء
- **بدائل للإنتاج**: PostgreSQL، MySQL

**الموقع الافتراضي لقاعدة البيانات:**
```
myproject/
├── db.sqlite3  ← ملف قاعدة البيانات
├── manage.py
└── myapp/
```

### SQL مقابل ORM

**SQL (لغة الاستعلام الهيكلية):**
```sql
SELECT * FROM posts WHERE published = TRUE;
```

**Django ORM (ربط الكائنات بالعلاقات):**
```python
Post.objects.filter(published=True)
```

**فوائد ORM:**
- اكتب Python بدلًا من SQL
- مستقل عن قاعدة البيانات (التبديل بسهولة)
- حماية من SQL injection
- أكثر قابلية للقراءة والصيانة

---

## 2. نماذج Django

### ما هو النموذج؟

**النموذج** هو كلاس Python يمثّل جدول قاعدة بيانات.

**النموذج = مخطط البيانات**

```python
# هذا الكلاس Python...
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

**...يُنشئ هذا الجدول في قاعدة البيانات:**
```
جدول posts:
┌────┬──────────────┬────────────────┬─────────────────────┐
│ id │    title     │    content     │     created_at      │
├────┼──────────────┼────────────────┼─────────────────────┤
│ 1  │ First Post   │ Hello World!   │ 2024-01-15 10:30:00 │
│ 2  │ Second Post  │ More content   │ 2024-01-15 11:45:00 │
└────┴──────────────┴────────────────┴─────────────────────┘
```

### إنشاء أول نموذج

**الخطوة 1: تعريف النموذج في `models.py`**

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

**الخطوة 2: تشغيل التهجيرات (سنغطي هذا قريبًا!)**

```bash
python manage.py makemigrations
python manage.py migrate
```

### أفضل ممارسات النماذج

**1. أضف دائمًا دالة `__str__()`:**
```python
def __str__(self):
    return self.title  # يعرض نصًا ذا معنى بدلًا من "Post object (1)"
```

**2. استخدم أسماء حقول وصفية:**
```python
# جيد
published_date = models.DateTimeField()

# سيئ
pd = models.DateTimeField()
```

**3. أضف related_name للعلاقات:**
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
```

---

## 3. أنواع الحقول

يوفّر Django أنواعًا كثيرة من الحقول لمختلف أنواع البيانات.

### حقول النصوص

#### CharField
للنصوص القصيرة (يتطلب `max_length`):
```python
title = models.CharField(max_length=200)
first_name = models.CharField(max_length=50)
```

**يُستخدم لـ:** العناوين، الأسماء، الأوصاف القصيرة

#### TextField
للنصوص الطويلة (بدون حد للطول):
```python
content = models.TextField()
bio = models.TextField()
```

**يُستخدم لـ:** المقالات، الأوصاف، المحتوى الطويل

#### EmailField
يتحقق من صحة عناوين البريد الإلكتروني:
```python
email = models.EmailField()
```

**يُستخدم لـ:** عناوين البريد الإلكتروني

#### URLField
يتحقق من صحة الروابط:
```python
website = models.URLField()
```

**يُستخدم لـ:** روابط المواقع

### حقول الأرقام

#### IntegerField
الأعداد الصحيحة:
```python
age = models.IntegerField()
count = models.IntegerField(default=0)
```

#### DecimalField
أرقام عشرية دقيقة (للأموال):
```python
price = models.DecimalField(max_digits=10, decimal_places=2)
# مثال: 12345678.99
```

#### FloatField
أرقام الفاصلة العائمة:
```python
rating = models.FloatField()
```

### حقول المنطق

#### BooleanField
قيم صح/خطأ:
```python
is_published = models.BooleanField(default=False)
is_active = models.BooleanField(default=True)
```

### حقول التاريخ والوقت

#### DateField
تخزين التواريخ فقط:
```python
birth_date = models.DateField()
```

#### DateTimeField
تخزين التاريخ والوقت معًا:
```python
created_at = models.DateTimeField(auto_now_add=True)  # يُضبط مرة عند الإنشاء
updated_at = models.DateTimeField(auto_now=True)      # يُحدَّث عند كل حفظ
```

**المعاملات المهمة:**
- `auto_now_add=True`: يُضبط عند إنشاء الكائن (لا يتغير)
- `auto_now=True`: يُحدَّث في كل مرة يُحفظ فيها الكائن

### حقول العلاقات

#### ForeignKey
علاقة كثير-إلى-واحد:
```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # تعليقات كثيرة تنتمي لمنشور واحد
```

**خيارات `on_delete`:**
- `models.CASCADE`: حذف التعليقات عند حذف المنشور
- `models.PROTECT`: منع حذف المنشور إذا وُجدت تعليقات
- `models.SET_NULL`: تعيين NULL عند حذف المنشور (يتطلب `null=True`)

#### ManyToManyField
علاقة كثير-إلى-كثير:
```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')
    # طلاب كثيرون يمكنهم التسجيل في دورات كثيرة
```

### خيارات الحقول

المعاملات الشائعة لجميع الحقول:

```python
# مطلوب مقابل اختياري
name = models.CharField(max_length=100)                    # مطلوب
middle_name = models.CharField(max_length=100, blank=True)  # اختياري في النماذج

# NULL في قاعدة البيانات
description = models.TextField(null=True, blank=True)      # يمكن أن يكون NULL في قاعدة البيانات

# قيم افتراضية
status = models.CharField(max_length=20, default='draft')

# قيم فريدة
email = models.EmailField(unique=True)  # لا يُسمح بالتكرار

# الاختيارات
STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]
status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
```

**فرق مهم:**
- `blank=True`: يسمح بالقيم الفارغة في النماذج (التحقق من الصحة)
- `null=True`: يسمح بـ NULL في قاعدة البيانات (التخزين)

### مثال كامل

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
        ordering = ['-created_at']  # الأحدث أولًا
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title
```

---

## 4. التهجيرات

### ما هي التهجيرات؟

**التهجيرات** هي طريقة Django لنقل التغييرات التي تُجريها على النماذج إلى مخطط قاعدة البيانات.

**فكّر في التهجيرات كنظام التحكم في الإصدارات لقاعدة بياناتك.**

### سير عمل التهجير

```
1. إنشاء/تعديل النموذج → 2. إنشاء التهجير → 3. تطبيق التهجير → 4. تحديث قاعدة البيانات
   (models.py)              (makemigrations)     (migrate)           (db.sqlite3)
```

### إنشاء التهجيرات

**الأمر:**
```bash
python manage.py makemigrations
```

**ما يفعله:**
- يفحص النماذج بحثًا عن تغييرات
- يُنشئ ملفات التهجير في مجلد `migrations/`
- لا يُغيّر قاعدة البيانات بعد

**مثال على المخرجات:**
```
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

### تطبيق التهجيرات

**الأمر:**
```bash
python manage.py migrate
```

**ما يفعله:**
- ينفّذ جميع التهجيرات المعلّقة
- يُحدّث مخطط قاعدة البيانات
- يُنشئ/يُعدّل الجداول

**مثال على المخرجات:**
```
Running migrations:
  Applying blog.0001_initial... OK
```

### ملفات التهجير

تُخزَّن التهجيرات في `app/migrations/`:
```
blog/
└── migrations/
    ├── __init__.py
    ├── 0001_initial.py      ← التهجير الأول
    ├── 0002_post_author.py  ← إضافة حقل المؤلف
    └── 0003_auto_20240115.py
```

**مثال على ملف تهجير:**
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

### أوامر التهجير الشائعة

```bash
# التحقق من تغييرات النموذج دون إنشاء تهجيرات
python manage.py makemigrations --dry-run

# عرض حالة التهجيرات
python manage.py showmigrations

# عرض SQL للتهجير (دون تشغيله)
python manage.py sqlmigrate blog 0001

# التراجع عن آخر تهجير
python manage.py migrate blog 0001
```

### أفضل ممارسات التهجير

1. **أنشئ التهجيرات دائمًا بعد تغييرات النموذج**
2. **أضف التهجيرات إلى نظام التحكم في الإصدارات (Git)**
3. **لا تُعدّل التهجيرات المُطبَّقة** (أنشئ واحدًا جديدًا بدلًا من ذلك)
4. **شغّل التهجيرات في جميع البيئات** (التطوير، الاختبار، الإنتاج)

### مشكلات التهجير الشائعة

**المشكلة: "No changes detected"**
```bash
# الحل: تأكد من أن التطبيق موجود في INSTALLED_APPS
# settings.py
INSTALLED_APPS = [
    'blog',  # أضف تطبيقك هنا
]
```

**المشكلة: تعارض التهجيرات**
```bash
# الحل: دمج التهجيرات
python manage.py makemigrations --merge
```

---

## 5. أساسيات Django ORM

### ما هو ORM؟

**ORM (ربط الكائنات بالعلاقات)** يسمح لك بالتفاعل مع قاعدة البيانات باستخدام كائنات Python بدلًا من SQL.

**بدون ORM (SQL):**
```sql
SELECT * FROM blog_post WHERE status = 'published';
```

**مع ORM (Python):**
```python
Post.objects.filter(status='published')
```

### مجموعات الاستعلام (QuerySets)

**QuerySet** هي مجموعة من استعلامات قاعدة البيانات.

```python
# الحصول على جميع المنشورات
posts = Post.objects.all()  # يُرجع QuerySet

# QuerySets كسولة (الاستعلام لم يُنفَّذ بعد)
posts = Post.objects.all()  # لا يوجد وصول لقاعدة البيانات

# يُنفَّذ الاستعلام عند التكرار
for post in posts:          # يحدث الوصول لقاعدة البيانات هنا
    print(post.title)
```

### المدير objects

كل نموذج لديه مدير `objects`:

```python
Post.objects  # مدير نموذج Post
```

**الأساليب الشائعة:**
- `all()` - الحصول على جميع السجلات
- `filter()` - الحصول على السجلات المطابقة للشروط
- `get()` - الحصول على سجل واحد
- `create()` - إنشاء سجل جديد
- `update()` - تحديث السجلات
- `delete()` - حذف السجلات

---

## 6. عمليات CRUD

### Create – إضافة البيانات

**الطريقة 1: الإنشاء والحفظ**
```python
post = Post(title="My First Post", content="Hello World!")
post.save()
```

**الطريقة 2: استخدام create()**
```python
post = Post.objects.create(
    title="My First Post",
    content="Hello World!"
)
```

**الطريقة 3: الإنشاء المجمّع**
```python
Post.objects.bulk_create([
    Post(title="Post 1", content="Content 1"),
    Post(title="Post 2", content="Content 2"),
    Post(title="Post 3", content="Content 3"),
])
```

### Read – استرجاع البيانات

**الحصول على جميع السجلات:**
```python
posts = Post.objects.all()
```

**تصفية السجلات:**
```python
# شرط واحد
published_posts = Post.objects.filter(status='published')

# شروط متعددة (AND)
recent_published = Post.objects.filter(status='published', is_featured=True)

# شروط OR
from django.db.models import Q
posts = Post.objects.filter(Q(status='published') | Q(is_featured=True))

# استبعاد السجلات (NOT)
not_drafts = Post.objects.exclude(status='draft')
```

**الحصول على سجل واحد:**
```python
# الحصول بالمعرّف
post = Post.objects.get(id=1)

# الحصول بحقل فريد
post = Post.objects.get(slug='my-first-post')

# انتبه: get() يرفع استثناءً إذا لم يُوجد أو وُجد أكثر من واحد
```

**الترتيب:**
```python
# تصاعدي
posts = Post.objects.order_by('created_at')

# تنازلي
posts = Post.objects.order_by('-created_at')

# حقول متعددة
posts = Post.objects.order_by('-is_featured', '-created_at')
```

**تحديد النتائج:**
```python
# أول 5 منشورات
posts = Post.objects.all()[:5]

# المنشورات 5-10 (للصفحات)
posts = Post.objects.all()[5:10]

# أول منشور
first_post = Post.objects.first()

# آخر منشور
last_post = Post.objects.last()
```

**العدّ:**
```python
total = Post.objects.count()
published_count = Post.objects.filter(status='published').count()
```

**التحقق من الوجود:**
```python
has_posts = Post.objects.filter(status='published').exists()
```

### Update – تعديل البيانات

**الطريقة 1: حفظ الكائن الموجود**
```python
post = Post.objects.get(id=1)
post.title = "Updated Title"
post.save()
```

**الطريقة 2: تحديث QuerySet (أكثر كفاءة)**
```python
# تحديث حقل واحد
Post.objects.filter(status='draft').update(status='published')

# تحديث حقول متعددة
Post.objects.filter(id=1).update(
    title="New Title",
    content="New Content"
)
```

**الطريقة 3: التحديث أو الإنشاء**
```python
post, created = Post.objects.update_or_create(
    slug='my-post',
    defaults={'title': 'My Post', 'content': 'Content'}
)
```

### Delete – حذف البيانات

**حذف كائن واحد:**
```python
post = Post.objects.get(id=1)
post.delete()
```

**حذف كائنات متعددة:**
```python
# حذف جميع المسودات
Post.objects.filter(status='draft').delete()

# حذف جميع المنشورات (كن حذرًا!)
Post.objects.all().delete()
```

### تسلسل أساليب QuerySet

```python
# فلاتر متعددة
posts = Post.objects.filter(status='published')\
                    .filter(is_featured=True)\
                    .order_by('-created_at')[:5]

# ما يعادله في SQL:
SELECT * FROM blog_post
WHERE status = 'published' AND is_featured = TRUE
ORDER BY created_at DESC
LIMIT 5;
```

---

## 7. واجهة إدارة Django

### ما هي واجهة إدارة Django؟

واجهة إدارة Django هي **واجهة ويب مدمجة** لإدارة بياناتك.

**الميزات:**
- واجهة CRUD تلقائية
- مصادقة المستخدمين
- البحث والتصفية
- التحقق من صحة البيانات
- قابلة للتخصيص

**الوصول:** `http://localhost:8000/admin/`

### إنشاء مستخدم خارق (Superuser)

**الأمر:**
```bash
python manage.py createsuperuser
```

**سيُطلب منك:**
- اسم المستخدم
- البريد الإلكتروني
- كلمة المرور

**مثال:**
```bash
Username: admin
Email: admin@example.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### تسجيل النماذج

**لإدارة النماذج في الإدارة، سجّلها:**

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

**الآن يظهر `Post` في واجهة الإدارة!**

### الاستخدام الأساسي للإدارة

1. تشغيل الخادم: `python manage.py runserver`
2. زيارة: `http://localhost:8000/admin/`
3. تسجيل الدخول ببيانات المستخدم الخارق
4. النقر على اسم النموذج (مثلًا "Posts")
5. إضافة/تعديل/حذف السجلات

---

## 8. تخصيص الإدارة

### كلاس ModelAdmin

تخصيص كيفية ظهور النماذج في الإدارة:

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

### التخصيصات الشائعة

#### list_display
الحقول التي تظهر في عرض القائمة:
```python
list_display = ('title', 'author', 'status', 'created_at')
```

#### list_filter
إضافة شريط التصفية الجانبي:
```python
list_filter = ('status', 'is_featured', 'created_at')
```

#### search_fields
تفعيل البحث:
```python
search_fields = ('title', 'content', 'author__username')
```

#### prepopulated_fields
ملء الحقول تلقائيًا (مفيد لـ slugs):
```python
prepopulated_fields = {'slug': ('title',)}
```

#### readonly_fields
جعل الحقول للقراءة فقط:
```python
readonly_fields = ('created_at', 'updated_at', 'views')
```

#### fieldsets
تنظيم الحقول في أقسام:
```python
fieldsets = (
    ('المعلومات الأساسية', {
        'fields': ('title', 'slug', 'author')
    }),
    ('المحتوى', {
        'fields': ('content', 'excerpt')
    }),
    ('الإعدادات', {
        'fields': ('status', 'is_featured', 'featured_image')
    }),
)
```

### أساليب الإدارة المخصصة

عرض أعمدة مخصصة:

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'word_count', 'created_at')

    @admin.display(description='عدد الكلمات')
    def word_count(self, obj):
        return len(obj.content.split())
```

---

## 9. Django Shell

### ما هو Django Shell؟

صدفة Python تفاعلية مع تحميل بيئة Django.

**تشغيل الصدفة:**
```bash
python manage.py shell
```

### استخدام الصدفة

```python
# استيراد النموذج
>>> from blog.models import Post

# إنشاء منشور
>>> post = Post.objects.create(title="Test", content="Testing")

# الحصول على جميع المنشورات
>>> Post.objects.all()
<QuerySet [<Post: Test>]>

# تصفية المنشورات
>>> Post.objects.filter(status='published')

# الحصول على منشور واحد
>>> post = Post.objects.get(id=1)
>>> post.title
'Test'

# تحديث منشور
>>> post.title = "Updated"
>>> post.save()

# حذف منشور
>>> post.delete()

# عدّ المنشورات
>>> Post.objects.count()
5

# الخروج من الصدفة
>>> exit()
```

### أفضل ممارسات الصدفة

**استخدم الصدفة لـ:**
- اختبار الاستعلامات قبل كتابة العروض
- تصحيح مشكلات البيانات
- عمليات البيانات لمرة واحدة
- تعلّم ORM

**لا تستخدم الصدفة لـ:**
- إدخال البيانات المنتظم (استخدم واجهة الإدارة)
- تغييرات بيانات الإنتاج (اكتب سكريبتات بدلًا من ذلك)

---

## 10. مشروع مصغّر: مدونة بسيطة مع قاعدة بيانات

### أهداف المشروع

بناء تطبيق مدونة يحتوي على:
- نموذج Post (العنوان، المحتوى، تاريخ الإنشاء)
- صفحة لعرض جميع المنشورات
- صفحة تفاصيل المنشور
- واجهة إدارة لإدارة المنشورات

### الخطوة 1: إنشاء تطبيق المدونة

```bash
python manage.py startapp blog
```

**إضافته إلى الإعدادات:**
```python
# settings.py
INSTALLED_APPS = [
    # ...
    'blog',
]
```

### الخطوة 2: إنشاء نموذج Post

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

### الخطوة 3: إنشاء التهجيرات وتطبيقها

```bash
python manage.py makemigrations
python manage.py migrate
```

### الخطوة 4: التسجيل في الإدارة

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

### الخطوة 5: إنشاء العروض

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

### الخطوة 6: إعداد عناوين URL

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

### الخطوة 7: إنشاء القوالب

```html
<!-- blog/templates/blog/post_list.html -->
<!DOCTYPE html>
<html>
<head>
    <title>منشورات المدونة</title>
</head>
<body>
    <h1>جميع منشورات المدونة</h1>
    {% for post in posts %}
        <article>
            <h2>
                <a href="{% url 'blog:post_detail' post.id %}">{{ post.title }}</a>
            </h2>
            <p>تاريخ النشر: {{ post.created_at|date:"F j, Y" }}</p>
            <p>{{ post.content|truncatewords:30 }}</p>
        </article>
        <hr>
    {% empty %}
        <p>لا توجد منشورات بعد.</p>
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
        <p>تاريخ النشر: {{ post.created_at|date:"F j, Y" }}</p>
        <div>
            {{ post.content|linebreaks }}
        </div>
    </article>
    <a href="{% url 'blog:post_list' %}">← العودة إلى جميع المنشورات</a>
</body>
</html>
```

### الخطوة 8: اختبار كل شيء

1. إنشاء مستخدم خارق: `python manage.py createsuperuser`
2. تشغيل الخادم: `python manage.py runserver`
3. إضافة منشورات عبر الإدارة: `http://localhost:8000/admin/`
4. عرض المدونة: `http://localhost:8000/blog/`
5. النقر على منشور لرؤية التفاصيل

### الخطوة 9: استخدام Django Shell

```bash
python manage.py shell
```

```python
# اختبار استعلامات ORM
from blog.models import Post

# إنشاء منشور
Post.objects.create(title="Shell Post", content="Created from shell!")

# الحصول على جميع المنشورات
Post.objects.all()

# تصفية المنشورات
Post.objects.filter(title__contains="Shell")

# عدّ المنشورات
Post.objects.count()
```

---

## الملخص

هذا الأسبوع تعلّمت:

1. **قواعد البيانات**: لماذا نحتاجها وكيف يستخدم Django SQLite
2. **النماذج**: تعريف هيكل البيانات باستخدام كلاسات Python
3. **أنواع الحقول**: CharField، TextField، DateTimeField، ForeignKey، إلخ
4. **التهجيرات**: التحكم في الإصدارات لمخطط قاعدة البيانات
5. **ORM**: الاستعلام عن قاعدة البيانات باستخدام Python (عمليات CRUD)
6. **واجهة الإدارة**: أداة مدمجة لإدارة البيانات
7. **Django Shell**: بيئة اختبار تفاعلية

### الأوامر الرئيسية

```bash
# التهجيرات
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations

# الإدارة
python manage.py createsuperuser

# الصدفة
python manage.py shell
```

### معاينة الأسبوع القادم

الأسبوع السادس سيتناول:
- نماذج Django
- التحقق من صحة النماذج
- مصادقة المستخدمين (تسجيل الدخول/الخروج)
- العروض المستندة إلى الكلاسات
- إطار الرسائل

---

## موارد إضافية

- [توثيق نماذج Django](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [واجهة برمجة QuerySet في Django](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [توثيق إدارة Django](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [مرجع حقول قاعدة البيانات](https://docs.djangoproject.com/en/stable/ref/models/fields/)
