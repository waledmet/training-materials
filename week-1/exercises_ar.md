# تمارين الأسبوع الأول

يحتوي هذا الملف على تمارين تطبيقية للأسبوع الأول. حاول حل كل مشكلة بنفسك قبل النظر إلى الحل!

---

## جدول المحتويات

1. [اليوم 1-2: المتغيرات والعمليات الأساسية](#اليوم-1-2-المتغيرات-والعمليات-الأساسية)
2. [اليوم 3: جمل If](#اليوم-3-جمل-if)
3. [اليوم 4: الحلقات](#اليوم-4-الحلقات)
4. [اليوم 5: مسائل التحدي](#اليوم-5-مسائل-التحدي)
5. [الحلول](#الحلول)

---

## اليوم 1-2: المتغيرات والعمليات الأساسية

### التمرين 1: مرحباً بك!

**المهمة**: اكتب برنامجاً يسأل عن اسم المستخدم ويرحب به.

**مثال على الإخراج**:
```
What is your name? Ahmed
Hello, Ahmed! Welcome to Python programming.
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python programming.")
```
</details>

---

### التمرين 2: آلة حاسبة بسيطة

**المهمة**: اكتب برنامجاً:
- يسأل عن رقمين
- يحسب ويعرض:
  - المجموع (Sum)
  - الفرق (Difference)
  - الناتج (Product)
  - القسمة (Division)

**مثال على الإخراج**:
```
Enter first number: 10
Enter second number: 3
Sum: 13
Difference: 7
Product: 30
Division: 3.33
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2:.2f}")
```
</details>

---

### التمرين 3: حاسبة المساحة

**المهمة**: اكتب برنامجاً يحسب مساحة المستطيل.
- اسأل عن الطول والعرض
- احسب المساحة (الطول × العرض)
- اعرض النتيجة

**مثال على الإخراج**:
```
Enter length: 5
Enter width: 3
The area is: 15
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print(f"The area is: {area}")
```
</details>

---

### التمرين 4: محول درجة الحرارة

**المهمة**: تحويل من سيليزية إلى فهرنهايت.
- الصيغة: F = (C × 9/5) + 32
- اسأل عن درجة الحرارة بالسيليزية
- اعرضها بالفهرنهايت

**مثال على الإخراج**:
```
Enter temperature in Celsius: 25
25°C is 77.0°F
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is {fahrenheit}°F")
```
</details>

---

### التمرين 5: المعلومات الشخصية

**المهمة**: أنشئ برنامجاً يجمع ويعرض المعلومات الشخصية:
- الاسم
- العمر
- الطول (بالأمتار)
- احسب واعرض العمر في السنة القادمة

**مثال على الإخراج**:
```
Name: Sara
Age: 22
Height: 1.65
--- Summary ---
Hello Sara!
You are 22 years old
Your height is 1.65 meters
Next year you will be 23
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height: "))

print("\n--- Summary ---")
print(f"Hello {name}!")
print(f"You are {age} years old")
print(f"Your height is {height} meters")
print(f"Next year you will be {age + 1}")
```
</details>

---

## اليوم 3: جمل If

### التمرين 6: زوجي أم فردي

**المهمة**: اكتب برنامجاً يتحقق من أن الرقم زوجي أم فردي.

**مثال على الإخراج**:
```
Enter a number: 7
7 is odd
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```
</details>

---

### التمرين 7: فئة العمر

**المهمة**: حدد فئة العمر:
- 0-12: طفل (Child)
- 13-19: مراهق (Teenager)
- 20-59: بالغ (Adult)
- 60+: كبير السن (Senior)

**مثال على الإخراج**:
```
Enter your age: 25
You are an Adult
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
age = int(input("Enter your age: "))

if age <= 12:
    print("You are a Child")
elif age <= 19:
    print("You are a Teenager")
elif age <= 59:
    print("You are an Adult")
else:
    print("You are a Senior")
```
</details>

---

### التمرين 8: حاسبة الدرجات

**المهمة**: تحويل الدرجة الرقمية إلى درجة حرفية:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- أقل من 60: F

**مثال على الإخراج**:
```
Enter your grade: 85
Your grade is: B
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Your grade is: A")
elif grade >= 80:
    print("Your grade is: B")
elif grade >= 70:
    print("Your grade is: C")
elif grade >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")
```
</details>

---

### التمرين 9: موجب، سالب، أم صفر

**المهمة**: تحقق من أن الرقم موجب أو سالب أو صفر.

**مثال على الإخراج**:
```
Enter a number: -5
The number is negative
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
```
</details>

---

### التمرين 10: نظام تسجيل الدخول

**المهمة**: أنشئ نظام تسجيل دخول بسيط:
- اسم المستخدم الصحيح: "admin"
- كلمة المرور الصحيحة: "python123"
- تحقق من كليهما واعرض رسالة مناسبة

**مثال على الإخراج**:
```
Username: admin
Password: python123
Login successful!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
correct_username = "admin"
correct_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password")
```
</details>

---

### التمرين 11: حاسبة الخصم

**المهمة**: احسب الخصم بناءً على مبلغ الشراء:
- $100+: خصم 20%
- $50-$99: خصم 10%
- أقل من $50: بدون خصم

**مثال على الإخراج**:
```
Enter purchase amount: 120
Discount: 20%
Final price: $96.00
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
amount = float(input("Enter purchase amount: "))

if amount >= 100:
    discount = 0.20
elif amount >= 50:
    discount = 0.10
else:
    discount = 0

discount_amount = amount * discount
final_price = amount - discount_amount

print(f"Discount: {discount * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")
```
</details>

---

### التمرين 12: أكبر من ثلاثة أرقام

**المهمة**: جد أكبر من ثلاثة أرقام.

**مثال على الإخراج**:
```
Enter first number: 45
Enter second number: 82
Enter third number: 37
The largest number is: 82
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")
```
</details>

---

## اليوم 4: الحلقات

### التمرين 13: العد حتى العشرة

**المهمة**: اطبع الأرقام من 1 إلى 10.

**الإخراج المتوقع**:
```
1
2
3
4
5
6
7
8
9
10
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
for i in range(1, 11):
    print(i)
```
</details>

---

### التمرين 14: الأرقام الزوجية

**المهمة**: اطبع جميع الأرقام الزوجية من 1 إلى 20.

**الإخراج المتوقع**:
```
2
4
6
8
10
12
14
16
18
20
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
# الطريقة 1: استخدام step
for i in range(2, 21, 2):
    print(i)

# الطريقة 2: استخدام if
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```
</details>

---

### التمرين 15: حاسبة المجموع

**المهمة**: احسب مجموع الأرقام من 1 إلى 100.

**الإخراج المتوقع**:
```
The sum of numbers from 1 to 100 is: 5050
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
total = 0
for i in range(1, 101):
    total += i

print(f"The sum of numbers from 1 to 100 is: {total}")
```
</details>

---

### التمرين 16: جدول الضرب

**المهمة**: اطبع جدول الضرب لرقم معين (من 1 إلى 10).

**مثال على الإخراج**:
```
Enter a number: 7
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```
</details>

---

### التمرين 17: العد التنازلي

**المهمة**: اطبع عداً تنازلياً من 10 إلى 1، ثم اطبع "Blast off!"

**الإخراج المتوقع**:
```
10
9
8
7
6
5
4
3
2
1
Blast off!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```
</details>

---

### التمرين 18: التحقق من كلمة المرور (حلقة While)

**المهمة**: استمر في طلب كلمة المرور حتى تكون صحيحة:
- كلمة المرور الصحيحة: "secret"
- الحد الأقصى 3 محاولات
- قفل الحساب بعد 3 محاولات فاشلة

**مثال على الإخراج**:
```
Enter password: wrong
Incorrect! 2 attempts left
Enter password: wrong
Incorrect! 1 attempts left
Enter password: secret
Access granted!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
password = "secret"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect! {remaining} attempts left")
        else:
            print("Account locked!")
```
</details>

---

### التمرين 19: لعبة تخمين الرقم

**المهمة**: أنشئ لعبة تخمين رقم:
- رقم سري بين 1-10
- أعط تلميحات (مرتفع جداً/منخفض جداً)
- استمر حتى يتم التخمين بشكل صحيح

**مثال على الإخراج**:
```
Guess the number (1-10): 5
Too low!
Guess the number (1-10): 8
Too high!
Guess the number (1-10): 7
Correct! You win!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
secret_number = 7

while True:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Correct! You win!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
```
</details>

---

### التمرين 20: حاسبة المضروب

**المهمة**: احسب المضروب (factorial) لرقم.
- المضروب لـ 5 = 5 × 4 × 3 × 2 × 1 = 120

**مثال على الإخراج**:
```
Enter a number: 5
Factorial of 5 is: 120
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is: {factorial}")
```
</details>

---

## اليوم 5: مسائل التحدي

### التحدي 1: FizzBuzz

**المهمة**: اطبع الأرقام من 1 إلى 30، ولكن:
- لمضاعفات 3، اطبع "Fizz"
- لمضاعفات 5، اطبع "Buzz"
- لمضاعفات كل من 3 و 5، اطبع "FizzBuzz"
- وإلا، اطبع الرقم

**الإخراج المتوقع**:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
</details>

---

### التحدي 2: فاحص الأعداد الأولية

**المهمة**: تحقق من أن الرقم أولي (قابل للقسمة على 1 ونفسه فقط).

**مثال على الإخراج**:
```
Enter a number: 17
17 is a prime number
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not a prime number")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
```
</details>

---

### التحدي 3: طباعة النمط

**المهمة**: اطبع هذا النمط:
```
*
**
***
****
*****
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
for i in range(1, 6):
    print("*" * i)
```
</details>

---

### التحدي 4: النمط العكسي

**المهمة**: اطبع هذا النمط:
```
*****
****
***
**
*
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
for i in range(5, 0, -1):
    print("*" * i)
```
</details>

---

### التحدي 5: مجموع الأرقام الزوجية

**المهمة**: احسب مجموع جميع الأرقام الزوجية من 1 إلى 100.

**الإخراج المتوقع**:
```
The sum of even numbers from 1 to 100 is: 2550
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
total = 0

for i in range(2, 101, 2):
    total += i

print(f"The sum of even numbers from 1 to 100 is: {total}")
```
</details>

---

### التحدي 6: مجموع الأرقام

**المهمة**: احسب مجموع الأرقام في رقم.
- مثال: 1234 → 1+2+3+4 = 10

**مثال على الإخراج**:
```
Enter a number: 1234
Sum of digits: 10
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
number = input("Enter a number: ")
digit_sum = 0

for digit in number:
    digit_sum += int(digit)

print(f"Sum of digits: {digit_sum}")
```
</details>

---

### التحدي 7: فاحص التناظر

**المهمة**: تحقق من أن الكلمة متناظرة (تقرأ نفسها من الأمام والخلف).
- أمثلة: "racecar", "madam", "level"

**مثال على الإخراج**:
```
Enter a word: racecar
"racecar" is a palindrome
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
word = input("Enter a word: ").lower()
reversed_word = word[::-1]

if word == reversed_word:
    print(f'"{word}" is a palindrome')
else:
    print(f'"{word}" is not a palindrome')
```
</details>

---

### التحدي 8: آلة حاسبة متقدمة

**المهمة**: أنشئ آلة حاسبة:
- تسأل عن رقمين
- تسأل عن العملية (+, -, *, /)
- تنفذ العملية
- تتعامل مع القسمة على صفر
- تسمح بحسابات مستمرة حتى يخرج المستخدم

**مثال على الإخراج**:
```
Enter first number: 10
Enter operation (+, -, *, /): /
Enter second number: 2
Result: 5.0

Calculate again? (yes/no): yes
Enter first number: 8
Enter operation (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero

Calculate again? (yes/no): no
Thank you!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
while True:
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print(f"Result: {result}")
    else:
        print("Invalid operation")

    continue_calc = input("\nCalculate again? (yes/no): ")
    if continue_calc.lower() != "yes":
        print("Thank you!")
        break
```
</details>

---

### التحدي 9: هرم الأرقام

**المهمة**: اطبع هرم الأرقام هذا:
```
1
22
333
4444
55555
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
for i in range(1, 6):
    print(str(i) * i)
```
</details>

---

### التحدي 10: برنامج موجه بالقائمة

**المهمة**: أنشئ برنامجاً بقائمة:
```
1. Calculate area of rectangle
2. Calculate area of circle
3. Calculate area of triangle
4. Exit
```

**مثال على الإخراج**:
```
=== Area Calculator ===
1. Rectangle
2. Circle
3. Triangle
4. Exit

Choose an option: 1
Enter length: 5
Enter width: 3
Area: 15

Choose an option: 4
Goodbye!
```

<details>
<summary>انقر لرؤية الحل</summary>

```python
while True:
    print("\n=== Area Calculator ===")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Area: {area}")

    elif choice == "2":
        radius = float(input("Enter radius: "))
        area = 3.14159 * radius ** 2
        print(f"Area: {area:.2f}")

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area: {area}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please try again.")
```
</details>

---

## تحديات تحسين المشروع الصغير

حسّن حاسبة درجات الطلاب بهذه الميزات:

### التحسين 1: إيجاد أعلى وأدنى الدرجات

أضف كوداً لتتبع وعرض أعلى وأدنى الدرجات.

<details>
<summary>انقر لرؤية الحل</summary>

```python
num_students = int(input("How many students? "))

total_grades = 0
passing_students = 0
highest = 0
lowest = 100

for i in range(num_students):
    grade = float(input(f"Student {i + 1}: "))
    total_grades += grade

    if grade >= 60:
        passing_students += 1

    if grade > highest:
        highest = grade

    if grade < lowest:
        lowest = grade

average = total_grades / num_students

print(f"\nAverage: {average:.2f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passed: {passing_students}")
```
</details>

---

### التحسين 2: توزيع الدرجات

عد كم عدد الطلاب حصلوا على A, B, C, D, و F.

<details>
<summary>انقر لرؤية الحل</summary>

```python
num_students = int(input("How many students? "))

total_grades = 0
grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_F = 0

for i in range(num_students):
    grade = float(input(f"Student {i + 1}: "))
    total_grades += grade

    if grade >= 90:
        grade_A += 1
    elif grade >= 80:
        grade_B += 1
    elif grade >= 70:
        grade_C += 1
    elif grade >= 60:
        grade_D += 1
    else:
        grade_F += 1

average = total_grades / num_students

print(f"\nAverage: {average:.2f}")
print("\nGrade Distribution:")
print(f"A: {grade_A}")
print(f"B: {grade_B}")
print(f"C: {grade_C}")
print(f"D: {grade_D}")
print(f"F: {grade_F}")
```
</details>

---

### التحسين 3: التحقق من صحة الإدخال

تأكد من أن الدرجات بين 0 و 100.

<details>
<summary>انقر لرؤية الحل</summary>

```python
num_students = int(input("How many students? "))
total_grades = 0
passing_students = 0

for i in range(num_students):
    while True:
        grade = float(input(f"Student {i + 1}: "))

        if 0 <= grade <= 100:
            break
        else:
            print("Invalid! Grade must be between 0 and 100.")

    total_grades += grade

    if grade >= 60:
        passing_students += 1

average = total_grades / num_students
print(f"\nAverage: {average:.2f}")
print(f"Passed: {passing_students}")
```
</details>

---

## نصائح للنجاح

1. **اقرأ المشكلة بعناية** - تأكد من فهمك لما يُطلب منك
2. **خطط قبل الترميز** - اكتب pseudocode أو خطوات أولاً
3. **اختبر كودك** - جرب إدخالات مختلفة للتأكد من أنه يعمل
4. **صحح خطوة بخطوة** - استخدم print() لرؤية ما يحدث
5. **تعلم من الأخطاء** - رسائل الخطأ تساعدك على التعلم
6. **تدرب يومياً** - حتى 20-30 دقيقة تحدث فرقاً

---

## التقييم الذاتي

بعد إكمال هذه التمارين، يجب أن تكون قادراً على:

- [ ] استخدام المتغيرات وأنواع البيانات الأساسية
- [ ] الحصول على إدخال من المستخدمين وعرض الإخراج
- [ ] كتابة جمل if-elif-else
- [ ] استخدام العوامل المنطقية (and, or, not)
- [ ] كتابة حلقات for مع range()
- [ ] كتابة حلقات while
- [ ] استخدام break و continue
- [ ] دمج المفاهيم لحل المشاكل

إذا لم تكن واثقاً من أي من هذه، راجع الدروس وتدرب أكثر!

---

برمجة سعيدة! تذكر، الممارسة تصنع الإتقان!
