# Week 2 Practice Exercises

This file contains practice exercises for Week 2. Try to solve each problem on your own before looking at the solution!

---

## Table of Contents

1. [Day 1-2: Lists](#day-1-2-lists)
2. [Day 3: Tuples and Dictionaries](#day-3-tuples-and-dictionaries)
3. [Day 4: Sets and Functions](#day-4-sets-and-functions)
4. [Day 5: Modules and Error Handling](#day-5-modules-and-error-handling)
5. [Challenge Problems](#challenge-problems)

---

## Day 1-2: Lists

### Exercise 1: Create and Access Lists

**Task**: Create a list of your favorite foods and print the first and last items.

**Example Output**:
```
Foods: ['pizza', 'pasta', 'burger', 'sushi']
First: pizza
Last: sushi
```

<details>
<summary>Click to see solution</summary>

```python
foods = ["pizza", "pasta", "burger", "sushi"]
print(f"Foods: {foods}")
print(f"First: {foods[0]}")
print(f"Last: {foods[-1]}")
```
</details>

---

### Exercise 2: Add and Remove Items

**Task**: Start with an empty list, add 5 items, remove 2 items, and print the final list.

**Example Output**:
```
After adding: ['apple', 'banana', 'orange', 'grape', 'mango']
After removing: ['apple', 'orange', 'grape']
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 3: List Slicing

**Task**: Create a list of numbers 1-10, then print:
- First 3 numbers
- Last 3 numbers
- Middle numbers (4-7)

**Example Output**:
```
Full list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First 3: [1, 2, 3]
Last 3: [8, 9, 10]
Middle: [4, 5, 6, 7]
```

<details>
<summary>Click to see solution</summary>

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Full list: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle: {numbers[3:7]}")
```
</details>

---

### Exercise 4: Loop Through List

**Task**: Create a list of names and print each name with its position.

**Example Output**:
```
1. Ahmed
2. Sara
3. Mohammed
4. Fatima
```

<details>
<summary>Click to see solution</summary>

```python
names = ["Ahmed", "Sara", "Mohammed", "Fatima"]

for i, name in enumerate(names, 1):
    print(f"{i}. {name}")
```
</details>

---

### Exercise 5: Shopping List Manager

**Task**: Create a shopping list program that:
- Starts with an empty list
- Lets user add 3 items
- Shows the list
- Lets user remove 1 item
- Shows final list

**Example Output**:
```
Add item 1: milk
Add item 2: bread
Add item 3: eggs
Shopping list: ['milk', 'bread', 'eggs']
Remove item: bread
Final list: ['milk', 'eggs']
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 6: Find Maximum in List

**Task**: Create a list of numbers and find the maximum value without using max().

**Example Output**:
```
Numbers: [45, 23, 67, 12, 89, 34]
Maximum: 89
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 7: Count Even Numbers

**Task**: Create a list of numbers and count how many are even.

**Example Output**:
```
Numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers count: 5
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 8: Reverse a List

**Task**: Create a list and print it in reverse order without using reverse().

**Example Output**:
```
Original: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
```

<details>
<summary>Click to see solution</summary>

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

## Day 3: Tuples and Dictionaries

### Exercise 9: Create and Access Tuples

**Task**: Create a tuple with your personal information (name, age, city) and print each item.

**Example Output**:
```
Name: Ahmed
Age: 25
City: Cairo
```

<details>
<summary>Click to see solution</summary>

```python
person = ("Ahmed", 25, "Cairo")

print(f"Name: {person[0]}")
print(f"Age: {person[1]}")
print(f"City: {person[2]}")
```
</details>

---

### Exercise 10: Tuple Unpacking

**Task**: Create a tuple with coordinates (x, y) and unpack them into variables.

**Example Output**:
```
Coordinates: (10, 20)
X: 10
Y: 20
```

<details>
<summary>Click to see solution</summary>

```python
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

x, y = coordinates
print(f"X: {x}")
print(f"Y: {y}")
```
</details>

---

### Exercise 11: Create a Dictionary

**Task**: Create a dictionary to store student information (name, age, grade, city).

**Example Output**:
```
Student: {'name': 'Sara', 'age': 22, 'grade': 'A', 'city': 'Dubai'}
Name: Sara
Grade: A
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 12: Add and Remove Dictionary Items

**Task**: Create a dictionary, add 2 new items, remove 1 item, and print the result.

**Example Output**:
```
Original: {'name': 'Ahmed', 'age': 25}
After adding: {'name': 'Ahmed', 'age': 25, 'city': 'Cairo', 'job': 'Engineer'}
After removing: {'name': 'Ahmed', 'city': 'Cairo', 'job': 'Engineer'}
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 13: Loop Through Dictionary

**Task**: Create a dictionary of product prices and print each product with its price.

**Example Output**:
```
Product: apple, Price: $2.50
Product: banana, Price: $1.20
Product: orange, Price: $3.00
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 14: Dictionary Methods

**Task**: Create a dictionary and demonstrate get(), keys(), values(), and items().

**Example Output**:
```
Age: 25
Default: N/A
Keys: dict_keys(['name', 'age', 'city'])
Values: dict_values(['Ahmed', 25, 'Cairo'])
Items: dict_items([('name', 'Ahmed'), ('age', 25), ('city', 'Cairo')])
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 15: Phone Book

**Task**: Create a simple phone book program:
- Store 3 contacts (name: phone number)
- Let user search for a name
- Display the phone number or "Not found"

**Example Output**:
```
Search for: Ahmed
Phone: 0501234567
```

<details>
<summary>Click to see solution</summary>

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

## Day 4: Sets and Functions

### Exercise 16: Create and Use Sets

**Task**: Create two sets of numbers and show union, intersection, and difference.

**Example Output**:
```
Set A: {1, 2, 3, 4, 5}
Set B: {4, 5, 6, 7, 8}
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
Difference: {1, 2, 3}
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 17: Remove Duplicates

**Task**: Create a list with duplicates and use a set to remove them.

**Example Output**:
```
Original: [1, 2, 2, 3, 3, 3, 4, 5, 5]
Unique: [1, 2, 3, 4, 5]
```

<details>
<summary>Click to see solution</summary>

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"Original: {numbers}")

unique = list(set(numbers))
unique.sort()
print(f"Unique: {unique}")
```
</details>

---

### Exercise 18: Simple Function

**Task**: Create a function that greets a person by name.

**Example Output**:
```
Hello, Ahmed! Welcome!
Hello, Sara! Welcome!
```

<details>
<summary>Click to see solution</summary>

```python
def greet(name):
    print(f"Hello, {name}! Welcome!")

greet("Ahmed")
greet("Sara")
```
</details>

---

### Exercise 19: Function with Return

**Task**: Create a function that calculates the area of a rectangle.

**Example Output**:
```
Area: 15
Area: 24
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 20: Function with Default Parameters

**Task**: Create a function that calculates power with default exponent of 2.

**Example Output**:
```
5^2 = 25
3^3 = 27
2^2 = 4
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 21: Temperature Converter Function

**Task**: Create functions to convert between Celsius and Fahrenheit.

**Example Output**:
```
25°C = 77.0°F
77°F = 25.0°C
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 22: List Processing Function

**Task**: Create a function that takes a list and returns the sum and average.

**Example Output**:
```
Numbers: [10, 20, 30, 40, 50]
Sum: 150
Average: 30.0
```

<details>
<summary>Click to see solution</summary>

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

## Day 5: Modules and Error Handling

### Exercise 23: Using Built-in Modules

**Task**: Use the math and random modules to:
- Calculate square root
- Generate a random number
- Calculate factorial

**Example Output**:
```
Square root of 16: 4.0
Random number (1-10): 7
Factorial of 5: 120
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 24: Date and Time

**Task**: Use datetime module to display current date and time.

**Example Output**:
```
Current date: 2025-01-15
Current time: 14:30:45
Day of week: Wednesday
```

<details>
<summary>Click to see solution</summary>

```python
from datetime import datetime

now = datetime.now()

print(f"Current date: {now.strftime('%Y-%m-%d')}")
print(f"Current time: {now.strftime('%H:%M:%S')}")
print(f"Day of week: {now.strftime('%A')}")
```
</details>

---

### Exercise 25: Try-Except Basic

**Task**: Write a program that handles division by zero error.

**Example Output**:
```
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 26: Multiple Exception Handling

**Task**: Handle both ValueError and ZeroDivisionError.

**Example Output**:
```
Enter a number: abc
Error: Please enter a valid number

Enter a number: 10
Enter divisor: 0
Error: Cannot divide by zero
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 27: File Reading with Error Handling

**Task**: Try to read a file and handle the error if it doesn't exist.

**Example Output**:
```
Error: File 'data.txt' not found
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 28: Try-Except-Finally

**Task**: Demonstrate finally block execution.

**Example Output**:
```
Attempting operation...
Error occurred
This always runs
```

<details>
<summary>Click to see solution</summary>

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

## Challenge Problems

### Challenge 1: Contact Manager

**Task**: Create a contact manager using a dictionary:
- Add contact
- Remove contact
- Search contact
- List all contacts

**Example Output**:
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
<summary>Click to see solution</summary>

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

### Challenge 2: Grade Statistics

**Task**: Create a function that takes a list of grades and returns:
- Average
- Highest
- Lowest
- Pass count (>=60)

**Example Output**:
```
Grades: [85, 92, 78, 60, 95, 88]
Average: 83.0
Highest: 95
Lowest: 60
Passed: 6
```

<details>
<summary>Click to see solution</summary>

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

### Challenge 3: Word Frequency Counter

**Task**: Count how many times each word appears in a sentence.

**Example Output**:
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
<summary>Click to see solution</summary>

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

### Challenge 4: List Comprehension Practice

**Task**: Use list comprehension to:
- Create list of squares from 1-10
- Create list of even numbers from 1-20
- Create list of lengths of words

**Example Output**:
```
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Evens: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Lengths: [5, 6, 6]
```

<details>
<summary>Click to see solution</summary>

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

### Challenge 5: Inventory System

**Task**: Create an inventory system using nested dictionaries:
- Each product has name, price, quantity
- Add product
- Update quantity
- Show inventory

**Example Output**:
```
Inventory:
apple: $2.50, Qty: 100
banana: $1.20, Qty: 150
```

<details>
<summary>Click to see solution</summary>

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

### Challenge 6: Calculator with Functions

**Task**: Create a calculator with separate functions for each operation and error handling.

**Example Output**:
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
<summary>Click to see solution</summary>

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

## Tips for Success

1. **Start with simple exercises** - Build your confidence
2. **Type, don't copy** - Muscle memory helps learning
3. **Experiment** - Try changing values and see what happens
4. **Use print()** - Debug by printing intermediate values
5. **Read error messages** - They tell you what's wrong
6. **Practice daily** - Consistency beats intensity
7. **Review solutions** - But try first on your own

---

## Self-Assessment

After completing these exercises, you should be able to:

- [ ] Create and manipulate lists
- [ ] Use tuples for immutable data
- [ ] Work with dictionaries (key-value pairs)
- [ ] Use sets for unique collections
- [ ] Write functions with parameters and return values
- [ ] Import and use modules
- [ ] Handle errors with try-except
- [ ] Solve real-world problems with data structures

If you're not confident with any of these, review the lessons and practice more!

---

Happy coding! Remember, every expert was once a beginner!
