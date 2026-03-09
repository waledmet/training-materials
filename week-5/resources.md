# Week 5 Resources – Models, ORM, Migrations & Admin

Curated learning resources for Week 5 topics: Django models, database operations, ORM, and admin interface.

---

## Official Django Documentation

### Essential Reading

1. **Django Models**
   - URL: https://docs.djangoproject.com/en/stable/topics/db/models/
   - What: Complete guide to defining models
   - Why: Official reference for all model features

2. **Model Field Reference**
   - URL: https://docs.djangoproject.com/en/stable/ref/models/fields/
   - What: Comprehensive list of all field types
   - Why: Reference for field options and parameters

3. **QuerySet API**
   - URL: https://docs.djangoproject.com/en/stable/ref/models/querysets/
   - What: All QuerySet methods and lookups
   - Why: Essential for writing database queries

4. **Django Migrations**
   - URL: https://docs.djangoproject.com/en/stable/topics/migrations/
   - What: How migrations work in Django
   - Why: Understand migration workflow

5. **Django Admin Site**
   - URL: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
   - What: Complete admin documentation
   - Why: Learn all admin customization options

---

## Video Tutorials

### Recommended YouTube Channels

**1. Corey Schafer - Django Models & ORM**
- Series: Django Tutorial for Beginners
- Topics: Models, migrations, admin
- Length: ~20 min per video
- Level: Beginner-friendly
- URL: Search "Corey Schafer Django Models"

**2. Tech with Tim - Django Database Tutorial**
- Topics: Complete database walkthrough
- Length: ~30 min
- Level: Beginner
- URL: Search "Tech with Tim Django Database"

**3. Traversy Media - Django Crash Course**
- Topics: Full Django including models
- Length: 1 hour complete course
- Level: Beginner
- URL: Search "Traversy Media Django"

**4. Programming with Mosh - Django ORM**
- Topics: ORM deep dive
- Length: ~40 min
- Level: Intermediate
- Quality: Professional production

---

## Interactive Learning

### Practice Platforms

**1. Django Official Tutorial**
- URL: https://docs.djangoproject.com/en/stable/intro/tutorial02/
- What: Part 2 covers models and admin
- Why: Official step-by-step tutorial
- Time: 1-2 hours

**2. Real Python - Django Models**
- URL: https://realpython.com/tutorials/django/
- What: In-depth Django tutorials
- Why: High-quality explanations
- Note: Some content requires membership

**3. Django for Everybody (Dr. Chuck)**
- URL: https://www.dj4e.com/
- What: Free Django course
- Why: Structured learning path
- Certificate: Available

---

## Books & References

### Recommended Books

**1. "Django for Beginners" by William S. Vincent**
- Focus: Building real Django projects
- Models Coverage: Chapters 4-6
- Level: Beginner
- Format: PDF/Print

**2. "Two Scoops of Django" by Daniel & Audrey Feldman**
- Focus: Best practices
- Models Coverage: Chapter 6 (Model Best Practices)
- Level: Intermediate
- Note: Reference for clean code

**3. "Django Design Patterns and Best Practices"**
- Focus: Professional Django development
- Models Coverage: Model design patterns
- Level: Intermediate to Advanced

---

## Cheat Sheets & Quick References

### Model Field Types Quick Reference

```python
# Text Fields
CharField(max_length=200)              # Short text
TextField()                             # Long text
EmailField()                           # Email validation
URLField()                             # URL validation
SlugField()                            # URL-safe text

# Numeric Fields
IntegerField()                         # Whole numbers
DecimalField(max_digits=10, decimal_places=2)  # Precise decimals
FloatField()                           # Floating point

# Date/Time Fields
DateField()                            # Date only
DateTimeField()                        # Date and time
TimeField()                            # Time only
DateTimeField(auto_now_add=True)       # Set on creation
DateTimeField(auto_now=True)           # Update on save

# Boolean Fields
BooleanField()                         # True/False
BooleanField(default=True)             # With default

# Relationships
ForeignKey(Model, on_delete=models.CASCADE)  # Many-to-one
ManyToManyField(Model)                       # Many-to-many
OneToOneField(Model, on_delete=models.CASCADE)  # One-to-one
```

### QuerySet Methods Cheat Sheet

```python
# Retrieving
Model.objects.all()                    # All records
Model.objects.get(id=1)                # Single record (error if not found)
Model.objects.filter(field=value)      # Multiple matching records
Model.objects.exclude(field=value)     # All except matching
Model.objects.first()                  # First record
Model.objects.last()                   # Last record

# Creating
Model.objects.create(**kwargs)         # Create and save
instance.save()                        # Save instance

# Updating
instance.save()                        # Update instance
Model.objects.filter().update(field=value)  # Bulk update

# Deleting
instance.delete()                      # Delete instance
Model.objects.filter().delete()        # Bulk delete

# Ordering
Model.objects.order_by('field')        # Ascending
Model.objects.order_by('-field')       # Descending

# Limiting
Model.objects.all()[:5]                # First 5
Model.objects.all()[5:10]              # 6th to 10th

# Counting
Model.objects.count()                  # Count all
Model.objects.filter().count()         # Count filtered

# Checking existence
Model.objects.filter().exists()        # Returns True/False
```

### Field Lookups Cheat Sheet

```python
# Exact match
Model.objects.filter(field=value)
Model.objects.filter(field__exact=value)

# Case-insensitive
Model.objects.filter(field__iexact=value)

# Contains
Model.objects.filter(field__contains='text')
Model.objects.filter(field__icontains='text')  # Case-insensitive

# Starts/ends with
Model.objects.filter(field__startswith='text')
Model.objects.filter(field__endswith='text')

# Numeric comparisons
Model.objects.filter(field__gt=100)     # Greater than
Model.objects.filter(field__gte=100)    # Greater than or equal
Model.objects.filter(field__lt=100)     # Less than
Model.objects.filter(field__lte=100)    # Less than or equal

# Range
Model.objects.filter(field__range=(1, 10))

# Date
Model.objects.filter(date__year=2024)
Model.objects.filter(date__month=1)
Model.objects.filter(date__day=15)

# NULL checks
Model.objects.filter(field__isnull=True)
Model.objects.filter(field__isnull=False)

# In list
Model.objects.filter(field__in=[1, 2, 3])
```

---

## SQLite Resources

### Understanding SQLite

**1. SQLite Browser**
- URL: https://sqlitebrowser.org/
- What: Visual tool to browse SQLite databases
- Why: See your data visually
- Use: Open db.sqlite3 to explore tables

**2. SQLite Tutorial**
- URL: https://www.sqlitetutorial.net/
- What: Learn SQL basics
- Why: Understand what ORM does behind scenes

### Useful SQL Commands

```sql
-- View all tables
.tables

-- Describe table structure
.schema blog_post

-- View data
SELECT * FROM blog_post;

-- Count records
SELECT COUNT(*) FROM blog_post;
```

---

## Community Resources

### Forums & Discussion

**1. Django Forum**
- URL: https://forum.djangoproject.com/
- What: Official Django community forum
- Why: Ask questions, get help

**2. Stack Overflow**
- Tag: [django]
- URL: https://stackoverflow.com/questions/tagged/django
- Why: Search for common issues

**3. Reddit**
- Subreddit: r/django
- URL: https://reddit.com/r/django
- Why: Community discussions, news

**4. Django Discord**
- Multiple Django Discord servers
- Real-time chat and help
- Search: "Django Discord server"

---

## Blog Posts & Articles

### Must-Read Articles

**1. "Django Models Best Practices"**
- Search: Django models best practices
- Topics: Model design, field choices, relationships
- Multiple quality articles available

**2. "Understanding Django ORM"**
- Various in-depth ORM explanations
- Query optimization tips
- Performance considerations

**3. "Django Admin Customization Guide"**
- Advanced admin techniques
- Real-world examples
- UI improvements

---

## Practice Projects

### Build These for Practice

**1. Personal Library**
- Models: Book, Author, Category
- Features: Track reading status
- Difficulty: Beginner

**2. Task Management**
- Models: Task, Project, Tag
- Features: Due dates, priorities
- Difficulty: Beginner

**3. Recipe Manager**
- Models: Recipe, Ingredient, Category
- Features: Search, ratings
- Difficulty: Intermediate

**4. Student Management**
- Models: Student, Course, Grade
- Features: Enrollment, GPA calculation
- Difficulty: Intermediate

**5. Blog with Comments**
- Models: Post, Comment, Category, Tag
- Features: Published/draft, timestamps
- Difficulty: Intermediate

---

## Tools & Extensions

### Development Tools

**1. Django Debug Toolbar**
- URL: https://django-debug-toolbar.readthedocs.io/
- What: Debug panel showing SQL queries
- Why: See what ORM generates
- Install: `pip install django-debug-toolbar`

**2. Django Extensions**
- URL: https://django-extensions.readthedocs.io/
- What: Additional management commands
- Why: shell_plus, graph_models, and more
- Install: `pip install django-extensions`

**3. ipython**
- What: Enhanced Python shell
- Why: Better Django shell experience
- Install: `pip install ipython`
- Use: Automatically used by Django shell if installed

---

## Week 5 Study Plan

### Day-by-Day Resources

**Day 1: Models & Migrations**
- Read: Django Models documentation
- Watch: Corey Schafer Models video
- Practice: Exercises 1-5
- Time: 3-4 hours

**Day 2: ORM & CRUD**
- Read: QuerySet API reference
- Watch: Django ORM tutorial
- Practice: Exercises 6-10 in shell
- Time: 3-4 hours

**Day 3: Django Admin**
- Read: Django Admin documentation
- Watch: Admin customization video
- Practice: Exercises 11-15
- Time: 2-3 hours

**Day 4: Relationships**
- Read: Model relationships docs
- Practice: Exercises 16-20
- Time: 3-4 hours

**Day 5: Complete Project**
- Build: Complete blog application
- Review: All week concepts
- Time: 4-5 hours

---

## Common Issues & Solutions

### Troubleshooting Resources

**1. "Migrations not working"**
- Check: App in INSTALLED_APPS
- Try: `python manage.py migrate --fake-initial`
- Resource: Django migrations troubleshooting docs

**2. "Admin not showing changes"**
- Solution: Clear browser cache, restart server
- Check: Model is registered

**3. "QuerySet returning wrong data"**
- Debug: Use `print(queryset.query)` to see SQL
- Tool: Django Debug Toolbar

**4. "Import errors"**
- Check: Circular imports in models
- Solution: Use string references for ForeignKey

---

## Additional Learning Paths

### After Week 5

**Next Topics to Learn:**
1. Form handling (Week 6 preview)
2. Authentication (Week 6 preview)
3. Complex queries and performance
4. Database optimization
5. Multiple database support

**Advanced ORM Topics:**
- Aggregation and annotation
- Q objects for complex queries
- F expressions
- Subqueries
- Raw SQL when needed

---

## Quick Links Summary

**Essential:**
- [Django Models Docs](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [QuerySet Reference](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [Field Types](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [Admin Site](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

**Practice:**
- Django Official Tutorial Part 2
- Django for Everybody course
- Real Python Django tutorials

**Community:**
- Django Forum
- Stack Overflow [django] tag
- Reddit r/django

**Tools:**
- SQLite Browser
- Django Debug Toolbar
- ipython for better shell

---

## Notes for Students

### How to Use These Resources

**1. Don't try to read everything**
- Focus on official docs first
- Use videos for concepts you don't understand
- Reference cheat sheets while coding

**2. Practice is more important than reading**
- Build projects
- Use Django shell daily
- Break things and fix them

**3. When stuck:**
- Check official docs first
- Search Stack Overflow
- Ask in forums
- Review cheat sheets

**4. Build a reference collection:**
- Bookmark useful pages
- Keep cheat sheets handy
- Save code snippets

---

**Remember:** The best resource is practice. Use Django shell every day, build small projects, and don't be afraid to experiment!
