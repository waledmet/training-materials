# Week 5 Exercises – Models, ORM, Migrations & Admin Practice

Practice exercises for Week 5: Creating models, performing CRUD operations, using Django admin, and working with the ORM.

---

## Table of Contents

1. [Day 1: Models & Migrations](#day-1-models--migrations)
2. [Day 2: CRUD Operations & ORM](#day-2-crud-operations--orm)
3. [Day 3: Django Admin Customization](#day-3-django-admin-customization)
4. [Day 4: Relationships & Complex Queries](#day-4-relationships--complex-queries)
5. [Day 5: Complete Blog Project](#day-5-complete-blog-project)
6. [Challenge Exercises](#challenge-exercises)

---

## Day 1: Models & Migrations

### Exercise 1: Create Your First Model

**Task:**
1. Create a Django project called `library`
2. Create an app called `books`
3. Create a `Book` model with these fields:
   - `title` (CharField, max_length=200)
   - `author` (CharField, max_length=100)
   - `published_date` (DateField)
   - `isbn` (CharField, max_length=13, unique=True)
   - `pages` (IntegerField)
4. Add a `__str__()` method that returns the book title

<details>
<summary>Solution</summary>

```bash
# Create project and app
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
    'books',  # Add this
]
```
</details>

---

### Exercise 2: Create and Apply Migrations

**Task:**
1. Create migrations for the `Book` model
2. Apply the migrations
3. Check migration status

**Commands:**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

<details>
<summary>Expected Output</summary>

```bash
# makemigrations output
Migrations for 'books':
  books/migrations/0001_initial.py
    - Create model Book

# migrate output
Running migrations:
  Applying books.0001_initial... OK

# showmigrations output
books
 [X] 0001_initial
```
</details>

---

### Exercise 3: Add Fields to Existing Model

**Task:**
1. Add these new fields to the `Book` model:
   - `description` (TextField, blank=True)
   - `cover_image` (URLField, blank=True)
   - `is_available` (BooleanField, default=True)
2. Create and apply migrations

<details>
<summary>Solution</summary>

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

### Exercise 4: Create Student Model

**Task:**
Create a `Student` model with:
- `first_name` (CharField, max_length=50)
- `last_name` (CharField, max_length=50)
- `email` (EmailField, unique=True)
- `enrollment_date` (DateField)
- `grade` (DecimalField, max_digits=4, decimal_places=2)
- `is_active` (BooleanField, default=True)

Add a `__str__()` method that returns "First Last" format.

<details>
<summary>Solution</summary>

```python
# books/models.py (add to existing file)
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

### Exercise 5: Model with Choices

**Task:**
Create a `Task` model with:
- `title` (CharField, max_length=200)
- `description` (TextField)
- `status` with choices: 'pending', 'in_progress', 'completed'
- `priority` with choices: 'low', 'medium', 'high'
- `due_date` (DateField)
- `created_at` (DateTimeField, auto_now_add=True)

<details>
<summary>Solution</summary>

```python
# books/models.py (add to existing file)
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

## Day 2: CRUD Operations & ORM

### Exercise 6: Create Records Using Shell

**Task:**
Use Django shell to create 3 books:

1. "The Great Gatsby" by F. Scott Fitzgerald, published 1925-04-10, ISBN: 9780743273565, 180 pages
2. "To Kill a Mockingbird" by Harper Lee, published 1960-07-11, ISBN: 9780061120084, 324 pages
3. "1984" by George Orwell, published 1949-06-08, ISBN: 9780451524935, 328 pages

<details>
<summary>Solution</summary>

```bash
python manage.py shell
```

```python
from books.models import Book
from datetime import date

# Method 1: Create and save
book1 = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    published_date=date(1925, 4, 10),
    isbn="9780743273565",
    pages=180
)
book1.save()

# Method 2: Using create()
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

# Verify
Book.objects.all()
```
</details>

---

### Exercise 7: Read Records

**Task:**
Using Django shell:
1. Get all books
2. Get books by F. Scott Fitzgerald
3. Get the book with ISBN "9780451524935"
4. Get books with more than 300 pages
5. Count total books

<details>
<summary>Solution</summary>

```python
from books.models import Book

# 1. Get all books
all_books = Book.objects.all()
print(all_books)

# 2. Get books by F. Scott Fitzgerald
fitzgerald_books = Book.objects.filter(author="F. Scott Fitzgerald")
print(fitzgerald_books)

# 3. Get book by ISBN
book = Book.objects.get(isbn="9780451524935")
print(book.title)

# 4. Books with more than 300 pages
long_books = Book.objects.filter(pages__gt=300)
print(long_books)

# 5. Count total books
total = Book.objects.count()
print(f"Total books: {total}")
```
</details>

---

### Exercise 8: Update Records

**Task:**
1. Change the title of "1984" to "Nineteen Eighty-Four"
2. Mark all books as unavailable (is_available=False)
3. Update the description of "The Great Gatsby"

<details>
<summary>Solution</summary>

```python
from books.models import Book

# 1. Update single book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# 2. Update multiple books
Book.objects.all().update(is_available=False)

# 3. Update using filter
Book.objects.filter(title="The Great Gatsby").update(
    description="A novel set in the Jazz Age that tells the story of Jay Gatsby's pursuit of the American Dream."
)

# Verify changes
print(Book.objects.get(isbn="9780451524935").title)
print(Book.objects.filter(is_available=True).count())  # Should be 0
```
</details>

---

### Exercise 9: Delete Records

**Task:**
1. Delete the book with ISBN "9780743273565"
2. Create 2 test books and then delete all books by author "Test Author"

<details>
<summary>Solution</summary>

```python
from books.models import Book

# 1. Delete specific book
book = Book.objects.get(isbn="9780743273565")
book.delete()

# 2. Create test books
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

# Delete all by Test Author
Book.objects.filter(author="Test Author").delete()

# Verify
print(Book.objects.filter(author="Test Author").count())  # Should be 0
```
</details>

---

### Exercise 10: Advanced Queries

**Task:**
1. Get books ordered by pages (ascending)
2. Get books ordered by published date (newest first)
3. Get the first 2 books
4. Check if any book has more than 400 pages
5. Get books published after 1950

<details>
<summary>Solution</summary>

```python
from books.models import Book
from datetime import date

# 1. Order by pages
books_by_pages = Book.objects.order_by('pages')
print(books_by_pages)

# 2. Order by date (newest first)
newest_books = Book.objects.order_by('-published_date')
print(newest_books)

# 3. First 2 books
first_two = Book.objects.all()[:2]
print(first_two)

# 4. Check if any book > 400 pages
has_long_books = Book.objects.filter(pages__gt=400).exists()
print(f"Has books > 400 pages: {has_long_books}")

# 5. Books published after 1950
modern_books = Book.objects.filter(published_date__gt=date(1950, 1, 1))
print(modern_books)
```
</details>

---

## Day 3: Django Admin Customization

### Exercise 11: Create Superuser and Register Model

**Task:**
1. Create a superuser with username "admin", email "admin@example.com"
2. Register the `Book` model in admin
3. Login to admin and add a book

<details>
<summary>Solution</summary>

```bash
# Create superuser
python manage.py createsuperuser
# Follow prompts
```

```python
# books/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

```bash
# Run server and visit admin
python manage.py runserver
# Visit http://localhost:8000/admin/
# Login and add a book
```
</details>

---

### Exercise 12: Customize Admin Display

**Task:**
Customize the `Book` admin to show:
- List display: title, author, pages, is_available
- List filter: is_available, published_date
- Search fields: title, author, isbn

<details>
<summary>Solution</summary>

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

### Exercise 13: Advanced Admin Customization

**Task:**
Add more customizations to `BookAdmin`:
- Readonly fields: published_date
- Ordering: by title
- Date hierarchy: published_date
- Add custom method to show "Short" or "Long" based on pages

<details>
<summary>Solution</summary>

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

    @admin.display(description='Length')
    def book_length(self, obj):
        return "Long" if obj.pages > 300 else "Short"
```
</details>

---

### Exercise 14: Register Multiple Models

**Task:**
1. Register the `Student` model in admin
2. Customize it to show: first_name, last_name, email, is_active
3. Add filters for is_active and enrollment_date

<details>
<summary>Solution</summary>

```python
# books/admin.py (add to existing file)
from .models import Book, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')
    list_filter = ('is_active', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email')
```
</details>

---

### Exercise 15: Admin Fieldsets

**Task:**
Organize the `Book` admin form into sections:
- "Basic Information": title, author, isbn
- "Details": published_date, pages, description
- "Availability": is_available
- "Media": cover_image

<details>
<summary>Solution</summary>

```python
# books/admin.py
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'is_available')
    list_filter = ('is_available', 'published_date')
    search_fields = ('title', 'author', 'isbn')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('Details', {
            'fields': ('published_date', 'pages', 'description')
        }),
        ('Availability', {
            'fields': ('is_available',)
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
    )
```
</details>

---

## Day 4: Relationships & Complex Queries

### Exercise 16: Create Models with ForeignKey

**Task:**
Create two models:
1. `Author` model:
   - first_name, last_name (CharField)
   - bio (TextField)
   - birth_date (DateField)
2. Update `Book` model to use ForeignKey to `Author` instead of CharField

<details>
<summary>Solution</summary>

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

### Exercise 17: Query Across Relationships

**Task:**
1. Create an author and 2 books by that author
2. Get all books by a specific author
3. Get the author of a specific book
4. Count how many books each author has

<details>
<summary>Solution</summary>

```python
from books.models import Author, Book
from datetime import date

# 1. Create author and books
author = Author.objects.create(
    first_name="Jane",
    last_name="Austen",
    bio="English novelist",
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

# 2. Get all books by author
austen_books = Book.objects.filter(author=author)
# Or using related_name:
austen_books = author.books.all()

# 3. Get author of a book
book = Book.objects.get(title="Pride and Prejudice")
print(book.author.first_name)

# 4. Count books per author
from django.db.models import Count
authors_with_count = Author.objects.annotate(book_count=Count('books'))
for author in authors_with_count:
    print(f"{author} has {author.book_count} books")
```
</details>

---

### Exercise 18: Create ManyToMany Relationship

**Task:**
Create models for students and courses:
1. `Course` model: name, code, credits
2. Update `Student` model to have ManyToMany with Course
3. Create students and enroll them in courses

<details>
<summary>Solution</summary>

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
# In shell
from books.models import Student, Course
from datetime import date

# Create courses
python = Course.objects.create(name="Python Programming", code="CS101", credits=3)
web = Course.objects.create(name="Web Development", code="CS201", credits=4)

# Create student
student = Student.objects.create(
    first_name="Ahmed",
    last_name="Ali",
    email="ahmed@example.com",
    enrollment_date=date.today(),
    grade=3.5
)

# Enroll student in courses
student.courses.add(python, web)

# Get student's courses
print(student.courses.all())

# Get students in a course
print(python.students.all())
```
</details>

---

### Exercise 19: Complex Filtering

**Task:**
1. Get all available books with more than 300 pages
2. Get books published between 1900 and 1950
3. Get books whose title contains "the" (case-insensitive)
4. Get books by authors born after 1800

<details>
<summary>Solution</summary>

```python
from books.models import Book, Author
from datetime import date

# 1. Available books > 300 pages
books = Book.objects.filter(is_available=True, pages__gt=300)

# 2. Books published 1900-1950
books = Book.objects.filter(
    published_date__gte=date(1900, 1, 1),
    published_date__lte=date(1950, 12, 31)
)

# 3. Title contains "the" (case-insensitive)
books = Book.objects.filter(title__icontains="the")

# 4. Books by authors born after 1800
books = Book.objects.filter(author__birth_date__gt=date(1800, 1, 1))
```
</details>

---

### Exercise 20: Aggregation Queries

**Task:**
1. Calculate average number of pages across all books
2. Find the longest book (max pages)
3. Count how many books are available vs unavailable
4. Sum total pages of all books

<details>
<summary>Solution</summary>

```python
from books.models import Book
from django.db.models import Avg, Max, Count, Sum

# 1. Average pages
avg_pages = Book.objects.aggregate(avg_pages=Avg('pages'))
print(f"Average pages: {avg_pages['avg_pages']}")

# 2. Longest book
longest = Book.objects.aggregate(max_pages=Max('pages'))
print(f"Longest book: {longest['max_pages']} pages")

# 3. Count available vs unavailable
availability = Book.objects.aggregate(
    available=Count('id', filter=models.Q(is_available=True)),
    unavailable=Count('id', filter=models.Q(is_available=False))
)
print(availability)

# 4. Total pages
total = Book.objects.aggregate(total_pages=Sum('pages'))
print(f"Total pages: {total['total_pages']}")
```
</details>

---

## Day 5: Complete Blog Project

### Exercise 21: Build Complete Blog App

**Task:**
Create a complete blog application with:
1. Models: Post, Category, Tag
2. Relationships: Post has ForeignKey to Category, ManyToMany to Tags
3. Admin interface with full customization
4. Views: list all posts, single post detail
5. Templates with proper styling

**Post Model Requirements:**
- title, slug, content, excerpt
- author (ForeignKey to User)
- category (ForeignKey to Category)
- tags (ManyToMany to Tag)
- featured_image (URLField)
- status (choices: draft, published)
- created_at, updated_at
- Meta: ordering by -created_at

<details>
<summary>Solution Structure</summary>

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
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('Metadata', {
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

## Challenge Exercises

### Challenge 1: Create Library System

Build a complete library management system with:
- Books, Authors, Members, Borrowings
- Track who borrowed which book and when
- Due dates and late fees
- Search and filter functionality

### Challenge 2: E-commerce Models

Create models for a simple e-commerce site:
- Products, Categories, Orders, OrderItems
- Inventory tracking
- Customer reviews
- Price history

### Challenge 3: Social Media Post System

Build a basic social media data model:
- Users, Posts, Comments, Likes
- Followers/Following relationship
- Hashtags (ManyToMany)
- Trending posts based on likes count

---

## Testing Your Knowledge

After completing these exercises, you should be able to:
- ✓ Create Django models with various field types
- ✓ Create and apply migrations
- ✓ Perform CRUD operations using ORM
- ✓ Work with relationships (ForeignKey, ManyToMany)
- ✓ Use Django admin effectively
- ✓ Customize admin interface
- ✓ Write complex queries
- ✓ Use Django shell for testing

---

## Next Steps

1. Complete all exercises in order
2. Experiment with different field types
3. Practice ORM queries in Django shell
4. Build your own model from scratch
5. Explore Django documentation for advanced features
