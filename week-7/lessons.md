# Week 7 Lessons – APIs, Basic JavaScript & Django REST Framework

Welcome to Week 7! This week, we'll learn how to build REST APIs with Django and Django REST Framework, and use JavaScript to consume those APIs. By the end of this week, you'll be able to create JSON APIs and build interactive pages that fetch data dynamically.

---

## Table of Contents

1. [Introduction to APIs](#1-introduction-to-apis)
2. [REST API Concepts](#2-rest-api-concepts)
3. [JSON Data Format](#3-json-data-format)
4. [Django and JSON](#4-django-and-json)
5. [Introduction to Django REST Framework](#5-introduction-to-django-rest-framework)
6. [Serializers](#6-serializers)
7. [API Views](#7-api-views)
8. [ViewSets and Routers](#8-viewsets-and-routers)
9. [API Authentication](#9-api-authentication)
10. [JavaScript Basics](#10-javascript-basics)
11. [Fetch API](#11-fetch-api)
12. [DOM Manipulation](#12-dom-manipulation)
13. [Mini-Project: Blog API with JavaScript Frontend](#13-mini-project-blog-api-with-javascript-frontend)

---

## 1. Introduction to APIs

### What is an API?

**API** stands for **Application Programming Interface**. It's a way for different software applications to communicate with each other.

**Real-world analogy:**
- A restaurant menu is like an API
- You (the client) look at the menu (API documentation)
- You place an order (make a request)
- The kitchen (server) prepares your food
- The waiter brings your food (response)

**Why APIs?**
- Mobile apps need data from servers
- Single Page Applications (SPAs)
- Third-party integrations
- Microservices architecture
- Separate frontend and backend

**Without API:**
```html
<!-- Traditional: Server renders HTML -->
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>
```

**With API:**
```javascript
// Modern: Client fetches data and renders
fetch('/api/posts/1/')
  .then(response => response.json())
  .then(post => {
    document.getElementById('title').textContent = post.title;
  });
```

### Types of APIs

1. **Web APIs** - Over HTTP (what we'll build)
2. **Library APIs** - Python modules, functions
3. **Operating System APIs** - File system, hardware

---

## 2. REST API Concepts

### What is REST?

**REST** (Representational State Transfer) is an architectural style for designing networked applications.

**REST Principles:**
1. **Client-Server** - Separation of concerns
2. **Stateless** - Each request is independent
3. **Uniform Interface** - Standard HTTP methods
4. **Resource-Based** - Everything is a resource

### Resources and Endpoints

**Resource:** A data object (e.g., Post, User, Comment)

**Endpoint:** The URL to access a resource

```
/api/posts/        # Collection of posts
/api/posts/1/      # Single post with ID 1
/api/users/        # Collection of users
/api/users/5/      # Single user with ID 5
```

### HTTP Methods (Verbs)

| Method | Action | Example |
|--------|--------|---------|
| GET | Read data | Get all posts |
| POST | Create new | Create a new post |
| PUT | Update (full) | Replace entire post |
| PATCH | Update (partial) | Update only title |
| DELETE | Remove | Delete a post |

### CRUD to HTTP Mapping

| CRUD | HTTP | Endpoint | Description |
|------|------|----------|-------------|
| Create | POST | /api/posts/ | Create new post |
| Read | GET | /api/posts/ | List all posts |
| Read | GET | /api/posts/1/ | Get single post |
| Update | PUT/PATCH | /api/posts/1/ | Update post |
| Delete | DELETE | /api/posts/1/ | Delete post |

### Request and Response

**Request Structure:**
```
POST /api/posts/ HTTP/1.1
Host: example.com
Content-Type: application/json
Authorization: Token abc123

{
    "title": "My Post",
    "content": "Hello World"
}
```

**Response Structure:**
```
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "title": "My Post",
    "content": "Hello World",
    "created_at": "2024-01-15T10:30:00Z"
}
```

### HTTP Status Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Successful GET/PUT/PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Not authenticated |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Something went wrong |

---

## 3. JSON Data Format

### What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data format for exchanging data between client and server.

**Why JSON?**
- Human-readable
- Language-independent
- Easy to parse
- Standard for web APIs

### JSON Syntax

```json
{
    "name": "Ahmed",
    "age": 25,
    "is_student": true,
    "courses": ["Python", "Django", "JavaScript"],
    "address": {
        "city": "Riyadh",
        "country": "Saudi Arabia"
    }
}
```

**JSON Data Types:**
- **String:** `"Hello"`
- **Number:** `42`, `3.14`
- **Boolean:** `true`, `false`
- **Array:** `[1, 2, 3]`
- **Object:** `{"key": "value"}`
- **Null:** `null`

### JSON in Python

```python
import json

# Python dict to JSON string
data = {'name': 'Ahmed', 'age': 25}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Ahmed", "age": 25}'

# JSON string to Python dict
json_string = '{"name": "Ahmed", "age": 25}'
data = json.loads(json_string)
print(data['name'])  # Ahmed
```

---

## 4. Django and JSON

### JsonResponse

Django provides `JsonResponse` for returning JSON data.

**Basic Example:**
```python
# views.py
from django.http import JsonResponse

def api_hello(request):
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return JsonResponse(data)
```

**URL Configuration:**
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/hello/', views.api_hello, name='api_hello'),
]
```

**Response:**
```json
{
    "message": "Hello, World!",
    "status": "success"
}
```

### Returning Model Data

```python
# views.py
from django.http import JsonResponse
from .models import Post

def api_posts_list(request):
    posts = Post.objects.all()
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.isoformat()
        })
    return JsonResponse({'posts': data})

def api_post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.isoformat()
        }
        return JsonResponse(data)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)
```

### Handling POST Requests

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post

@csrf_exempt  # For demo only - use proper auth in production
def api_post_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post = Post.objects.create(
                title=data['title'],
                content=data['content']
            )
            return JsonResponse({
                'id': post.id,
                'title': post.title,
                'message': 'Post created successfully'
            }, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
```

### Problems with Manual JSON APIs

- Lots of repetitive code
- Manual serialization
- No automatic validation
- No browsable API
- Security considerations

**Solution:** Django REST Framework!

---

## 5. Introduction to Django REST Framework

### What is DRF?

**Django REST Framework (DRF)** is a powerful toolkit for building Web APIs in Django.

**Features:**
- Serialization (model to JSON and back)
- Authentication and permissions
- Browsable API interface
- ViewSets and Routers
- Pagination
- Filtering
- Documentation

### Installation

```bash
pip install djangorestframework
```

**settings.py:**
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
]

# Optional: Configure DRF settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### Quick Example

**Before DRF (manual):**
```python
def api_posts(request):
    posts = Post.objects.all()
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            # ... more fields
        })
    return JsonResponse({'posts': data})
```

**After DRF:**
```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

Much cleaner!

---

## 6. Serializers

### What are Serializers?

**Serializers** convert complex data types (like Django models) to Python native types that can be rendered into JSON.

**Two-way conversion:**
- **Serialization:** Model → JSON (for responses)
- **Deserialization:** JSON → Model (for requests)

### Creating a Serializer

**serializers.py:**
```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
```

### ModelSerializer

**ModelSerializer** automatically generates fields from a model.

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
        # Or use: fields = '__all__'
```

**Benefits:**
- Automatic field generation
- Built-in create() and update()
- Less code

### Serializer Field Options

```python
class PostSerializer(serializers.ModelSerializer):
    # Read-only field
    created_at = serializers.DateTimeField(read_only=True)

    # Custom field
    excerpt = serializers.SerializerMethodField()

    # Nested serializer
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'excerpt', 'author', 'created_at']

    def get_excerpt(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
```

### Validation in Serializers

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

    # Field-level validation
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters")
        return value

    # Object-level validation
    def validate(self, data):
        if 'spam' in data.get('content', '').lower():
            raise serializers.ValidationError("Content contains spam")
        return data
```

### Using Serializers

```python
# Serialize a single object
post = Post.objects.get(pk=1)
serializer = PostSerializer(post)
print(serializer.data)  # {'id': 1, 'title': '...', ...}

# Serialize multiple objects
posts = Post.objects.all()
serializer = PostSerializer(posts, many=True)
print(serializer.data)  # [{'id': 1, ...}, {'id': 2, ...}]

# Deserialize and create
data = {'title': 'New Post', 'content': 'Hello!'}
serializer = PostSerializer(data=data)
if serializer.is_valid():
    serializer.save()
else:
    print(serializer.errors)
```

---

## 7. API Views

### Function-Based API Views

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### Class-Based API Views

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if post is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### Generic Views

DRF provides generic views that handle common patterns.

```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

**Available Generic Views:**
- `ListAPIView` - GET list
- `CreateAPIView` - POST create
- `RetrieveAPIView` - GET single
- `UpdateAPIView` - PUT/PATCH update
- `DestroyAPIView` - DELETE
- `ListCreateAPIView` - GET list + POST create
- `RetrieveUpdateDestroyAPIView` - GET + PUT + DELETE

---

## 8. ViewSets and Routers

### ViewSets

**ViewSet** combines multiple views into a single class.

```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

This single class provides:
- `list()` - GET /posts/
- `create()` - POST /posts/
- `retrieve()` - GET /posts/{id}/
- `update()` - PUT /posts/{id}/
- `partial_update()` - PATCH /posts/{id}/
- `destroy()` - DELETE /posts/{id}/

### Routers

**Routers** automatically generate URL patterns for ViewSets.

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

**Generated URLs:**
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create post
- `GET /api/posts/1/` - Get post 1
- `PUT /api/posts/1/` - Update post 1
- `PATCH /api/posts/1/` - Partial update
- `DELETE /api/posts/1/` - Delete post 1

### Custom Actions

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        post = self.get_object()
        post.is_published = True
        post.save()
        return Response({'status': 'post published'})

    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_posts = Post.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_posts, many=True)
        return Response(serializer.data)
```

**URLs:**
- `POST /api/posts/1/publish/` - Publish post 1
- `GET /api/posts/recent/` - Get recent posts

---

## 9. API Authentication

### Authentication Types

**1. Session Authentication (default):**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

**2. Token Authentication:**
```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

```bash
python manage.py migrate  # Create token table
```

### Creating Tokens

```python
# Create token for user
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='ahmed')
token, created = Token.objects.get_or_create(user=user)
print(token.key)  # abc123...
```

### Using Tokens

**Client request:**
```
GET /api/posts/ HTTP/1.1
Authorization: Token abc123...
```

**JavaScript:**
```javascript
fetch('/api/posts/', {
    headers: {
        'Authorization': 'Token abc123...'
    }
})
```

### Permissions

```python
from rest_framework import permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
```

**Built-in Permissions:**
- `AllowAny` - No restrictions
- `IsAuthenticated` - Logged in users only
- `IsAdminUser` - Admin users only
- `IsAuthenticatedOrReadOnly` - Read for all, write for authenticated

### Custom Permissions

```python
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for author
        return obj.author == request.user
```

---

## 10. JavaScript Basics

### Why JavaScript?

JavaScript allows you to:
- Update page content without reloading
- Make API calls (AJAX)
- Handle user interactions
- Build dynamic interfaces

### Variables

```javascript
// Modern JavaScript (ES6+)
let name = 'Ahmed';        // Can be reassigned
const age = 25;            // Cannot be reassigned
var city = 'Riyadh';       // Old way (avoid)

// Data types
let text = 'Hello';        // String
let number = 42;           // Number
let decimal = 3.14;        // Number
let isTrue = true;         // Boolean
let items = [1, 2, 3];     // Array
let person = {             // Object
    name: 'Ahmed',
    age: 25
};
```

### Functions

```javascript
// Regular function
function greet(name) {
    return 'Hello, ' + name;
}

// Arrow function (ES6+)
const greet = (name) => {
    return 'Hello, ' + name;
};

// Short arrow function
const greet = name => 'Hello, ' + name;

// Usage
console.log(greet('Ahmed'));  // Hello, Ahmed
```

### Arrays

```javascript
const fruits = ['apple', 'banana', 'orange'];

// Access
console.log(fruits[0]);  // apple

// Add
fruits.push('mango');

// Loop
fruits.forEach(fruit => {
    console.log(fruit);
});

// Map (transform)
const upperFruits = fruits.map(fruit => fruit.toUpperCase());

// Filter
const longNames = fruits.filter(fruit => fruit.length > 5);
```

### Objects

```javascript
const person = {
    name: 'Ahmed',
    age: 25,
    city: 'Riyadh',
    greet: function() {
        return 'Hello, I am ' + this.name;
    }
};

// Access
console.log(person.name);      // Ahmed
console.log(person['age']);    // 25

// Method
console.log(person.greet());   // Hello, I am Ahmed

// Destructuring
const { name, age } = person;
console.log(name);  // Ahmed
```

### Template Literals

```javascript
const name = 'Ahmed';
const age = 25;

// Old way
const message = 'Hello, ' + name + '. You are ' + age + ' years old.';

// Template literals (ES6+)
const message = `Hello, ${name}. You are ${age} years old.`;
```

---

## 11. Fetch API

### What is Fetch?

**Fetch** is a modern JavaScript API for making HTTP requests.

### Basic GET Request

```javascript
fetch('/api/posts/')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
```

### Async/Await Syntax

```javascript
async function getPosts() {
    try {
        const response = await fetch('/api/posts/');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

getPosts();
```

### POST Request

```javascript
async function createPost(title, content) {
    try {
        const response = await fetch('/api/posts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title,
                content: content
            })
        });

        if (!response.ok) {
            throw new Error('Failed to create post');
        }

        const data = await response.json();
        console.log('Created:', data);
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

createPost('My New Post', 'This is the content');
```

### PUT Request

```javascript
async function updatePost(id, title, content) {
    const response = await fetch(`/api/posts/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: title,
            content: content
        })
    });

    return await response.json();
}
```

### DELETE Request

```javascript
async function deletePost(id) {
    const response = await fetch(`/api/posts/${id}/`, {
        method: 'DELETE'
    });

    if (response.ok) {
        console.log('Post deleted');
    }
}
```

### With Authentication Token

```javascript
const token = 'your-auth-token';

async function getProtectedData() {
    const response = await fetch('/api/posts/', {
        headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
        }
    });

    return await response.json();
}
```

### Handling Errors

```javascript
async function fetchWithErrorHandling() {
    try {
        const response = await fetch('/api/posts/');

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('Posts not found');
            } else if (response.status === 401) {
                throw new Error('Not authorized');
            } else {
                throw new Error('Something went wrong');
            }
        }

        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error.message);
        // Show error to user
        document.getElementById('error').textContent = error.message;
    }
}
```

---

## 12. DOM Manipulation

### What is the DOM?

**DOM** (Document Object Model) is a programming interface for HTML documents. It represents the page as a tree of objects.

### Selecting Elements

```javascript
// By ID
const title = document.getElementById('title');

// By class (returns collection)
const items = document.getElementsByClassName('item');

// By tag (returns collection)
const paragraphs = document.getElementsByTagName('p');

// Query selector (CSS selector)
const header = document.querySelector('.header');

// Query all (returns NodeList)
const buttons = document.querySelectorAll('.btn');
```

### Changing Content

```javascript
const title = document.getElementById('title');

// Change text
title.textContent = 'New Title';

// Change HTML
title.innerHTML = '<em>New Title</em>';

// Change attribute
title.setAttribute('class', 'main-title');

// Change style
title.style.color = 'blue';
title.style.fontSize = '24px';
```

### Creating Elements

```javascript
// Create element
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello!';
newDiv.className = 'message';

// Add to page
document.body.appendChild(newDiv);

// Or insert at specific position
const container = document.getElementById('container');
container.appendChild(newDiv);
```

### Event Listeners

```javascript
const button = document.getElementById('submit-btn');

button.addEventListener('click', function(event) {
    console.log('Button clicked!');
});

// Arrow function version
button.addEventListener('click', (e) => {
    e.preventDefault();  // Prevent default behavior
    console.log('Button clicked!');
});
```

### Complete Example: Display Posts

**HTML:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Blog Posts</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <div id="posts-container">
        <p>Loading posts...</p>
    </div>

    <script src="app.js"></script>
</body>
</html>
```

**JavaScript (app.js):**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    loadPosts();
});

async function loadPosts() {
    const container = document.getElementById('posts-container');

    try {
        const response = await fetch('/api/posts/');
        const posts = await response.json();

        // Clear loading message
        container.innerHTML = '';

        // Create element for each post
        posts.forEach(post => {
            const postDiv = document.createElement('div');
            postDiv.className = 'post';
            postDiv.innerHTML = `
                <h2>${post.title}</h2>
                <p>${post.content}</p>
                <small>Posted: ${new Date(post.created_at).toLocaleDateString()}</small>
            `;
            container.appendChild(postDiv);
        });

    } catch (error) {
        container.innerHTML = '<p>Error loading posts</p>';
        console.error('Error:', error);
    }
}
```

---

## 13. Mini-Project: Blog API with JavaScript Frontend

### Project Overview

Build a complete blog application with:
- Django REST Framework API backend
- JavaScript frontend that fetches and displays data
- Create, read, update, delete posts via API

### Backend Setup

**models.py:**
```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
```

**serializers.py:**
```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_name', 'created_at', 'updated_at']
        read_only_fields = ['author']
```

**views.py:**
```python
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

**urls.py (app):**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### Frontend Setup

**templates/blog/index.html:**
```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Blog API Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .post {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
        }
        .post h2 {
            margin-top: 0;
        }
        .post-meta {
            color: #666;
            font-size: 0.9em;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }
        .btn {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .btn:hover {
            background: #0056b3;
        }
        .btn-danger {
            background: #dc3545;
        }
        .btn-danger:hover {
            background: #c82333;
        }
        #message {
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 5px;
            display: none;
        }
        .success {
            background: #d4edda;
            color: #155724;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
        }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>

    <div id="message"></div>

    <!-- Create Post Form -->
    <div id="create-form">
        <h2>Create New Post</h2>
        <form id="post-form">
            <div class="form-group">
                <label for="title">Title:</label>
                <input type="text" id="title" name="title" required>
            </div>
            <div class="form-group">
                <label for="content">Content:</label>
                <textarea id="content" name="content" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn">Create Post</button>
        </form>
    </div>

    <hr>

    <!-- Posts List -->
    <h2>All Posts</h2>
    <div id="posts-container">
        <p>Loading posts...</p>
    </div>

    <script>
        // Get CSRF token from cookie
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        const csrftoken = getCookie('csrftoken');

        // Show message
        function showMessage(text, type) {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = text;
            messageDiv.className = type;
            messageDiv.style.display = 'block';
            setTimeout(() => {
                messageDiv.style.display = 'none';
            }, 3000);
        }

        // Load all posts
        async function loadPosts() {
            const container = document.getElementById('posts-container');

            try {
                const response = await fetch('/api/posts/');
                const posts = await response.json();

                container.innerHTML = '';

                if (posts.length === 0) {
                    container.innerHTML = '<p>No posts yet.</p>';
                    return;
                }

                posts.forEach(post => {
                    const postDiv = document.createElement('div');
                    postDiv.className = 'post';
                    postDiv.innerHTML = `
                        <h2>${post.title}</h2>
                        <p>${post.content}</p>
                        <div class="post-meta">
                            By ${post.author_name || 'Unknown'} |
                            ${new Date(post.created_at).toLocaleDateString()}
                        </div>
                        <button class="btn btn-danger" onclick="deletePost(${post.id})">Delete</button>
                    `;
                    container.appendChild(postDiv);
                });

            } catch (error) {
                container.innerHTML = '<p>Error loading posts</p>';
                console.error('Error:', error);
            }
        }

        // Create new post
        async function createPost(title, content) {
            try {
                const response = await fetch('/api/posts/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({ title, content })
                });

                if (response.ok) {
                    showMessage('Post created successfully!', 'success');
                    document.getElementById('post-form').reset();
                    loadPosts();
                } else {
                    const error = await response.json();
                    showMessage('Error: ' + JSON.stringify(error), 'error');
                }
            } catch (error) {
                showMessage('Error creating post', 'error');
                console.error('Error:', error);
            }
        }

        // Delete post
        async function deletePost(id) {
            if (!confirm('Are you sure you want to delete this post?')) {
                return;
            }

            try {
                const response = await fetch(`/api/posts/${id}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': csrftoken
                    }
                });

                if (response.ok) {
                    showMessage('Post deleted!', 'success');
                    loadPosts();
                } else {
                    showMessage('Error deleting post', 'error');
                }
            } catch (error) {
                showMessage('Error deleting post', 'error');
                console.error('Error:', error);
            }
        }

        // Form submission
        document.getElementById('post-form').addEventListener('submit', (e) => {
            e.preventDefault();
            const title = document.getElementById('title').value;
            const content = document.getElementById('content').value;
            createPost(title, content);
        });

        // Load posts on page load
        document.addEventListener('DOMContentLoaded', loadPosts);
    </script>
</body>
</html>
```

### Running the Project

1. Create migrations and migrate
2. Create a superuser
3. Run the server
4. Visit the page to see posts
5. Create, view, and delete posts using the JavaScript interface

### Key Learning Points

1. **REST API** provides data in JSON format
2. **DRF** simplifies API creation with serializers and viewsets
3. **JavaScript fetch()** makes HTTP requests to the API
4. **DOM manipulation** updates the page dynamically
5. **CSRF token** is required for POST/DELETE requests in Django

---

## Summary

This week you learned:

1. **REST API Concepts** - Resources, endpoints, HTTP methods, status codes
2. **JSON Format** - Data exchange format for APIs
3. **Django JsonResponse** - Simple JSON responses
4. **Django REST Framework** - Powerful API toolkit
5. **Serializers** - Convert models to JSON and back
6. **API Views** - Function-based, class-based, generic views
7. **ViewSets and Routers** - Automatic URL routing
8. **API Authentication** - Token authentication and permissions
9. **JavaScript Basics** - Variables, functions, arrays, objects
10. **Fetch API** - Making HTTP requests from JavaScript
11. **DOM Manipulation** - Updating page content dynamically

**Next Week:** Final Project - Design and Build a complete Django application!
