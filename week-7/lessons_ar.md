# دروس الأسبوع السابع – واجهات برمجة التطبيقات، أساسيات JavaScript وDjango REST Framework

مرحبًا بك في الأسبوع السابع! هذا الأسبوع سنتعلم كيفية بناء واجهات برمجة تطبيقات REST باستخدام Django وDjango REST Framework، واستخدام JavaScript لاستهلاك تلك الواجهات. بنهاية هذا الأسبوع، ستكون قادرًا على إنشاء واجهات برمجة JSON وبناء صفحات تفاعلية تجلب البيانات بشكل ديناميكي.

---

## جدول المحتويات

1. [مقدمة إلى واجهات برمجة التطبيقات](#1-مقدمة-إلى-واجهات-برمجة-التطبيقات)
2. [مفاهيم REST API](#2-مفاهيم-rest-api)
3. [صيغة بيانات JSON](#3-صيغة-بيانات-json)
4. [Django وJSON](#4-django-وjson)
5. [مقدمة إلى Django REST Framework](#5-مقدمة-إلى-django-rest-framework)
6. [المسلسلات (Serializers)](#6-المسلسلات-serializers)
7. [عروض واجهة برمجة التطبيقات](#7-عروض-واجهة-برمجة-التطبيقات)
8. [ViewSets والـ Routers](#8-viewsets-والـ-routers)
9. [المصادقة في واجهة برمجة التطبيقات](#9-المصادقة-في-واجهة-برمجة-التطبيقات)
10. [أساسيات JavaScript](#10-أساسيات-javascript)
11. [Fetch API](#11-fetch-api)
12. [التعامل مع DOM](#12-التعامل-مع-dom)
13. [مشروع مصغّر: واجهة برمجة مدونة مع واجهة JavaScript أمامية](#13-مشروع-مصغّر)

---

## 1. مقدمة إلى واجهات برمجة التطبيقات

### ما هي واجهة برمجة التطبيقات (API)؟

**API** اختصار لـ **Application Programming Interface** (واجهة برمجة التطبيقات). وهي طريقة تتيح لتطبيقات البرمجيات المختلفة التواصل مع بعضها.

**تشبيه من الواقع:**
- قائمة الطعام في المطعم تشبه الـ API
- أنت (العميل) تقرأ القائمة (توثيق الـ API)
- تضع طلبًا (ترسل طلبًا)
- المطبخ (الخادم) يجهّز طعامك
- النادل يحضر طعامك (الاستجابة)

**لماذا نستخدم واجهات برمجة التطبيقات؟**
- تطبيقات الجوال تحتاج إلى بيانات من الخوادم
- تطبيقات الصفحة الواحدة (SPAs)
- التكاملات مع أطراف ثالثة
- بنية الخدمات المصغّرة (Microservices)
- الفصل بين الواجهة الأمامية والخلفية

**بدون API:**
```html
<!-- الطريقة التقليدية: الخادم يولّد HTML -->
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>
```

**مع API:**
```javascript
// الطريقة الحديثة: العميل يجلب البيانات ويعرضها
fetch('/api/posts/1/')
  .then(response => response.json())
  .then(post => {
    document.getElementById('title').textContent = post.title;
  });
```

### أنواع واجهات برمجة التطبيقات

1. **واجهات برمجة الويب** - عبر HTTP (ما سنبنيه)
2. **واجهات برمجة المكتبات** - وحدات Python، الدوال
3. **واجهات برمجة نظام التشغيل** - نظام الملفات، الأجهزة

---

## 2. مفاهيم REST API

### ما هو REST؟

**REST** (Representational State Transfer) هو أسلوب معماري لتصميم التطبيقات الشبكية.

**مبادئ REST:**
1. **العميل والخادم** - فصل المسؤوليات
2. **بدون حالة** - كل طلب مستقل بذاته
3. **واجهة موحّدة** - أساليب HTTP قياسية
4. **قائم على الموارد** - كل شيء مورد

### الموارد ونقاط النهاية

**المورد:** كائن بيانات (مثل: Post، User، Comment)

**نقطة النهاية:** الرابط للوصول إلى مورد معين

```
/api/posts/        # مجموعة من المنشورات
/api/posts/1/      # منشور واحد بمعرّف 1
/api/users/        # مجموعة من المستخدمين
/api/users/5/      # مستخدم واحد بمعرّف 5
```

### طرق HTTP (الأفعال)

| الطريقة | الإجراء | مثال |
|---------|---------|------|
| GET | قراءة البيانات | الحصول على جميع المنشورات |
| POST | إنشاء جديد | إنشاء منشور جديد |
| PUT | تحديث (كامل) | استبدال المنشور بالكامل |
| PATCH | تحديث (جزئي) | تحديث العنوان فقط |
| DELETE | حذف | حذف منشور |

### ربط CRUD بـ HTTP

| CRUD | HTTP | نقطة النهاية | الوصف |
|------|------|-------------|-------|
| إنشاء | POST | /api/posts/ | إنشاء منشور جديد |
| قراءة | GET | /api/posts/ | عرض جميع المنشورات |
| قراءة | GET | /api/posts/1/ | الحصول على منشور واحد |
| تحديث | PUT/PATCH | /api/posts/1/ | تحديث منشور |
| حذف | DELETE | /api/posts/1/ | حذف منشور |

### بنية الطلب والاستجابة

**بنية الطلب:**
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

**بنية الاستجابة:**
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

### رموز حالة HTTP

| الرمز | المعنى | متى يُستخدم |
|-------|--------|------------|
| 200 | OK | GET/PUT/PATCH ناجح |
| 201 | تم الإنشاء | POST ناجح |
| 204 | لا محتوى | DELETE ناجح |
| 400 | طلب غير صحيح | مدخلات غير صالحة |
| 401 | غير مُصادق | غير مسجّل الدخول |
| 403 | محظور | لا صلاحية |
| 404 | غير موجود | المورد غير موجود |
| 500 | خطأ في الخادم | حدث خطأ ما |

---

## 3. صيغة بيانات JSON

### ما هو JSON؟

**JSON** (JavaScript Object Notation) هو صيغة بيانات خفيفة الوزن لتبادل البيانات بين العميل والخادم.

**لماذا JSON؟**
- مقروء من قِبل الإنسان
- مستقل عن لغات البرمجة
- سهل التحليل
- المعيار القياسي لواجهات برمجة الويب

### صياغة JSON

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

**أنواع بيانات JSON:**
- **نص:** `"Hello"`
- **رقم:** `42`, `3.14`
- **منطقي:** `true`, `false`
- **مصفوفة:** `[1, 2, 3]`
- **كائن:** `{"key": "value"}`
- **فارغ:** `null`

### JSON في Python

```python
import json

# قاموس Python إلى نص JSON
data = {'name': 'Ahmed', 'age': 25}
json_string = json.dumps(data)
print(json_string)  # '{"name": "Ahmed", "age": 25}'

# نص JSON إلى قاموس Python
json_string = '{"name": "Ahmed", "age": 25}'
data = json.loads(json_string)
print(data['name'])  # Ahmed
```

---

## 4. Django وJSON

### JsonResponse

يوفّر Django كائن `JsonResponse` لإعادة بيانات JSON.

**مثال أساسي:**
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

**إعداد الرابط:**
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/hello/', views.api_hello, name='api_hello'),
]
```

**الاستجابة:**
```json
{
    "message": "Hello, World!",
    "status": "success"
}
```

### إعادة بيانات النموذج

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

### معالجة طلبات POST

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post

@csrf_exempt  # للتجريب فقط - استخدم المصادقة الصحيحة في الإنتاج
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

### مشكلات واجهات JSON اليدوية

- الكثير من الكود المتكرر
- تحويل يدوي للبيانات
- لا تحقق تلقائي
- لا واجهة تصفح للـ API
- اعتبارات أمنية كثيرة

**الحل:** Django REST Framework!

---

## 5. مقدمة إلى Django REST Framework

### ما هو DRF؟

**Django REST Framework (DRF)** هو مجموعة أدوات قوية لبناء واجهات برمجة الويب في Django.

**المميزات:**
- التسلسل (تحويل النماذج إلى JSON والعكس)
- المصادقة والصلاحيات
- واجهة تصفح للـ API
- ViewSets والـ Routers
- التقسيم إلى صفحات
- التصفية
- التوثيق

### التثبيت

```bash
pip install djangorestframework
```

**settings.py:**
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
]

# اختياري: إعداد خيارات DRF
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

### مثال سريع

**قبل DRF (يدويًا):**
```python
def api_posts(request):
    posts = Post.objects.all()
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            # ... المزيد من الحقول
        })
    return JsonResponse({'posts': data})
```

**بعد DRF:**
```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

أقصر وأنظف بكثير!

---

## 6. المسلسلات (Serializers)

### ما هي المسلسلات؟

**المسلسلات** تحوّل أنواع البيانات المعقدة (كنماذج Django) إلى أنواع Python الأصلية التي يمكن تحويلها إلى JSON.

**تحويل في اتجاهين:**
- **التسلسل:** نموذج → JSON (للاستجابات)
- **فك التسلسل:** JSON → نموذج (للطلبات)

### إنشاء مسلسل

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

**ModelSerializer** يولّد الحقول تلقائيًا من النموذج.

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
        # أو استخدم: fields = '__all__'
```

**المزايا:**
- توليد تلقائي للحقول
- create() وupdate() مدمجة
- كود أقل

### خيارات حقول المسلسل

```python
class PostSerializer(serializers.ModelSerializer):
    # حقل للقراءة فقط
    created_at = serializers.DateTimeField(read_only=True)

    # حقل مخصص
    excerpt = serializers.SerializerMethodField()

    # مسلسل متداخل
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'excerpt', 'author', 'created_at']

    def get_excerpt(self, obj):
        return obj.content[:100] + '...' if len(obj.content) > 100 else obj.content
```

### التحقق في المسلسلات

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']

    # التحقق على مستوى الحقل
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("يجب أن يحتوي العنوان على 5 أحرف على الأقل")
        return value

    # التحقق على مستوى الكائن
    def validate(self, data):
        if 'spam' in data.get('content', '').lower():
            raise serializers.ValidationError("المحتوى يحتوي على بريد مزعج")
        return data
```

### استخدام المسلسلات

```python
# تسلسل كائن واحد
post = Post.objects.get(pk=1)
serializer = PostSerializer(post)
print(serializer.data)  # {'id': 1, 'title': '...', ...}

# تسلسل كائنات متعددة
posts = Post.objects.all()
serializer = PostSerializer(posts, many=True)
print(serializer.data)  # [{'id': 1, ...}, {'id': 2, ...}]

# فك التسلسل والإنشاء
data = {'title': 'New Post', 'content': 'Hello!'}
serializer = PostSerializer(data=data)
if serializer.is_valid():
    serializer.save()
else:
    print(serializer.errors)
```

---

## 7. عروض واجهة برمجة التطبيقات

### العروض القائمة على الدوال

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

### العروض القائمة على الفئات

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

### العروض العامة (Generic Views)

يوفّر DRF عروضًا عامة تتعامل مع الأنماط الشائعة.

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

**العروض العامة المتاحة:**
- `ListAPIView` - GET قائمة
- `CreateAPIView` - POST إنشاء
- `RetrieveAPIView` - GET عنصر واحد
- `UpdateAPIView` - PUT/PATCH تحديث
- `DestroyAPIView` - DELETE حذف
- `ListCreateAPIView` - GET قائمة + POST إنشاء
- `RetrieveUpdateDestroyAPIView` - GET + PUT + DELETE

---

## 8. ViewSets والـ Routers

### ViewSets

**ViewSet** يجمع عدة عروض في فئة واحدة.

```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

هذه الفئة الواحدة توفّر:
- `list()` - GET /posts/
- `create()` - POST /posts/
- `retrieve()` - GET /posts/{id}/
- `update()` - PUT /posts/{id}/
- `partial_update()` - PATCH /posts/{id}/
- `destroy()` - DELETE /posts/{id}/

### Routers

**Routers** تولّد أنماط URL تلقائيًا لـ ViewSets.

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

**الروابط المولّدة:**
- `GET /api/posts/` - عرض جميع المنشورات
- `POST /api/posts/` - إنشاء منشور
- `GET /api/posts/1/` - الحصول على منشور 1
- `PUT /api/posts/1/` - تحديث منشور 1
- `PATCH /api/posts/1/` - تحديث جزئي
- `DELETE /api/posts/1/` - حذف منشور 1

### الإجراءات المخصصة

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

**الروابط:**
- `POST /api/posts/1/publish/` - نشر المنشور 1
- `GET /api/posts/recent/` - الحصول على أحدث المنشورات

---

## 9. المصادقة في واجهة برمجة التطبيقات

### أنواع المصادقة

**1. مصادقة الجلسة (افتراضية):**
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

**2. مصادقة الرمز (Token):**
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
python manage.py migrate  # إنشاء جدول الرموز
```

### إنشاء الرموز

```python
# إنشاء رمز للمستخدم
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='ahmed')
token, created = Token.objects.get_or_create(user=user)
print(token.key)  # abc123...
```

### استخدام الرموز

**طلب العميل:**
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

### الصلاحيات

```python
from rest_framework import permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
```

**الصلاحيات المدمجة:**
- `AllowAny` - بلا قيود
- `IsAuthenticated` - للمستخدمين المسجّلين فقط
- `IsAdminUser` - للمسؤولين فقط
- `IsAuthenticatedOrReadOnly` - القراءة للجميع، الكتابة للمسجّلين

### الصلاحيات المخصصة

```python
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # صلاحيات القراءة لأي طلب
        if request.method in permissions.SAFE_METHODS:
            return True
        # صلاحيات الكتابة للمؤلف فقط
        return obj.author == request.user
```

---

## 10. أساسيات JavaScript

### لماذا JavaScript؟

JavaScript تتيح لك:
- تحديث محتوى الصفحة دون إعادة تحميلها
- إجراء استدعاءات API (AJAX)
- التعامل مع تفاعلات المستخدم
- بناء واجهات ديناميكية

### المتغيرات

```javascript
// JavaScript الحديثة (ES6+)
let name = 'Ahmed';        // يمكن إعادة تعيينه
const age = 25;            // لا يمكن إعادة تعيينه
var city = 'Riyadh';       // الطريقة القديمة (تجنّبها)

// أنواع البيانات
let text = 'Hello';        // نص
let number = 42;           // رقم
let decimal = 3.14;        // رقم عشري
let isTrue = true;         // منطقي
let items = [1, 2, 3];     // مصفوفة
let person = {             // كائن
    name: 'Ahmed',
    age: 25
};
```

### الدوال

```javascript
// دالة عادية
function greet(name) {
    return 'Hello, ' + name;
}

// دالة السهم (ES6+)
const greet = (name) => {
    return 'Hello, ' + name;
};

// دالة سهم مختصرة
const greet = name => 'Hello, ' + name;

// الاستخدام
console.log(greet('Ahmed'));  // Hello, Ahmed
```

### المصفوفات

```javascript
const fruits = ['apple', 'banana', 'orange'];

// الوصول
console.log(fruits[0]);  // apple

// الإضافة
fruits.push('mango');

// الحلقة
fruits.forEach(fruit => {
    console.log(fruit);
});

// التحويل (map)
const upperFruits = fruits.map(fruit => fruit.toUpperCase());

// التصفية (filter)
const longNames = fruits.filter(fruit => fruit.length > 5);
```

### الكائنات

```javascript
const person = {
    name: 'Ahmed',
    age: 25,
    city: 'Riyadh',
    greet: function() {
        return 'Hello, I am ' + this.name;
    }
};

// الوصول
console.log(person.name);      // Ahmed
console.log(person['age']);    // 25

// الطريقة
console.log(person.greet());   // Hello, I am Ahmed

// التفكيك
const { name, age } = person;
console.log(name);  // Ahmed
```

### القوالب النصية (Template Literals)

```javascript
const name = 'Ahmed';
const age = 25;

// الطريقة القديمة
const message = 'Hello, ' + name + '. You are ' + age + ' years old.';

// القوالب النصية (ES6+)
const message = `Hello, ${name}. You are ${age} years old.`;
```

---

## 11. Fetch API

### ما هو Fetch؟

**Fetch** هو واجهة JavaScript حديثة لإجراء طلبات HTTP.

### طلب GET أساسي

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

### صياغة Async/Await

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

### طلب POST

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

### طلب PUT

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

### طلب DELETE

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

### مع رمز المصادقة

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

### معالجة الأخطاء

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
        // عرض الخطأ للمستخدم
        document.getElementById('error').textContent = error.message;
    }
}
```

---

## 12. التعامل مع DOM

### ما هو DOM؟

**DOM** (Document Object Model) هو واجهة برمجية لمستندات HTML. يمثّل الصفحة كشجرة من الكائنات.

### تحديد العناصر

```javascript
// بالمعرّف
const title = document.getElementById('title');

// بالفئة (يعيد مجموعة)
const items = document.getElementsByClassName('item');

// بالوسم (يعيد مجموعة)
const paragraphs = document.getElementsByTagName('p');

// محدد الاستعلام (CSS selector)
const header = document.querySelector('.header');

// جميع المطابقات (يعيد NodeList)
const buttons = document.querySelectorAll('.btn');
```

### تغيير المحتوى

```javascript
const title = document.getElementById('title');

// تغيير النص
title.textContent = 'New Title';

// تغيير HTML
title.innerHTML = '<em>New Title</em>';

// تغيير السمة
title.setAttribute('class', 'main-title');

// تغيير التنسيق
title.style.color = 'blue';
title.style.fontSize = '24px';
```

### إنشاء العناصر

```javascript
// إنشاء عنصر
const newDiv = document.createElement('div');
newDiv.textContent = 'Hello!';
newDiv.className = 'message';

// إضافته للصفحة
document.body.appendChild(newDiv);

// أو الإدراج في موضع محدد
const container = document.getElementById('container');
container.appendChild(newDiv);
```

### مستمعو الأحداث

```javascript
const button = document.getElementById('submit-btn');

button.addEventListener('click', function(event) {
    console.log('Button clicked!');
});

// نسخة دالة السهم
button.addEventListener('click', (e) => {
    e.preventDefault();  // منع السلوك الافتراضي
    console.log('Button clicked!');
});
```

### مثال متكامل: عرض المنشورات

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

        // مسح رسالة التحميل
        container.innerHTML = '';

        // إنشاء عنصر لكل منشور
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

## 13. مشروع مصغّر: واجهة برمجة مدونة مع واجهة JavaScript أمامية

### نظرة عامة على المشروع

بناء تطبيق مدونة متكامل يشمل:
- واجهة برمجة DRF خلفية
- واجهة JavaScript أمامية تجلب البيانات وتعرضها
- إنشاء المنشورات وقراءتها وتحديثها وحذفها عبر الـ API

### إعداد الخلفية

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

**urls.py (التطبيق):**
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

### إعداد الواجهة الأمامية

راجع ملف الدروس الإنجليزي للاطلاع على الكود الكامل للقالب.

### تشغيل المشروع

1. إنشاء التهجيرات وتطبيقها
2. إنشاء مستخدم مسؤول
3. تشغيل الخادم
4. زيارة الصفحة لعرض المنشورات
5. إنشاء المنشورات وعرضها وحذفها عبر واجهة JavaScript

### نقاط التعلم الرئيسية

1. **REST API** توفّر البيانات بصيغة JSON
2. **DRF** يبسّط إنشاء الـ API بالمسلسلات والـ ViewSets
3. **JavaScript fetch()** ترسل طلبات HTTP إلى الـ API
4. **التعامل مع DOM** يحدّث الصفحة ديناميكيًا
5. **رمز CSRF** مطلوب لطلبات POST/DELETE في Django

---

## الملخص

هذا الأسبوع تعلّمت:

1. **مفاهيم REST API** - الموارد، نقاط النهاية، طرق HTTP، رموز الحالة
2. **صيغة JSON** - صيغة تبادل البيانات للـ APIs
3. **Django JsonResponse** - استجابات JSON البسيطة
4. **Django REST Framework** - مجموعة أدوات API قوية
5. **المسلسلات** - تحويل النماذج إلى JSON والعكس
6. **عروض الـ API** - العروض القائمة على الدوال، والفئات، والعامة
7. **ViewSets والـ Routers** - توجيه URL التلقائي
8. **مصادقة الـ API** - مصادقة الرمز والصلاحيات
9. **أساسيات JavaScript** - المتغيرات، الدوال، المصفوفات، الكائنات
10. **Fetch API** - إجراء طلبات HTTP من JavaScript
11. **التعامل مع DOM** - تحديث محتوى الصفحة ديناميكيًا

**الأسبوع القادم:** المشروع النهائي - تصميم وبناء تطبيق Django متكامل!
