# تمارين الأسبوع السابع – واجهات برمجة التطبيقات، JavaScript وDjango REST Framework

تمارين تطبيقية للأسبوع السابع: REST APIs، Django REST Framework، وJavaScript لاستهلاك الـ APIs.

---

## جدول المحتويات

1. [اليوم الأول: مفاهيم REST API وJsonResponse](#اليوم-الأول-مفاهيم-rest-api-وjsonresponse)
2. [اليوم الثاني: أساسيات Django REST Framework](#اليوم-الثاني-أساسيات-django-rest-framework)
3. [اليوم الثالث: المسلسلات والـ ViewSets](#اليوم-الثالث-المسلسلات-والـ-viewsets)
4. [اليوم الرابع: JavaScript وFetch API](#اليوم-الرابع-javascript-وfetch-api)
5. [اليوم الخامس: مشروع API متكامل مع واجهة JavaScript أمامية](#اليوم-الخامس-مشروع-api-متكامل-مع-واجهة-javascript-أمامية)
6. [تمارين تحدي](#تمارين-تحدي)

---

## اليوم الأول: مفاهيم REST API وJsonResponse

### تمرين 1: إنشاء نقطة نهاية JSON بسيطة

**المهمة:**
1. أنشئ مشروع Django باسم `api_demo`
2. أنشئ تطبيقًا باسم `core`
3. أنشئ عرضًا يعيد JSON بمعلوماتك

```python
# الاستجابة المتوقعة:
{
    "name": "Your Name",
    "role": "Django Developer",
    "skills": ["Python", "Django", "REST APIs"]
}
```

<details>
<summary>الحل</summary>

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
# api_demo/settings.py - أضف إلى INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'core',
]
```
</details>

---

### تمرين 2: إنشاء نموذج Posts ونقطة نهاية JSON للقائمة

**المهمة:**
1. أنشئ نموذج `Post` بحقول: title، content، created_at
2. أنشئ نقطة نهاية `/api/posts/` تعيد جميع المنشورات بصيغة JSON

<details>
<summary>الحل</summary>

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

### تمرين 3: إنشاء نقطة نهاية تفاصيل المنشور

**المهمة:**
1. أنشئ نقطة نهاية `/api/posts/<id>/` تعيد منشورًا واحدًا
2. أعد خطأ 404 إذا لم يكن المنشور موجودًا

<details>
<summary>الحل</summary>

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

### تمرين 4: إنشاء نقطة نهاية POST للمنشورات الجديدة

**المهمة:**
1. عدّل نقطة النهاية `/api/posts/` لمعالجة طلبات POST
2. اقبل بيانات JSON تحتوي على title وcontent
3. أعد المنشور المنشأ مع رمز الحالة 201

<details>
<summary>الحل</summary>

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

### تمرين 5: إضافة نقطة نهاية DELETE

**المهمة:**
1. أضف طريقة DELETE لنقطة نهاية تفاصيل المنشور
2. احذف المنشور وأعد رمز الحالة 204 No Content

<details>
<summary>الحل</summary>

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

## اليوم الثاني: أساسيات Django REST Framework

### تمرين 6: تثبيت وإعداد DRF

**المهمة:**
1. ثبّت Django REST Framework
2. أضفه إلى INSTALLED_APPS
3. أنشئ عرض API بسيط باستخدام مُزيّن `@api_view`

<details>
<summary>الحل</summary>

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

### تمرين 7: إنشاء مسلسل

**المهمة:**
1. أنشئ `PostSerializer` باستخدام `serializers.Serializer`
2. أدرج الحقول: id، title، content، created_at

<details>
<summary>الحل</summary>

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

### تمرين 8: إنشاء ModelSerializer

**المهمة:**
1. حوّل المسلسل إلى `ModelSerializer`
2. أضف حقل `excerpt` يعرض أول 50 حرفًا من المحتوى

<details>
<summary>الحل</summary>

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

### تمرين 9: إنشاء عروض API مع المسلسل

**المهمة:**
1. أنشئ عرض `post_list_api` باستخدام `@api_view`
2. تعامل مع GET (عرض الكل) وPOST (إنشاء جديد)
3. استخدم PostSerializer

<details>
<summary>الحل</summary>

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

### تمرين 10: إنشاء عرض تفاصيل API

**المهمة:**
1. أنشئ عرض `post_detail_api`
2. تعامل مع طرق GET وPUT وDELETE
3. أعد رموز الحالة الصحيحة

<details>
<summary>الحل</summary>

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

## اليوم الثالث: المسلسلات والـ ViewSets

### تمرين 11: إضافة التحقق إلى المسلسل

**المهمة:**
1. أضف تحققًا للتأكد من أن العنوان يحتوي على 5 أحرف على الأقل
2. أضف تحققًا للتأكد من أن المحتوى لا يحتوي على كلمة "spam"

<details>
<summary>الحل</summary>

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
            raise serializers.ValidationError("يجب أن يحتوي العنوان على 5 أحرف على الأقل")
        return value

    def validate_content(self, value):
        if 'spam' in value.lower():
            raise serializers.ValidationError("لا يمكن أن يحتوي المحتوى على بريد مزعج")
        return value
```
</details>

---

### تمرين 12: إنشاء عروض API قائمة على الفئات

**المهمة:**
1. حوّل العروض القائمة على الدوال إلى فئات باستخدام `APIView`
2. أنشئ `PostListView` و`PostDetailView`

<details>
<summary>الحل</summary>

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

### تمرين 13: استخدام العروض العامة

**المهمة:**
1. بسّط العروض باستخدام العروض العامة
2. استخدم `ListCreateAPIView` و`RetrieveUpdateDestroyAPIView`

<details>
<summary>الحل</summary>

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

### تمرين 14: إنشاء ViewSet

**المهمة:**
1. أنشئ `PostViewSet` باستخدام `ModelViewSet`
2. سجّله مع Router
3. يجب أن تعمل جميع عمليات CRUD تلقائيًا

<details>
<summary>الحل</summary>

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
    # ... روابط أخرى
    path('api/v5/', include(router.urls)),
]
```
</details>

---

### تمرين 15: إضافة إجراء مخصص للـ ViewSet

**المهمة:**
1. أضف إجراءً مخصصًا `recent` يعيد أحدث 5 منشورات
2. يجب أن يكون الرابط `/api/v5/posts/recent/`

<details>
<summary>الحل</summary>

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

## اليوم الرابع: JavaScript وFetch API

### تمرين 16: إنشاء صفحة HTML مع JavaScript

**المهمة:**
1. أنشئ قالبًا يعرض "ستُحمَّل المنشورات هنا..."
2. أضف سكريبت يطبع "Page loaded!" في الكونسول عند تحميل الصفحة

<details>
<summary>الحل</summary>

```python
# core/views.py
def home(request):
    return render(request, 'core/home.html')
```

```python
# core/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    # ... روابط أخرى
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
        <p>ستُحمَّل المنشورات هنا...</p>
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

### تمرين 17: جلب المنشورات من الـ API

**المهمة:**
1. استخدم `fetch()` للحصول على المنشورات من `/api/v5/posts/`
2. اطبع المنشورات في الكونسول

<details>
<summary>الحل</summary>

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
        <p>جارٍ التحميل...</p>
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

### تمرين 18: عرض المنشورات في HTML

**المهمة:**
1. اعرض المنشورات المُجلبة في الصفحة
2. أظهر العنوان والمحتوى لكل منشور

<details>
<summary>الحل</summary>

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
        <p>جارٍ التحميل...</p>
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
                        container.innerHTML = '<p>لا توجد منشورات بعد.</p>';
                        return;
                    }

                    posts.forEach(post => {
                        const postDiv = document.createElement('div');
                        postDiv.className = 'post';
                        postDiv.innerHTML = `
                            <h2>${post.title}</h2>
                            <p>${post.content}</p>
                            <small>تاريخ الإنشاء: ${new Date(post.created_at).toLocaleString()}</small>
                        `;
                        container.appendChild(postDiv);
                    });
                })
                .catch(error => {
                    container.innerHTML = '<p>خطأ في تحميل المنشورات.</p>';
                    console.error('Error:', error);
                });
        }
    </script>
</body>
</html>
```
</details>

---

### تمرين 19: إضافة نموذج إنشاء منشور

**المهمة:**
1. أضف نموذجًا لإنشاء منشورات جديدة
2. استخدم `fetch()` مع طريقة POST لإنشاء المنشورات
3. حدّث القائمة بعد الإنشاء

<details>
<summary>الحل</summary>

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

    <h2>إنشاء منشور جديد</h2>
    <form id="post-form">
        <div class="form-group">
            <label for="title">العنوان:</label>
            <input type="text" id="title" name="title" required>
        </div>
        <div class="form-group">
            <label for="content">المحتوى:</label>
            <textarea id="content" name="content" rows="4" required></textarea>
        </div>
        <button type="submit" class="btn">إنشاء المنشور</button>
    </form>

    <hr>

    <h2>جميع المنشورات</h2>
    <div id="posts-container">
        <p>جارٍ التحميل...</p>
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

        function loadPosts() {
            const container = document.getElementById('posts-container');

            fetch('/api/v5/posts/')
                .then(response => response.json())
                .then(posts => {
                    container.innerHTML = '';

                    if (posts.length === 0) {
                        container.innerHTML = '<p>لا توجد منشورات بعد.</p>';
                        return;
                    }

                    posts.forEach(post => {
                        const postDiv = document.createElement('div');
                        postDiv.className = 'post';
                        postDiv.innerHTML = `
                            <h2>${post.title}</h2>
                            <p>${post.content}</p>
                            <small>تاريخ الإنشاء: ${new Date(post.created_at).toLocaleString()}</small>
                        `;
                        container.appendChild(postDiv);
                    });
                })
                .catch(error => {
                    container.innerHTML = '<p>خطأ في تحميل المنشورات.</p>';
                });
        }

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
                showMessage('تم إنشاء المنشور بنجاح!', 'success');
                document.getElementById('post-form').reset();
                loadPosts();
            })
            .catch(error => {
                showMessage('خطأ في إنشاء المنشور', 'error');
            });
        });

        document.addEventListener('DOMContentLoaded', loadPosts);
    </script>
</body>
</html>
```
</details>

---

### تمرين 20: إضافة وظيفة الحذف

**المهمة:**
1. أضف زر حذف لكل منشور
2. استخدم `fetch()` مع طريقة DELETE
3. اطلب التأكيد قبل الحذف
4. حدّث القائمة بعد الحذف

<details>
<summary>الحل</summary>

```html
<!-- حدّث دالة loadPosts في السكريبت -->
<script>
    // ... (احتفظ بالكود السابق)

    function loadPosts() {
        const container = document.getElementById('posts-container');

        fetch('/api/v5/posts/')
            .then(response => response.json())
            .then(posts => {
                container.innerHTML = '';

                if (posts.length === 0) {
                    container.innerHTML = '<p>لا توجد منشورات بعد.</p>';
                    return;
                }

                posts.forEach(post => {
                    const postDiv = document.createElement('div');
                    postDiv.className = 'post';
                    postDiv.innerHTML = `
                        <h2>${post.title}</h2>
                        <p>${post.content}</p>
                        <small>تاريخ الإنشاء: ${new Date(post.created_at).toLocaleString()}</small>
                        <br><br>
                        <button class="btn" style="background: #dc3545;" onclick="deletePost(${post.id})">حذف</button>
                    `;
                    container.appendChild(postDiv);
                });
            })
            .catch(error => {
                container.innerHTML = '<p>خطأ في تحميل المنشورات.</p>';
            });
    }

    function deletePost(id) {
        if (!confirm('هل أنت متأكد من حذف هذا المنشور؟')) {
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
                showMessage('تم حذف المنشور!', 'success');
                loadPosts();
            } else {
                throw new Error('Failed to delete');
            }
        })
        .catch(error => {
            showMessage('خطأ في حذف المنشور', 'error');
        });
    }
</script>
```
</details>

---

## اليوم الخامس: مشروع API متكامل مع واجهة JavaScript أمامية

### تمرين 21: بناء واجهة برمجة مدير المهام

**المهمة:**
بناء تطبيق مدير مهام يشمل:
1. نموذج Task (title، description، is_completed، created_at)
2. واجهة برمجة REST كاملة باستخدام DRF ViewSet
3. واجهة JavaScript أمامية لـ:
   - عرض جميع المهام
   - إنشاء مهمة جديدة
   - تبديل حالة إتمام المهمة
   - حذف مهمة

<details>
<summary>الحل</summary>

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

راجع ملف التمارين الإنجليزي للاطلاع على الكود الكامل للقالب HTML.
</details>

---

## تمارين تحدي

### تحدي 1: إضافة مصادقة API

**المهمة:**
1. أضف مصادقة الرمز (Token) إلى الـ API
2. أنشئ نقطة نهاية تسجيل دخول تعيد رمزًا
3. احمِ نقاط نهاية الإنشاء/التحديث/الحذف

---

### تحدي 2: إضافة التقسيم إلى صفحات

**المهمة:**
1. اضبط التقسيم إلى صفحات في DRF (10 عناصر لكل صفحة)
2. حدّث JavaScript للتعامل مع التقسيم
3. أضف "تحميل المزيد" أو تنقل الصفحات

---

### تحدي 3: إضافة البحث والتصفية

**المهمة:**
1. أضف وظيفة البحث إلى الـ API
2. أضف تصفية حسب الحالة (مكتمل/معلق)
3. حدّث JavaScript بحقل البحث وأزرار التصفية

---

### تحدي 4: إضافة الفئات/الوسوم

**المهمة:**
1. أنشئ نموذج Category
2. أضف ForeignKey إلى Task/Post
3. أنشئ CategorySerializer مع المهام المتداخلة
4. صفّح الـ API حسب الفئة

---

### تحدي 5: بناء تحديثات في الوقت الفعلي

**المهمة:**
1. نفّذ استطلاع (polling) للتحقق من التحديثات كل 5 ثوانٍ
2. أو استخدم WebSockets للتحديثات الفورية
3. حدّث الواجهة عند تغيّر البيانات

---

**تذكّر:** واجهات برمجة التطبيقات هي العمود الفقري لتطبيقات الويب الحديثة. تدرّب على بناء واجهات نظيفة وموثّقة جيدًا!
