# Week 3 Lessons: Web Concepts, HTML/CSS Basics & Git

Welcome to Week 3! This week marks an exciting transition from Python programming to understanding how the web works. You'll learn web fundamentals, create your first web pages with HTML and CSS, and start using Git for version control.

---

## Table of Contents

1. [How the Web Works](#how-the-web-works)
2. [HTTP Protocol Fundamentals](#http-protocol-fundamentals)
3. [HTML Basics](#html-basics)
4. [CSS Basics](#css-basics)
5. [JSON Introduction](#json-introduction)
6. [Git and Version Control](#git-and-version-control)
7. [GitHub Integration](#github-integration)
8. [Mini-Project: Portfolio Website](#mini-project-portfolio-website)

---

## How the Web Works

### Client-Server Architecture

The web operates on a client-server model:

**Client:**
- Your web browser (Chrome, Firefox, Safari, Edge)
- Requests resources from servers
- Displays web pages to users
- Runs JavaScript code

**Server:**
- A computer that stores website files
- Listens for requests from clients
- Sends back responses (HTML, CSS, images, data)
- Can run backend code (Python, Node.js, PHP, etc.)

### The Request-Response Cycle

```
1. You type www.example.com in browser
   ↓
2. Browser sends HTTP request to server
   ↓
3. Server processes the request
   ↓
4. Server sends HTTP response with content
   ↓
5. Browser receives and displays the content
```

### Example: Loading a Web Page

```
User → Browser → DNS → Server
                         ↓
User ← Browser ← HTML, CSS, Images
```

**Step by step:**
1. **User enters URL**: `https://www.google.com`
2. **DNS lookup**: Converts domain to IP address (like a phone book)
3. **HTTP request**: Browser asks server for the page
4. **Server responds**: Sends HTML, CSS, JavaScript files
5. **Browser renders**: Displays the page to the user

---

## HTTP Protocol Fundamentals

### What is HTTP?

**HTTP** (HyperText Transfer Protocol) is the language browsers and servers use to communicate.

**HTTPS** is the secure version (encrypted).

### HTTP Request Structure

```http
GET /about HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Parts:**
- **Method**: GET, POST, PUT, DELETE
- **Path**: /about
- **Headers**: Additional information
- **Body**: Data (for POST/PUT requests)

### HTTP Methods

#### GET
- **Purpose**: Retrieve data
- **Example**: Loading a web page, fetching search results
- **Has body**: No
- **Safe**: Yes (doesn't change server data)

```
GET /products
GET /users/123
GET /search?q=python
```

#### POST
- **Purpose**: Send data to create something new
- **Example**: Submitting a form, creating an account
- **Has body**: Yes
- **Safe**: No (changes server data)

```
POST /users
Body: {"name": "Ahmed", "email": "ahmed@example.com"}
```

#### PUT
- **Purpose**: Update existing data
- **Example**: Editing a profile
- **Has body**: Yes
- **Safe**: No

```
PUT /users/123
Body: {"name": "Ahmed Ali", "email": "ahmed@example.com"}
```

#### DELETE
- **Purpose**: Remove data
- **Example**: Deleting a post
- **Has body**: Usually no
- **Safe**: No

```
DELETE /posts/456
```

### HTTP Status Codes

The server responds with a status code indicating what happened:

#### 2xx - Success
- **200 OK**: Request succeeded
- **201 Created**: New resource created
- **204 No Content**: Success but no content to return

#### 3xx - Redirection
- **301 Moved Permanently**: Resource moved to new URL
- **302 Found**: Temporary redirect
- **304 Not Modified**: Cached version is still valid

#### 4xx - Client Errors
- **400 Bad Request**: Invalid request syntax
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: You don't have permission
- **404 Not Found**: Resource doesn't exist

#### 5xx - Server Errors
- **500 Internal Server Error**: Server crashed
- **502 Bad Gateway**: Server got invalid response
- **503 Service Unavailable**: Server overloaded or down

### Cookies and Sessions

#### Cookies
Small pieces of data stored in your browser by websites.

**Uses:**
- Remember login status
- Store preferences
- Track user behavior
- Shopping cart items

**Example:**
```
Set-Cookie: user_id=12345; expires=Fri, 31 Dec 2025 23:59:59 GMT
```

#### Sessions
Server-side storage of user data. The server gives your browser a session ID cookie to identify you.

**Flow:**
```
1. You log in
2. Server creates session
3. Server sends session ID cookie
4. Browser includes cookie in future requests
5. Server recognizes you from session ID
```

---

## HTML Basics

### What is HTML?

**HTML** (HyperText Markup Language) is the structure of web pages. It's not a programming language—it's a markup language that defines content structure.

### Basic HTML Structure

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

**Explanation:**
- `<!DOCTYPE html>`: Tells browser this is HTML5
- `<html>`: Root element
- `<head>`: Metadata (not displayed)
- `<title>`: Page title (shown in browser tab)
- `<body>`: Visible content

### Common HTML Tags

#### Headings

```html
<h1>Main Heading</h1>
<h2>Subheading</h2>
<h3>Smaller Heading</h3>
<h4>Even Smaller</h4>
<h5>Very Small</h5>
<h6>Smallest</h6>
```

#### Paragraphs and Text

```html
<p>This is a paragraph of text.</p>

<p>This is <strong>bold text</strong>.</p>
<p>This is <em>italic text</em>.</p>
<p>This is <u>underlined text</u>.</p>

<br> <!-- Line break -->
<hr> <!-- Horizontal line -->
```

#### Lists

**Unordered List (bullets):**
```html
<ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Orange</li>
</ul>
```

**Ordered List (numbers):**
```html
<ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</ol>
```

#### Links

```html
<!-- External link -->
<a href="https://www.google.com">Go to Google</a>

<!-- Link to another page -->
<a href="about.html">About Us</a>

<!-- Open in new tab -->
<a href="https://www.google.com" target="_blank">Google (new tab)</a>

<!-- Link to section on same page -->
<a href="#contact">Jump to Contact</a>
```

#### Images

```html
<img src="photo.jpg" alt="Description of image">

<!-- With width/height -->
<img src="photo.jpg" alt="Description" width="300" height="200">

<!-- From URL -->
<img src="https://example.com/image.jpg" alt="Online image">
```

#### Divisions and Spans

```html
<!-- div: Block-level container -->
<div class="container">
    <h2>Section Title</h2>
    <p>Section content</p>
</div>

<!-- span: Inline container -->
<p>This is <span style="color: red;">red text</span> in a paragraph.</p>
```

#### Forms and Inputs

```html
<form action="/submit" method="POST">
    <!-- Text input -->
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <!-- Email input -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <!-- Password input -->
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">

    <!-- Number input -->
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" min="1" max="120">

    <!-- Textarea -->
    <label for="message">Message:</label>
    <textarea id="message" name="message" rows="4"></textarea>

    <!-- Checkbox -->
    <input type="checkbox" id="subscribe" name="subscribe">
    <label for="subscribe">Subscribe to newsletter</label>

    <!-- Radio buttons -->
    <input type="radio" id="male" name="gender" value="male">
    <label for="male">Male</label>
    <input type="radio" id="female" name="gender" value="female">
    <label for="female">Female</label>

    <!-- Select dropdown -->
    <label for="city">City:</label>
    <select id="city" name="city">
        <option value="riyadh">Riyadh</option>
        <option value="jeddah">Jeddah</option>
        <option value="dammam">Dammam</option>
    </select>

    <!-- Submit button -->
    <button type="submit">Submit</button>
</form>
```

#### Tables

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

### Semantic HTML

Use meaningful tags that describe content:

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

## CSS Basics

### What is CSS?

**CSS** (Cascading Style Sheets) controls the appearance of HTML elements.

### Three Ways to Add CSS

#### 1. Inline CSS (not recommended)
```html
<p style="color: red; font-size: 20px;">Red text</p>
```

#### 2. Internal CSS (in `<head>`)
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

#### 3. External CSS (best practice)
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

### CSS Selectors

#### Element Selector
```css
p {
    color: blue;
}

h1 {
    font-size: 32px;
}
```

#### Class Selector
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

#### ID Selector
```html
<div id="header">Header content</div>
```

```css
#header {
    background-color: navy;
    color: white;
}
```

#### Multiple Selectors
```css
h1, h2, h3 {
    font-family: Arial, sans-serif;
}
```

#### Descendant Selector
```css
div p {
    color: red; /* Only paragraphs inside divs */
}
```

### Common CSS Properties

#### Text Styling
```css
.text-example {
    color: #333;              /* Text color */
    font-size: 16px;         /* Text size */
    font-family: Arial;      /* Font */
    font-weight: bold;       /* Bold */
    text-align: center;      /* Alignment */
    text-decoration: underline; /* Underline */
    line-height: 1.5;        /* Space between lines */
    letter-spacing: 2px;     /* Space between letters */
}
```

#### Background
```css
.bg-example {
    background-color: lightblue;
    background-image: url('image.jpg');
    background-size: cover;
    background-position: center;
}
```

#### Box Model
```css
.box {
    width: 300px;
    height: 200px;
    padding: 20px;           /* Inside space */
    margin: 10px;            /* Outside space */
    border: 2px solid black; /* Border */
}
```

**Box Model Visualization:**
```
┌─────────────── margin ──────────────┐
│ ┌────────── border ────────────┐    │
│ │ ┌──── padding ─────┐         │    │
│ │ │                  │         │    │
│ │ │     CONTENT      │         │    │
│ │ │                  │         │    │
│ │ └──────────────────┘         │    │
│ └──────────────────────────────┘    │
└─────────────────────────────────────┘
```

#### Borders
```css
.border-example {
    border: 2px solid black;
    border-radius: 10px;     /* Rounded corners */
    border-top: 3px dashed red;
}
```

#### Display
```css
.inline {
    display: inline;   /* Inline element */
}

.block {
    display: block;    /* Block element */
}

.none {
    display: none;     /* Hide element */
}
```

#### Colors

```css
.colors {
    color: red;                    /* Name */
    color: #FF0000;               /* Hex */
    color: rgb(255, 0, 0);        /* RGB */
    color: rgba(255, 0, 0, 0.5);  /* RGBA (with transparency) */
}
```

### Simple Layout Example

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

## JSON Introduction

### What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data format for storing and exchanging data.

### JSON Syntax

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

**Rules:**
- Data in key-value pairs
- Keys must be strings (in quotes)
- Values can be: string, number, boolean, array, object, null
- Use double quotes, not single quotes
- No trailing commas

### JSON Data Types

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

### JSON vs Python Dictionary

**Python Dictionary:**
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

**Differences:**
- Python: `True`, `False`, `None`
- JSON: `true`, `false`, `null`

### Working with JSON in Python

```python
import json

# Python dict to JSON string
person = {"name": "Ahmed", "age": 25}
json_string = json.dumps(person)
print(json_string)  # '{"name": "Ahmed", "age": 25}'

# JSON string to Python dict
json_data = '{"name": "Sara", "age": 23}'
person = json.loads(json_data)
print(person["name"])  # Sara

# Write to JSON file
with open("data.json", "w") as file:
    json.dump(person, file, indent=2)

# Read from JSON file
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

### Why JSON is Important for Web Development

1. **APIs**: Most web APIs return data in JSON format
2. **Configuration**: Many tools use JSON for settings
3. **Data exchange**: Easy to send between frontend and backend
4. **Language independent**: Works with Python, JavaScript, Java, etc.

---

## Git and Version Control

### What is Git?

**Git** is a version control system that tracks changes to files over time.

**Benefits:**
- Track history of changes
- Collaborate with others
- Revert to previous versions
- Work on features without breaking main code

### Installing Git

**Check if installed:**
```bash
git --version
```

**Configure Git (first time):**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Basic Git Workflow

```
Working Directory → Staging Area → Repository

    modify files → git add → git commit
```

### Essential Git Commands

#### Initialize a Repository
```bash
# Create new repository
git init

# This creates a hidden .git folder
```

#### Check Status
```bash
git status

# Shows:
# - Modified files
# - Staged files
# - Untracked files
```

#### Add Files to Staging
```bash
# Add specific file
git add index.html

# Add all files
git add .

# Add multiple files
git add index.html style.css
```

#### Commit Changes
```bash
# Commit with message
git commit -m "Add homepage structure"

# Good commit messages:
# - "Add login form"
# - "Fix navigation bug"
# - "Update contact page styling"
```

#### View Commit History
```bash
# See all commits
git log

# See compact log
git log --oneline

# See last 5 commits
git log -5
```

#### View Differences
```bash
# See changes not staged
git diff

# See changes staged
git diff --staged
```

### .gitignore File

Tells Git which files to ignore.

**Create `.gitignore`:**
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

## GitHub Integration

### What is GitHub?

**GitHub** is a cloud platform for hosting Git repositories. It adds:
- Remote backup
- Collaboration features
- Project management
- Code review tools

### GitHub vs Git

- **Git**: Version control software (local)
- **GitHub**: Hosting service for Git repositories (remote)

### Creating a GitHub Account

1. Go to https://github.com
2. Sign up with email
3. Verify email
4. Choose free plan

### Creating a Repository on GitHub

1. Click "New Repository"
2. Enter repository name
3. Choose public or private
4. (Optional) Add README
5. Click "Create repository"

### Connecting Local Repository to GitHub

```bash
# Add remote repository
git remote add origin https://github.com/username/repo-name.git

# Verify remote
git remote -v

# Push to GitHub (first time)
git push -u origin main

# Future pushes
git push
```

### Clone a Repository

```bash
# Clone repository from GitHub
git clone https://github.com/username/repo-name.git

# Clone to specific folder
git clone https://github.com/username/repo-name.git my-folder
```

### Pull Changes

```bash
# Get latest changes from GitHub
git pull
```

### Common Git Workflow with GitHub

```bash
# 1. Make changes to files
# Edit index.html, style.css

# 2. Check status
git status

# 3. Stage changes
git add .

# 4. Commit changes
git commit -m "Update homepage design"

# 5. Push to GitHub
git push
```

### Viewing Repository on GitHub

After pushing, your code is visible at:
```
https://github.com/your-username/repository-name
```

---

## Mini-Project: Portfolio Website

Let's build a simple portfolio website using everything we learned!

### Project Structure

```
portfolio/
├── index.html
├── style.css
└── README.md
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

### Upload to GitHub

```bash
# 1. Initialize Git repository
cd portfolio
git init

# 2. Add files
git add .

# 3. Commit
git commit -m "Initial commit: Add portfolio website"

# 4. Create repository on GitHub (via website)
# Then connect:
git remote add origin https://github.com/your-username/portfolio.git

# 5. Push to GitHub
git push -u origin main
```

---

## Key Takeaways from Week 3

**Web Fundamentals:**
- Client-server architecture
- HTTP methods (GET, POST, PUT, DELETE)
- HTTP status codes (200, 404, 500)
- Cookies and sessions

**HTML:**
- Basic structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- Common tags (headings, paragraphs, links, images, lists, forms)
- Semantic elements (`<header>`, `<nav>`, `<main>`, `<footer>`)

**CSS:**
- Selectors (element, class, ID)
- Common properties (color, font, padding, margin, border)
- Box model
- Basic layouts

**JSON:**
- Data format for APIs
- Key-value structure
- Working with JSON in Python

**Git & GitHub:**
- Version control basics
- Essential commands (`init`, `add`, `commit`, `push`, `pull`)
- Connecting to GitHub
- `.gitignore` file

---

## Next Steps

**Before Week 4:**
- Complete all practice exercises
- Build your own portfolio website
- Upload your project to GitHub
- Experiment with different CSS styles
- Practice Git commands

**Week 4 Preview:**
You'll learn about:
- Django framework
- Creating Django projects and apps
- URLs and views
- Templates and static files
- Building your first Django web application

Keep practicing and see you next week!
