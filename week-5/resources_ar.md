# موارد الأسبوع الخامس – النماذج، ORM، التهجيرات وواجهة الإدارة

موارد تعليمية مختارة لموضوعات الأسبوع الخامس: نماذج Django، عمليات قواعد البيانات، ORM، وواجهة الإدارة.

---

## جدول المحتويات

1. [التوثيق الرسمي لـ Django](#التوثيق-الرسمي-لـ-django)
2. [دروس فيديو](#دروس-فيديو)
3. [التعلم التفاعلي](#التعلم-التفاعلي)
4. [كتب ومراجع](#كتب-ومراجع)
5. [أوراق مرجعية سريعة](#أوراق-مرجعية-سريعة)
6. [موارد SQLite](#موارد-sqlite)
7. [موارد المجتمع](#موارد-المجتمع)
8. [مقالات ومدونات](#مقالات-ومدونات)
9. [مشاريع تدريبية](#مشاريع-تدريبية)
10. [أدوات وإضافات](#أدوات-وإضافات)
11. [خطة دراسة الأسبوع الخامس](#خطة-دراسة-الأسبوع-الخامس)

---

## التوثيق الرسمي لـ Django

### قراءات أساسية

1. **نماذج Django**
   - الرابط: https://docs.djangoproject.com/en/stable/topics/db/models/
   - الموضوع: دليل كامل لتعريف النماذج
   - السبب: المرجع الرسمي لجميع ميزات النماذج

2. **مرجع حقول النماذج**
   - الرابط: https://docs.djangoproject.com/en/stable/ref/models/fields/
   - الموضوع: قائمة شاملة بجميع أنواع الحقول
   - السبب: مرجع لخيارات الحقول ومعاملاتها

3. **واجهة برمجة QuerySet**
   - الرابط: https://docs.djangoproject.com/en/stable/ref/models/querysets/
   - الموضوع: جميع أساليب QuerySet والبحث
   - السبب: ضروري لكتابة استعلامات قاعدة البيانات

4. **تهجيرات Django**
   - الرابط: https://docs.djangoproject.com/en/stable/topics/migrations/
   - الموضوع: كيفية عمل التهجيرات في Django
   - السبب: فهم سير عمل التهجيرات

5. **موقع إدارة Django**
   - الرابط: https://docs.djangoproject.com/en/stable/ref/contrib/admin/
   - الموضوع: التوثيق الكامل للإدارة
   - السبب: تعلّم جميع خيارات تخصيص الإدارة

---

## دروس فيديو

### قنوات YouTube الموصى بها

**1. Corey Schafer - نماذج Django و ORM**
- السلسلة: Django Tutorial for Beginners
- الموضوعات: النماذج، التهجيرات، الإدارة
- المدة: ~20 دقيقة لكل فيديو
- المستوى: مناسب للمبتدئين
- البحث عن: "Corey Schafer Django Models"

**2. Tech with Tim - دليل قاعدة بيانات Django**
- الموضوعات: شرح كامل لقاعدة البيانات
- المدة: ~30 دقيقة
- المستوى: مبتدئ
- البحث عن: "Tech with Tim Django Database"

**3. Traversy Media - الدورة المكثفة في Django**
- الموضوعات: Django الكامل بما في ذلك النماذج
- المدة: ساعة كاملة
- المستوى: مبتدئ
- البحث عن: "Traversy Media Django"

**4. Programming with Mosh - ORM في Django**
- الموضوعات: تعمّق في ORM
- المدة: ~40 دقيقة
- المستوى: متوسط
- الجودة: إنتاج احترافي

---

## التعلم التفاعلي

### منصات التدريب

**1. الدليل التعليمي الرسمي لـ Django**
- الرابط: https://docs.djangoproject.com/en/stable/intro/tutorial02/
- الموضوع: الجزء الثاني يغطي النماذج والإدارة
- السبب: دليل خطوة بخطوة رسمي
- الوقت: 1-2 ساعة

**2. Real Python - نماذج Django**
- الرابط: https://realpython.com/tutorials/django/
- الموضوع: دروس Django معمّقة
- السبب: شروحات عالية الجودة
- ملاحظة: بعض المحتوى يتطلب عضوية

**3. Django for Everybody (Dr. Chuck)**
- الرابط: https://www.dj4e.com/
- الموضوع: دورة Django مجانية
- السبب: مسار تعلّم منظّم
- الشهادة: متاحة

---

## كتب ومراجع

### كتب موصى بها

**1. "Django for Beginners" بقلم William S. Vincent**
- التركيز: بناء مشاريع Django حقيقية
- تغطية النماذج: الفصول 4-6
- المستوى: مبتدئ
- التنسيق: PDF/مطبوع

**2. "Two Scoops of Django" بقلم Daniel & Audrey Feldman**
- التركيز: أفضل الممارسات
- تغطية النماذج: الفصل 6 (أفضل ممارسات النماذج)
- المستوى: متوسط
- ملاحظة: مرجع للكود النظيف

**3. "Django Design Patterns and Best Practices"**
- التركيز: تطوير Django الاحترافي
- تغطية النماذج: أنماط تصميم النماذج
- المستوى: متوسط إلى متقدم

---

## أوراق مرجعية سريعة

### مرجع سريع لأنواع حقول النماذج

```python
# حقول النصوص
CharField(max_length=200)              # نص قصير
TextField()                             # نص طويل
EmailField()                           # التحقق من البريد الإلكتروني
URLField()                             # التحقق من الرابط
SlugField()                            # نص آمن لعناوين URL

# حقول الأرقام
IntegerField()                         # أعداد صحيحة
DecimalField(max_digits=10, decimal_places=2)  # أرقام عشرية دقيقة
FloatField()                           # أرقام الفاصلة العائمة

# حقول التاريخ/الوقت
DateField()                            # التاريخ فقط
DateTimeField()                        # التاريخ والوقت
TimeField()                            # الوقت فقط
DateTimeField(auto_now_add=True)       # يُضبط عند الإنشاء
DateTimeField(auto_now=True)           # يُحدَّث عند الحفظ

# حقول المنطق
BooleanField()                         # صح/خطأ
BooleanField(default=True)             # مع قيمة افتراضية

# العلاقات
ForeignKey(Model, on_delete=models.CASCADE)  # كثير-إلى-واحد
ManyToManyField(Model)                       # كثير-إلى-كثير
OneToOneField(Model, on_delete=models.CASCADE)  # واحد-إلى-واحد
```

### ورقة مرجعية لأساليب QuerySet

```python
# الاسترجاع
Model.objects.all()                    # جميع السجلات
Model.objects.get(id=1)                # سجل واحد (خطأ إذا لم يُوجد)
Model.objects.filter(field=value)      # سجلات متعددة مطابقة
Model.objects.exclude(field=value)     # جميع السجلات ما عدا المطابقة
Model.objects.first()                  # أول سجل
Model.objects.last()                   # آخر سجل

# الإنشاء
Model.objects.create(**kwargs)         # إنشاء وحفظ
instance.save()                        # حفظ الكائن

# التحديث
instance.save()                        # تحديث الكائن
Model.objects.filter().update(field=value)  # تحديث مجمّع

# الحذف
instance.delete()                      # حذف الكائن
Model.objects.filter().delete()        # حذف مجمّع

# الترتيب
Model.objects.order_by('field')        # تصاعدي
Model.objects.order_by('-field')       # تنازلي

# التحديد
Model.objects.all()[:5]                # أول 5 سجلات
Model.objects.all()[5:10]              # من 6 إلى 10

# العدّ
Model.objects.count()                  # عدّ الكل
Model.objects.filter().count()         # عدّ المُصفَّى

# التحقق من الوجود
Model.objects.filter().exists()        # يُرجع True/False
```

### ورقة مرجعية لبحث الحقول

```python
# التطابق التام
Model.objects.filter(field=value)
Model.objects.filter(field__exact=value)

# غير حساس للأحرف
Model.objects.filter(field__iexact=value)

# يحتوي
Model.objects.filter(field__contains='text')
Model.objects.filter(field__icontains='text')  # غير حساس للأحرف

# يبدأ بـ / ينتهي بـ
Model.objects.filter(field__startswith='text')
Model.objects.filter(field__endswith='text')

# المقارنات الرقمية
Model.objects.filter(field__gt=100)     # أكبر من
Model.objects.filter(field__gte=100)    # أكبر من أو يساوي
Model.objects.filter(field__lt=100)     # أصغر من
Model.objects.filter(field__lte=100)    # أصغر من أو يساوي

# نطاق
Model.objects.filter(field__range=(1, 10))

# التاريخ
Model.objects.filter(date__year=2024)
Model.objects.filter(date__month=1)
Model.objects.filter(date__day=15)

# التحقق من NULL
Model.objects.filter(field__isnull=True)
Model.objects.filter(field__isnull=False)

# ضمن قائمة
Model.objects.filter(field__in=[1, 2, 3])
```

---

## موارد SQLite

### فهم SQLite

**1. متصفح SQLite**
- الرابط: https://sqlitebrowser.org/
- الموضوع: أداة مرئية لتصفح قواعد بيانات SQLite
- السبب: عرض بياناتك بصريًا
- الاستخدام: افتح db.sqlite3 لاستكشاف الجداول

**2. دليل SQLite**
- الرابط: https://www.sqlitetutorial.net/
- الموضوع: تعلّم أساسيات SQL
- السبب: فهم ما يفعله ORM خلف الكواليس

### أوامر SQL المفيدة

```sql
-- عرض جميع الجداول
.tables

-- وصف هيكل الجدول
.schema blog_post

-- عرض البيانات
SELECT * FROM blog_post;

-- عدّ السجلات
SELECT COUNT(*) FROM blog_post;
```

---

## موارد المجتمع

### المنتديات والنقاشات

**1. منتدى Django**
- الرابط: https://forum.djangoproject.com/
- الموضوع: منتدى مجتمع Django الرسمي
- السبب: طرح الأسئلة والحصول على المساعدة

**2. Stack Overflow**
- الوسم: [django]
- الرابط: https://stackoverflow.com/questions/tagged/django
- السبب: البحث عن مشكلات شائعة

**3. Reddit**
- المنتدى الفرعي: r/django
- الرابط: https://reddit.com/r/django
- السبب: نقاشات المجتمع والأخبار

**4. Discord الخاص بـ Django**
- خوادم Discord متعددة خاصة بـ Django
- محادثات فورية ومساعدة
- ابحث عن: "Django Discord server"

---

## مقالات ومدونات

### مقالات يجب قراءتها

**1. "أفضل ممارسات نماذج Django"**
- البحث عن: Django models best practices
- الموضوعات: تصميم النماذج، خيارات الحقول، العلاقات
- تتوفر مقالات متعددة عالية الجودة

**2. "فهم Django ORM"**
- شروحات معمّقة متنوعة لـ ORM
- نصائح لتحسين الاستعلامات
- اعتبارات الأداء

**3. "دليل تخصيص واجهة إدارة Django"**
- تقنيات الإدارة المتقدمة
- أمثلة من العالم الحقيقي
- تحسينات واجهة المستخدم

---

## مشاريع تدريبية

### ابنِ هذه المشاريع للتدريب

**1. مكتبة شخصية**
- النماذج: Book، Author، Category
- الميزات: تتبع حالة القراءة
- الصعوبة: مبتدئ

**2. إدارة المهام**
- النماذج: Task، Project، Tag
- الميزات: تواريخ الاستحقاق، الأولويات
- الصعوبة: مبتدئ

**3. مدير الوصفات**
- النماذج: Recipe، Ingredient، Category
- الميزات: بحث، تقييمات
- الصعوبة: متوسط

**4. إدارة الطلاب**
- النماذج: Student، Course، Grade
- الميزات: التسجيل، حساب المعدل التراكمي
- الصعوبة: متوسط

**5. مدونة مع تعليقات**
- النماذج: Post، Comment، Category، Tag
- الميزات: منشور/مسودة، طوابع زمنية
- الصعوبة: متوسط

---

## أدوات وإضافات

### أدوات التطوير

**1. Django Debug Toolbar**
- الرابط: https://django-debug-toolbar.readthedocs.io/
- الموضوع: لوحة تصحيح تعرض استعلامات SQL
- السبب: رؤية ما يُولّده ORM
- التثبيت: `pip install django-debug-toolbar`

**2. Django Extensions**
- الرابط: https://django-extensions.readthedocs.io/
- الموضوع: أوامر إدارة إضافية
- السبب: shell_plus، graph_models، والمزيد
- التثبيت: `pip install django-extensions`

**3. ipython**
- الموضوع: صدفة Python محسّنة
- السبب: تجربة Django shell أفضل
- التثبيت: `pip install ipython`
- الاستخدام: يُستخدم تلقائيًا بواسطة Django shell إذا كان مثبّتًا

---

## خطة دراسة الأسبوع الخامس

### الموارد اليومية

**اليوم 1: النماذج والتهجيرات**
- اقرأ: توثيق نماذج Django
- شاهد: فيديو Corey Schafer عن النماذج
- تدرّب: التمارين 1-5
- الوقت: 3-4 ساعات

**اليوم 2: ORM و CRUD**
- اقرأ: مرجع واجهة برمجة QuerySet
- شاهد: دليل Django ORM
- تدرّب: التمارين 6-10 في الصدفة
- الوقت: 3-4 ساعات

**اليوم 3: واجهة إدارة Django**
- اقرأ: توثيق إدارة Django
- شاهد: فيديو تخصيص الإدارة
- تدرّب: التمارين 11-15
- الوقت: 2-3 ساعات

**اليوم 4: العلاقات**
- اقرأ: توثيق علاقات النماذج
- تدرّب: التمارين 16-20
- الوقت: 3-4 ساعات

**اليوم 5: المشروع الكامل**
- ابنِ: تطبيق المدونة الكامل
- راجع: جميع مفاهيم الأسبوع
- الوقت: 4-5 ساعات

---

## المشكلات الشائعة وحلولها

### موارد استكشاف الأخطاء وإصلاحها

**1. "التهجيرات لا تعمل"**
- تحقق: التطبيق موجود في INSTALLED_APPS
- جرّب: `python manage.py migrate --fake-initial`
- المورد: توثيق استكشاف أخطاء تهجيرات Django

**2. "الإدارة لا تعرض التغييرات"**
- الحل: امسح ذاكرة التخزين المؤقت للمتصفح وأعد تشغيل الخادم
- تحقق: النموذج مسجَّل

**3. "QuerySet يُرجع بيانات خاطئة"**
- تصحيح: استخدم `print(queryset.query)` لرؤية SQL
- الأداة: Django Debug Toolbar

**4. "أخطاء الاستيراد"**
- تحقق: الاستيرادات الدائرية في النماذج
- الحل: استخدم مراجع النصوص لـ ForeignKey

---

## ملخص الروابط المهمة

**الأساسيات:**
- [توثيق نماذج Django](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [مرجع QuerySet](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
- [أنواع الحقول](https://docs.djangoproject.com/en/stable/ref/models/fields/)
- [موقع الإدارة](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

**التدريب:**
- الجزء الثاني من الدليل التعليمي الرسمي لـ Django
- دورة Django for Everybody
- دروس Real Python Django

**المجتمع:**
- منتدى Django
- وسم [django] على Stack Overflow
- Reddit r/django

**الأدوات:**
- متصفح SQLite
- Django Debug Toolbar
- ipython لصدفة أفضل

---

## ملاحظات للطلاب

### كيفية استخدام هذه الموارد

**1. لا تحاول قراءة كل شيء**
- ركّز على التوثيق الرسمي أولًا
- استخدم الفيديوهات للمفاهيم التي لا تفهمها
- ارجع إلى الأوراق المرجعية أثناء البرمجة

**2. التدريب أهم من القراءة**
- ابنِ مشاريع
- استخدم Django shell يوميًا
- اكسر الأشياء وأصلحها

**3. عند الإعاقة:**
- ابحث في التوثيق الرسمي أولًا
- ابحث في Stack Overflow
- اسأل في المنتديات
- راجع الأوراق المرجعية

**4. ابنِ مجموعة مراجع:**
- احفظ الصفحات المفيدة في المفضلة
- احتفظ بالأوراق المرجعية في متناول اليد
- احفظ مقتطفات الكود

---

**تذكّر:** أفضل مورد هو التدريب. استخدم Django shell كل يوم، ابنِ مشاريع صغيرة، ولا تخف من التجربة!
