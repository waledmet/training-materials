# دروس الأسبوع الثاني: أساسيات Python (تعميق المهارات)

مرحباً بك في الأسبوع الثاني! هذا الأسبوع ستتقن هياكل بيانات Python الأساسية وتتعلم كتابة كود قابل لإعادة الاستخدام ومنظم مع الدوال والوحدات النمطية.

---

## جدول المحتويات

1. [القوائم: العمل مع المجموعات](#القوائم-العمل-مع-المجموعات)
2. [المجموعات: التسلسلات غير القابلة للتغيير](#المجموعات-التسلسلات-غير-القابلة-للتغيير)
3. [القواميس: أزواج المفتاح-القيمة](#القواميس-أزواج-المفتاح-القيمة)
4. [المجموعات الفريدة: المجموعات الفريدة](#المجموعات-الفريدة-المجموعات-الفريدة)
5. [الدوال: كتل الكود القابلة لإعادة الاستخدام](#الدوال-كتل-الكود-القابلة-لإعادة-الاستخدام)
6. [الوحدات والحزم](#الوحدات-والحزم)
7. [معالجة الأخطاء](#معالجة-الأخطاء)
8. [البيئات الافتراضية](#البيئات-الافتراضية)
9. [مشروع صغير: تطبيق قائمة المهام](#مشروع-صغير-تطبيق-قائمة-المهام)

---

## القوائم: العمل مع المجموعات

### ما هي القائمة؟

القائمة هي مثل حاوية يمكنها احتواء عناصر متعددة بترتيب معين. فكر فيها مثل قائمة التسوق أو قائمة المهام.

**إنشاء القوائم:**

```python
# قائمة فارغة
shopping_list = []

# قائمة مع عناصر
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # يمكن خلط الأنواع!

# التحقق من الطول
print(len(fruits))  # 3
```

### الوصول إلى عناصر القائمة

القوائم تستخدم أرقام الفهرس بدءاً من 0:

```python
fruits = ["apple", "banana", "orange", "grape"]

# الوصول بالفهرس
print(fruits[0])   # apple (أول عنصر)
print(fruits[1])   # banana
print(fruits[-1])  # grape (آخر عنصر)
print(fruits[-2])  # orange (الثاني من النهاية)

# التقطيع (الحصول على عناصر متعددة)
print(fruits[1:3])   # ['banana', 'orange']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['orange', 'grape']
```

### تعديل القوائم

القوائم **قابلة للتغيير** (يمكن تغييرها):

```python
fruits = ["apple", "banana", "orange"]

# تغيير عنصر
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'orange']

# إضافة عناصر
fruits.append("grape")       # إضافة إلى النهاية
print(fruits)  # ['apple', 'mango', 'orange', 'grape']

fruits.insert(1, "kiwi")     # إدراج في الموقع 1
print(fruits)  # ['apple', 'kiwi', 'mango', 'orange', 'grape']

# إزالة عناصر
fruits.remove("mango")       # إزالة بالقيمة
print(fruits)  # ['apple', 'kiwi', 'orange', 'grape']

last_fruit = fruits.pop()    # إزالة وإرجاع آخر عنصر
print(last_fruit)  # grape
print(fruits)  # ['apple', 'kiwi', 'orange']

fruits.pop(0)               # إزالة العنصر في الفهرس 0
print(fruits)  # ['kiwi', 'orange']
```

### عمليات القائمة

```python
# دمج القوائم
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# تكرار القائمة
repeated = [0] * 5
print(repeated)  # [0, 0, 0, 0, 0]

# التحقق من وجود عنصر
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)    # True
print("grape" in fruits)    # False

# عد التكرارات
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # 3

# إيجاد الفهرس
fruits = ["apple", "banana", "orange"]
print(fruits.index("banana"))  # 1
```

### التكرار عبر القوائم

```python
fruits = ["apple", "banana", "orange"]

# الطريقة 1: التكرار عبر العناصر
for fruit in fruits:
    print(fruit)

# الطريقة 2: التكرار مع الفهرس
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# الطريقة 3: التكرار مع enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### ملخص دوال القائمة

```python
fruits = ["apple", "banana", "orange"]

# إضافة عناصر
fruits.append("grape")      # إضافة إلى النهاية
fruits.insert(0, "kiwi")    # إدراج في موقع
fruits.extend([1, 2, 3])    # إضافة عناصر متعددة

# إزالة عناصر
fruits.remove("apple")      # إزالة بالقيمة
fruits.pop()                # إزالة الأخير
fruits.pop(0)               # إزالة في الفهرس
fruits.clear()              # إزالة الكل

# الترتيب
numbers = [3, 1, 4, 1, 5]
numbers.sort()              # ترتيب في المكان
print(numbers)              # [1, 1, 3, 4, 5]

numbers.reverse()           # عكس في المكان
print(numbers)              # [5, 4, 3, 1, 1]

# النسخ
original = [1, 2, 3]
copy1 = original.copy()     # إنشاء نسخة
copy2 = original[:]         # طريقة أخرى للنسخ
```

### مثال عملي: إدارة الطلاب

```python
# قائمة أسماء الطلاب
students = ["Ahmed", "Sara", "Mohammed"]

# إضافة طالب جديد
students.append("Fatima")
print(f"Students: {students}")

# إزالة طالب
students.remove("Sara")
print(f"After removal: {students}")

# التحقق من وجود طالب
name = input("Enter student name: ")
if name in students:
    print(f"{name} is in the class")
else:
    print(f"{name} is not in the class")

# طباعة جميع الطلاب
print("\nClass roster:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student}")
```

---

## المجموعات: التسلسلات غير القابلة للتغيير

### ما هي المجموعة؟

المجموعة مثل القائمة، ولكنها **غير قابلة للتغيير** (لا يمكن تغييرها بعد الإنشاء). استخدم المجموعات للبيانات التي لا ينبغي تغييرها.

**إنشاء المجموعات:**

```python
# مجموعة فارغة
empty = ()

# مجموعة مع عناصر
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed = (1, "hello", 3.14)

# مجموعة بعنصر واحد (لاحظ الفاصلة!)
single = (42,)     # هذه مجموعة
not_tuple = (42)   # هذا مجرد int!

# بدون أقواس (تعبئة المجموعة)
point = 10, 20, 30
print(type(point))  # <class 'tuple'>
```

### الوصول إلى عناصر المجموعة

نفس القوائم:

```python
coordinates = (10, 20, 30)

print(coordinates[0])   # 10
print(coordinates[-1])  # 30
print(coordinates[1:3]) # (20, 30)

# فك المجموعة
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# تبديل المتغيرات باستخدام المجموعات
a = 5
b = 10
a, b = b, a  # تبديل!
print(a, b)  # 10 5
```

### متى تستخدم المجموعات

```python
# 1. إرجاع قيم متعددة من الدوال
def get_user_info():
    name = "Ahmed"
    age = 25
    city = "Riyadh"
    return name, age, city  # ترجع مجموعة

user_name, user_age, user_city = get_user_info()

# 2. استخدامها كمفاتيح القاموس (القوائم لا تستطيع ذلك!)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}

# 3. حماية البيانات من التعديل
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
```

---

## القواميس: أزواج المفتاح-القيمة

### ما هو القاموس؟

القاموس يخزن البيانات في **أزواج مفتاح-قيمة**. فكر فيه مثل القاموس الحقيقي حيث تبحث عن كلمة (مفتاح) لإيجاد معناها (قيمة).

**إنشاء القواميس:**

```python
# قاموس فارغ
empty = {}

# قاموس مع بيانات
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5,
    "is_active": True
}

# طريقة أخرى
person = dict(name="Sara", age=25, city="Jeddah")
```

### الوصول إلى قيم القاموس

```python
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5
}

# الوصول بالمفتاح
print(student["name"])   # Ahmed
print(student["age"])    # 22

# الوصول الآمن مع ()get
print(student.get("name"))    # Ahmed
print(student.get("email"))   # None (غير موجود)
print(student.get("email", "No email"))  # قيمة افتراضية
```

### تعديل القواميس

```python
student = {
    "name": "Ahmed",
    "age": 22
}

# إضافة/تعديل العناصر
student["email"] = "ahmed@example.com"  # إضافة جديد
student["age"] = 23                     # تعديل موجود

print(student)
# {'name': 'Ahmed', 'age': 23, 'email': 'ahmed@example.com'}

# إزالة العناصر
del student["email"]     # حذف مفتاح محدد

removed_age = student.pop("age")  # إزالة وإرجاع القيمة
print(removed_age)  # 23

student.clear()  # إزالة جميع العناصر
```

### دوال القاموس

```python
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5
}

# الحصول على جميع المفاتيح
print(student.keys())   # dict_keys(['name', 'age', 'grade'])

# الحصول على جميع القيم
print(student.values()) # dict_values(['Ahmed', 22, 85.5])

# الحصول على جميع أزواج المفتاح-القيمة
print(student.items())  # dict_items([('name', 'Ahmed'), ...])

# التحقق من وجود المفتاح
if "name" in student:
    print("Name exists!")

# الحصول على عدد العناصر
print(len(student))  # 3
```

### التكرار عبر القواميس

```python
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5
}

# التكرار عبر المفاتيح
for key in student:
    print(key)

# التكرار عبر المفاتيح صراحة
for key in student.keys():
    print(key)

# التكرار عبر القيم
for value in student.values():
    print(value)

# التكرار عبر أزواج المفتاح-القيمة
for key, value in student.items():
    print(f"{key}: {value}")
```

### مثال عملي: قاعدة بيانات الطلاب

```python
# قاموس بالطلاب
students = {
    "S001": {"name": "Ahmed", "grade": 85, "age": 20},
    "S002": {"name": "Sara", "grade": 92, "age": 19},
    "S003": {"name": "Mohammed", "grade": 78, "age": 21}
}

# الوصول إلى طالب
student_id = "S001"
student = students[student_id]
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

# إضافة طالب جديد
students["S004"] = {
    "name": "Fatima",
    "grade": 88,
    "age": 20
}

# التكرار عبر جميع الطلاب
print("\nAll Students:")
for id, info in students.items():
    print(f"{id}: {info['name']} - Grade: {info['grade']}")

# حساب متوسط الدرجات
total = sum(s['grade'] for s in students.values())
average = total / len(students)
print(f"\nAverage grade: {average:.2f}")
```

---

## المجموعات الفريدة: المجموعات الفريدة

### ما هي المجموعة الفريدة؟

المجموعة الفريدة هي مجموعة **غير مرتبة** من العناصر **الفريدة**. لا توجد عناصر مكررة!

**إنشاء المجموعات الفريدة:**

```python
# مجموعة فارغة (يجب استخدام ()set، وليس {})
empty = set()

# مجموعة مع عناصر
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# تحويل القائمة إلى مجموعة (يزيل المكررات)
numbers_list = [1, 2, 2, 3, 3, 3, 4]
numbers_set = set(numbers_list)
print(numbers_set)  # {1, 2, 3, 4}
```

### عمليات المجموعة الفريدة

```python
# إضافة عناصر
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.add("apple")  # لن يضيف مكرر
print(fruits)  # {'apple', 'banana', 'orange'}

# إزالة عناصر
fruits.remove("banana")      # يرفع خطأ إذا لم يوجد
fruits.discard("grape")      # لا خطأ إذا لم يوجد
fruits.pop()                 # إزالة عنصر عشوائي

# التحقق من العضوية
print("apple" in fruits)  # True

# الحصول على الحجم
print(len(fruits))
```

### العمليات الرياضية للمجموعات

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# الاتحاد (جميع العناصر من كليهما)
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))

# التقاطع (العناصر المشتركة)
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))

# الفرق (في الأول، وليس في الثاني)
print(set1 - set2)  # {1, 2, 3}
print(set1.difference(set2))

# الفرق المتماثل (في أحدهما، ولكن ليس في كليهما)
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))
```

### متى تستخدم المجموعات

```python
# إزالة المكررات
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]

# التحقق من العناصر المشتركة
course1_students = {"Ahmed", "Sara", "Mohammed"}
course2_students = {"Sara", "Ali", "Fatima"}

# من يأخذ كلا الدورتين؟
both_courses = course1_students & course2_students
print(both_courses)  # {'Sara'}

# من يأخذ الدورة 1 فقط؟
only_course1 = course1_students - course2_students
print(only_course1)  # {'Ahmed', 'Mohammed'}
```

---

## الدوال: كتل الكود القابلة لإعادة الاستخدام

### لماذا الدوال؟

الدوال تسمح لك بكتابة الكود مرة واحدة واستخدامه مرات عديدة. مبدأ DRY: لا تكرر نفسك!

### تعريف الدوال

```python
# دالة أساسية
def greet():
    print("Hello!")

# استدعاء الدالة
greet()  # Hello!

# دالة مع معاملات
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ahmed")   # Hello, Ahmed!
greet_person("Sara")    # Hello, Sara!

# معاملات متعددة
def greet_full(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full("Ahmed", "Ali")  # Hello, Ahmed Ali!
```

### قيم الإرجاع

```python
# دالة ترجع قيمة
def add(a, b):
    result = a + b
    return result

sum = add(5, 3)
print(sum)  # 8

# إرجاع قيم متعددة
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# دالة بدون إرجاع (ترجع None)
def print_message(msg):
    print(msg)

result = print_message("Hello")
print(result)  # None
```

### المعاملات الافتراضية

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ahmed")              # Hello, Ahmed!
greet("Sara", "Hi")         # Hi, Sara!
greet("Ali", greeting="Hey")  # Hey, Ali!

# القيم الافتراضية يجب أن تكون في النهاية
def create_profile(name, age=18, city="Riyadh"):
    return {"name": name, "age": age, "city": city}

profile1 = create_profile("Ahmed")
profile2 = create_profile("Sara", 25)
profile3 = create_profile("Ali", 30, "Jeddah")
```

### النطاق: المتغيرات المحلية مقابل العامة

```python
# متغير عام
x = 10

def print_x():
    print(x)  # يمكن قراءة المتغير العام

print_x()  # 10

# متغير محلي
def my_function():
    y = 20  # محلي لهذه الدالة
    print(y)

my_function()  # 20
# print(y)  # خطأ! y غير موجود خارج الدالة

# تعديل المتغيرات العامة
count = 0

def increment():
    global count  # نعلن أننا نريد تعديل العامة
    count += 1

increment()
increment()
print(count)  # 2
```

### مثال عملي: حاسبة الضريبة

```python
def calculate_tax(price, tax_rate=0.15):
    """
    حساب السعر الإجمالي بما في ذلك الضريبة.

    Args:
        price: السعر الأساسي
        tax_rate: معدل الضريبة (افتراضي 15٪)

    Returns:
        السعر الإجمالي بما في ذلك الضريبة
    """
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

# استخدام الدالة
item_price = 100
total_price = calculate_tax(item_price)
print(f"Total: ${total_price:.2f}")  # Total: $115.00

# مع معدل ضريبة مخصص
total_price = calculate_tax(100, 0.20)
print(f"Total: ${total_price:.2f}")  # Total: $120.00
```

### المزيد من أمثلة الدوال

```python
# التحقق مما إذا كان الرقم زوجياً
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# حساب مساحة المستطيل
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 3)
print(f"Area: {area}")  # Area: 15

# تصفية الطلاب الناجحين
def filter_passed_students(students):
    """ترجع قائمة بالطلاب الذين نجحوا (الدرجة >= 60)"""
    passed = []
    for student in students:
        if student['grade'] >= 60:
            passed.append(student)
    return passed

students = [
    {"name": "Ahmed", "grade": 85},
    {"name": "Sara", "grade": 45},
    {"name": "Ali", "grade": 72}
]

passed_students = filter_passed_students(students)
print(passed_students)
```

---

## الوحدات والحزم

### ما هي الوحدات؟

الوحدة هي ملف Python يحتوي على دوال وفئات ومتغيرات يمكنك استخدامها في برامج أخرى.

### استخدام الوحدات المدمجة

```python
# استيراد الوحدة بالكامل
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.pow(2, 3))    # 8.0

# استيراد عناصر محددة
from math import pi, sqrt

print(pi)       # 3.141592653589793
print(sqrt(25)) # 5.0

# استيراد مع اسم مستعار
import math as m

print(m.pi)
print(m.sqrt(16))

# استيراد كل شيء (غير موصى به)
from math import *

print(ceil(3.2))  # 4
```

### وحدات المكتبة القياسية الشائعة

#### 1. random - توليد أرقام عشوائية

```python
import random

# عدد صحيح عشوائي
dice = random.randint(1, 6)
print(f"Dice roll: {dice}")

# اختيار عشوائي من القائمة
fruits = ["apple", "banana", "orange"]
fruit = random.choice(fruits)
print(f"Random fruit: {fruit}")

# خلط القائمة
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# عدد عشري عشوائي بين 0 و 1
print(random.random())
```

#### 2. datetime - العمل مع التواريخ والأوقات

```python
import datetime

# التاريخ والوقت الحالي
now = datetime.datetime.now()
print(now)

# التاريخ الحالي
today = datetime.date.today()
print(today)

# تنسيق التاريخ
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# حساب العمر
birth_date = datetime.date(2000, 1, 15)
age = (today - birth_date).days // 365
print(f"Age: {age}")
```

#### 3. os - دوال نظام التشغيل

```python
import os

# الحصول على الدليل الحالي
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# قائمة الملفات في الدليل
files = os.listdir()
print("Files:", files)

# التحقق من وجود الملف
exists = os.path.exists("myfile.txt")
print(f"File exists: {exists}")
```

### إنشاء وحدتك الخاصة

**الملف: calculator.py**
```python
# calculator.py
"""وحدة حاسبة بسيطة"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

PI = 3.14159
```

**الملف: main.py**
```python
# main.py
import calculator

result = calculator.add(5, 3)
print(result)  # 8

result = calculator.multiply(4, 7)
print(result)  # 28

print(calculator.PI)  # 3.14159
```

---

## معالجة الأخطاء

### لماذا معالجة الأخطاء؟

الأخطاء ستحدث. بدلاً من التعطل، تعامل معها بشكل جيد!

### كتلة Try-Except

```python
# بدون معالجة الأخطاء
# age = int(input("Enter age: "))  # يتعطل إذا أدخل المستخدم "abc"

# مع معالجة الأخطاء
try:
    age = int(input("Enter age: "))
    print(f"Your age is {age}")
except:
    print("Invalid input! Please enter a number.")
```

### التقاط أخطاء محددة

```python
# التقاط أنواع أخطاء محددة
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Try-Except-Else-Finally

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # يعمل إذا لم يحدث خطأ
    print(f"Result: {result}")
finally:
    # يعمل دائماً
    print("Operation complete!")
```

### مثال عملي: القسمة الآمنة

```python
def safe_divide(a, b):
    """قسمة رقمين بأمان"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both inputs must be numbers"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: Cannot divide by zero
print(safe_divide(10, "a")) # Error: Both inputs must be numbers
```

---

## البيئات الافتراضية

### ما هي البيئة الافتراضية؟

البيئة الافتراضية هي بيئة Python معزولة لمشروعك. تبقي تبعيات المشروع منفصلة.

### لماذا تستخدم البيئات الافتراضية؟

- مشاريع مختلفة تحتاج إصدارات مختلفة من الحزم
- تجنب التعارضات بين الحزم
- سهولة مشاركة متطلبات المشروع
- نظيف ومنظم

### إنشاء بيئة افتراضية

**Windows:**
```bash
# إنشاء بيئة افتراضية
python -m venv venv

# تفعيل
venv\Scripts\activate

# إلغاء التفعيل
deactivate
```

**macOS/Linux:**
```bash
# إنشاء بيئة افتراضية
python3 -m venv venv

# تفعيل
source venv/bin/activate

# إلغاء التفعيل
deactivate
```

### تثبيت الحزم باستخدام pip

```bash
# تفعيل البيئة الافتراضية أولاً!

# تثبيت حزمة
pip install requests

# تثبيت إصدار محدد
pip install django==4.2.0

# قائمة الحزم المثبتة
pip list

# حفظ المتطلبات
pip freeze > requirements.txt

# التثبيت من المتطلبات
pip install -r requirements.txt

# إلغاء تثبيت حزمة
pip uninstall requests
```

### مثال requirements.txt

```
# requirements.txt
django==4.2.0
requests==2.31.0
python-dateutil==2.8.2
```

### سير العمل الأفضل

```bash
# 1. إنشاء مجلد المشروع
mkdir my_project
cd my_project

# 2. إنشاء بيئة افتراضية
python -m venv venv

# 3. تفعيل البيئة الافتراضية
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 4. تثبيت الحزم
pip install django requests

# 5. حفظ المتطلبات
pip freeze > requirements.txt

# 6. اعمل على مشروعك...

# 7. إلغاء التفعيل عند الانتهاء
deactivate
```

---

## مشروع صغير: تطبيق قائمة المهام

لنبني تطبيق قائمة مهام يعمل في الطرفية باستخدام كل ما تعلمناه!

### المتطلبات

1. إضافة المهام
2. عرض جميع المهام
3. وضع علامة على المهام كمكتملة
4. حذف المهام
5. حفظ وتحميل المهام من الملف
6. استخدام الدوال للتنظيم
7. معالجة الأخطاء بشكل جيد

### التنفيذ خطوة بخطوة

```python
import json

# ملف لتخزين المهام
TASKS_FILE = "tasks.json"

def load_tasks():
    """تحميل المهام من الملف"""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """حفظ المهام إلى الملف"""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def add_task(tasks):
    """إضافة مهمة جديدة"""
    task_name = input("Enter task: ")
    if task_name.strip():
        task = {
            "name": task_name,
            "done": False
        }
        tasks.append(task)
        print("Task added!")
        return True
    else:
        print("Task cannot be empty!")
        return False

def view_tasks(tasks):
    """عرض جميع المهام"""
    if not tasks:
        print("\nNo tasks yet!")
        return

    print("\n" + "="*50)
    print("YOUR TASKS")
    print("="*50)

    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['name']}")

    print("="*50)

def mark_done(tasks):
    """وضع علامة على مهمة كمكتملة"""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    """حذف مهمة"""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def show_menu():
    """عرض خيارات القائمة"""
    print("\n" + "="*50)
    print("TO-DO LIST APP")
    print("="*50)
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print("="*50)

def main():
    """الدالة الرئيسية"""
    print("Welcome to To-Do List App!")

    # تحميل المهام الموجودة
    tasks = load_tasks()

    while True:
        show_menu()

        choice = input("\nEnter choice (1-5): ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)

        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)

        elif choice == "5":
            print("\nGoodbye!")
            save_tasks(tasks)
            break

        else:
            print("\nInvalid choice! Please try again.")

# تشغيل التطبيق
if __name__ == "__main__":
    main()
```

### اختبار التطبيق

جرب هذه الإجراءات:
1. أضف عدة مهام
2. اعرض قائمة المهام
3. ضع علامة على بعض المهام كمكتملة
4. احذف مهمة
5. اخرج وأعد التشغيل للتحقق من حفظ المهام

---

## النقاط الرئيسية من الأسبوع الثاني

**هياكل البيانات:**
- **القوائم** - مجموعات مرتبة قابلة للتغيير
- **المجموعات** - مجموعات مرتبة غير قابلة للتغيير
- **القواميس** - أزواج المفتاح-القيمة
- **المجموعات الفريدة** - عناصر غير مرتبة فريدة

**الدوال:**
- تقسيم الكود إلى أجزاء قابلة لإعادة الاستخدام
- قبول المعاملات وإرجاع القيم
- استخدام المعاملات الافتراضية للمرونة
- فهم نطاق المتغيرات

**الوحدات:**
- استخدام الوحدات المدمجة (math, random, datetime)
- إنشاء وحداتك الخاصة
- الحفاظ على تنظيم الكود

**معالجة الأخطاء:**
- استخدام try-except للتعامل مع الأخطاء
- التقاط أنواع الاستثناءات المحددة
- توفير رسائل خطأ مفيدة

**البيئات الافتراضية:**
- عزل تبعيات المشروع
- استخدام pip لإدارة الحزم
- إنشاء requirements.txt

---

## الخطوات التالية

**قبل الأسبوع 3:**
- أكمل جميع التمارين التطبيقية
- ابنِ مشروع قائمة المهام الصغير
- حاول إضافة ميزات جديدة للمشروع
- راجع هياكل البيانات
- تدرب على كتابة الدوال

**معاينة الأسبوع 3:**
ستتعلم عن:
- مفاهيم الويب (العميل-الخادم، HTTP)
- أساسيات HTML و CSS
- سير عمل Git و GitHub
- بناء صفحات ويب ثابتة

استمر في التدريب وإلى اللقاء في الأسبوع القادم!
