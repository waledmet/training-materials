# دروس الأسبوع الثالث: مفاهيم الويب وأساسيات HTML/CSS و Git

مرحبًا بك في الأسبوع الثالث! يمثل هذا الأسبوع انتقالًا ممتعًا من برمجة بايثون إلى فهم كيف يعمل الويب. ستتعلم أساسيات الويب، وتبني أولى صفحاتك باستخدام HTML و CSS، وتبدأ باستخدام Git للتحكم بالإصدارات.

---

## جدول المحتويات

1. [كيف يعمل الويب](#كيف-يعمل-الويب)
2. [أساسيات بروتوكول HTTP](#أساسيات-بروتوكول-http)
3. [أساسيات HTML](#أساسيات-html)
4. [أساسيات CSS](#أساسيات-css)
5. [مقدمة إلى JSON](#مقدمة-إلى-json)
6. [Git والتحكم بالإصدارات](#git-والتحكم-بالإصدارات)
7. [التكامل مع GitHub](#التكامل-مع-github)
8. [مشروع مصغّر: موقع بورتفوليو](#مشروع-مصغّر-موقع-بورتفوليو)

---

## كيف يعمل الويب

### بنية العميل-الخادم

يعمل الويب وفق نموذج العميل-الخادم:

**العميل:**
- متصفح الويب (Chrome, Firefox, Safari, Edge)
- يطلب الموارد من الخوادم
- يعرض صفحات الويب للمستخدمين
- يشغّل كود JavaScript

**الخادم:**
- جهاز يخزّن ملفات الموقع
- يستمع لطلبات العملاء
- يعيد الاستجابات (HTML, CSS, صور, بيانات)
- يمكنه تشغيل كود خلفي (Python, Node.js, PHP, إلخ)

### دورة الطلب والاستجابة

```
1. تكتب www.example.com في المتصفح
   ->
2. يرسل المتصفح طلب HTTP إلى الخادم
   ->
3. يعالج الخادم الطلب
   ->
4. يرسل الخادم استجابة HTTP بالمحتوى
   ->
5. يستقبل المتصفح المحتوى ويعرضه
```

### مثال: تحميل صفحة ويب

```
المستخدم -> المتصفح -> DNS -> الخادم
                         ->
المستخدم <- المتصفح <- HTML, CSS, الصور
```

**خطوة بخطوة:**
1. **يدخل المستخدم الرابط**: `https://www.google.com`
2. **استعلام DNS**: تحويل النطاق إلى عنوان IP (مثل دليل الهاتف)
3. **طلب HTTP**: يطلب المتصفح الصفحة من الخادم
4. **استجابة الخادم**: يرسل ملفات HTML و CSS و JavaScript
5. **عرض المتصفح**: يعرض الصفحة للمستخدم

---

## أساسيات بروتوكول HTTP

### ما هو HTTP؟

**HTTP** (HyperText Transfer Protocol) هو اللغة التي تتواصل بها المتصفحات مع الخوادم.

**HTTPS** هو النسخة الآمنة (مشفرة).

### بنية طلب HTTP

```http
GET /about HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**الأجزاء:**
- **الطريقة**: GET, POST, PUT, DELETE
- **المسار**: /about
- **الرؤوس**: معلومات إضافية
- **الجسم**: بيانات (لطلبات POST/PUT)

### طرق HTTP

#### GET
- **الهدف**: جلب البيانات
- **مثال**: تحميل صفحة، جلب نتائج بحث
- **جسم**: لا
- **آمن**: نعم (لا يغير بيانات الخادم)

```
GET /products
GET /users/123
GET /search?q=python
```

#### POST
- **الهدف**: إرسال بيانات لإنشاء شيء جديد
- **مثال**: إرسال نموذج، إنشاء حساب
- **جسم**: نعم
- **آمن**: لا (يغير بيانات الخادم)

```
POST /users
Body: {"name": "Ahmed", "email": "ahmed@example.com"}
```

#### PUT
- **الهدف**: تحديث بيانات موجودة
- **مثال**: تعديل ملف شخصي
- **جسم**: نعم
- **آمن**: لا

```
PUT /users/123
Body: {"name": "Ahmed Ali", "email": "ahmed@example.com"}
```

#### DELETE
- **الهدف**: حذف بيانات
- **مثال**: حذف منشور
- **جسم**: عادة لا
- **آمن**: لا

```
DELETE /posts/456
```

### رموز حالة HTTP

يرد الخادم برمز حالة يوضح ما حدث:

#### 2xx - نجاح
- **200 OK**: نجح الطلب
- **201 Created**: تم إنشاء مورد جديد
- **204 No Content**: نجاح بدون محتوى للإرجاع

#### 3xx - إعادة توجيه
- **301 Moved Permanently**: تم نقل المورد إلى رابط جديد
- **302 Found**: إعادة توجيه مؤقتة
- **304 Not Modified**: النسخة المخزنة لا تزال صالحة

#### 4xx - أخطاء العميل
- **400 Bad Request**: صيغة الطلب غير صحيحة
- **401 Unauthorized**: يحتاج مصادقة
- **403 Forbidden**: لا تملك صلاحية
- **404 Not Found**: المورد غير موجود

#### 5xx - أخطاء الخادم
- **500 Internal Server Error**: تعطل الخادم
- **502 Bad Gateway**: استجابة غير صالحة من خادم آخر
- **503 Service Unavailable**: الخادم مشغول أو متوقف

### الكوكيز والجلسات

#### الكوكيز
بيانات صغيرة يخزنها الموقع في المتصفح.

**الاستخدامات:**
- تذكّر تسجيل الدخول
- حفظ التفضيلات
- تتبع سلوك المستخدم
- عناصر سلة التسوق

**مثال:**
```
Set-Cookie: user_id=12345; expires=Fri, 31 Dec 2025 23:59:59 GMT
```

#### الجلسات
تخزين بيانات المستخدم على الخادم. يرسل الخادم كوكي تعريف للجلسة لتمييز المستخدم.

**التسلسل:**
```
1. تسجل الدخول
2. ينشئ الخادم جلسة
3. يرسل الخادم كوكي معرف الجلسة
4. يرسل المتصفح الكوكي مع الطلبات التالية
5. يتعرف الخادم عليك عبر معرف الجلسة
```

---

## أساسيات HTML

### ما هي HTML؟

**HTML** (HyperText Markup Language) هي بنية صفحات الويب. ليست لغة برمجة، بل لغة توصيف تحدد هيكل المحتوى.

### هيكل HTML الأساسي

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first web page.</p>
</body>
</html>
```

**الشرح:**
- `<!DOCTYPE html>`: يحدد أن الصفحة HTML5
- `<html>`: العنصر الجذر
- `<head>`: بيانات تعريفية (لا تظهر)
- `<title>`: عنوان الصفحة (يظهر في التبويب)
- `<body>`: المحتوى الظاهر

### وسوم HTML الشائعة

#### العناوين

```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
<h3>Smaller Heading</h3>
<h4>Even Smaller</h4>
<h5>Very Small</h5>
<h6>Smallest</h6>
```

#### الفقرات والنص

```html
<p>This is a paragraph of text.</p>

<p>This is <strong>bold text</strong>.</p>
<p>This is <em>italic text</em>.</p>
<p>This is <u>underlined text</u>.</p>

<br> <!-- Line break -->
<hr> <!-- Horizontal line -->
```

#### القوائم

**قائمة غير مرتبة:**
```html
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Orange</li>
</ul>
```

**قائمة مرتبة:**
```html
<ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</ol>
```

#### الروابط

```html
<!-- رابط خارجي -->
<a href="https://www.google.com">Go to Google</a>

<!-- رابط لصفحة أخرى -->
<a href="about.html">About Us</a>

<!-- فتح في تبويب جديد -->
<a href="https://www.google.com" target="_blank">Google (new tab)</a>

<!-- رابط لقسم في نفس الصفحة -->
<a href="#contact">Jump to Contact</a>
```

#### الصور

```html
<img src="photo.jpg" alt="Description of image">

<!-- مع عرض وارتفاع -->
<img src="photo.jpg" alt="Description" width="300" height="200">

<!-- من رابط -->
<img src="https://example.com/image.jpg" alt="Online image">
```

#### الأقسام والعناصر المضمّنة

```html
<!-- div: حاوية على مستوى الكتلة -->
<div class="container">
    <h2>Section Title</h2>
    <p>Section content</p>
</div>

<!-- span: حاوية داخل السطر -->
<p>This is <span style="color: red;">red text</span> in a paragraph.</p>
```

#### النماذج والمدخلات

```html
<form action="/submit" method="POST">
    <!-- نص -->
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <!-- بريد -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <!-- كلمة مرور -->
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">

    <!-- رقم -->
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" min="1" max="120">

    <!-- مساحة نصية -->
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4"></textarea>

    <!-- اختيار متعدد -->
    <input type="checkbox" id="subscribe" name="subscribe">
    <label for="subscribe">Subscribe to newsletter</label>

    <!-- أزرار اختيار -->
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>

    <!-- قائمة منسدلة -->
    <label for="city">City:</label>
    <select id="city" name="city">
        <option value="riyadh">Riyadh</option>
        <option value="jeddah">Jeddah</option>
        <option value="dammam">Dammam</option>
    </select>

    <!-- زر إرسال -->
    <button type="submit">Submit</button>
</form>
```

#### الجداول

```html
<table border="1">
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>City</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Ahmed</td>
            <td>25</td>
            <td>Riyadh</td>
        </tr>
        <tr>
            <td>Sara</td>
            <td>23</td>
            <td>Jeddah</td>
        </tr>
    </tbody>
</table>
```

### HTML الدلالي

استخدم وسومًا ذات معنى يصف المحتوى:

```html
<header>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h1>Article Title</h1>
        <p>Article content...</p>
    </article>

    <section id="about">
        <h2>About Us</h2>
        <p>Information about us...</p>
    </section>
</main>

<footer>
    <p>&copy; 2025 My Website</p>
</footer>
```

---

## أساسيات CSS

### ما هي CSS؟

**CSS** (Cascading Style Sheets) تتحكم في مظهر عناصر HTML.

### ثلاث طرق لإضافة CSS

#### 1. CSS داخل السطر (غير مُوصى بها)
```html
<p style="color: red; font-size: 20px;">Red text</p>
```

#### 2. CSS داخلي (داخل `<head>`)
```html
<head>
    <style>
        p {
            color: blue;
            font-size: 16px;
        }
    </style>
</head>
```

#### 3. CSS خارجي (أفضل ممارسة)
```html
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

**style.css:**
```css
p {
    color: green;
    font-size: 18px;
}
```

### محددات CSS

#### محدد العناصر
```css
p {
    color: blue;
}

h1 {
    font-size: 32px;
}
```

#### محدد الفئة (Class)
```html
<p class="highlight">This is highlighted</p>
<p class="highlight">This too!</p>
```

```css
.highlight {
    background-color: yellow;
    padding: 10px;
}
```

#### محدد المعرّف (ID)
```html
<div id="header">Header content</div>
```

```css
#header {
    background-color: navy;
    color: white;
}
```

#### محددات متعددة
```css
h1, h2, h3 {
    font-family: Arial, sans-serif;
}
```

#### محددات التابع
```css
div p {
    color: red; /* فقط الفقرات داخل div */
}
```

### خصائص CSS الشائعة

#### تنسيق النص
```css
.text-example {
    color: #333;              /* لون النص */
    font-size: 16px;         /* حجم النص */
    font-family: Arial;      /* الخط */
    font-weight: bold;       /* عريض */
    text-align: center;      /* محاذاة */
    text-decoration: underline; /* تسطير */
    line-height: 1.5;        /* تباعد الأسطر */
    letter-spacing: 2px;     /* تباعد الحروف */
}
```

#### الخلفية
```css
.bg-example {
    background-color: lightblue;
    background-image: url('image.jpg');
    background-size: cover;
    background-position: center;
}
```

#### نموذج الصندوق
```css
.box {
    width: 300px;
    height: 200px;
    padding: 20px;           /* المساحة الداخلية */
    margin: 10px;            /* المساحة الخارجية */
    border: 2px solid black; /* الحد */
}
```

**تصور نموذج الصندوق:**
```
+------------------------------ margin ------------------------------+
|  +--------------------------- border ---------------------------+  |
|  |  +------------------------ padding ------------------------+  |  |
|  |  |                      CONTENT                            |  |  |
|  |  +---------------------------------------------------------+  |  |
|  +---------------------------------------------------------------+  |
+--------------------------------------------------------------------+
```

#### الحدود
```css
.border-example {
    border: 2px solid black;
    border-radius: 10px;     /* زوايا دائرية */
    border-top: 3px dashed red;
}
```

#### العرض
```css
.inline {
    display: inline;   /* عنصر ضمن السطر */
}

.block {
    display: block;    /* عنصر كتلي */
}

.none {
    display: none;     /* إخفاء العنصر */
}
```

#### الألوان

```css
.colors {
    color: red;                    /* اسم */
    color: #FF0000;               /* Hex */
    color: rgb(255, 0, 0);        /* RGB */
    color: rgba(255, 0, 0, 0.5);  /* RGBA (مع شفافية) */
}
```

### مثال تخطيط بسيط

```html
<!DOCTYPE html>
<html>
<head>
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
            background-color: #444;
            padding: 10px;
        }

        nav a {
            color: white;
            padding: 10px 20px;
            text-decoration: none;
        }

        nav a:hover {
            background-color: #555;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
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
        <h1>My Website</h1>
    </header>

    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>

    <div class="container">
        <h2>Welcome</h2>
        <p>This is my website content.</p>
    </div>

    <footer>
        <p>&copy; 2025 My Website</p>
    </footer>
</body>
</html>
```

---

## مقدمة إلى JSON

### ما هي JSON؟

**JSON** (JavaScript Object Notation) صيغة خفيفة لتخزين البيانات وتبادلها.

### صياغة JSON

```json
{
    "name": "Ahmed",
    "age": 25,
    "city": "Riyadh",
    "is_student": true,
    "skills": ["Python", "HTML", "CSS"],
    "address": {
        "street": "King Fahd Road",
        "zip": "12345"
    }
}
```

**القواعد:**
- البيانات على شكل أزواج مفتاح-قيمة
- المفاتيح يجب أن تكون نصوصًا (بين علامات اقتباس)
- القيم يمكن أن تكون: نص، رقم، منطقية، قائمة، كائن، أو null
- استخدم علامات الاقتباس المزدوجة فقط
- لا توجد فواصل زائدة في النهاية

### أنواع بيانات JSON

```json
{
    "string": "Hello",
    "number": 123,
    "float": 45.67,
    "boolean": true,
    "null_value": null,
    "array": [1, 2, 3],
    "object": {"key": "value"}
}
```

### JSON مقابل قاموس بايثون

**قاموس بايثون:**
```python
person = {
    "name": "Ahmed",
    "age": 25,
    "is_student": True,
    "courses": None
}
```

**JSON:**
```json
{
    "name": "Ahmed",
    "age": 25,
    "is_student": true,
    "courses": null
}
```

**الاختلافات:**
- بايثون: `True`, `False`, `None`
- JSON: `true`, `false`, `null`

### التعامل مع JSON في بايثون

```python
import json

# تحويل قاموس بايثون إلى نص JSON
person = {"name": "Ahmed", "age": 25}
json_string = json.dumps(person)
print(json_string)  # '{"name": "Ahmed", "age": 25}'

# تحويل نص JSON إلى قاموس بايثون
json_data = '{"name": "Sara", "age": 23}'
person = json.loads(json_data)
print(person["name"])  # Sara

# كتابة JSON إلى ملف
with open("data.json", "w") as file:
    json.dump(person, file, indent=2)

# قراءة JSON من ملف
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

### لماذا JSON مهمة لتطوير الويب؟

1. **واجهات API**: أغلب واجهات الويب تعيد البيانات بصيغة JSON
2. **الإعدادات**: العديد من الأدوات تستخدم JSON للإعدادات
3. **تبادل البيانات**: سهلة الإرسال بين الواجهة والخلفية
4. **مستقلة عن اللغة**: تعمل مع بايثون وجافا سكربت وجافا وغيرها

---

## Git والتحكم بالإصدارات

### ما هو Git؟

**Git** هو نظام للتحكم بالإصدارات يتتبع التغييرات على الملفات عبر الزمن.

**الفوائد:**
- تتبع تاريخ التغييرات
- التعاون مع الآخرين
- الرجوع لإصدارات سابقة
- العمل على ميزات بدون كسر الكود الرئيسي

### تثبيت Git

**التأكد من التثبيت:**
```bash
git --version
```

**إعداد Git (لأول مرة):**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### سير عمل Git الأساسي

```
Working Directory -> Staging Area -> Repository

    تعديل الملفات -> git add -> git commit
```

### أوامر Git الأساسية

#### تهيئة مستودع
```bash
# إنشاء مستودع جديد
git init

# ينشئ مجلد .git مخفي
```

#### التحقق من الحالة
```bash
git status

# يعرض:
# - الملفات المعدلة
# - الملفات المضافة
# - الملفات غير المتتبعة
```

#### إضافة الملفات إلى Stage
```bash
# إضافة ملف محدد
git add index.html

# إضافة كل الملفات
git add .

# إضافة عدة ملفات
git add index.html style.css
```

#### عمل Commit
```bash
# عمل commit مع رسالة
git commit -m "Add homepage structure"

# أمثلة على رسائل جيدة:
# - "Add login form"
# - "Fix navigation bug"
# - "Update contact page styling"
```

#### عرض سجل التغييرات
```bash
# عرض جميع الالتزامات
git log

# عرض مختصر
git log --oneline

# عرض آخر 5 التزامات
git log -5
```

#### عرض الفروق
```bash
# الفروق غير المضافة
git diff

# الفروق المضافة
git diff --staged
```

### ملف .gitignore

يخبر Git بتجاهل ملفات معينة.

**إنشاء `.gitignore`:**
```
# Python
__pycache__/
*.pyc
*.pyo
venv/
.env

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp

# Project specific
node_modules/
build/
dist/
```

---

## التكامل مع GitHub

### ما هو GitHub؟

**GitHub** منصة سحابية لاستضافة مستودعات Git. توفر:
- نسخة احتياطية بعيدة
- ميزات تعاون
- إدارة مشاريع
- أدوات مراجعة الكود

### GitHub مقابل Git

- **Git**: برنامج تحكم بالإصدارات (محلي)
- **GitHub**: خدمة استضافة مستودعات Git (سحابي)

### إنشاء حساب على GitHub

1. انتقل إلى https://github.com
2. سجّل بالبريد الإلكتروني
3. تحقق من البريد
4. اختر الخطة المجانية

### إنشاء مستودع على GitHub

1. اضغط "New Repository"
2. أدخل اسم المستودع
3. اختر عام أو خاص
4. (اختياري) أضف README
5. اضغط "Create repository"

### ربط المستودع المحلي بـ GitHub

```bash
# إضافة المستودع البعيد
git remote add origin https://github.com/username/repo-name.git

# التحقق من البعيد
git remote -v

# أول مرة دفع
git push -u origin main

# في المرات التالية
git push
```

### استنساخ مستودع

```bash
# استنساخ مستودع من GitHub
git clone https://github.com/username/repo-name.git

# استنساخ إلى مجلد محدد
git clone https://github.com/username/repo-name.git my-folder
```

### سحب التغييرات

```bash
# جلب آخر التغييرات من GitHub
git pull
```

### سير عمل شائع مع GitHub

```bash
# 1. إجراء تغييرات على الملفات
# عدّل index.html و style.css

# 2. التحقق من الحالة
git status

# 3. إضافة التغييرات
git add .

# 4. عمل commit
git commit -m "Update homepage design"

# 5. دفع إلى GitHub
git push
```

### عرض المستودع على GitHub

بعد الدفع، سيكون الكود موجودًا على:
```
https://github.com/your-username/repository-name
```

---

## مشروع مصغّر: موقع بورتفوليو

لنَبْنِ موقع بورتفوليو بسيطًا باستخدام كل ما تعلمناه!

### هيكل المشروع

```
portfolio/
|-- index.html
|-- style.css
`-- README.md
```

### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ahmed's Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Ahmed Ali</h1>
        <p>Python Developer</p>
    </header>

    <nav>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
    </nav>

    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>
                Hello! I'm Ahmed, a passionate developer learning Python and web development.
                I love creating solutions that make people's lives easier.
            </p>
        </section>

        <section id="skills">
            <h2>My Skills</h2>
            <ul>
                <li>Python Programming</li>
                <li>HTML & CSS</li>
                <li>Git & GitHub</li>
                <li>Problem Solving</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact Me</h2>
            <form>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Ahmed Ali. All rights reserved.</p>
    </footer>
</body>
</html>
```

### style.css

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
    padding: 60px 20px;
}

header h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

header p {
    font-size: 20px;
}

nav {
    background-color: #333;
    padding: 15px;
    text-align: center;
    position: sticky;
    top: 0;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 10px 20px;
    margin: 0 5px;
    border-radius: 5px;
    transition: background-color 0.3s;
}

nav a:hover {
    background-color: #555;
}

main {
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
}

section {
    margin-bottom: 60px;
    padding: 30px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

section h2 {
    color: #667eea;
    margin-bottom: 20px;
    font-size: 32px;
    border-bottom: 3px solid #667eea;
    padding-bottom: 10px;
}

section p {
    font-size: 18px;
    margin-bottom: 15px;
}

section ul {
    list-style: none;
}

section li {
    background-color: white;
    padding: 15px;
    margin-bottom: 10px;
    border-left: 4px solid #667eea;
    border-radius: 5px;
}

form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-top: 15px;
    margin-bottom: 5px;
    font-weight: bold;
}

form input,
form textarea {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
}

form button {
    margin-top: 20px;
    padding: 12px;
    background-color: #667eea;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
    transition: background-color 0.3s;
}

form button:hover {
    background-color: #5568d3;
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 60px;
}
```

### الرفع إلى GitHub

```bash
# 1. تهيئة مستودع Git
cd portfolio
git init

# 2. إضافة الملفات
git add .

# 3. عمل commit
git commit -m "Initial commit: Add portfolio website"

# 4. إنشاء مستودع على GitHub (عبر الموقع)
# ثم الربط:
git remote add origin https://github.com/your-username/portfolio.git

# 5. الدفع إلى GitHub
git push -u origin main
```

---

## أهم النقاط في الأسبوع الثالث

**أساسيات الويب:**
- بنية العميل-الخادم
- طرق HTTP (GET, POST, PUT, DELETE)
- رموز حالة HTTP (200, 404, 500)
- الكوكيز والجلسات

**HTML:**
- البنية الأساسية (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- الوسوم الشائعة (العناوين، الفقرات، الروابط، الصور، القوائم، النماذج)
- الوسوم الدلالية (`<header>`, `<nav>`, `<main>`, `<footer>`)

**CSS:**
- المحددات (عنصر، فئة، معرّف)
- الخصائص الشائعة (اللون، الخط، الحشو، الهامش، الحدود)
- نموذج الصندوق
- التخطيطات الأساسية

**JSON:**
- صيغة البيانات لواجهات API
- بنية مفتاح-قيمة
- التعامل مع JSON في بايثون

**Git و GitHub:**
- أساسيات التحكم بالإصدارات
- أوامر أساسية (`init`, `add`, `commit`, `push`, `pull`)
- ربط المستودع بـ GitHub
- ملف `.gitignore`

---

## الخطوات التالية

**قبل الأسبوع الرابع:**
- أكمل جميع التمارين
- ابْنِ بورتفوليوك الخاص
- ارفع مشروعك على GitHub
- جرّب أنماط CSS مختلفة
- تدرب على أوامر Git

**لمحة عن الأسبوع الرابع:**
ستتعلم عن:
- إطار Django
- إنشاء مشاريع وتطبيقات Django
- عناوين URL و Views
- القوالب والملفات الثابتة
- بناء أول تطبيق ويب باستخدام Django

استمر في التدريب ونراك الأسبوع القادم!
