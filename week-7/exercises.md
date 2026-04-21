# Week 7 Exercises – APIs, JavaScript & Django REST Framework Practice

Practice exercises for Week 7: REST APIs, Django REST Framework, and JavaScript for API consumption.

---

## Table of Contents

1. [Day 1: REST API Concepts & JsonResponse](#day-1-rest-api-concepts--jsonresponse)
2. [Day 2: Django REST Framework Basics](#day-2-django-rest-framework-basics)
3. [Day 3: Serializers & ViewSets](#day-3-serializers--viewsets)
4. [Day 4: JavaScript & Fetch API](#day-4-javascript--fetch-api)
5. [Day 5: Complete API Project with JavaScript Frontend](#day-5-complete-api-project-with-javascript-frontend)
6. [Challenge Exercises](#challenge-exercises)

---

## Day 1: REST API Concepts & JsonResponse

### Exercise 1: Create a Simple JSON Endpoint

**Task:**
1. Create a Django project called `api_demo`
2. Create an app called `core`
3. Create a view that returns JSON with your information

```python
# Expected response:
{
    "name": "Your Name",
    "role": "Django Developer",
    "skills": ["Python", "Django", "REST APIs"]
}
```

<details>
<summary>Solution</summary>

```bash
django-admin startproject api_demo
cd api_demo
python manage.py startapp core
```

```python
# core/views.py
from django.http import JsonResponse

def about_me(request):
    data = {
        "name": "Ahmed",
        "role": "Django Developer",
        "skills": ["Python", "Django", "REST APIs"]
    }
    return JsonResponse(data)
```

```python
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/about/', views.about_me, name='about_me'),
]
```

```python
# api_demo/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

```python
# api_demo/settings.py - Add to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'core',
]
```
</details>

---

### Exercise 2: Create a Posts Model and JSON List Endpoint

**Task:**
1. Create a `Post` model with fields: title, content, created_at
2. Create an endpoint `/api/posts/` that returns all posts as JSON

<details>
<summary>Solution</summary>

```python
# core/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

```bash
python manage.py makemigrations
python manage.py migrate
```

```python
# core/views.py
from django.http import JsonResponse
from .models import Post

def post_list(request):
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
```

```python
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/about/', views.about_me, name='about_me'),
    path('api/posts/', views.post_list, name='post_list'),
]
```
</details>

---

### Exercise 3: Create a Single Post Detail Endpoint

**Task:**
1. Create an endpoint `/api/posts/<id>/` that returns a single post
2. Return 404 error if post doesn't exist

<details>
<summary>Solution</summary>

```python
# core/views.py
from django.http import JsonResponse
from .models import Post

def post_detail(request, pk):
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

```python
# core/urls.py
urlpatterns = [
    path('api/about/', views.about_me, name='about_me'),
    path('api/posts/', views.post_list, name='post_list'),
    path('api/posts/<int:pk>/', views.post_detail, name='post_detail'),
]
```
</details>

---

### Exercise 4: Create POST Endpoint for New Posts

**Task:**
1. Modify the `/api/posts/` endpoint to handle POST requests
2. Accept JSON data with title and content
3. Return the created post with status 201

<details>
<summary>Solution</summary>

```python
# core/views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
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

    elif request.method == 'POST':
        try:
            body = json.loads(request.body)
            post = Post.objects.create(
                title=body['title'],
                content=body['content']
            )
            return JsonResponse({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at.isoformat()
            }, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
```
</details>

---

### Exercise 5: Add DELETE Endpoint

**Task:**
1. Add DELETE method to the post detail endpoint
2. Delete the post and return 204 No Content

<details>
<summary>Solution</summary>

```python
# core/views.py
@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

    if request.method == 'GET':
        data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.isoformat()
        }
        return JsonResponse(data)

    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({}, status=204)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
```
</details>

---

## Day 2: Django REST Framework Basics

### Exercise 6: Install and Configure DRF

**Task:**
1. Install Django REST Framework
2. Add it to INSTALLED_APPS
3. Create a simple API view using `@api_view` decorator

<details>
<summary>Solution</summary>

```bash
pip install djangorestframework
```

```python
# api_demo/settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'core',
]
```

```python
# core/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_api(request):
    return Response({'message': 'Hello from DRF!'})
```

```python
# core/urls.py
urlpatterns = [
    # ...
    path('api/hello/', views.hello_api, name='hello_api'),
]
```
</details>

---

### Exercise 7: Create a Serializer

**Task:**
1. Create a `PostSerializer` using `serializers.Serializer`
2. Include fields: id, title, content, created_at

<details>
<summary>Solution</summary>

```python
# core/serializers.py
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
</details>

---

### Exercise 8: Create a ModelSerializer

**Task:**
1. Convert the serializer to `ModelSerializer`
2. Add an `excerpt` field that shows first 50 characters of content

<details>
<summary>Solution</summary>

```python
# core/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    excerpt = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'excerpt', 'created_at']

    def get_excerpt(self, obj):
        if len(obj.content) > 50:
            return obj.content[:50] + '...'
        return obj.content
```
</details>

---

### Exercise 9: Create API Views with Serializer

**Task:**
1. Create a `post_list_api` view using `@api_view`
2. Handle GET (list all) and POST (create new)
3. Use the PostSerializer

<details>
<summary>Solution</summary>

```python
# core/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list_api(request):
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
```

```python
# core/urls.py
urlpatterns = [
    # ...
    path('api/v2/posts/', views.post_list_api, name='post_list_api'),
]
```
</details>

---

### Exercise 10: Create Detail API View

**Task:**
1. Create a `post_detail_api` view
2. Handle GET, PUT, and DELETE methods
3. Return proper status codes

<details>
<summary>Solution</summary>

```python
# core/views.py
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_api(request, pk):
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

```python
# core/urls.py
urlpatterns = [
    # ...
    path('api/v2/posts/<int:pk>/', views.post_detail_api, name='post_detail_api'),
]
```
</details>

---

## Day 3: Serializers & ViewSets

### Exercise 11: Add Validation to Serializer

**Task:**
1. Add validation to ensure title is at least 5 characters
2. Add validation to ensure content doesn't contain "spam"

<details>
<summary>Solution</summary>

```python
# core/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    excerpt = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'excerpt', 'created_at']

    def get_excerpt(self, obj):
        if len(obj.content) > 50:
            return obj.content[:50] + '...'
        return obj.content

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return value

    def validate_content(self, value):
        if 'spam' in value.lower():
            raise serializers.ValidationError("Content cannot contain spam")
        return value
```
</details>

---

### Exercise 12: Create Class-Based API Views

**Task:**
1. Convert the function-based views to class-based using `APIView`
2. Create `PostListView` and `PostDetailView`

<details>
<summary>Solution</summary>

```python
# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostListView(APIView):
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

class PostDetailView(APIView):
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

```python
# core/urls.py
urlpatterns = [
    # ...
    path('api/v3/posts/', views.PostListView.as_view(), name='post_list_cbv'),
    path('api/v3/posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail_cbv'),
]
```
</details>

---

### Exercise 13: Use Generic Views

**Task:**
1. Simplify the views using generic views
2. Use `ListCreateAPIView` and `RetrieveUpdateDestroyAPIView`

<details>
<summary>Solution</summary>

```python
# core/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

```python
# core/urls.py
urlpatterns = [
    # ...
    path('api/v4/posts/', views.PostListCreateView.as_view(), name='post_list_generic'),
    path('api/v4/posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post_detail_generic'),
]
```
</details>

---

### Exercise 14: Create a ViewSet

**Task:**
1. Create a `PostViewSet` using `ModelViewSet`
2. Register it with a Router
3. All CRUD operations should work automatically

<details>
<summary>Solution</summary>

```python
# core/views.py
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

```python
# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # ... other urls
    path('api/v5/', include(router.urls)),
]
```
</details>

---

### Exercise 15: Add Custom Action to ViewSet

**Task:**
1. Add a custom action `recent` that returns the 5 most recent posts
2. URL should be `/api/v5/posts/recent/`

<details>
<summary>Solution</summary>

```python
# core/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_posts = Post.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_posts, many=True)
        return Response(serializer.data)
```
</details>

---

## Day 4: JavaScript & Fetch API

### Exercise 16: Create HTML Page with JavaScript

**Task:**
1. Create a template that displays "Posts will load here..."
2. Add a script that logs "Page loaded!" to console on page load

<details>
<summary>Solution</summary>

```python
# core/views.py
def home(request):
    return render(request, 'core/home.html')
```

```python
# core/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    # ... other urls
]
```

```html
<!-- core/templates/core/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Blog API</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <div id="posts-container">
        <p>Posts will load here...</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Page loaded!');
        });
    </script>
</body>
</html>
```
</details>

---

### Exercise 17: Fetch Posts from API

**Task:**
1. Use fetch() to get posts from `/api/v5/posts/`
2. Log the posts to console

<details>
<summary>Solution</summary>

```html
<!-- core/templates/core/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Blog API</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <div id="posts-container">
        <p>Loading posts...</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/api/v5/posts/')
                .then(response => response.json())
                .then(data => {
                    console.log('Posts:', data);
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    </script>
</body>
</html>
```
</details>

---

### Exercise 18: Display Posts in HTML

**Task:**
1. Display fetched posts on the page
2. Show title and content for each post

<details>
<summary>Solution</summary>

```html
<!-- core/templates/core/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Blog API</title>
    <style>
        .post {
            border: 1px solid #ccc;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .post h2 {
            margin-top: 0;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>
    <div id="posts-container">
        <p>Loading posts...</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            loadPosts();
        });

        function loadPosts() {
            const container = document.getElementById('posts-container');

            fetch('/api/v5/posts/')
                .then(response => response.json())
                .then(posts => {
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
                            <small>Created: ${new Date(post.created_at).toLocaleString()}</small>
                        `;
                        container.appendChild(postDiv);
                    });
                })
                .catch(error => {
                    container.innerHTML = '<p>Error loading posts.</p>';
                    console.error('Error:', error);
                });
        }
    </script>
</body>
</html>
```
</details>

---

### Exercise 19: Add Create Post Form

**Task:**
1. Add a form to create new posts
2. Use fetch() with POST method to create posts
3. Refresh the list after creating

<details>
<summary>Solution</summary>

```html
<!-- core/templates/core/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Blog API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .post {
            border: 1px solid #ccc;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
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
        }
        #message {
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>Blog Posts</h1>

    <div id="message" style="display: none;"></div>

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

    <hr>

    <h2>All Posts</h2>
    <div id="posts-container">
        <p>Loading posts...</p>
    </div>

    <script>
        // CSRF token helper
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
            const msg = document.getElementById('message');
            msg.textContent = text;
            msg.className = type;
            msg.style.display = 'block';
            setTimeout(() => { msg.style.display = 'none'; }, 3000);
        }

        // Load posts
        function loadPosts() {
            const container = document.getElementById('posts-container');

            fetch('/api/v5/posts/')
                .then(response => response.json())
                .then(posts => {
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
                            <small>Created: ${new Date(post.created_at).toLocaleString()}</small>
                        `;
                        container.appendChild(postDiv);
                    });
                })
                .catch(error => {
                    container.innerHTML = '<p>Error loading posts.</p>';
                });
        }

        // Create post
        document.getElementById('post-form').addEventListener('submit', function(e) {
            e.preventDefault();

            const title = document.getElementById('title').value;
            const content = document.getElementById('content').value;

            fetch('/api/v5/posts/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ title, content })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Failed to create post');
            })
            .then(data => {
                showMessage('Post created successfully!', 'success');
                document.getElementById('post-form').reset();
                loadPosts();
            })
            .catch(error => {
                showMessage('Error creating post', 'error');
            });
        });

        // Load posts on page load
        document.addEventListener('DOMContentLoaded', loadPosts);
    </script>
</body>
</html>
```
</details>

---

### Exercise 20: Add Delete Functionality

**Task:**
1. Add a delete button to each post
2. Use fetch() with DELETE method
3. Confirm before deleting
4. Refresh list after deleting

<details>
<summary>Solution</summary>

```html
<!-- Update the loadPosts function in the script -->
<script>
    // ... (keep previous code)

    function loadPosts() {
        const container = document.getElementById('posts-container');

        fetch('/api/v5/posts/')
            .then(response => response.json())
            .then(posts => {
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
                        <small>Created: ${new Date(post.created_at).toLocaleString()}</small>
                        <br><br>
                        <button class="btn" style="background: #dc3545;" onclick="deletePost(${post.id})">Delete</button>
                    `;
                    container.appendChild(postDiv);
                });
            })
            .catch(error => {
                container.innerHTML = '<p>Error loading posts.</p>';
            });
    }

    function deletePost(id) {
        if (!confirm('Are you sure you want to delete this post?')) {
            return;
        }

        fetch(`/api/v5/posts/${id}/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .then(response => {
            if (response.ok) {
                showMessage('Post deleted!', 'success');
                loadPosts();
            } else {
                throw new Error('Failed to delete');
            }
        })
        .catch(error => {
            showMessage('Error deleting post', 'error');
        });
    }
</script>
```
</details>

---

## Day 5: Complete API Project with JavaScript Frontend

### Exercise 21: Build Complete Task Manager API

**Task:**
Build a Task Manager application with:
1. Task model (title, description, is_completed, created_at)
2. Full REST API using DRF ViewSet
3. JavaScript frontend to:
   - List all tasks
   - Create new task
   - Toggle task completion
   - Delete task

<details>
<summary>Solution</summary>

```python
# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
```

```python
# tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'is_completed', 'created_at']
```

```python
# tasks/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        task = self.get_object()
        task.is_completed = not task.is_completed
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

def task_home(request):
    return render(request, 'tasks/home.html')
```

```python
# tasks/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', views.task_home, name='task_home'),
    path('api/', include(router.urls)),
]
```

```html
<!-- tasks/templates/tasks/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        h1 { color: #333; }
        .task {
            background: white;
            border: 1px solid #ddd;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .task.completed {
            opacity: 0.6;
        }
        .task.completed .task-title {
            text-decoration: line-through;
        }
        .task-info { flex: 1; }
        .task-title { font-weight: bold; margin-bottom: 5px; }
        .task-desc { color: #666; font-size: 0.9em; }
        .task-actions { display: flex; gap: 10px; }
        .btn {
            padding: 8px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            color: white;
        }
        .btn-primary { background: #007bff; }
        .btn-success { background: #28a745; }
        .btn-danger { background: #dc3545; }
        .btn-secondary { background: #6c757d; }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        #create-form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        #message {
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            display: none;
        }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
        .stats {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        .stat {
            background: white;
            padding: 15px 25px;
            border-radius: 5px;
            text-align: center;
        }
        .stat-number { font-size: 2em; font-weight: bold; color: #007bff; }
        .stat-label { color: #666; }
    </style>
</head>
<body>
    <h1>Task Manager</h1>

    <div id="message"></div>

    <div class="stats">
        <div class="stat">
            <div class="stat-number" id="total-count">0</div>
            <div class="stat-label">Total Tasks</div>
        </div>
        <div class="stat">
            <div class="stat-number" id="completed-count">0</div>
            <div class="stat-label">Completed</div>
        </div>
        <div class="stat">
            <div class="stat-number" id="pending-count">0</div>
            <div class="stat-label">Pending</div>
        </div>
    </div>

    <div id="create-form">
        <h2>Add New Task</h2>
        <form id="task-form">
            <div class="form-group">
                <label for="title">Title:</label>
                <input type="text" id="title" name="title" required>
            </div>
            <div class="form-group">
                <label for="description">Description (optional):</label>
                <textarea id="description" name="description" rows="2"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Add Task</button>
        </form>
    </div>

    <h2>Tasks</h2>
    <div id="tasks-container">
        <p>Loading tasks...</p>
    </div>

    <script>
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

        function showMessage(text, type) {
            const msg = document.getElementById('message');
            msg.textContent = text;
            msg.className = type;
            msg.style.display = 'block';
            setTimeout(() => { msg.style.display = 'none'; }, 3000);
        }

        function updateStats(tasks) {
            const total = tasks.length;
            const completed = tasks.filter(t => t.is_completed).length;
            const pending = total - completed;

            document.getElementById('total-count').textContent = total;
            document.getElementById('completed-count').textContent = completed;
            document.getElementById('pending-count').textContent = pending;
        }

        function loadTasks() {
            const container = document.getElementById('tasks-container');

            fetch('/api/tasks/')
                .then(response => response.json())
                .then(tasks => {
                    updateStats(tasks);
                    container.innerHTML = '';

                    if (tasks.length === 0) {
                        container.innerHTML = '<p>No tasks yet. Add one above!</p>';
                        return;
                    }

                    tasks.forEach(task => {
                        const taskDiv = document.createElement('div');
                        taskDiv.className = 'task' + (task.is_completed ? ' completed' : '');
                        taskDiv.innerHTML = `
                            <div class="task-info">
                                <div class="task-title">${task.title}</div>
                                ${task.description ? `<div class="task-desc">${task.description}</div>` : ''}
                            </div>
                            <div class="task-actions">
                                <button class="btn ${task.is_completed ? 'btn-secondary' : 'btn-success'}"
                                        onclick="toggleTask(${task.id})">
                                    ${task.is_completed ? 'Undo' : 'Complete'}
                                </button>
                                <button class="btn btn-danger" onclick="deleteTask(${task.id})">Delete</button>
                            </div>
                        `;
                        container.appendChild(taskDiv);
                    });
                })
                .catch(error => {
                    container.innerHTML = '<p>Error loading tasks.</p>';
                });
        }

        function toggleTask(id) {
            fetch(`/api/tasks/${id}/toggle/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            })
            .then(response => response.json())
            .then(data => {
                loadTasks();
            });
        }

        function deleteTask(id) {
            if (!confirm('Delete this task?')) return;

            fetch(`/api/tasks/${id}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': csrftoken
                }
            })
            .then(response => {
                if (response.ok) {
                    showMessage('Task deleted!', 'success');
                    loadTasks();
                }
            });
        }

        document.getElementById('task-form').addEventListener('submit', function(e) {
            e.preventDefault();

            const title = document.getElementById('title').value;
            const description = document.getElementById('description').value;

            fetch('/api/tasks/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ title, description })
            })
            .then(response => {
                if (response.ok) return response.json();
                throw new Error('Failed to create task');
            })
            .then(data => {
                showMessage('Task added!', 'success');
                document.getElementById('task-form').reset();
                loadTasks();
            })
            .catch(error => {
                showMessage('Error adding task', 'error');
            });
        });

        document.addEventListener('DOMContentLoaded', loadTasks);
    </script>
</body>
</html>
```
</details>

---

## Challenge Exercises

### Challenge 1: Add API Authentication

**Task:**
1. Add Token authentication to the API
2. Create a login endpoint that returns a token
3. Protect create/update/delete endpoints

---

### Challenge 2: Add Pagination

**Task:**
1. Configure DRF pagination (10 items per page)
2. Update JavaScript to handle pagination
3. Add "Load More" or page navigation

---

### Challenge 3: Add Search and Filter

**Task:**
1. Add search functionality to the API
2. Add filter by status (completed/pending)
3. Update JavaScript with search input and filter buttons

---

### Challenge 4: Add Categories/Tags

**Task:**
1. Create a Category model
2. Add ForeignKey to Task/Post
3. Create CategorySerializer with nested tasks
4. Filter API by category

---

### Challenge 5: Build Real-time Updates

**Task:**
1. Implement polling (check for updates every 5 seconds)
2. Or use WebSockets for real-time updates
3. Update the UI when data changes

---

**Remember:** APIs are the backbone of modern web applications. Practice building clean, well-documented APIs!
