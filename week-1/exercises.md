# Week 1 Practice Exercises

This file contains practice exercises for Week 1. Try to solve each problem on your own before looking at the solution!

---

## Table of Contents

1. [Day 1-2: Variables and Basic Operations](#day-1-2-variables-and-basic-operations)
2. [Day 3: If Statements](#day-3-if-statements)
3. [Day 4: Loops](#day-4-loops)
4. [Day 5: Challenge Problems](#day-5-challenge-problems)
5. [Solutions](#solutions)

---

## Day 1-2: Variables and Basic Operations

### Exercise 1: Hello, You!

**Task**: Write a program that asks for the user's name and greets them.

**Example Output**:
```
What is your name? Ahmed
Hello, Ahmed! Welcome to Python programming.
```

<details>
<summary>Click to see solution</summary>

```python
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python programming.")
```
</details>

---

### Exercise 2: Simple Calculator

**Task**: Write a program that:
- Asks for two numbers
- Calculates and displays:
  - Sum
  - Difference
  - Product
  - Division

**Example Output**:
```
Enter first number: 10
Enter second number: 3
Sum: 13
Difference: 7
Product: 30
Division: 3.33
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 3: Area Calculator

**Task**: Write a program that calculates the area of a rectangle.
- Ask for length and width
- Calculate area (length × width)
- Display the result

**Example Output**:
```
Enter length: 5
Enter width: 3
The area is: 15
```

<details>
<summary>Click to see solution</summary>

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print(f"The area is: {area}")
```
</details>

---

### Exercise 4: Temperature Converter

**Task**: Convert Celsius to Fahrenheit.
- Formula: F = (C × 9/5) + 32
- Ask for temperature in Celsius
- Display in Fahrenheit

**Example Output**:
```
Enter temperature in Celsius: 25
25°C is 77.0°F
```

<details>
<summary>Click to see solution</summary>

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is {fahrenheit}°F")
```
</details>

---

### Exercise 5: Personal Info

**Task**: Create a program that collects and displays personal information:
- Name
- Age
- Height (in meters)
- Calculate and show age next year

**Example Output**:
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
<summary>Click to see solution</summary>

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

## Day 3: If Statements

### Exercise 6: Even or Odd

**Task**: Write a program that checks if a number is even or odd.

**Example Output**:
```
Enter a number: 7
7 is odd
```

<details>
<summary>Click to see solution</summary>

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```
</details>

---

### Exercise 7: Age Category

**Task**: Determine age category:
- 0-12: Child
- 13-19: Teenager
- 20-59: Adult
- 60+: Senior

**Example Output**:
```
Enter your age: 25
You are an Adult
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 8: Grade Calculator

**Task**: Convert numeric grade to letter grade:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

**Example Output**:
```
Enter your grade: 85
Your grade is: B
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 9: Positive, Negative, or Zero

**Task**: Check if a number is positive, negative, or zero.

**Example Output**:
```
Enter a number: -5
The number is negative
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 10: Login System

**Task**: Create a simple login system:
- Correct username: "admin"
- Correct password: "python123"
- Check both and display appropriate message

**Example Output**:
```
Username: admin
Password: python123
Login successful!
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 11: Discount Calculator

**Task**: Calculate discount based on purchase amount:
- $100+: 20% discount
- $50-$99: 10% discount
- Below $50: No discount

**Example Output**:
```
Enter purchase amount: 120
Discount: 20%
Final price: $96.00
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 12: Largest of Three Numbers

**Task**: Find the largest of three numbers.

**Example Output**:
```
Enter first number: 45
Enter second number: 82
Enter third number: 37
The largest number is: 82
```

<details>
<summary>Click to see solution</summary>

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

## Day 4: Loops

### Exercise 13: Count to Ten

**Task**: Print numbers from 1 to 10.

**Expected Output**:
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
<summary>Click to see solution</summary>

```python
for i in range(1, 11):
    print(i)
```
</details>

---

### Exercise 14: Even Numbers

**Task**: Print all even numbers from 1 to 20.

**Expected Output**:
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
<summary>Click to see solution</summary>

```python
# Method 1: Using step
for i in range(2, 21, 2):
    print(i)

# Method 2: Using if
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```
</details>

---

### Exercise 15: Sum Calculator

**Task**: Calculate the sum of numbers from 1 to 100.

**Expected Output**:
```
The sum of numbers from 1 to 100 is: 5050
```

<details>
<summary>Click to see solution</summary>

```python
total = 0
for i in range(1, 101):
    total += i

print(f"The sum of numbers from 1 to 100 is: {total}")
```
</details>

---

### Exercise 16: Multiplication Table

**Task**: Print the multiplication table for a given number (1 to 10).

**Example Output**:
```
Enter a number: 7
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70
```

<details>
<summary>Click to see solution</summary>

```python
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```
</details>

---

### Exercise 17: Countdown

**Task**: Print a countdown from 10 to 1, then print "Blast off!"

**Expected Output**:
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
<summary>Click to see solution</summary>

```python
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```
</details>

---

### Exercise 18: Password Validator (While Loop)

**Task**: Keep asking for password until correct:
- Correct password: "secret"
- Maximum 3 attempts
- Lock account after 3 failed attempts

**Example Output**:
```
Enter password: wrong
Incorrect! 2 attempts left
Enter password: wrong
Incorrect! 1 attempts left
Enter password: secret
Access granted!
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 19: Number Guessing Game

**Task**: Create a number guessing game:
- Secret number between 1-10
- Give hints (too high/too low)
- Continue until guessed correctly

**Example Output**:
```
Guess the number (1-10): 5
Too low!
Guess the number (1-10): 8
Too high!
Guess the number (1-10): 7
Correct! You win!
```

<details>
<summary>Click to see solution</summary>

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

### Exercise 20: Factorial Calculator

**Task**: Calculate factorial of a number.
- Factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120

**Example Output**:
```
Enter a number: 5
Factorial of 5 is: 120
```

<details>
<summary>Click to see solution</summary>

```python
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is: {factorial}")
```
</details>

---

## Day 5: Challenge Problems

### Challenge 1: FizzBuzz

**Task**: Print numbers from 1 to 30, but:
- For multiples of 3, print "Fizz"
- For multiples of 5, print "Buzz"
- For multiples of both 3 and 5, print "FizzBuzz"
- Otherwise, print the number

**Expected Output**:
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
<summary>Click to see solution</summary>

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

### Challenge 2: Prime Number Checker

**Task**: Check if a number is prime (only divisible by 1 and itself).

**Example Output**:
```
Enter a number: 17
17 is a prime number
```

<details>
<summary>Click to see solution</summary>

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

### Challenge 3: Pattern Printing

**Task**: Print this pattern:
```
*
**
***
****
*****
```

<details>
<summary>Click to see solution</summary>

```python
for i in range(1, 6):
    print("*" * i)
```
</details>

---

### Challenge 4: Reverse Pattern

**Task**: Print this pattern:
```
*****
****
***
**
*
```

<details>
<summary>Click to see solution</summary>

```python
for i in range(5, 0, -1):
    print("*" * i)
```
</details>

---

### Challenge 5: Sum of Even Numbers

**Task**: Calculate the sum of all even numbers from 1 to 100.

**Expected Output**:
```
The sum of even numbers from 1 to 100 is: 2550
```

<details>
<summary>Click to see solution</summary>

```python
total = 0

for i in range(2, 101, 2):
    total += i

print(f"The sum of even numbers from 1 to 100 is: {total}")
```
</details>

---

### Challenge 6: Digit Sum

**Task**: Calculate the sum of digits in a number.
- Example: 1234 → 1+2+3+4 = 10

**Example Output**:
```
Enter a number: 1234
Sum of digits: 10
```

<details>
<summary>Click to see solution</summary>

```python
number = input("Enter a number: ")
digit_sum = 0

for digit in number:
    digit_sum += int(digit)

print(f"Sum of digits: {digit_sum}")
```
</details>

---

### Challenge 7: Palindrome Checker

**Task**: Check if a word is a palindrome (reads same forwards and backwards).
- Examples: "racecar", "madam", "level"

**Example Output**:
```
Enter a word: racecar
"racecar" is a palindrome
```

<details>
<summary>Click to see solution</summary>

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

### Challenge 8: Advanced Calculator

**Task**: Create a calculator that:
- Asks for two numbers
- Asks for operation (+, -, *, /)
- Performs the operation
- Handles division by zero
- Allows continuous calculations until user quits

**Example Output**:
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
<summary>Click to see solution</summary>

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

### Challenge 9: Number Pyramid

**Task**: Print this number pyramid:
```
1
22
333
4444
55555
```

<details>
<summary>Click to see solution</summary>

```python
for i in range(1, 6):
    print(str(i) * i)
```
</details>

---

### Challenge 10: Menu-Driven Program

**Task**: Create a program with a menu:
```
1. Calculate area of rectangle
2. Calculate area of circle
3. Calculate area of triangle
4. Exit
```

**Example Output**:
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
<summary>Click to see solution</summary>

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

## Mini-Project Enhancement Challenges

Enhance the Student Grades Calculator with these features:

### Enhancement 1: Find Highest and Lowest Grades

Add code to track and display the highest and lowest grades.

<details>
<summary>Click to see solution</summary>

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

### Enhancement 2: Grade Distribution

Count how many students got A, B, C, D, and F.

<details>
<summary>Click to see solution</summary>

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

### Enhancement 3: Input Validation

Make sure grades are between 0 and 100.

<details>
<summary>Click to see solution</summary>

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

## Tips for Success

1. **Read the problem carefully** - Make sure you understand what's being asked
2. **Plan before coding** - Write pseudocode or steps first
3. **Test your code** - Try different inputs to make sure it works
4. **Debug step by step** - Use print() to see what's happening
5. **Learn from errors** - Error messages help you learn
6. **Practice daily** - Even 20-30 minutes makes a difference

---

## Self-Assessment

After completing these exercises, you should be able to:

- [ ] Use variables and basic data types
- [ ] Get input from users and display output
- [ ] Write if-elif-else statements
- [ ] Use logical operators (and, or, not)
- [ ] Write for loops with range()
- [ ] Write while loops
- [ ] Use break and continue
- [ ] Combine concepts to solve problems

If you're not confident with any of these, review the lessons and practice more!

---

Happy coding! Remember, practice makes perfect!
