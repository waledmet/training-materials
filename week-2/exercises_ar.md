# تمارين الأسبوع الثاني

يحتوي هذا الملف على تمارين تطبيقية للأسبوع الثاني. حاول حل كل مشكلة بنفسك قبل النظر إلى الحل!

---

## جدول المحتويات

1. [اليوم 1-2: القوائم](#اليوم-1-2-القوائم)
2. [اليوم 3: المجموعات والقواميس](#اليوم-3-المجموعات-والقواميس)
3. [اليوم 4: المجموعات الفريدة والدوال](#اليوم-4-المجموعات-الفريدة-والدوال)
4. [اليوم 5: الوحدات النمطية ومعالجة الأخطاء](#اليوم-5-الوحدات-النمطية-ومعالجة-الأخطاء)
5. [مسائل التحدي](#مسائل-التحدي)

---

## اليوم 1-2: القوائم

### التمرين 1: إنشاء والوصول إلى القوائم

**المهمة**: أنشئ قائمة بأطعمتك المفضلة واطبع العنصر الأول والأخير.

**مثال على الإخراج**:
```
Foods: ['pizza', 'pasta', 'burger', 'sushi']
First: pizza
Last: sushi
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
foods = ["pizza", "pasta", "burger", "sushi"]
print(f"Foods: {foods}")
print(f"First: {foods[0]}")
print(f"Last: {foods[-1]}")
```
</details>

---

### التمرين 2: إضافة وإزالة العناصر

**المهمة**: ابدأ بقائمة فارغة، أضف 5 عناصر، احذف عنصرين، واطبع القائمة النهائية.

**مثال على الإخراج**:
```
After adding: ['apple', 'banana', 'orange', 'grape', 'mango']
After removing: ['apple', 'orange', 'grape']
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
fruits = []

# Add items
fruits.append("apple")
fruits.append("banana")
fruits.append("orange")
fruits.append("grape")
fruits.append("mango")
print(f"After adding: {fruits}")

# Remove items
fruits.remove("banana")
fruits.remove("mango")
print(f"After removing: {fruits}")
```
</details>

---

### التمرين 3: تقطيع القوائم

**المهمة**: أنشئ قائمة بالأرقام من 1-10، ثم اطبع:
- أول 3 أرقام
- آخر 3 أرقام
- الأرقام الوسطى (4-7)

**مثال على الإخراج**:
```
Full list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First 3: [1, 2, 3]
Last 3: [8, 9, 10]
Middle: [4, 5, 6, 7]
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Full list: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle: {numbers[3:7]}")
```
</details>

---

### التمرين 4: التكرار عبر القائمة

**المهمة**: أنشئ قائمة بالأسماء واطبع كل اسم مع موقعه.

**مثال على الإخراج**:
```
1. Ahmed
2. Sara
3. Mohammed
4. Fatima
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
names = ["Ahmed", "Sara", "Mohammed", "Fatima"]

for i, name in enumerate(names, 1):
    print(f"{i}. {name}")
```
</details>

---

### التمرين 5: مدير قائمة التسوق

**المهمة**: أنشئ برنامج قائمة تسوق:
- يبدأ بقائمة فارغة
- يسمح للمستخدم بإضافة 3 عناصر
- يعرض القائمة
- يسمح للمستخدم بإزالة عنصر واحد
- يعرض القائمة النهائية

**مثال على الإخراج**:
```
Add item 1: milk
Add item 2: bread
Add item 3: eggs
Shopping list: ['milk', 'bread', 'eggs']
Remove item: bread
Final list: ['milk', 'eggs']
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
shopping_list = []

# Add items
for i in range(1, 4):
    item = input(f"Add item {i}: ")
    shopping_list.append(item)

print(f"Shopping list: {shopping_list}")

# Remove item
remove_item = input("Remove item: ")
if remove_item in shopping_list:
    shopping_list.remove(remove_item)
    print(f"Final list: {shopping_list}")
else:
    print(f"{remove_item} not in list")
```
</details>

---

### التمرين 6: إيجاد القيمة القصوى في القائمة

**المهمة**: أنشئ قائمة بالأرقام وابحث عن القيمة القصوى بدون استخدام ()max.

**مثال على الإخراج**:
```
Numbers: [45, 23, 67, 12, 89, 34]
Maximum: 89
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
numbers = [45, 23, 67, 12, 89, 34]
print(f"Numbers: {numbers}")

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum: {maximum}")
```
</details>

---

### التمرين 7: عد الأرقام الزوجية

**المهمة**: أنشئ قائمة بالأرقام وعُد كم عدداً منها زوجياً.

**مثال على الإخراج**:
```
Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers count: 5
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1

print(f"Even numbers count: {count}")
```
</details>

---

### التمرين 8: عكس القائمة

**المهمة**: أنشئ قائمة واطبعها بالعكس بدون استخدام ()reverse.

**مثال على الإخراج**:
```
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
original = [1, 2, 3, 4, 5]
print(f"Original: {original}")

reversed_list = []
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])

print(f"Reversed: {reversed_list}")

# Alternative using slicing
reversed_list2 = original[::-1]
print(f"Reversed (slicing): {reversed_list2}")
```
</details>

---

## اليوم 3: المجموعات والقواميس

### التمرين 9: إنشاء والوصول إلى المجموعات

**المهمة**: أنشئ مجموعة بمعلوماتك الشخصية (الاسم، العمر، المدينة) واطبع كل عنصر.

**مثال على الإخراج**:
```
Name: Ahmed
Age: 25
City: Cairo
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
person = ("Ahmed", 25, "Cairo")

print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"City: {person[2]}")
```
</details>

---

### التمرين 10: فك المجموعات

**المهمة**: أنشئ مجموعة بإحداثيات (x, y) وافكك محتواها إلى متغيرات.

**مثال على الإخراج**:
```
Coordinates: (10, 20)
X: 10
Y: 20
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

x, y = coordinates
print(f"X: {x}")
print(f"Y: {y}")
```
</details>

---

### التمرين 11: إنشاء قاموس

**المهمة**: أنشئ قاموساً لتخزين معلومات طالب (الاسم، العمر، الدرجة، المدينة).

**مثال على الإخراج**:
```
Student: {'name': 'Sara', 'age': 22, 'grade': 'A', 'city': 'Dubai'}
Name: Sara
Grade: A
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
student = {
    "name": "Sara",
    "age": 22,
    "grade": "A",
    "city": "Dubai"
}

print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")
```
</details>

---

### التمرين 12: إضافة وإزالة عناصر القاموس

**المهمة**: أنشئ قاموساً، أضف عنصرين جديدين، احذف عنصراً واحداً، واطبع النتيجة.

**مثال على الإخراج**:
```
Original: {'name': 'Ahmed', 'age': 25}
After adding: {'name': 'Ahmed', 'age': 25, 'city': 'Cairo', 'job': 'Engineer'}
After removing: {'name': 'Ahmed', 'city': 'Cairo', 'job': 'Engineer'}
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
person = {"name": "Ahmed", "age": 25}
print(f"Original: {person}")

# Add items
person["city"] = "Cairo"
person["job"] = "Engineer"
print(f"After adding: {person}")

# Remove item
del person["age"]
print(f"After removing: {person}")
```
</details>

---

### التمرين 13: التكرار عبر القاموس

**المهمة**: أنشئ قاموساً بأسعار المنتجات واطبع كل منتج مع سعره.

**مثال على الإخراج**:
```
Product: apple, Price: $2.50
Product: banana, Price: $1.20
Product: orange, Price: $3.00
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
prices = {
    "apple": 2.50,
    "banana": 1.20,
    "orange": 3.00
}

for product, price in prices.items():
    print(f"Product: {product}, Price: ${price:.2f}")
```
</details>

---

### التمرين 14: دوال القاموس

**المهمة**: أنشئ قاموساً وأظهر استخدام ()get، ()keys، ()values، ()items.

**مثال على الإخراج**:
```
Age: 25
Default: N/A
Keys: dict_keys(['name', 'age', 'city'])
Values: dict_values(['Ahmed', 25, 'Cairo'])
Items: dict_items([('name', 'Ahmed'), ('age', 25), ('city', 'Cairo')])
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
person = {"name": "Ahmed", "age": 25, "city": "Cairo"}

# get() method
print(f"Age: {person.get('age')}")
print(f"Default: {person.get('job', 'N/A')}")

# keys(), values(), items()
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")
```
</details>

---

### التمرين 15: دفتر الهاتف

**المهمة**: أنشئ برنامج دفتر هاتف بسيط:
- احفظ 3 جهات اتصال (الاسم: رقم الهاتف)
- اسمح للمستخدم بالبحث عن اسم
- اعرض رقم الهاتف أو "Not found"

**مثال على الإخراج**:
```
Search for: Ahmed
Phone: 0501234567
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
phone_book = {
    "Ahmed": "0501234567",
    "Sara": "0507654321",
    "Mohammed": "0509876543"
}

name = input("Search for: ")
if name in phone_book:
    print(f"Phone: {phone_book[name]}")
else:
    print("Not found")
```
</details>

---

## اليوم 4: المجموعات الفريدة والدوال

### التمرين 16: إنشاء واستخدام المجموعات الفريدة

**المهمة**: أنشئ مجموعتين من الأرقام وأظهر الاتحاد، التقاطع، والفرق.

**مثال على الإخراج**:
```
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference: {1, 2, 3}
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference: {set_a - set_b}")
```
</details>

---

### التمرين 17: إزالة المكررات

**المهمة**: أنشئ قائمة بها عناصر مكررة واستخدم مجموعة لإزالتها.

**مثال على الإخراج**:
```
Original: [1, 2, 2, 3, 3, 3, 4, 5, 5]
Unique: [1, 2, 3, 4, 5]
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Original: {numbers}")

unique = list(set(numbers))
unique.sort()
print(f"Unique: {unique}")
```
</details>

---

### التمرين 18: دالة بسيطة

**المهمة**: أنشئ دالة تحيي شخصاً باسمه.

**مثال على الإخراج**:
```
Hello, Ahmed! Welcome!
Hello, Sara! Welcome!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def greet(name):
    print(f"Hello, {name}! Welcome!")

greet("Ahmed")
greet("Sara")
```
</details>

---

### التمرين 19: دالة مع قيمة الإرجاع

**المهمة**: أنشئ دالة تحسب مساحة المستطيل.

**مثال على الإخراج**:
```
Area: 15
Area: 24
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def calculate_area(length, width):
    area = length * width
    return area

result1 = calculate_area(5, 3)
print(f"Area: {result1}")

result2 = calculate_area(6, 4)
print(f"Area: {result2}")
```
</details>

---

### التمرين 20: دالة مع معاملات افتراضية

**المهمة**: أنشئ دالة تحسب الأس مع قيمة افتراضية للأس هي 2.

**مثال على الإخراج**:
```
5^2 = 25
3^3 = 27
2^2 = 4
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def power(base, exponent=2):
    result = base ** exponent
    return result

print(f"5^2 = {power(5)}")
print(f"3^3 = {power(3, 3)}")
print(f"2^2 = {power(2)}")
```
</details>

---

### التمرين 21: دالة تحويل درجة الحرارة

**المهمة**: أنشئ دوال للتحويل بين سلسيوس وفهرنهايت.

**مثال على الإخراج**:
```
25°C = 77.0°F
77°F = 25.0°C
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

c = 25
f = celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")

f = 77
c = fahrenheit_to_celsius(f)
print(f"{f}°F = {c}°C")
```
</details>

---

### التمرين 22: دالة معالجة القوائم

**المهمة**: أنشئ دالة تأخذ قائمة وترجع المجموع والمتوسط.

**مثال على الإخراج**:
```
Numbers: [10, 20, 30, 40, 50]
Sum: 150
Average: 30.0
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

nums = [10, 20, 30, 40, 50]
print(f"Numbers: {nums}")

total, avg = calculate_stats(nums)
print(f"Sum: {total}")
print(f"Average: {avg}")
```
</details>

---

## اليوم 5: الوحدات النمطية ومعالجة الأخطاء

### التمرين 23: استخدام الوحدات المدمجة

**المهمة**: استخدم وحدتي math و random لـ:
- حساب الجذر التربيعي
- توليد رقم عشوائي
- حساب العاملي

**مثال على الإخراج**:
```
Square root of 16: 4.0
Random number (1-10): 7
Factorial of 5: 120
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
import math
import random

# Square root
num = 16
sqrt = math.sqrt(num)
print(f"Square root of {num}: {sqrt}")

# Random number
rand = random.randint(1, 10)
print(f"Random number (1-10): {rand}")

# Factorial
n = 5
fact = math.factorial(n)
print(f"Factorial of {n}: {fact}")
```
</details>

---

### التمرين 24: التاريخ والوقت

**المهمة**: استخدم وحدة datetime لعرض التاريخ والوقت الحالي.

**مثال على الإخراج**:
```
Current date: 2025-01-15
Current time: 14:30:45
Day of week: Wednesday
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
from datetime import datetime

now = datetime.now()

print(f"Current date: {now.strftime('%Y-%m-%d')}")
print(f"Current time: {now.strftime('%H:%M:%S')}")
print(f"Day of week: {now.strftime('%A')}")
```
</details>

---

### التمرين 25: معالجة الأخطاء الأساسية

**المهمة**: اكتب برنامجاً يعالج خطأ القسمة على صفر.

**مثال على الإخراج**:
```
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```
</details>

---

### التمرين 26: معالجة أخطاء متعددة

**المهمة**: عالج كلاً من ValueError و ZeroDivisionError.

**مثال على الإخراج**:
```
Enter a number: abc
Error: Please enter a valid number

Enter a number: 10
Enter divisor: 0
Error: Cannot divide by zero
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
try:
    num = float(input("Enter a number: "))
    divisor = float(input("Enter divisor: "))
    result = num / divisor
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```
</details>

---

### التمرين 27: قراءة الملفات مع معالجة الأخطاء

**المهمة**: حاول قراءة ملف وعالج الخطأ إذا لم يكن موجوداً.

**مثال على الإخراج**:
```
Error: File 'data.txt' not found
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File 'data.txt' not found")
```
</details>

---

### التمرين 28: Try-Except-Finally

**المهمة**: أظهر تنفيذ الكتلة finally.

**مثال على الإخراج**:
```
Attempting operation...
Error occurred
This always runs
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
try:
    print("Attempting operation...")
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("This always runs")
```
</details>

---

## مسائل التحدي

### التحدي 1: مدير جهات الاتصال

**المهمة**: أنشئ مدير جهات اتصال باستخدام قاموس:
- إضافة جهة اتصال
- إزالة جهة اتصال
- البحث عن جهة اتصال
- عرض جميع جهات الاتصال

**مثال على الإخراج**:
```
1. Add contact
2. Remove contact
3. Search contact
4. List all
5. Exit
Choice: 1
Name: Ahmed
Phone: 0501234567
Contact added!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Remove contact")
    print("3. Search contact")
    print("4. List all")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact added!")

    elif choice == "2":
        name = input("Name to remove: ")
        if name in contacts:
            del contacts[name]
            print("Contact removed!")
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Search for: ")
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Contact not found!")

    elif choice == "4":
        print("\nAll Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
```
</details>

---

### التحدي 2: إحصائيات الدرجات

**المهمة**: أنشئ دالة تأخذ قائمة بالدرجات وترجع:
- المتوسط
- الأعلى
- الأدنى
- عدد الناجحين (>=60)

**مثال على الإخراج**:
```
Grades: [85, 92, 78, 60, 95, 88]
Average: 83.0
Highest: 95
Lowest: 60
Passed: 6
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def grade_statistics(grades):
    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = sum(1 for grade in grades if grade >= 60)

    return {
        "average": avg,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }

grades = [85, 92, 78, 60, 95, 88]
print(f"Grades: {grades}")

stats = grade_statistics(grades)
print(f"Average: {stats['average']:.1f}")
print(f"Highest: {stats['highest']}")
print(f"Lowest: {stats['lowest']}")
print(f"Passed: {stats['passed']}")
```
</details>

---

### التحدي 3: عداد تكرار الكلمات

**المهمة**: عُد كم مرة تظهر كل كلمة في جملة.

**مثال على الإخراج**:
```
Sentence: the cat and the dog and the bird
Word frequency:
the: 3
cat: 1
and: 2
dog: 1
bird: 1
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
sentence = input("Sentence: ")
words = sentence.lower().split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
```
</details>

---

### التحدي 4: تمرين على القوائم المضغوطة

**المهمة**: استخدم القوائم المضغوطة لـ:
- إنشاء قائمة بالمربعات من 1-10
- إنشاء قائمة بالأرقام الزوجية من 1-20
- إنشاء قائمة بأطوال الكلمات

**مثال على الإخراج**:
```
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Lengths: [5, 6, 6]
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
# Squares
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# Evens
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Evens: {evens}")

# Word lengths
words = ["hello", "python", "world"]
lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")
```
</details>

---

### التحدي 5: نظام الجرد

**المهمة**: أنشئ نظام جرد باستخدام قواميس متداخلة:
- كل منتج له اسم، سعر، كمية
- إضافة منتج
- تحديث الكمية
- عرض الجرد

**مثال على الإخراج**:
```
Inventory:
apple: $2.50, Qty: 100
banana: $1.20, Qty: 150
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
inventory = {}

def add_product(name, price, quantity):
    inventory[name] = {"price": price, "quantity": quantity}
    print(f"Added {name}")

def update_quantity(name, quantity):
    if name in inventory:
        inventory[name]["quantity"] = quantity
        print(f"Updated {name}")
    else:
        print("Product not found")

def show_inventory():
    print("\nInventory:")
    for name, info in inventory.items():
        print(f"{name}: ${info['price']:.2f}, Qty: {info['quantity']}")

# Test
add_product("apple", 2.50, 100)
add_product("banana", 1.20, 150)
show_inventory()
update_quantity("apple", 120)
show_inventory()
```
</details>

---

### التحدي 6: آلة حاسبة مع دوال

**المهمة**: أنشئ آلة حاسبة بدوال منفصلة لكل عملية ومعالجة أخطاء.

**مثال على الإخراج**:
```
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Choice: 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "5":
        print("Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("Invalid choice!")
            continue

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
```
</details>

---

## نصائح للنجاح

1. **ابدأ بالتمارين البسيطة** - اب��� ثقتك
2. **اكتب الكود بنفسك، لا تنسخ** - الذاكرة العضلية تساعد في التعلم
3. **جرب** - حاول تغيير القيم وانظر ماذا يحدث
4. **استخدم ()print** - أظهر القيم الوسيطة للتصحيح
5. **اقرأ رسائل الخطأ** - تخبرك بما هو الخطأ
6. **تدرب يومياً** - الاستمرارية أفضل من الكثافة
7. **راجع الحلول** - ولكن حاول أولاً بنفسك

---

## التقييم الذاتي

بعد إكمال هذه التمارين، يجب أن تكون قادراً على:

- [ ] إنشاء ومعالجة القوائم
- [ ] استخدام المجموعات للبيانات غير القابلة للتغيير
- [ ] العمل مع القواميس (أزواج المفتاح-القيمة)
- [ ] استخدام المجموعات للمجموعات الفريدة
- [ ] كتابة دوال مع معاملات وقيم إرجاع
- [ ] استيراد واستخدام الوحدات
- [ ] معالجة الأخطاء باستخدام try-except
- [ ] حل مشاكل العالم الحقيقي مع هياكل البيانات

إذا لم تكن واثقاً من أي من هذه النقاط، راجع الدروس وتدرب أكثر!

---

برمجة سعيدة! تذكر، كل خبير كان مبتدئاً يوماً ما!
