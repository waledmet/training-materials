# تمارين الأسبوع الثالث

يحتوي هذا الملف على تمارين الأسبوع الثالث. حاول حل كل تمرين بنفسك قبل الاطلاع على الحل.

---

## جدول المحتويات

1. [اليوم 1: أساسيات HTML](#اليوم-1-أساسيات-html)
2. [اليوم 2: المزيد من HTML والنماذج](#اليوم-2-المزيد-من-html-والنماذج)
3. [اليوم 3: أساسيات CSS](#اليوم-3-أساسيات-css)
4. [اليوم 4: أساسيات Git](#اليوم-4-أساسيات-git)
5. [اليوم 5: مشروع البورتفوليو](#اليوم-5-مشروع-البورتفوليو)
6. [تمارين التحدي](#تمارين-التحدي)

---

## اليوم 1: أساسيات HTML

### التمرين 1: إنشاء أول صفحة HTML

**المهمة**: أنشئ صفحة HTML بسيطة تحتوي على:
- هيكل HTML صحيح
- عنوان في تبويب المتصفح
- عنوان رئيسي
- فقرة

**المخرجات المتوقعة**: صفحة ويب تعرض عنوانًا وفقرة.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is my first HTML page. I'm learning web development!</p>
</body>
</html>
```
</details>

---

### التمرين 2: تسلسل العناوين

**المهمة**: أنشئ صفحة تعرض جميع مستويات العناوين (h1 إلى h6) مع نصوص وصفية.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Heading Levels</title>
</head>
<body>
    <h1>This is Heading 1 - Main Title</h1>
    <h2>This is Heading 2 - Major Section</h2>
    <h3>This is Heading 3 - Subsection</h3>
    <h4>This is Heading 4 - Sub-subsection</h4>
    <h5>This is Heading 5 - Minor Section</h5>
    <h6>This is Heading 6 - Smallest Heading</h6>
</body>
</html>
```
</details>

---

### التمرين 3: تنسيق النص

**المهمة**: أنشئ فقرة تُظهر النص الغامق والمائل والمسطر.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text Formatting</title>
</head>
<body>
    <h1>Text Formatting Examples</h1>

    <p>
        This text is <strong>bold</strong>.
        This text is <em>italic</em>.
        This text is <u>underlined</u>.
    </p>

    <p>
        You can <strong><em>combine formatting</em></strong> too!
    </p>
</body>
</html>
```
</details>

---

### التمرين 4: القوائم

**المهمة**: أنشئ قائمة مرتبة وأخرى غير مرتبة تعرض:
- قائمة غير مرتبة: أطعمتك المفضلة (4 على الأقل)
- قائمة مرتبة: خطوات تحضير القهوة (3 على الأقل)

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Lists Example</title>
</head>
<body>
    <h2>My Favorite Foods</h2>
    <ul>
        <li>Pizza</li>
        <li>Pasta</li>
        <li>Sushi</li>
        <li>Ice Cream</li>
    </ul>

    <h2>How to Make Coffee</h2>
    <ol>
        <li>Boil water</li>
        <li>Add coffee grounds to filter</li>
        <li>Pour hot water over grounds</li>
        <li>Wait 4-5 minutes</li>
        <li>Enjoy your coffee!</li>
    </ol>
</body>
</html>
```
</details>

---

### التمرين 5: الروابط

**المهمة**: أنشئ صفحة تحتوي على:
- رابط إلى Google
- رابط لصفحة أخرى (about.html)
- رابط يفتح في تبويب جديد

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Links Example</title>
</head>
<body>
    <h1>My Links</h1>

    <p><a href="https://www.google.com">Go to Google</a></p>

    <p><a href="about.html">About Page</a></p>

    <p><a href="https://www.github.com" target="_blank">GitHub (opens in new tab)</a></p>
</body>
</html>
```
</details>

---

### التمرين 6: الصور

**المهمة**: أضف صورة إلى صفحتك. استخدم رابط صورة من الإنترنت أو ملفًا محليًا.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Images Example</title>
</head>
<body>
    <h1>My Image Gallery</h1>

    <!-- Online image -->
    <img src="https://via.placeholder.com/300x200" alt="Placeholder image">

    <!-- Local image (make sure photo.jpg exists) -->
    <img src="photo.jpg" alt="My photo" width="300">

    <p>Image with caption:</p>
    <figure>
        <img src="https://via.placeholder.com/400x300" alt="Sample">
        <figcaption>This is a sample image</figcaption>
    </figure>
</body>
</html>
```
</details>

---

## اليوم 2: المزيد من HTML والنماذج

### التمرين 7: جدول بسيط

**المهمة**: أنشئ جدولًا للطلاب بأعمدة: الاسم، العمر، المدينة.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Student Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Student Information</h1>

    <table>
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
                <td>22</td>
                <td>Riyadh</td>
            </tr>
            <tr>
                <td>Sara</td>
                <td>20</td>
                <td>Jeddah</td>
            </tr>
            <tr>
                <td>Mohammed</td>
                <td>23</td>
                <td>Dammam</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
```
</details>

---

### التمرين 8: نموذج تواصل

**المهمة**: أنشئ نموذج تواصل يحتوي على الاسم والبريد والرسالة.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>

    <form action="/submit" method="POST">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" cols="30" required></textarea><br><br>

        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```
</details>

---

### التمرين 9: نموذج تسجيل

**المهمة**: أنشئ نموذج تسجيل يحتوي على:
- الاسم الكامل
- البريد الإلكتروني
- كلمة المرور
- العمر
- الجنس (أزرار اختيار)
- مربع الموافقة على الشروط

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration Form</title>
</head>
<body>
    <h1>User Registration</h1>

    <form action="/register" method="POST">
        <label for="fullname">Full Name:</label><br>
        <input type="text" id="fullname" name="fullname" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" min="1" max="120" required><br><br>

        <label>Gender:</label><br>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">Male</label><br>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">Female</label><br><br>

        <input type="checkbox" id="terms" name="terms" required>
        <label for="terms">I agree to the terms and conditions</label><br><br>

        <button type="submit">Register</button>
    </form>
</body>
</html>
```
</details>

---

### التمرين 10: قائمة منسدلة

**المهمة**: أنشئ نموذجًا يحتوي على قائمة منسدلة لاختيار مدينة.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>City Selection</title>
</head>
<body>
    <h1>Select Your City</h1>

    <form>
        <label for="city">Choose a city:</label><br>
        <select id="city" name="city">
            <option value="">-- Select a city --</option>
            <option value="riyadh">Riyadh</option>
            <option value="jeddah">Jeddah</option>
            <option value="dammam">Dammam</option>
            <option value="makkah">Makkah</option>
            <option value="madinah">Madinah</option>
        </select><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
</details>

---

## اليوم 3: أساسيات CSS

### التمرين 11: CSS داخل السطر وداخلي وخارجي

**المهمة**: أنشئ صفحة تعرض طرق إضافة CSS الثلاث.

<details>
<summary>اضغط لعرض الحل</summary>

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Methods</title>

    <!-- Internal CSS -->
    <style>
        .internal {
            color: blue;
            font-size: 20px;
        }
    </style>

    <!-- External CSS -->
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Inline CSS -->
    <p style="color: red; font-size: 18px;">This uses inline CSS</p>

    <!-- Internal CSS -->
    <p class="internal">This uses internal CSS</p>

    <!-- External CSS -->
    <p class="external">This uses external CSS</p>
</body>
</html>
```

**style.css:**
```css
.external {
    color: green;
    font-size: 22px;
}
```
</details>

---

### التمرين 12: محددات CSS

**المهمة**: أنشئ صفحة باستخدام محددات العناصر والفئات والمعرفات.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Selectors</title>
    <style>
        /* Element selector */
        p {
            color: #333;
            line-height: 1.6;
        }

        /* Class selector */
        .highlight {
            background-color: yellow;
            padding: 5px;
        }

        .important {
            color: red;
            font-weight: bold;
        }

        /* ID selector */
        #header {
            background-color: navy;
            color: white;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="header">
        <h1>CSS Selectors Demo</h1>
    </div>

    <p>This is a regular paragraph.</p>

    <p class="highlight">This paragraph is highlighted.</p>

    <p class="important">This is important information!</p>

    <p class="highlight important">This is both highlighted and important.</p>
</body>
</html>
```
</details>

---

### التمرين 13: نموذج الصندوق

**المهمة**: أنشئ صناديق توضح الحشو والهامش والحدود.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Box Model</title>
    <style>
        .box {
            width: 200px;
            height: 100px;
            background-color: lightblue;
            margin: 20px;
            padding: 15px;
            border: 3px solid navy;
        }

        .box1 {
            margin: 10px;
            padding: 20px;
            border: 2px solid red;
        }

        .box2 {
            margin: 30px;
            padding: 10px;
            border: 5px dashed green;
        }
    </style>
</head>
<body>
    <h1>Box Model Examples</h1>

    <div class="box">
        Box with padding, margin, and border
    </div>

    <div class="box box1">
        Box 1 - Different margins and padding
    </div>

    <div class="box box2">
        Box 2 - Dashed border
    </div>
</body>
</html>
```
</details>

---

### التمرين 14: تنسيق النص

**المهمة**: أنشئ صفحة بأنماط نص مختلفة: ألوان، خطوط، أحجام، محاذاة.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Text Styling</title>
    <style>
        .red-text {
            color: red;
        }

        .large-text {
            font-size: 24px;
        }

        .arial-font {
            font-family: Arial, sans-serif;
        }

        .center-text {
            text-align: center;
        }

        .bold-text {
            font-weight: bold;
        }

        .underline-text {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1 class="center-text">Text Styling Examples</h1>

    <p class="red-text">This text is red.</p>

    <p class="large-text">This text is large.</p>

    <p class="arial-font">This text uses Arial font.</p>

    <p class="center-text">This text is centered.</p>

    <p class="bold-text">This text is bold.</p>

    <p class="underline-text">This text is underlined.</p>

    <p class="red-text large-text bold-text">Multiple styles combined!</p>
</body>
</html>
```
</details>

---

### التمرين 15: شريط تنقل بسيط

**المهمة**: أنشئ شريط تنقل أفقي مع تأثير تحويم.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Navigation Bar</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        nav {
            background-color: #333;
            overflow: hidden;
        }

        nav a {
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
        }

        nav a:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <nav>
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </nav>

    <div style="padding: 20px;">
        <h1>Welcome to My Website</h1>
        <p>This is the content area.</p>
    </div>
</body>
</html>
```
</details>

---

## اليوم 4: أساسيات Git

### التمرين 16: تهيئة مستودع Git

**المهمة**: أنشئ مجلد مشروع جديدًا، وابدأ مستودع Git، وقم بأول commit.

<details>
<summary>اضغط لعرض الحل</summary>

```bash
# Create project folder
mkdir my-website
cd my-website

# Create a file
echo "# My Website" > README.md

# Initialize Git
git init

# Check status
git status

# Add file
git add README.md

# Commit
git commit -m "Initial commit: Add README"

# View history
git log
```
</details>

---

### التمرين 17: تتبع عدة ملفات

**المهمة**: أنشئ index.html و style.css، أضفهما إلى Git، ثم نفّذ commit.

<details>
<summary>اضغط لعرض الحل</summary>

```bash
# Create files
echo "<!DOCTYPE html><html><head><title>My Site</title></head><body><h1>Hello</h1></body></html>" > index.html
echo "body { font-family: Arial; }" > style.css

# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Add index.html and style.css"

# View log
git log --oneline
```
</details>

---

### التمرين 18: إنشاء .gitignore

**المهمة**: أنشئ ملف .gitignore لتجاهل ملفات معينة.

<details>
<summary>اضغط لعرض الحل</summary>

**Create .gitignore:**
```bash
# Create .gitignore file
cat > .gitignore << EOF
# Python
__pycache__/
*.pyc
venv/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/

# Personal
notes.txt
secrets.env
EOF

# Add and commit
git add .gitignore
git commit -m "Add .gitignore file"
```
</details>

---

### التمرين 19: عرض الفروق

**المهمة**: عدّل ملفًا واعرض الفروق.

<details>
<summary>اضغط لعرض الحل</summary>

```bash
# Edit index.html (add a paragraph)
echo "<p>New content</p>" >> index.html

# View differences (not staged)
git diff

# Stage the changes
git add index.html

# View staged differences
git diff --staged

# Commit
git commit -m "Add new paragraph to index.html"
```
</details>

---

### التمرين 20: الربط بـ GitHub

**المهمة**: أنشئ مستودعًا على GitHub وادفع الكود.

<details>
<summary>اضغط لعرض الحل</summary>

```bash
# 1. Create repository on GitHub.com (via browser)
#    Name: my-website
#    Don't initialize with README

# 2. Connect local repository to GitHub
git remote add origin https://github.com/your-username/my-website.git

# 3. Verify remote
git remote -v

# 4. Push to GitHub
git push -u origin main

# 5. For future pushes
git push
```
</details>

---

## اليوم 5: مشروع البورتفوليو

### التمرين 21: إنشاء هيكل بورتفوليو أساسي

**المهمة**: أنشئ بورتفوليو ببنية HTML صحيحة وأقسام.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Your Name</h1>
        <p>Web Developer</p>
    </header>

    <nav>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </nav>

    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>Write about yourself here...</p>
        </section>

        <section id="skills">
            <h2>Skills</h2>
            <ul>
                <li>Python</li>
                <li>HTML</li>
                <li>CSS</li>
                <li>Git</li>
            </ul>
        </section>

        <section id="projects">
            <h2>Projects</h2>
            <p>Coming soon...</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <form>
                <input type="text" placeholder="Name" required>
                <input type="email" placeholder="Email" required>
                <textarea placeholder="Message" required></textarea>
                <button type="submit">Send</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Your Name</p>
    </footer>
</body>
</html>
```
</details>

---

### التمرين 22: تنسيق البورتفوليو

**المهمة**: أضف CSS لجعل البورتفوليو يبدو احترافيًا.

<details>
<summary>اضغط لعرض الحل</summary>

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
}

section h2 {
    color: #667eea;
    margin-bottom: 20px;
    font-size: 32px;
}

footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 20px;
}
```
</details>

---

## تمارين التحدي

### التحدي 1: موقع بورتفوليو كامل

**المهمة**: ابنِ بورتفوليو كاملًا يحتوي على:
- ترويسة بالاسم واللقب
- شريط تنقل
- قسم نبذة مع صورة
- قسم مهارات مع قائمة
- قسم مشاريع (يمكن أن يكون مؤقتًا)
- نموذج تواصل
- تذييل
- تنسيق كامل بـ CSS

<details>
<summary>اضغط لعرض الحل</summary>

هذا يجمع جميع التمارين السابقة. استخدم مثال البورتفوليو في الدروس كنقطة انطلاق وعدّل بياناتك وألوانك وأسلوبك.
</details>

---

### التحدي 2: تخطيط بطاقات متجاوب

**المهمة**: أنشئ صفحة ببطاقات تعرض خدمات أو مشاريع مختلفة.

<details>
<summary>اضغط لعرض الحل</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Services</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .cards {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 30px;
        }

        .card {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            flex: 1 1 300px;
        }

        .card h2 {
            color: #667eea;
            margin-bottom: 15px;
        }

        .card p {
            color: #666;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Our Services</h1>

        <div class="cards">
            <div class="card">
                <h2>Web Development</h2>
                <p>Build modern, responsive websites using the latest technologies.</p>
            </div>

            <div class="card">
                <h2>App Development</h2>
                <p>Create mobile applications for iOS and Android platforms.</p>
            </div>

            <div class="card">
                <h2>UI/UX Design</h2>
                <p>Design beautiful and intuitive user interfaces.</p>
            </div>
        </div>
    </div>
</body>
</html>
```
</details>

---

### التحدي 3: موقع متعدد الصفحات مع Git

**المهمة**: أنشئ موقعًا متعدد الصفحات يحتوي على:
- index.html (الصفحة الرئيسية)
- about.html (صفحة من نحن)
- contact.html (صفحة تواصل)
- ملف style.css مشترك
- روابط تنقل بين الصفحات
- رفع إلى GitHub

<details>
<summary>اضغط لعرض الحل</summary>

**index.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home - My Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
    </nav>

    <main>
        <h1>Welcome to My Website</h1>
        <p>This is the home page.</p>
    </main>
</body>
</html>
```

**about.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About - My Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
    </nav>

    <main>
        <h1>About Us</h1>
        <p>Learn more about us here.</p>
    </main>
</body>
</html>
```

**contact.html:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Contact - My Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
    </nav>

    <main>
        <h1>Contact Us</h1>
        <form>
            <input type="text" placeholder="Name" required><br>
            <input type="email" placeholder="Email" required><br>
            <textarea placeholder="Message" required></textarea><br>
            <button type="submit">Send</button>
        </form>
    </main>
</body>
</html>
```

**style.css:**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

nav {
    background-color: #333;
    padding: 15px;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 10px 20px;
    margin: 0 5px;
}

nav a:hover {
    background-color: #555;
}

main {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
}
```

**أوامر Git:**
```bash
git init
git add .
git commit -m "Initial commit: Add multi-page website"
git remote add origin https://github.com/your-username/my-website.git
git push -u origin main
```
</details>

---

### التحدي 4: عرض بيانات JSON

**المهمة**: أنشئ سكربت بايثون يقرأ بيانات JSON ويولد HTML.

<details>
<summary>اضغط لعرض الحل</summary>

**data.json:**
```json
{
    "name": "Ahmed Ali",
    "title": "Python Developer",
    "skills": ["Python", "HTML", "CSS", "Git"],
    "projects": [
        {
            "name": "Calculator",
            "description": "A simple calculator app"
        },
        {
            "name": "To-Do List",
            "description": "Task management application"
        }
    ]
}
```

**generate_portfolio.py:**
```python
import json

# Read JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Generate HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{data['name']} - Portfolio</title>
</head>
<body>
    <h1>{data['name']}</h1>
    <p>{data['title']}</p>

    <h2>Skills</h2>
    <ul>
"""

for skill in data['skills']:
    html += f"        <li>{skill}</li>\n"

html += """    </ul>

    <h2>Projects</h2>
"""

for project in data['projects']:
    html += f"""    <div>
        <h3>{project['name']}</h3>
        <p>{project['description']}</p>
    </div>
"""

html += """</body>
</html>"""

# Write HTML file
with open('portfolio.html', 'w') as file:
    file.write(html)

print("Portfolio generated successfully!")
```

**Run:**
```bash
python generate_portfolio.py
```
</details>

---

## نصائح للنجاح

1. **تدرّب على هيكل HTML** - ابدأ دائمًا بـ DOCTYPE وبنية صحيحة
2. **استخدم HTML الدلالي** - استخدم وسومًا ذات معنى (header, nav, main, section, footer)
3. **نظّم CSS** - اجمع الأنماط المتشابهة معًا
4. **اختبر في المتصفح** - اعرض صفحاتك دائمًا في المتصفح
5. **استخدم Git بشكل متكرر** - نفّذ commit بعد كل تغيير مهم
6. **اكتب رسائل commit جيدة** - كن واضحًا ومختصرًا
7. **تحقق من HTML** - استخدم أداة W3C للتحقق
8. **حافظ على البساطة** - ابدأ بسيطًا ثم طوّر

---

## التقييم الذاتي

بعد إنهاء هذه التمارين، ينبغي أن تكون قادرًا على:

- [ ] إنشاء بنية HTML صحيحة
- [ ] استخدام وسوم HTML الشائعة (عناوين، فقرات، روابط، صور، قوائم)
- [ ] بناء نماذج HTML بأنواع إدخال مختلفة
- [ ] تطبيق CSS بطرق مختلفة (داخل السطر، داخلي، خارجي)
- [ ] استخدام محددات CSS (عنصر، فئة، معرّف)
- [ ] تنسيق النصوص والخلفيات والصناديق
- [ ] فهم نموذج الصندوق
- [ ] تهيئة واستخدام مستودعات Git
- [ ] تنفيذ commits وعرض السجل
- [ ] الربط بـ GitHub ودفع الكود
- [ ] إنشاء موقع بورتفوليو كامل

---

برمجة سعيدة! تذكّر أن تنفذ commits بانتظام وأن ترفع مشاريعك إلى GitHub لبناء بورتفوليو قوي.
