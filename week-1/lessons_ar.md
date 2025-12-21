# دروس الأسبوع الأول: أساسيات الكمبيوتر والويب + مقدمة في Python

مرحباً بك في الأسبوع الأول من رحلتك في تطوير الويب باستخدام Django! هذا الأسبوع ستتعلم أساسيات كيفية عمل الويب وستبدأ البرمجة باستخدام Python.

---

## جدول المحتويات

1. [فهم الويب](#فهم-الويب)
2. [إعداد بيئة التطوير الخاصة بك](#إعداد-بيئة-التطوير-الخاصة-بك)
3. [أساسيات Python: المتغيرات وأنواع البيانات](#أساسيات-python-المتغيرات-وأنواع-البيانات)
4. [التحكم في التدفق: اتخاذ القرارات](#التحكم-في-التدفق-اتخاذ-القرارات)
5. [الحلقات: تكرار الإجراءات](#الحلقات-تكرار-الإجراءات)
6. [مشروع صغير: حاسبة درجات الطلاب](#مشروع-صغير-حاسبة-درجات-الطلاب)

---

## فهم الويب

### ما هو الويب؟

الويب (World Wide Web) هو نظام من المستندات والموارد المترابطة التي يمكنك الوصول إليها عبر الإنترنت باستخدام المتصفح.

**المصطلحات الأساسية:**

**الموقع الإلكتروني (Website)**: مجموعة من صفحات الويب المرتبطة ببعضها ويتم الوصول إليها من خلال اسم نطاق.
- أمثلة: google.com, facebook.com, github.com

**النطاق (Domain)**: عنوان قابل للقراءة البشرية لموقع ويب.
- مثال: `www.example.com`

**عنوان URL (Uniform Resource Locator)**: العنوان الكامل لمورد على الويب.
- مثال: `https://www.example.com/page.html`
- الأجزاء:
  - `https://` - البروتوكول (Protocol)
  - `www.example.com` - النطاق (Domain)
  - `/page.html` - المسار إلى مورد محدد (Path)

### المتصفح مقابل الخادم

**المتصفح (Browser) - العميل (Client)**:
- التطبيق الذي تستخدمه للوصول إلى المواقع (Chrome, Firefox, Safari, Edge)
- يرسل طلبات لصفحات الويب
- يعرض المحتوى المستلم لك
- فكر فيه كعميل في مطعم

**الخادم (Server)**:
- جهاز كمبيوتر قوي يخزن المواقع وتطبيقات الويب
- ينتظر الطلبات من المتصفحات
- يرسل المحتوى المطلوب
- فكر فيه كالمطبخ في المطعم

### HTTP: لغة الويب

**HTTP** (Hypertext Transfer Protocol) هو كيفية تواصل المتصفحات والخوادم.

**طرق HTTP الشائعة:**

**GET**: طلب للحصول على/استرجاع البيانات
- مثال: تحميل صفحة ويب
- مثل السؤال "هل يمكنني رؤية القائمة؟"

**POST**: طلب لإرسال/إرسال البيانات
- مثال: إرسال نموذج، إنشاء منشور جديد
- مثل تقديم طلب

**رموز حالة HTTP:**
- **200 OK**: نجاح! الطلب نجح
- **404 Not Found**: المورد المطلوب غير موجود
- **500 Internal Server Error**: حدث خطأ ما على الخادم

### كيف يتم تحميل موقع ويب

```
1. تكتب www.example.com في متصفحك
2. المتصفح يرسل طلب HTTP GET إلى الخادم
3. الخادم يجد الصفحة المطلوبة
4. الخادم يرسل استجابة HTTP مع HTML, CSS, JS
5. المتصفح يستقبل ويعرض الصفحة
```

**جرب هذا:**
1. افتح متصفحك
2. اضغط F12 لفتح أدوات المطور (Developer Tools)
3. انتقل إلى علامة التبويب "Network"
4. قم بزيارة أي موقع
5. شاهد طلبات HTTP تحدث في الوقت الفعلي!

---

## إعداد بيئة التطوير الخاصة بك

قبل أن تتمكن من بدء البرمجة، تحتاج إلى تثبيت الأدوات اللازمة.

### ما الذي ستقوم بتثبيته:

1. **Python** - لغة البرمجة
2. **VS Code** - حيث ستكتب الكود الخاص بك
3. **Git** - التحكم في الإصدار لتتبع تغييرات الكود الخاصة بك
4. **حساب GitHub** - لتخزين ومشاركة الكود الخاص بك عبر الإنترنت

### خطوات التثبيت

راجع ملف `setup-instructions.md` للحصول على أدلة تثبيت مفصلة خطوة بخطوة لنظام التشغيل الخاص بك.

### برنامج Python الأول الخاص بك

بعد تثبيت Python و VS Code:

1. أنشئ مجلداً يسمى `python-training`
2. افتح VS Code
3. افتح المجلد: File → Open Folder
4. أنشئ ملفاً جديداً: `hello.py`
5. اكتب هذا الكود:

```python
print("Hello, World!")
```

6. احفظ الملف (Ctrl+S أو Cmd+S)
7. انقر بزر الماوس الأيمن في المحرر → Run Python File in Terminal

يجب أن ترى: `Hello, World!`

مبروك! لقد كتبت وقمت بتشغيل برنامج Python الأول الخاص بك!

---

## أساسيات Python: المتغيرات وأنواع البيانات

### ما هو المتغير؟

المتغير مثل صندوق معنون حيث يمكنك تخزين المعلومات.

```python
name = "Ahmed"
```

هنا:
- `name` هو اسم المتغير (العنوان على الصندوق)
- `=` هو عامل التعيين (وضع شيء في الصندوق)
- `"Ahmed"` هي القيمة (ما بداخل الصندوق)

### قواعد تسمية المتغيرات

**أسماء متغيرات جيدة:**
```python
age = 25
first_name = "Sara"
total_price = 100.50
is_student = True
```

**القواعد:**
- استخدم الحروف والأرقام والشرطات السفلية فقط
- يجب أن تبدأ بحرف أو شرطة سفلية
- لا يمكن استخدام كلمات Python الأساسية (مثل `if`, `for`, `while`)
- حساس لحالة الأحرف (`Name` و `name` مختلفان)

**الاتفاقية:**
- استخدم الأحرف الصغيرة مع الشرطات السفلية: `my_variable`
- استخدم أسماء وصفية: `student_age` وليس `sa`

### أنواع البيانات

Python لديها عدة أنواع بيانات أساسية:

#### 1. العدد الصحيح (Integer - int)
الأعداد الكاملة، موجبة أو سالبة.

```python
age = 25
temperature = -5
year = 2024
```

#### 2. العدد العشري (Float - float)
الأعداد العشرية.

```python
height = 1.75
price = 99.99
temperature = 36.6
```

#### 3. النص (String - str)
النص، محاط بعلامات اقتباس.

```python
name = "Mohammed"
message = 'Hello, World!'
address = "123 Main Street"
```

#### 4. القيمة المنطقية (Boolean - bool)
قيم True أو False.

```python
is_student = True
has_graduated = False
is_raining = False
```

### التحقق من الأنواع

استخدم دالة `type()`:

```python
age = 25
print(type(age))  # <class 'int'>

name = "Ahmed"
print(type(name))  # <class 'str'>

height = 1.75
print(type(height))  # <class 'float'>

is_active = True
print(type(is_active))  # <class 'bool'>
```

### الإدخال والإخراج

#### الإخراج باستخدام print()

```python
print("Hello")
print("Welcome to Python")

name = "Sara"
print(name)

# طباعة أشياء متعددة
print("My name is", name)

# الطباعة باستخدام f-strings (سلاسل منسقة)
age = 22
print(f"My name is {name} and I am {age} years old")
```

#### الإدخال من المستخدم

```python
# الحصول على إدخال نصي
name = input("What is your name? ")
print("Hello, " + name)

# الحصول على إدخال رقمي (يحتاج إلى تحويل)
age = input("What is your age? ")  # هذا نص!
age = int(age)  # تحويل إلى عدد صحيح
print(f"Next year you will be {age + 1}")

# أو قم به في سطر واحد
age = int(input("What is your age? "))
```

### العمليات الأساسية

#### العمليات الحسابية

```python
a = 10
b = 3

print(a + b)   # 13 (الجمع - addition)
print(a - b)   # 7  (الطرح - subtraction)
print(a * b)   # 30 (الضرب - multiplication)
print(a / b)   # 3.333... (القسمة - division)
print(a // b)  # 3  (القسمة الصحيحة - integer division)
print(a % b)   # 1  (الباقي - remainder/modulo)
print(a ** b)  # 1000 (الأس - exponent/power)
```

#### عمليات النصوص

```python
first_name = "Mohammed"
last_name = "Ahmed"

# الدمج (Concatenation - joining)
full_name = first_name + " " + last_name
print(full_name)  # Mohammed Ahmed

# التكرار (Repetition)
print("Ha" * 3)  # HaHaHa

# الطول (Length)
print(len(full_name))  # 14
```

### تحويل الأنواع

التحويل بين أنواع البيانات:

```python
# من نص إلى عدد صحيح (String to Integer)
age_str = "25"
age_num = int(age_str)
print(age_num + 5)  # 30

# من نص إلى عدد عشري (String to Float)
price_str = "99.99"
price_num = float(price_str)
print(price_num * 2)  # 199.98

# من عدد صحيح إلى نص (Integer to String)
age = 25
age_str = str(age)
print("I am " + age_str + " years old")

# أو استخدم f-string (أسهل)
print(f"I am {age} years old")
```

### التعليقات

التعليقات هي ملاحظات في الكود الخاص بك يتجاهلها Python.

```python
# هذا تعليق من سطر واحد

x = 5  # يمكنك أيضاً وضع التعليقات بعد الكود

"""
هذا تعليق
متعدد الأسطر
يمكن أن يمتد لعدة أسطر
"""

# التعليقات مفيدة لـ:
# 1. شرح ما يفعله الكود
# 2. تعطيل الكود مؤقتاً
# 3. ترك ملاحظات لنفسك أو للآخرين
```

### مثال تطبيقي: برنامج معلومات شخصية

```python
# الحصول على معلومات المستخدم
name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height in meters? "))
is_student = input("Are you a student? (yes/no) ")

# تحويل yes/no إلى True/False
is_student = (is_student.lower() == "yes")

# عرض المعلومات
print("\n--- Your Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Student: {is_student}")
print(f"Next year you will be {age + 1} years old")
```

---

## التحكم في التدفق: اتخاذ القرارات

البرامج تحتاج إلى اتخاذ قرارات بناءً على الشروط. هنا يأتي دور جمل `if`.

### التعبيرات المنطقية

التعبيرات المنطقية تقيم إلى `True` أو `False`.

```python
5 > 3   # True
5 < 3   # False
5 == 5  # True (يساوي - equal to)
5 != 3  # True (لا يساوي - not equal to)
5 >= 5  # True (أكبر من أو يساوي - greater than or equal to)
3 <= 2  # False (أصغر من أو يساوي - less than or equal to)
```

**مهم**:
- `=` هو التعيين (إعطاء قيمة)
- `==` هو المقارنة (التحقق من المساواة)

### جملة if

```python
age = 18

if age >= 18:
    print("You are an adult")
```

**الهيكل:**
- كلمة `if`
- الشرط (يجب أن يكون True أو False)
- نقطتان `:`
- كتلة كود مسافة بادئة (ما يجب فعله إذا كان True)

**المسافة البادئة حاسمة في Python!** استخدم 4 مسافات أو Tab.

### جملة if-else

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```

### جملة if-elif-else

للشروط المتعددة:

```python
grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

**كيف يعمل:**
1. يتحقق من شرط `if` الأول
2. إذا كان False، يتحقق من `elif` الأول
3. إذا كان False، يتحقق من `elif` التالي
4. يستمر حتى يكون أحدها True
5. إذا لم يكن أي منها True، ينفذ `else`
6. كتلة واحدة فقط من الكود تعمل!

### العوامل المنطقية

دمج شروط متعددة:

#### and - يجب أن يكون كلاهما True

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("Access denied")
```

#### or - يجب أن يكون واحد على الأقل True

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")
```

#### not - عكس الشرط

```python
is_raining = False

if not is_raining:
    print("Good day to go out!")
else:
    print("Take an umbrella")
```

### جمل if المتداخلة

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You're too young to drive")
```

### أمثلة عملية

#### مثال 1: نصيحة درجة الحرارة

```python
temperature = int(input("What's the temperature? "))

if temperature > 35:
    print("Very hot! Stay hydrated")
elif temperature > 25:
    print("Nice weather")
elif temperature > 15:
    print("A bit cool, bring a jacket")
else:
    print("It's cold!")
```

#### مثال 2: نظام تسجيل الدخول

```python
username = "admin"
password = "secret123"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username and pass_input == password:
    print("Login successful!")
else:
    print("Invalid credentials")
```

#### مثال 3: زوجي أو فردي

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

---

## الحلقات: تكرار الإجراءات

الحلقات تتيح لك تكرار الكود عدة مرات دون كتابته مراراً وتكراراً.

### حلقة for

تستخدم عندما تعرف كم مرة تريد التكرار.

#### حلقة for أساسية مع range()

```python
# طباعة "Hello" 5 مرات
for i in range(5):
    print("Hello")
```

#### فهم range()

```python
# range(n) - من 0 إلى n-1
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# range(start, stop) - من start إلى stop-1
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10

# العد التنازلي
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, ..., 1
```

#### أمثلة عملية لحلقة for

```python
# مجموع الأرقام من 1 إلى 10
total = 0
for i in range(1, 11):
    total += i  # نفس total = total + i
print(f"Sum: {total}")

# جدول الضرب
number = 5
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

# طباعة الأرقام الزوجية
for i in range(2, 21, 2):
    print(i)
```

### حلقة while

تستخدم عندما لا تعرف كم مرة تريد التكرار.

```python
count = 1
while count <= 5:
    print(count)
    count += 1  # مهم: لا تنسى التحديث!
```

**تحذير**: تأكد دائماً من أن الشرط سيصبح False في النهاية، وإلا ستحصل على حلقة لا نهائية!

#### حلقة لا نهائية (لا تفعل هذا!)

```python
# سيء - هذا لن يتوقف أبداً!
while True:
    print("Forever...")
# استخدم Ctrl+C للإيقاف إذا حدث هذا
```

#### أمثلة عملية لحلقة while

```python
# نظام إعادة محاولة كلمة المرور
password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access granted!")
        break  # الخروج من الحلقة
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong! {remaining} attempts left")

if attempts == max_attempts:
    print("Account locked!")
```

```python
# لعبة تخمين الرقم
secret = 7

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret:
        print("Correct! You win!")
        break
    elif guess < secret:
        print("Too low! Try again")
    else:
        print("Too high! Try again")
```

### break و continue

#### break - الخروج من الحلقة فوراً

```python
for i in range(10):
    if i == 5:
        break  # التوقف عندما i يساوي 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

#### continue - التخطي إلى التكرار التالي

```python
for i in range(5):
    if i == 2:
        continue  # تخطي عندما i يساوي 2
    print(i)
# Output: 0, 1, 3, 4
```

### الحلقات المتداخلة

حلقات داخل حلقات:

```python
# جدول الضرب لـ 2 و 3
for number in range(2, 4):
    print(f"\nTable for {number}:")
    for i in range(1, 6):
        print(f"{number} × {i} = {number * i}")
```

### أنماط الحلقات الشائعة

#### النمط 1: المجمّع (Accumulator)

```python
# مجموع جميع الأرقام من 1 إلى 100
total = 0
for i in range(1, 101):
    total += i
print(total)
```

#### النمط 2: العداد (Counter)

```python
# عد كم عدد زوجي من 1 إلى 20
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
print(f"There are {count} even numbers")
```

#### النمط 3: البحث (Search)

```python
# البحث عما إذا كان رقم في نطاق
target = 42
found = False

for i in range(1, 101):
    if i == target:
        found = True
        break

if found:
    print(f"Found {target}!")
else:
    print(f"{target} not found")
```

---

## مشروع صغير: حاسبة درجات الطلاب

الآن دعنا نجمع كل شيء معاً!

### متطلبات المشروع

أنشئ برنامجاً:
1. يسأل عن عدد الطلاب
2. يحصل على درجة كل طالب
3. يحسب المتوسط
4. يعد الطلاب الناجحين (الدرجة >= 60)
5. يظهر ما إذا كان الصف نجح بشكل عام

### الحل خطوة بخطوة

```python
# الخطوة 1: الحصول على عدد الطلاب
num_students = int(input("How many students? "))

# الخطوة 2: تهيئة المتغيرات
total_grades = 0
passing_students = 0

# الخطوة 3: حلقة للحصول على كل درجة
print("\nEnter grades:")
for i in range(num_students):
    # الحصول على درجة الطالب i+1 (لأن i يبدأ من 0)
    grade = float(input(f"Student {i + 1}: "))

    # إضافة إلى المجموع
    total_grades += grade

    # التحقق من النجاح
    if grade >= 60:
        passing_students += 1

# الخطوة 4: حساب المتوسط
average = total_grades / num_students

# الخطوة 5: عرض النتائج
print("\n" + "="*40)
print("CLASS RESULTS")
print("="*40)
print(f"Number of students: {num_students}")
print(f"Average grade: {average:.2f}")
print(f"Students passed: {passing_students}")
print(f"Students failed: {num_students - passing_students}")

# الحالة العامة
if average >= 60:
    print("\n✓ The class PASSED overall")
else:
    print("\n✗ The class FAILED overall")
```

### فهم الكود

**سطر بسطر:**

```python
num_students = int(input("How many students? "))
```
- يحصل على إدخال من المستخدم
- يحوله إلى عدد صحيح
- يخزنه في `num_students`

```python
total_grades = 0
passing_students = 0
```
- تهيئة المجمعات
- تبدأ من 0، سنضيف إليها لاحقاً

```python
for i in range(num_students):
```
- حلقة لهذا العدد من المرات
- `i` يذهب من 0 إلى num_students-1

```python
grade = float(input(f"Student {i + 1}: "))
```
- الحصول على الدرجة (كرقم عشري)
- استخدم `i + 1` للعرض (Student 1, 2, 3... بدلاً من 0, 1, 2...)

```python
total_grades += grade
```
- إضافة الدرجة الحالية إلى المجموع الجاري
- نفس `total_grades = total_grades + grade`

```python
if grade >= 60:
    passing_students += 1
```
- التحقق من نجاح الطالب
- إذا نعم، زيادة العداد

```python
average = total_grades / num_students
```
- حساب المتوسط
- المجموع مقسوماً على العدد

```python
print(f"Average grade: {average:.2f}")
```
- `:.2f` يعني عرض منزلتين عشريتين

### اختبار برنامجك

جرب حالات الاختبار هذه:

**الاختبار 1: الجميع ينجح**
- 3 طلاب
- الدرجات: 90, 85, 75
- المتوقع: المتوسط 83.33، 3 نجحوا

**الاختبار 2: مختلط**
- 5 طلاب
- الدرجات: 90, 50, 70, 45, 80
- المتوقع: المتوسط 67، 3 نجحوا، 2 رسبوا

**الاختبار 3: الجميع يرسب**
- 2 طلاب
- الدرجات: 45, 30
- المتوقع: المتوسط 37.5، 0 نجحوا، الصف رسب

---

## النقاط الرئيسية من الأسبوع الأول

**المفاهيم:**
- الويب يعتمد على التواصل بين العميل والخادم
- HTTP هو البروتوكول الذي تستخدمه المتصفحات والخوادم
- Python هي لغة برمجة قوية وسهلة التعلم

**المهارات:**
- إعداد بيئة التطوير
- كتابة نصوص Python
- استخدام المتغيرات وأنواع البيانات
- اتخاذ قرارات باستخدام جمل if
- تكرار الإجراءات باستخدام الحلقات
- دمج المفاهيم لبناء برنامج كامل

**أفضل الممارسات:**
- استخدم أسماء متغيرات وصفية
- أضف تعليقات لشرح الكود الخاص بك
- اختبر الكود الخاص بك بإدخالات مختلفة
- اقرأ رسائل الخطأ بعناية
- قسّم المشاكل إلى خطوات أصغر

---

## الخطوات التالية

**قبل الأسبوع الثاني:**
- أكمل جميع تمارين الممارسة
- راجع ملاحظاتك
- حاول تحسين المشروع الصغير
- تدرب على أوامر الطرفية
- تأكد من تثبيت جميع البرامج بشكل صحيح

**معاينة الأسبوع الثاني:**
ستتعلم عن:
- القوائم والقواميس (Lists and dictionaries)
- الدوال (Functions)
- الوحدات والحزم (Modules and packages)
- البيئات الافتراضية (Virtual environments)

استمر في الممارسة ونراك الأسبوع القادم!

---

## الأخطاء الشائعة وكيفية إصلاحها

### SyntaxError: invalid syntax

**المشكلة:**
```python
if age >= 18  # نقص النقطتين
    print("Adult")
```

**الإصلاح:**
```python
if age >= 18:  # إضافة النقطتين
    print("Adult")
```

### IndentationError

**المشكلة:**
```python
if age >= 18:
print("Adult")  # لا توجد مسافة بادئة
```

**الإصلاح:**
```python
if age >= 18:
    print("Adult")  # مسافة بادئة بـ 4 مسافات أو Tab
```

### NameError: name 'x' is not defined

**المشكلة:**
```python
print(age)  # age غير موجود بعد
age = 25
```

**الإصلاح:**
```python
age = 25  # التعريف قبل الاستخدام
print(age)
```

### TypeError: unsupported operand type(s)

**المشكلة:**
```python
age = "25"
next_age = age + 1  # لا يمكن إضافة رقم إلى نص
```

**الإصلاح:**
```python
age = int("25")  # التحويل إلى عدد صحيح
next_age = age + 1
```

### ValueError: invalid literal for int()

**المشكلة:**
```python
age = int("hello")  # لا يمكن تحويل "hello" إلى رقم
```

**الإصلاح:**
```python
# تأكد من أن الإدخال رقم صحيح
age = int("25")  # هذا يعمل
```

---

تذكر: **الجميع يرتكب هذه الأخطاء عند التعلم!** قراءة رسائل الخطأ والتصحيح جزء طبيعي من البرمجة. لا تشعر بالإحباط!

برمجة سعيدة!
