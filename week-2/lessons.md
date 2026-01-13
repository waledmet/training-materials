# Week 2 Lessons: Python Foundations (Deepening Skills)

Welcome to Week 2! This week you'll master core Python data structures and learn to write reusable, organized code with functions and modules.

---

## Table of Contents

1. [Lists: Working with Collections](#lists-working-with-collections)
2. [Tuples: Immutable Sequences](#tuples-immutable-sequences)
3. [Dictionaries: Key-Value Pairs](#dictionaries-key-value-pairs)
4. [Sets: Unique Collections](#sets-unique-collections)
5. [Functions: Reusable Code Blocks](#functions-reusable-code-blocks)
6. [Modules and Packages](#modules-and-packages)
7. [Error Handling](#error-handling)
8. [Virtual Environments](#virtual-environments)
9. [Mini-Project: To-Do List Application](#mini-project-to-do-list-application)

---

## Lists: Working with Collections

### What is a List?

A list is like a container that can hold multiple items in order. Think of it as a shopping list or a to-do list.

**Creating Lists:**

```python
# Empty list
shopping_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Can mix types!

# Check length
print(len(fruits))  # 3
```

### Accessing List Items

Lists use index numbers starting from 0:

```python
fruits = ["apple", "banana", "orange", "grape"]

# Access by index
print(fruits[0])   # apple (first item)
print(fruits[1])   # banana
print(fruits[-1])  # grape (last item)
print(fruits[-2])  # orange (second from end)

# Slicing (getting multiple items)
print(fruits[1:3])   # ['banana', 'orange']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['orange', 'grape']
```

### Modifying Lists

Lists are **mutable** (can be changed):

```python
fruits = ["apple", "banana", "orange"]

# Change an item
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'orange']

# Add items
fruits.append("grape")       # Add to end
print(fruits)  # ['apple', 'mango', 'orange', 'grape']

fruits.insert(1, "kiwi")     # Insert at position 1
print(fruits)  # ['apple', 'kiwi', 'mango', 'orange', 'grape']

# Remove items
fruits.remove("mango")       # Remove by value
print(fruits)  # ['apple', 'kiwi', 'orange', 'grape']

last_fruit = fruits.pop()    # Remove and return last item
print(last_fruit)  # grape
print(fruits)  # ['apple', 'kiwi', 'orange']

fruits.pop(0)               # Remove item at index 0
print(fruits)  # ['kiwi', 'orange']
```

### List Operations

```python
# Combine lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Repeat list
repeated = [0] * 5
print(repeated)  # [0, 0, 0, 0, 0]

# Check if item exists
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)    # True
print("grape" in fruits)    # False

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # 3

# Find index
fruits = ["apple", "banana", "orange"]
print(fruits.index("banana"))  # 1
```

### Looping Through Lists

```python
fruits = ["apple", "banana", "orange"]

# Method 1: Loop through items
for fruit in fruits:
    print(fruit)

# Method 2: Loop with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Method 3: Loop with enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### List Methods Summary

```python
fruits = ["apple", "banana", "orange"]

# Adding items
fruits.append("grape")      # Add to end
fruits.insert(0, "kiwi")    # Insert at position
fruits.extend([1, 2, 3])    # Add multiple items

# Removing items
fruits.remove("apple")      # Remove by value
fruits.pop()                # Remove last
fruits.pop(0)               # Remove at index
fruits.clear()              # Remove all

# Sorting
numbers = [3, 1, 4, 1, 5]
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5]

numbers.reverse()           # Reverse in place
print(numbers)              # [5, 4, 3, 1, 1]

# Copying
original = [1, 2, 3]
copy1 = original.copy()     # Create a copy
copy2 = original[:]         # Another way to copy
```

### Practical Example: Managing Students

```python
# Student names list
students = ["Ahmed", "Sara", "Mohammed"]

# Add new student
students.append("Fatima")
print(f"Students: {students}")

# Remove a student
students.remove("Sara")
print(f"After removal: {students}")

# Check if student exists
name = input("Enter student name: ")
if name in students:
    print(f"{name} is in the class")
else:
    print(f"{name} is not in the class")

# Print all students
print("\nClass roster:")
for i, student in enumerate(students, 1):
    print(f"{i}. {student}")
```

---

## Tuples: Immutable Sequences

### What is a Tuple?

A tuple is like a list, but **immutable** (cannot be changed after creation). Use tuples for data that shouldn't change.

**Creating Tuples:**

```python
# Empty tuple
empty = ()

# Tuple with items
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed = (1, "hello", 3.14)

# Single item tuple (note the comma!)
single = (42,)     # This is a tuple
not_tuple = (42)   # This is just an int!

# Without parentheses (tuple packing)
point = 10, 20, 30
print(type(point))  # <class 'tuple'>
```

### Accessing Tuple Items

Same as lists:

```python
coordinates = (10, 20, 30)

print(coordinates[0])   # 10
print(coordinates[-1])  # 30
print(coordinates[1:3]) # (20, 30)

# Tuple unpacking
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Swap variables using tuples
a = 5
b = 10
a, b = b, a  # Swap!
print(a, b)  # 10 5
```

### When to Use Tuples

```python
# 1. Return multiple values from functions
def get_user_info():
    name = "Ahmed"
    age = 25
    city = "Riyadh"
    return name, age, city  # Returns a tuple

user_name, user_age, user_city = get_user_info()

# 2. Use as dictionary keys (lists can't do this!)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}

# 3. Protect data from modification
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
```

---

## Dictionaries: Key-Value Pairs

### What is a Dictionary?

A dictionary stores data in **key-value pairs**. Think of it like a real dictionary where you look up a word (key) to find its meaning (value).

**Creating Dictionaries:**

```python
# Empty dictionary
empty = {}

# Dictionary with data
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5,
    "is_active": True
}

# Another way
person = dict(name="Sara", age=25, city="Jeddah")
```

### Accessing Dictionary Values

```python
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5
}

# Access by key
print(student["name"])   # Ahmed
print(student["age"])    # 22

# Safe access with get()
print(student.get("name"))    # Ahmed
print(student.get("email"))   # None (doesn't exist)
print(student.get("email", "No email"))  # Default value
```

### Modifying Dictionaries

```python
student = {
    "name": "Ahmed",
    "age": 22
}

# Add/modify items
student["email"] = "ahmed@example.com"  # Add new
student["age"] = 23                     # Modify existing

print(student)
# {'name': 'Ahmed', 'age': 23, 'email': 'ahmed@example.com'}

# Remove items
del student["email"]     # Delete specific key

removed_age = student.pop("age")  # Remove and return value
print(removed_age)  # 23

student.clear()  # Remove all items
```

### Dictionary Methods

```python
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5
}

# Get all keys
print(student.keys())   # dict_keys(['name', 'age', 'grade'])

# Get all values
print(student.values()) # dict_values(['Ahmed', 22, 85.5])

# Get all key-value pairs
print(student.items())  # dict_items([('name', 'Ahmed'), ...])

# Check if key exists
if "name" in student:
    print("Name exists!")

# Get number of items
print(len(student))  # 3
```

### Looping Through Dictionaries

```python
student = {
    "name": "Ahmed",
    "age": 22,
    "grade": 85.5
}

# Loop through keys
for key in student:
    print(key)

# Loop through keys explicitly
for key in student.keys():
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

### Practical Example: Student Database

```python
# Dictionary of students
students = {
    "S001": {"name": "Ahmed", "grade": 85, "age": 20},
    "S002": {"name": "Sara", "grade": 92, "age": 19},
    "S003": {"name": "Mohammed", "grade": 78, "age": 21}
}

# Access a student
student_id = "S001"
student = students[student_id]
print(f"Name: {student['name']}")
print(f"Grade: {student['grade']}")

# Add new student
students["S004"] = {
    "name": "Fatima",
    "grade": 88,
    "age": 20
}

# Loop through all students
print("\nAll Students:")
for id, info in students.items():
    print(f"{id}: {info['name']} - Grade: {info['grade']}")

# Calculate average grade
total = sum(s['grade'] for s in students.values())
average = total / len(students)
print(f"\nAverage grade: {average:.2f}")
```

---

## Sets: Unique Collections

### What is a Set?

A set is an **unordered** collection of **unique** items. No duplicates allowed!

**Creating Sets:**

```python
# Empty set (must use set(), not {})
empty = set()

# Set with items
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# Convert list to set (removes duplicates)
numbers_list = [1, 2, 2, 3, 3, 3, 4]
numbers_set = set(numbers_list)
print(numbers_set)  # {1, 2, 3, 4}
```

### Set Operations

```python
# Add items
fruits = {"apple", "banana"}
fruits.add("orange")
fruits.add("apple")  # Won't add duplicate
print(fruits)  # {'apple', 'banana', 'orange'}

# Remove items
fruits.remove("banana")      # Raises error if not found
fruits.discard("grape")      # No error if not found
fruits.pop()                 # Remove random item

# Check membership
print("apple" in fruits)  # True

# Get size
print(len(fruits))
```

### Mathematical Set Operations

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union (all items from both)
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.union(set2))

# Intersection (common items)
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))

# Difference (in first, not in second)
print(set1 - set2)  # {1, 2, 3}
print(set1.difference(set2))

# Symmetric difference (in either, but not both)
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))
```

### When to Use Sets

```python
# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)  # [1, 2, 3, 4, 5]

# Check for common items
course1_students = {"Ahmed", "Sara", "Mohammed"}
course2_students = {"Sara", "Ali", "Fatima"}

# Who takes both courses?
both_courses = course1_students & course2_students
print(both_courses)  # {'Sara'}

# Who takes only course 1?
only_course1 = course1_students - course2_students
print(only_course1)  # {'Ahmed', 'Mohammed'}
```

---

## Functions: Reusable Code Blocks

### Why Functions?

Functions let you write code once and use it many times. DRY principle: Don't Repeat Yourself!

### Defining Functions

```python
# Basic function
def greet():
    print("Hello!")

# Call the function
greet()  # Hello!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ahmed")   # Hello, Ahmed!
greet_person("Sara")    # Hello, Sara!

# Multiple parameters
def greet_full(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet_full("Ahmed", "Ali")  # Hello, Ahmed Ali!
```

### Return Values

```python
# Function that returns a value
def add(a, b):
    result = a + b
    return result

sum = add(5, 3)
print(sum)  # 8

# Return multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Function with no return (returns None)
def print_message(msg):
    print(msg)

result = print_message("Hello")
print(result)  # None
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ahmed")              # Hello, Ahmed!
greet("Sara", "Hi")         # Hi, Sara!
greet("Ali", greeting="Hey")  # Hey, Ali!

# Default values should be at the end
def create_profile(name, age=18, city="Riyadh"):
    return {"name": name, "age": age, "city": city}

profile1 = create_profile("Ahmed")
profile2 = create_profile("Sara", 25)
profile3 = create_profile("Ali", 30, "Jeddah")
```

### Scope: Local vs Global Variables

```python
# Global variable
x = 10

def print_x():
    print(x)  # Can read global variable

print_x()  # 10

# Local variable
def my_function():
    y = 20  # Local to this function
    print(y)

my_function()  # 20
# print(y)  # Error! y doesn't exist outside the function

# Modifying global variables
count = 0

def increment():
    global count  # Declare we want to modify global
    count += 1

increment()
increment()
print(count)  # 2
```

### Practical Example: Tax Calculator

```python
def calculate_tax(price, tax_rate=0.15):
    """
    Calculate total price including tax.

    Args:
        price: The base price
        tax_rate: Tax rate (default 15%)

    Returns:
        Total price including tax
    """
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

# Use the function
item_price = 100
total_price = calculate_tax(item_price)
print(f"Total: ${total_price:.2f}")  # Total: $115.00

# With custom tax rate
total_price = calculate_tax(100, 0.20)
print(f"Total: ${total_price:.2f}")  # Total: $120.00
```

### More Function Examples

```python
# Check if number is even
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# Calculate area of rectangle
def rectangle_area(length, width):
    return length * width

area = rectangle_area(5, 3)
print(f"Area: {area}")  # Area: 15

# Filter passed students
def filter_passed_students(students):
    """Returns list of students who passed (grade >= 60)"""
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

## Modules and Packages

### What are Modules?

A module is a Python file containing functions, classes, and variables that you can use in other programs.

### Using Built-in Modules

```python
# Import entire module
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.pow(2, 3))    # 8.0

# Import specific items
from math import pi, sqrt

print(pi)       # 3.141592653589793
print(sqrt(25)) # 5.0

# Import with alias
import math as m

print(m.pi)
print(m.sqrt(16))

# Import everything (not recommended)
from math import *

print(ceil(3.2))  # 4
```

### Common Standard Library Modules

#### 1. random - Generate random numbers

```python
import random

# Random integer
dice = random.randint(1, 6)
print(f"Dice roll: {dice}")

# Random choice from list
fruits = ["apple", "banana", "orange"]
fruit = random.choice(fruits)
print(f"Random fruit: {fruit}")

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Random float between 0 and 1
print(random.random())
```

#### 2. datetime - Work with dates and times

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)

# Current date
today = datetime.date.today()
print(today)

# Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# Calculate age
birth_date = datetime.date(2000, 1, 15)
age = (today - birth_date).days // 365
print(f"Age: {age}")
```

#### 3. os - Operating system functions

```python
import os

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in directory
files = os.listdir()
print("Files:", files)

# Check if file exists
exists = os.path.exists("myfile.txt")
print(f"File exists: {exists}")
```

### Creating Your Own Module

**File: calculator.py**
```python
# calculator.py
"""A simple calculator module"""

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

**File: main.py**
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

## Error Handling

### Why Handle Errors?

Errors will happen. Instead of crashing, handle them gracefully!

### Try-Except Block

```python
# Without error handling
# age = int(input("Enter age: "))  # Crashes if user enters "abc"

# With error handling
try:
    age = int(input("Enter age: "))
    print(f"Your age is {age}")
except:
    print("Invalid input! Please enter a number.")
```

### Catching Specific Errors

```python
# Catch specific error types
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
    # Runs if no error occurred
    print(f"Result: {result}")
finally:
    # Always runs
    print("Operation complete!")
```

### Practical Example: Safe Division

```python
def safe_divide(a, b):
    """Safely divide two numbers"""
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

## Virtual Environments

### What is a Virtual Environment?

A virtual environment is an isolated Python environment for your project. It keeps project dependencies separate.

### Why Use Virtual Environments?

- Different projects need different package versions
- Avoid conflicts between packages
- Easy to share project requirements
- Clean and organized

### Creating a Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Deactivate
deactivate
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate
deactivate
```

### Installing Packages with pip

```bash
# Activate virtual environment first!

# Install a package
pip install requests

# Install specific version
pip install django==4.2.0

# List installed packages
pip list

# Save requirements
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Uninstall package
pip uninstall requests
```

### Requirements.txt Example

```
# requirements.txt
django==4.2.0
requests==2.31.0
python-dateutil==2.8.2
```

### Best Practice Workflow

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 4. Install packages
pip install django requests

# 5. Save requirements
pip freeze > requirements.txt

# 6. Work on your project...

# 7. Deactivate when done
deactivate
```

---

## Mini-Project: To-Do List Application

Let's build a terminal-based to-do list app using everything we learned!

### Requirements

1. Add tasks
2. View all tasks
3. Mark tasks as done
4. Delete tasks
5. Save and load tasks from file
6. Use functions for organization
7. Handle errors gracefully

### Step-by-Step Implementation

```python
import json

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file"""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Save tasks to file"""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def add_task(tasks):
    """Add a new task"""
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
    """Display all tasks"""
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
    """Mark a task as done"""
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
    """Delete a task"""
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
    """Display menu options"""
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
    """Main function"""
    print("Welcome to To-Do List App!")

    # Load existing tasks
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

# Run the app
if __name__ == "__main__":
    main()
```

### Testing the App

Try these actions:
1. Add several tasks
2. View the task list
3. Mark some tasks as done
4. Delete a task
5. Exit and restart to verify tasks are saved

---

## Key Takeaways from Week 2

**Data Structures:**
- **Lists** - Ordered, mutable collections
- **Tuples** - Ordered, immutable collections
- **Dictionaries** - Key-value pairs
- **Sets** - Unordered, unique items

**Functions:**
- Break code into reusable pieces
- Accept parameters and return values
- Use default parameters for flexibility
- Understand variable scope

**Modules:**
- Use built-in modules (math, random, datetime)
- Create your own modules
- Keep code organized

**Error Handling:**
- Use try-except to handle errors
- Catch specific exception types
- Provide helpful error messages

**Virtual Environments:**
- Isolate project dependencies
- Use pip to manage packages
- Create requirements.txt

---

## Next Steps

**Before Week 3:**
- Complete all practice exercises
- Build the to-do list mini-project
- Try adding new features to the project
- Review data structures
- Practice writing functions

**Week 3 Preview:**
You'll learn about:
- Web concepts (Client-Server, HTTP)
- HTML and CSS basics
- Git and GitHub workflows
- Building static web pages

Keep practicing and see you next week!
