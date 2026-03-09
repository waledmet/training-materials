# تمارين الأسبوع الخامس – ممارسة النماذج، ORM، التهجيرات وواجهة الإدارة

تمارين عملية للأسبوع الخامس: إنشاء النماذج، تنفيذ عمليات CRUD، استخدام واجهة إدارة Django، والعمل مع ORM.

---

## جدول المحتويات

1. [اليوم 1: النماذج والتهجيرات](#اليوم-1-النماذج-والتهجيرات)
2. [اليوم 2: عمليات CRUD و ORM](#اليوم-2-عمليات-crud-و-orm)
3. [اليوم 3: تخصيص واجهة الإدارة](#اليوم-3-تخصيص-واجهة-الإدارة)
4. [اليوم 4: العلاقات والاستعلامات المتقدمة](#اليوم-4-العلاقات-والاستعلامات-المتقدمة)
5. [اليوم 5: مشروع المدونة الكامل](#اليوم-5-مشروع-المدونة-الكامل)
6. [تمارين التحدي](#تمارين-التحدي)

---

## اليوم 1: النماذج والتهجيرات

### التمرين 1: إنشاء أول نموذج

**المهمة:**
1. أنشئ مشروع Django باسم `library`
2. أنشئ تطبيقًا باسم `books`
3. أنشئ نموذج `Book` بهذه الحقول:
   - `title` (CharField, max_length=200)
   - `author` (CharField, max_length=100)
   - `published_date` (DateField)
   - `isbn` (CharField, max_length=13, unique=True)
   - `pages` (IntegerField)
4. أضف دالة `__str__()` تُرجع عنوان الكتاب

<details>
<summary>الحل</summary>

```bash
# إنشاء المشروع والتطبيق
django-admin startproject library
cd library
python manage.py startapp books
```

```python
# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()

    def __str__(self):
        return self.title
```

```python
# library/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'books',  # أضف هذا
]
```
</details>

---

### التمرين 2: إنشاء التهجيرات وتطبيقها

**المهمة:**
1. أنشئ تهجيرات لنموذج `Book`
2. طبّق التهجيرات
3. تحقق من حالة التهجيرات

**الأوامر:**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

<details>
<summary>المخرجات المتوقعة</summary>

```bash
# مخرجات makemigrations
Migrations for 'books':
  books/migrations/0001_initial.py
    - Create model Book

# مخرجات migrate
Running migrations:
  Applying books.0001_initial... OK

# مخرجات showmigrations
books
 [X] 0001_initial
```
</details>

---

### التمرين 3: إضافة حقول إلى نموذج موجود

**المهمة:**
1. أضف هذه الحقول الجديدة إلى نموذج `Book`:
   - `description` (TextField, blank=True)
   - `cover_image` (URLField, blank=True)
   - `is_available` (BooleanField, default=True)
2. أنشئ التهجيرات وطبّقها

<details>
<summary>الحل</summary>

```python
# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    description = models.TextField(blank=True)
    cover_image = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
```

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

---

### التمرين 4: إنشاء نموذج Student

**المهمة:**
أنشئ نموذج `Student` بـ:
- `first_name` (CharField, max_length=50)
- `last_name` (CharField, max_length=50)
- `email` (EmailField, unique=True)
- `enrollment_date` (DateField)
- `grade` (DecimalField, max_digits=4, decimal_places=2)
- `is_active` (BooleanField, default=True)

أضف دالة `__str__()` تُرجع "الاسم الأول الاسم الأخير".

<details>
<summary>الحل</summary>

```python
# books/models.py (أضف إلى الملف الموجود)
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

---

### التمرين 5: نموذج مع الاختيارات

**المهمة:**
أنشئ نموذج `Task` بـ:
- `title` (CharField, max_length=200)
- `description` (TextField)
- `status` مع خيارات: 'pending'، 'in_progress'، 'completed'
- `priority` مع خيارات: 'low'، 'medium'، 'high'
- `due_date` (DateField)
- `created_at` (DateTimeField, auto_now_add=True)

<details>
<summary>الحل</summary>

```python
# books/models.py (أضف إلى الملف الموجود)
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

---

## اليوم 2: عمليات CRUD و ORM

### التمرين 6: إنشاء سجلات باستخدام الصدفة

**المهمة:**
استخدم Django shell لإنشاء 3 كتب:

1. "The Great Gatsby" بقلم F. Scott Fitzgerald، نُشر في 1925-04-10، ISBN: 9780743273565، 180 صفحة
2. "To Kill a Mockingbird" بقلم Harper Lee، نُشر في 1960-07-11، ISBN: 9780061120084، 324 صفحة
3. "1984" بقلم George Orwell، نُشر في 1949-06-08، ISBN: 9780451524935، 328 صفحة

<details>
<summary>الحل</summary>

```bash
python manage.py shell
```

```python
from books.models import Book
from datetime import date

# الطريقة 1: الإنشاء والحفظ
book1 = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    published_date=date(1925, 4, 10),
    isbn="9780743273565",
    pages=180
)
book1.save()

# الطريقة 2: استخدام create()
Book.objects.create(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    published_date=date(1960, 7, 11),
    isbn="9780061120084",
    pages=324
)

Book.objects.create(
    title="1984",
    author="George Orwell",
    published_date=date(1949, 6, 8),
    isbn="9780451524935",
    pages=328
)

# التحقق
Book.objects.all()
```
</details>

---

### التمرين 7: قراءة السجلات

**المهمة:**
باستخدام Django shell:
1. احصل على جميع الكتب
2. احصل على كتب F. Scott Fitzgerald
3. احصل على الكتاب برقم ISBN "9780451524935"
4. احصل على الكتب التي تزيد عن 300 صفحة
5. احسب إجمالي عدد الكتب

<details>
<summary>الحل</summary>

```python
from books.models import Book

# 1. الحصول على جميع الكتب
all_books = Book.objects.all()
print(all_books)

# 2. الحصول على كتب F. Scott Fitzgerald
fitzgerald_books = Book.objects.filter(author="F. Scott Fitzgerald")
print(fitzgerald_books)

# 3. الحصول على كتاب برقم ISBN
book = Book.objects.get(isbn="9780451524935")
print(book.title)

# 4. الكتب التي تزيد عن 300 صفحة
long_books = Book.objects.filter(pages__gt=300)
print(long_books)

# 5. إجمالي عدد الكتب
total = Book.objects.count()
print(f"إجمالي الكتب: {total}")
```
</details>

---

### التمرين 8: تحديث السجلات

**المهمة:**
1. غيّر عنوان "1984" إلى "Nineteen Eighty-Four"
2. اجعل جميع الكتب غير متاحة (is_available=False)
3. حدّث وصف "The Great Gatsby"

<details>
<summary>الحل</summary>

```python
from books.models import Book

# 1. تحديث كتاب واحد
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# 2. تحديث كتب متعددة
Book.objects.all().update(is_available=False)

# 3. التحديث باستخدام filter
Book.objects.filter(title="The Great Gatsby").update(
    description="رواية تدور في عصر الجاز تحكي قصة سعي جاي جاتسبي للحلم الأمريكي."
)

# التحقق من التغييرات
print(Book.objects.get(isbn="9780451524935").title)
print(Book.objects.filter(is_available=True).count())  # يجب أن يكون 0
```
</details>

---

### التمرين 9: حذف السجلات

**المهمة:**
1. احذف الكتاب برقم ISBN "9780743273565"
2. أنشئ كتابَين تجريبيَّين ثم احذف جميع كتب المؤلف "Test Author"

<details>
<summary>الحل</summary>

```python
from books.models import Book

# 1. حذف كتاب محدد
book = Book.objects.get(isbn="9780743273565")
book.delete()

# 2. إنشاء كتب تجريبية
Book.objects.create(
    title="Test Book 1",
    author="Test Author",
    published_date="2024-01-01",
    isbn="1111111111111",
    pages=100
)
Book.objects.create(
    title="Test Book 2",
    author="Test Author",
    published_date="2024-01-01",
    isbn="2222222222222",
    pages=150
)

# حذف جميع كتب Test Author
Book.objects.filter(author="Test Author").delete()

# التحقق
print(Book.objects.filter(author="Test Author").count())  # يجب أن يكون 0
```
</details>

---

### التمرين 10: استعلامات متقدمة

**المهمة:**
1. احصل على الكتب مرتبة بالصفحات (تصاعديًا)
2. احصل على الكتب مرتبة بتاريخ النشر (الأحدث أولًا)
3. احصل على أول كتابَين
4. تحقق مما إذا كان أي كتاب يزيد عن 400 صفحة
5. احصل على الكتب المنشورة بعد عام 1950

<details>
<summary>الحل</summary>

```python
from books.models import Book
from datetime import date

# 1. الترتيب بالصفحات
books_by_pages = Book.objects.order_by('pages')
print(books_by_pages)

# 2. الترتيب بالتاريخ (الأحدث أولًا)
newest_books = Book.objects.order_by('-published_date')
print(newest_books)

# 3. أول كتابَين
first_two = Book.objects.all()[:2]
print(first_two)

# 4. التحقق من وجود كتب > 400 صفحة
has_long_books = Book.objects.filter(pages__gt=400).exists()
print(f"توجد كتب > 400 صفحة: {has_long_books}")

# 5. الكتب المنشورة بعد 1950
modern_books = Book.objects.filter(published_date__gt=date(1950, 1, 1))
print(modern_books)
```
</details>

---

## اليوم 3: تخصيص واجهة الإدارة

### التمرين 11: إنشاء مستخدم خارق وتسجيل النموذج

**المهمة:**
1. أنشئ مستخدمًا خارقًا باسم "admin"، بريده "admin@example.com"
2. سجّل نموذج `Book` في الإدارة
3. سجّل دخولك إلى الإدارة وأضف كتابًا

<details>
<summary>الحل</summary>

```bash
# إنشاء مستخدم خارق
python manage.py createsuperuser
# اتبع التعليمات
```

```python
# books/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

```bash
# تشغيل الخادم والوصول للإدارة
python manage.py runserver
# زيارة http://localhost:8000/admin/
# تسجيل الدخول وإضافة كتاب
```
</details>

---

### التمرين 12: تخصيص عرض الإدارة

**المهمة:**
خصّص إدارة `Book` لعرض:
- عرض القائمة: title، author، pages، is_available
- التصفية: is_available، published_date
- حقول البحث: title، author، isbn

<details>
<summary>الحل</summary>

```python
# books/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'is_available')
    list_filter = ('is_available', 'published_date')
    search_fields = ('title', 'author', 'isbn')
```
</details>

---

### التمرين 13: تخصيص الإدارة المتقدم

**المهمة:**
أضف المزيد من التخصيصات إلى `BookAdmin`:
- حقول للقراءة فقط: published_date
- الترتيب: حسب العنوان
- التسلسل الزمني للتاريخ: published_date
- أضف طريقة مخصصة لعرض "قصير" أو "طويل" بناءً على عدد الصفحات

<details>
<summary>الحل</summary>

```python
# books/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'is_available', 'book_length')
    list_filter = ('is_available', 'published_date')
    search_fields = ('title', 'author', 'isbn')
    readonly_fields = ('published_date',)
    ordering = ('title',)
    date_hierarchy = 'published_date'

    @admin.display(description='الطول')
    def book_length(self, obj):
        return "طويل" if obj.pages > 300 else "قصير"
```
</details>

---

### التمرين 14: تسجيل نماذج متعددة

**المهمة:**
1. سجّل نموذج `Student` في الإدارة
2. خصّصه لعرض: first_name، last_name، email، is_active
3. أضف تصفية لـ is_active و enrollment_date

<details>
<summary>الحل</summary>

```python
# books/admin.py (أضف إلى الملف الموجود)
from .models import Book, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')
    list_filter = ('is_active', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email')
```
</details>

---

### التمرين 15: أقسام نموذج الإدارة (Fieldsets)

**المهمة:**
نظّم نموذج إدارة `Book` في أقسام:
- "المعلومات الأساسية": title، author، isbn
- "التفاصيل": published_date، pages، description
- "التوفر": is_available
- "الوسائط": cover_image

<details>
<summary>الحل</summary>

```python
# books/admin.py
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'is_available')
    list_filter = ('is_available', 'published_date')
    search_fields = ('title', 'author', 'isbn')

    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('التفاصيل', {
            'fields': ('published_date', 'pages', 'description')
        }),
        ('التوفر', {
            'fields': ('is_available',)
        }),
        ('الوسائط', {
            'fields': ('cover_image',)
        }),
    )
```
</details>

---

## اليوم 4: العلاقات والاستعلامات المتقدمة

### التمرين 16: إنشاء نماذج بعلاقة ForeignKey

**المهمة:**
أنشئ نموذجَين:
1. نموذج `Author`:
   - first_name، last_name (CharField)
   - bio (TextField)
   - birth_date (DateField)
2. حدّث نموذج `Book` ليستخدم ForeignKey إلى `Author` بدلًا من CharField

<details>
<summary>الحل</summary>

```python
# books/models.py
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    description = models.TextField(blank=True)
    cover_image = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
```

```bash
python manage.py makemigrations
python manage.py migrate
```
</details>

---

### التمرين 17: الاستعلام عبر العلاقات

**المهمة:**
1. أنشئ مؤلفًا وكتابَين لذلك المؤلف
2. احصل على جميع كتب مؤلف محدد
3. احصل على مؤلف كتاب محدد
4. احسب عدد كتب كل مؤلف

<details>
<summary>الحل</summary>

```python
from books.models import Author, Book
from datetime import date

# 1. إنشاء مؤلف وكتب
author = Author.objects.create(
    first_name="Jane",
    last_name="Austen",
    bio="روائية إنجليزية",
    birth_date=date(1775, 12, 16)
)

Book.objects.create(
    title="Pride and Prejudice",
    author=author,
    published_date=date(1813, 1, 28),
    isbn="9780141439518",
    pages=432
)

Book.objects.create(
    title="Sense and Sensibility",
    author=author,
    published_date=date(1811, 10, 30),
    isbn="9780141439662",
    pages=409
)

# 2. الحصول على جميع كتب المؤلف
austen_books = Book.objects.filter(author=author)
# أو باستخدام related_name:
austen_books = author.books.all()

# 3. الحصول على مؤلف كتاب
book = Book.objects.get(title="Pride and Prejudice")
print(book.author.first_name)

# 4. عدّ الكتب لكل مؤلف
from django.db.models import Count
authors_with_count = Author.objects.annotate(book_count=Count('books'))
for author in authors_with_count:
    print(f"{author} لديه {author.book_count} كتاب/كتب")
```
</details>

---

### التمرين 18: إنشاء علاقة ManyToMany

**المهمة:**
أنشئ نماذج للطلاب والدورات:
1. نموذج `Course`: name، code، credits
2. حدّث نموذج `Student` ليحتوي على ManyToMany مع Course
3. أنشئ طلابًا وسجّلهم في دورات

<details>
<summary>الحل</summary>

```python
# books/models.py
class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    grade = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

```bash
python manage.py makemigrations
python manage.py migrate
```

```python
# في الصدفة
from books.models import Student, Course
from datetime import date

# إنشاء دورات
python_course = Course.objects.create(name="Python Programming", code="CS101", credits=3)
web = Course.objects.create(name="Web Development", code="CS201", credits=4)

# إنشاء طالب
student = Student.objects.create(
    first_name="أحمد",
    last_name="علي",
    email="ahmed@example.com",
    enrollment_date=date.today(),
    grade=3.5
)

# تسجيل الطالب في الدورات
student.courses.add(python_course, web)

# الحصول على دورات الطالب
print(student.courses.all())

# الحصول على طلاب الدورة
print(python_course.students.all())
```
</details>

---

### التمرين 19: تصفية متقدمة

**المهمة:**
1. احصل على جميع الكتب المتاحة التي تزيد عن 300 صفحة
2. احصل على الكتب المنشورة بين 1900 و1950
3. احصل على الكتب التي تحتوي كلمة "the" في عنوانها (غير حساس للأحرف)
4. احصل على الكتب لمؤلفين وُلدوا بعد عام 1800

<details>
<summary>الحل</summary>

```python
from books.models import Book, Author
from datetime import date

# 1. الكتب المتاحة > 300 صفحة
books = Book.objects.filter(is_available=True, pages__gt=300)

# 2. الكتب المنشورة 1900-1950
books = Book.objects.filter(
    published_date__gte=date(1900, 1, 1),
    published_date__lte=date(1950, 12, 31)
)

# 3. العنوان يحتوي "the" (غير حساس للأحرف)
books = Book.objects.filter(title__icontains="the")

# 4. الكتب لمؤلفين وُلدوا بعد 1800
books = Book.objects.filter(author__birth_date__gt=date(1800, 1, 1))
```
</details>

---

### التمرين 20: استعلامات التجميع

**المهمة:**
1. احسب متوسط عدد الصفحات لجميع الكتب
2. ابحث عن أطول كتاب (أكبر عدد صفحات)
3. احسب عدد الكتب المتاحة مقابل غير المتاحة
4. احسب مجموع صفحات جميع الكتب

<details>
<summary>الحل</summary>

```python
from books.models import Book
from django.db.models import Avg, Max, Count, Sum

# 1. متوسط الصفحات
avg_pages = Book.objects.aggregate(avg_pages=Avg('pages'))
print(f"متوسط الصفحات: {avg_pages['avg_pages']}")

# 2. أطول كتاب
longest = Book.objects.aggregate(max_pages=Max('pages'))
print(f"أطول كتاب: {longest['max_pages']} صفحة")

# 3. عدد المتاح مقابل غير المتاح
from django.db import models
availability = Book.objects.aggregate(
    available=Count('id', filter=models.Q(is_available=True)),
    unavailable=Count('id', filter=models.Q(is_available=False))
)
print(availability)

# 4. مجموع الصفحات
total = Book.objects.aggregate(total_pages=Sum('pages'))
print(f"إجمالي الصفحات: {total['total_pages']}")
```
</details>

---

## اليوم 5: مشروع المدونة الكامل

### التمرين 21: بناء تطبيق مدونة كامل

**المهمة:**
أنشئ تطبيق مدونة كاملًا يحتوي على:
1. النماذج: Post، Category، Tag
2. العلاقات: Post لديه ForeignKey إلى Category، و ManyToMany إلى Tags
3. واجهة إدارة بتخصيص كامل
4. عروض: قائمة جميع المنشورات، تفاصيل منشور واحد
5. قوالب بتنسيق مناسب

**متطلبات نموذج Post:**
- title، slug، content، excerpt
- author (ForeignKey إلى User)
- category (ForeignKey إلى Category)
- tags (ManyToMany إلى Tag)
- featured_image (URLField)
- status (خيارات: draft، published)
- created_at، updated_at
- Meta: الترتيب بـ -created_at

<details>
<summary>هيكل الحل</summary>

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    featured_image = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags',)

    fieldsets = (
        ('المعلومات الأساسية', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('المحتوى', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('البيانات الوصفية', {
            'fields': ('tags', 'status')
        }),
    )
```

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})
```
</details>

---

## تمارين التحدي

### التحدي 1: إنشاء نظام مكتبة

بناء نظام إدارة مكتبة كامل يحتوي على:
- Books، Authors، Members، Borrowings
- تتبع من استعار أي كتاب ومتى
- تواريخ الاستحقاق والغرامات المتأخرة
- وظائف البحث والتصفية

### التحدي 2: نماذج التجارة الإلكترونية

أنشئ نماذج لموقع تجارة إلكترونية بسيط:
- Products، Categories، Orders، OrderItems
- تتبع المخزون
- مراجعات العملاء
- سجل الأسعار

### التحدي 3: نظام منشورات وسائل التواصل الاجتماعي

ابنِ نموذج بيانات وسائل التواصل الاجتماعي الأساسي:
- Users، Posts، Comments، Likes
- علاقة المتابعين/المتابَعين
- Hashtags (ManyToMany)
- المنشورات الرائجة بناءً على عدد الإعجابات

---

## اختبار معرفتك

بعد إكمال هذه التمارين، يجب أن تكون قادرًا على:
- ✓ إنشاء نماذج Django بأنواع حقول متنوعة
- ✓ إنشاء التهجيرات وتطبيقها
- ✓ تنفيذ عمليات CRUD باستخدام ORM
- ✓ العمل مع العلاقات (ForeignKey، ManyToMany)
- ✓ استخدام واجهة إدارة Django بفاعلية
- ✓ تخصيص واجهة الإدارة
- ✓ كتابة استعلامات معقدة
- ✓ استخدام Django shell للاختبار

---

## الخطوات التالية

1. أكمل جميع التمارين بالترتيب
2. جرّب أنواع حقول مختلفة
3. تدرّب على استعلامات ORM في Django shell
4. ابنِ نموذجك الخاص من الصفر
5. استكشف توثيق Django للميزات المتقدمة
