# Week 1 Lessons: Computer & Web Basics + Intro to Python

Welcome to Week 1 of your Django Web Development journey! This week you'll learn the fundamentals of how the web works and start programming with Python.

---

## Table of Contents

1. [Understanding the Web](#understanding-the-web)
2. [Setting Up Your Development Environment](#setting-up-your-development-environment)
3. [Python Basics: Variables and Data Types](#python-basics-variables-and-data-types)
4. [Control Flow: Making Decisions](#control-flow-making-decisions)
5. [Loops: Repeating Actions](#loops-repeating-actions)
6. [Mini-Project: Student Grades Calculator](#mini-project-student-grades-calculator)

---

## Understanding the Web

### What is the Web?

The web (World Wide Web) is a system of interconnected documents and resources that you can access through the internet using a browser.

**Key Terms:**

**Website**: A collection of web pages that are related and accessed through a domain name.
- Example: google.com, facebook.com, github.com

**Domain**: A human-readable address for a website.
- Example: `www.example.com`

**URL (Uniform Resource Locator)**: The complete address of a resource on the web.
- Example: `https://www.example.com/page.html`
- Parts:
  - `https://` - Protocol
  - `www.example.com` - Domain
  - `/page.html` - Path to specific resource

### Browser vs Server

**Browser (Client)**:
- The application you use to access websites (Chrome, Firefox, Safari, Edge)
- Sends requests for web pages
- Displays the received content to you
- Think of it as a customer in a restaurant

**Server**:
- A powerful computer that stores websites and web applications
- Waits for requests from browsers
- Sends back the requested content
- Think of it as the kitchen in a restaurant

### HTTP: The Language of the Web

**HTTP** (Hypertext Transfer Protocol) is how browsers and servers communicate.

**Common HTTP Methods:**

**GET**: Request to get/retrieve data
- Example: Loading a web page
- Like asking "Can I see the menu?"

**POST**: Request to send/submit data
- Example: Submitting a form, creating a new post
- Like placing an order

**HTTP Status Codes:**
- **200 OK**: Success! The request worked
- **404 Not Found**: The requested resource doesn't exist
- **500 Internal Server Error**: Something went wrong on the server

### How a Website Loads

```
1. You type www.example.com in your browser
2. Browser sends HTTP GET request to server
3. Server finds the requested page
4. Server sends HTTP response with HTML, CSS, JS
5. Browser receives and displays the page
```

**Try This:**
1. Open your browser
2. Press F12 to open Developer Tools
3. Go to the "Network" tab
4. Visit any website
5. Watch the HTTP requests happen in real-time!

---

## Setting Up Your Development Environment

Before you can start programming, you need to install the necessary tools.

### What You'll Install:

1. **Python** - The programming language
2. **VS Code** - Where you'll write your code
3. **Git** - Version control to track your code changes
4. **GitHub Account** - To store and share your code online

### Installation Steps

See the `setup-instructions.md` file for detailed, step-by-step installation guides for your operating system.

### Your First Python Program

After installing Python and VS Code:

1. Create a folder called `python-training`
2. Open VS Code
3. Open the folder: File → Open Folder
4. Create a new file: `hello.py`
5. Type this code:

```python
print("Hello, World!")
```

6. Save the file (Ctrl+S or Cmd+S)
7. Right-click in the editor → Run Python File in Terminal

You should see: `Hello, World!`

Congratulations! You just wrote and ran your first Python program!

---

## Python Basics: Variables and Data Types

### What is a Variable?

A variable is like a labeled box where you can store information.

```python
name = "Ahmed"
```

Here:
- `name` is the variable name (the label on the box)
- `=` is the assignment operator (putting something in the box)
- `"Ahmed"` is the value (what's in the box)

### Variable Naming Rules

**Good variable names:**
```python
age = 25
first_name = "Sara"
total_price = 100.50
is_student = True
```

**Rules:**
- Use letters, numbers, and underscores only
- Must start with a letter or underscore
- Cannot use Python keywords (like `if`, `for`, `while`)
- Case sensitive (`Name` and `name` are different)

**Convention:**
- Use lowercase with underscores: `my_variable`
- Use descriptive names: `student_age` not `sa`

### Data Types

Python has several basic data types:

#### 1. Integer (int)
Whole numbers, positive or negative.

```python
age = 25
temperature = -5
year = 2024
```

#### 2. Float (float)
Decimal numbers.

```python
height = 1.75
price = 99.99
temperature = 36.6
```

#### 3. String (str)
Text, enclosed in quotes.

```python
name = "Mohammed"
message = 'Hello, World!'
address = "123 Main Street"
```

#### 4. Boolean (bool)
True or False values.

```python
is_student = True
has_graduated = False
is_raining = False
```

### Checking Types

Use the `type()` function:

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

### Input and Output

#### Output with print()

```python
print("Hello")
print("Welcome to Python")

name = "Sara"
print(name)

# Print multiple things
print("My name is", name)

# Print with f-strings (formatted strings)
age = 22
print(f"My name is {name} and I am {age} years old")
```

#### Input from User

```python
# Get text input
name = input("What is your name? ")
print("Hello, " + name)

# Get number input (need to convert)
age = input("What is your age? ")  # This is a string!
age = int(age)  # Convert to integer
print(f"Next year you will be {age + 1}")

# Or do it in one line
age = int(input("What is your age? "))
```

### Basic Operators

#### Arithmetic Operators

```python
a = 10
b = 3

print(a + b)   # 13 (addition)
print(a - b)   # 7  (subtraction)
print(a * b)   # 30 (multiplication)
print(a / b)   # 3.333... (division)
print(a // b)  # 3  (integer division)
print(a % b)   # 1  (remainder/modulo)
print(a ** b)  # 1000 (exponent/power)
```

#### String Operations

```python
first_name = "Mohammed"
last_name = "Ahmed"

# Concatenation (joining)
full_name = first_name + " " + last_name
print(full_name)  # Mohammed Ahmed

# Repetition
print("Ha" * 3)  # HaHaHa

# Length
print(len(full_name))  # 14
```

### Type Conversion

Converting between data types:

```python
# String to Integer
age_str = "25"
age_num = int(age_str)
print(age_num + 5)  # 30

# String to Float
price_str = "99.99"
price_num = float(price_str)
print(price_num * 2)  # 199.98

# Integer to String
age = 25
age_str = str(age)
print("I am " + age_str + " years old")

# Or use f-string (easier)
print(f"I am {age} years old")
```

### Comments

Comments are notes in your code that Python ignores.

```python
# This is a single-line comment

x = 5  # You can also put comments after code

"""
This is a
multi-line comment
It can span several lines
"""

# Comments are useful for:
# 1. Explaining what code does
# 2. Temporarily disabling code
# 3. Leaving notes for yourself or others
```

### Practice Example: Personal Info Program

```python
# Get user information
name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height in meters? "))
is_student = input("Are you a student? (yes/no) ")

# Convert yes/no to True/False
is_student = (is_student.lower() == "yes")

# Display information
print("\n--- Your Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Student: {is_student}")
print(f"Next year you will be {age + 1} years old")
```

---

## Control Flow: Making Decisions

Programs need to make decisions based on conditions. This is where `if` statements come in.

### Boolean Expressions

Boolean expressions evaluate to `True` or `False`.

```python
5 > 3   # True
5 < 3   # False
5 == 5  # True (equal to)
5 != 3  # True (not equal to)
5 >= 5  # True (greater than or equal to)
3 <= 2  # False (less than or equal to)
```

**Important**:
- `=` is assignment (giving a value)
- `==` is comparison (checking equality)

### The if Statement

```python
age = 18

if age >= 18:
    print("You are an adult")
```

**Structure:**
- `if` keyword
- Condition (must be True or False)
- Colon `:`
- Indented code block (what to do if True)

**Indentation is CRITICAL in Python!** Use 4 spaces or Tab.

### if-else Statement

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```

### if-elif-else Statement

For multiple conditions:

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

**How it works:**
1. Checks first `if` condition
2. If False, checks first `elif`
3. If False, checks next `elif`
4. Continues until one is True
5. If none are True, runs `else`
6. Only ONE block of code runs!

### Logical Operators

Combine multiple conditions:

#### and - Both must be True

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("Access denied")
```

#### or - At least one must be True

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")
```

#### not - Reverses the condition

```python
is_raining = False

if not is_raining:
    print("Good day to go out!")
else:
    print("Take an umbrella")
```

### Nested if Statements

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

### Practical Examples

#### Example 1: Temperature Advisory

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

#### Example 2: Login System

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

#### Example 3: Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

---

## Loops: Repeating Actions

Loops let you repeat code multiple times without writing it over and over.

### The for Loop

Used when you know how many times to repeat.

#### Basic for Loop with range()

```python
# Print "Hello" 5 times
for i in range(5):
    print("Hello")
```

#### Understanding range()

```python
# range(n) - from 0 to n-1
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# range(start, stop) - from start to stop-1
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 11, 2):
    print(i)
# Output: 0, 2, 4, 6, 8, 10

# Counting backwards
for i in range(10, 0, -1):
    print(i)
# Output: 10, 9, 8, ..., 1
```

#### Practical for Loop Examples

```python
# Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i  # Same as total = total + i
print(f"Sum: {total}")

# Multiplication table
number = 5
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

# Print even numbers
for i in range(2, 21, 2):
    print(i)
```

### The while Loop

Used when you don't know how many times to repeat.

```python
count = 1
while count <= 5:
    print(count)
    count += 1  # IMPORTANT: Don't forget to update!
```

**WARNING**: Always make sure the condition will eventually become False, or you'll have an infinite loop!

#### Infinite Loop (Don't Do This!)

```python
# BAD - This will never stop!
while True:
    print("Forever...")
# Use Ctrl+C to stop if this happens
```

#### Practical while Loop Examples

```python
# Password retry system
password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access granted!")
        break  # Exit the loop
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong! {remaining} attempts left")

if attempts == max_attempts:
    print("Account locked!")
```

```python
# Guess the number game
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

### break and continue

#### break - Exit the loop immediately

```python
for i in range(10):
    if i == 5:
        break  # Stop when i is 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

#### continue - Skip to next iteration

```python
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)
# Output: 0, 1, 3, 4
```

### Nested Loops

Loops inside loops:

```python
# Multiplication table for 2 and 3
for number in range(2, 4):
    print(f"\nTable for {number}:")
    for i in range(1, 6):
        print(f"{number} × {i} = {number * i}")
```

### Common Loop Patterns

#### Pattern 1: Accumulator

```python
# Sum all numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(total)
```

#### Pattern 2: Counter

```python
# Count how many even numbers from 1 to 20
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
print(f"There are {count} even numbers")
```

#### Pattern 3: Search

```python
# Find if a number is in a range
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

## Mini-Project: Student Grades Calculator

Now let's put everything together!

### Project Requirements

Create a program that:
1. Asks how many students
2. Gets each student's grade
3. Calculates the average
4. Counts passing students (grade >= 60)
5. Shows if the class passed overall

### Step-by-Step Solution

```python
# Step 1: Get number of students
num_students = int(input("How many students? "))

# Step 2: Initialize variables
total_grades = 0
passing_students = 0

# Step 3: Loop to get each grade
print("\nEnter grades:")
for i in range(num_students):
    # Get grade for student i+1 (since i starts at 0)
    grade = float(input(f"Student {i + 1}: "))

    # Add to total
    total_grades += grade

    # Check if passing
    if grade >= 60:
        passing_students += 1

# Step 4: Calculate average
average = total_grades / num_students

# Step 5: Display results
print("\n" + "="*40)
print("CLASS RESULTS")
print("="*40)
print(f"Number of students: {num_students}")
print(f"Average grade: {average:.2f}")
print(f"Students passed: {passing_students}")
print(f"Students failed: {num_students - passing_students}")

# Overall status
if average >= 60:
    print("\n✓ The class PASSED overall")
else:
    print("\n✗ The class FAILED overall")
```

### Understanding the Code

**Line by line:**

```python
num_students = int(input("How many students? "))
```
- Gets input from user
- Converts to integer
- Stores in `num_students`

```python
total_grades = 0
passing_students = 0
```
- Initialize accumulators
- Start at 0, will add to them later

```python
for i in range(num_students):
```
- Loop that many times
- `i` goes from 0 to num_students-1

```python
grade = float(input(f"Student {i + 1}: "))
```
- Get grade (as decimal number)
- Use `i + 1` for display (Student 1, 2, 3... instead of 0, 1, 2...)

```python
total_grades += grade
```
- Add current grade to running total
- Same as `total_grades = total_grades + grade`

```python
if grade >= 60:
    passing_students += 1
```
- Check if student passed
- If yes, increment counter

```python
average = total_grades / num_students
```
- Calculate average
- Total divided by count

```python
print(f"Average grade: {average:.2f}")
```
- `:.2f` means show 2 decimal places

### Testing Your Program

Try these test cases:

**Test 1: All Pass**
- 3 students
- Grades: 90, 85, 75
- Expected: Average 83.33, 3 passed

**Test 2: Mixed**
- 5 students
- Grades: 90, 50, 70, 45, 80
- Expected: Average 67, 3 passed, 2 failed

**Test 3: All Fail**
- 2 students
- Grades: 45, 30
- Expected: Average 37.5, 0 passed, class failed

---

## Key Takeaways from Week 1

**Concepts:**
- The web is based on client-server communication
- HTTP is the protocol browsers and servers use
- Python is a powerful and easy-to-learn programming language

**Skills:**
- Set up development environment
- Write Python scripts
- Use variables and data types
- Make decisions with if statements
- Repeat actions with loops
- Combine concepts to build a complete program

**Best Practices:**
- Use descriptive variable names
- Add comments to explain your code
- Test your code with different inputs
- Read error messages carefully
- Break problems into smaller steps

---

## Next Steps

**Before Week 2:**
- Complete all practice exercises
- Review your notes
- Try enhancing the mini-project
- Practice terminal commands
- Make sure all software is properly installed

**Week 2 Preview:**
You'll learn about:
- Lists and dictionaries
- Functions
- Modules and packages
- Virtual environments

Keep practicing and see you next week!

---

## Common Errors and How to Fix Them

### SyntaxError: invalid syntax

**Problem:**
```python
if age >= 18  # Missing colon
    print("Adult")
```

**Fix:**
```python
if age >= 18:  # Add colon
    print("Adult")
```

### IndentationError

**Problem:**
```python
if age >= 18:
print("Adult")  # Not indented
```

**Fix:**
```python
if age >= 18:
    print("Adult")  # Indent with 4 spaces or Tab
```

### NameError: name 'x' is not defined

**Problem:**
```python
print(age)  # age doesn't exist yet
age = 25
```

**Fix:**
```python
age = 25  # Define before using
print(age)
```

### TypeError: unsupported operand type(s)

**Problem:**
```python
age = "25"
next_age = age + 1  # Can't add number to string
```

**Fix:**
```python
age = int("25")  # Convert to integer
next_age = age + 1
```

### ValueError: invalid literal for int()

**Problem:**
```python
age = int("hello")  # Can't convert "hello" to number
```

**Fix:**
```python
# Make sure input is a valid number
age = int("25")  # This works
```

---

Remember: **Everyone makes these mistakes when learning!** Reading error messages and debugging is a normal part of programming. Don't get discouraged!

Happy coding!
