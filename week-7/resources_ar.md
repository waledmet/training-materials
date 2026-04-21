# موارد الأسبوع السابع – واجهات برمجة التطبيقات، JavaScript وDjango REST Framework

موارد تعليمية منتقاة لموضوعات الأسبوع السابع.

---

## التوثيق الرسمي

### قراءة أساسية

1. **Django REST Framework** - https://www.django-rest-framework.org/
2. **دليل DRF السريع** - https://www.django-rest-framework.org/tutorial/quickstart/
3. **مسلسلات DRF** - https://www.django-rest-framework.org/api-guide/serializers/
4. **ViewSets في DRF** - https://www.django-rest-framework.org/api-guide/viewsets/
5. **دليل JavaScript من MDN** - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
6. **Fetch API من MDN** - https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

---

## دروس فيديو

**Corey Schafer - Django REST Framework**
- سلسلة دروس DRF متكاملة
- شرح مفاهيم واضح
- المستوى: مناسب للمبتدئين

**Traversy Media - JavaScript Crash Course**
- أساسيات JavaScript الحديثة
- مميزات ES6+
- المستوى: مبتدئ

**Tech with Tim - REST API Tutorial**
- بناء واجهات برمجة مع Django
- أمثلة عملية
- المستوى: مبتدئ

---

## أوراق مرجعية سريعة

### مرجع REST API السريع

```
طرق HTTP:
GET     - قراءة/استرجاع
POST    - إنشاء جديد
PUT     - تحديث (كامل)
PATCH   - تحديث (جزئي)
DELETE  - حذف

رموز الحالة:
200 OK              - نجاح
201 Created         - تم إنشاء المورد
204 No Content      - تم الحذف
400 Bad Request     - مدخلات غير صحيحة
401 Unauthorized    - غير مسجّل الدخول
403 Forbidden       - لا صلاحية
404 Not Found       - غير موجود
500 Server Error    - خطأ/عطل
```

### مسلسلات DRF

```python
# مسلسل أساسي
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()

# ModelSerializer (موصى به)
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
        # أو: fields = '__all__'

# حقل مخصص
excerpt = serializers.SerializerMethodField()

def get_excerpt(self, obj):
    return obj.content[:100]

# التحقق
def validate_title(self, value):
    if len(value) < 5:
        raise serializers.ValidationError("قصير جدًا")
    return value
```

### عروض DRF

```python
# قائم على الدوال
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

# قائم على الفئات
class PostList(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

# العروض العامة
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### Routers في DRF

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### أساسيات JavaScript

```javascript
// المتغيرات
let name = 'Ahmed';      // يمكن إعادة تعيينه
const age = 25;          // لا يمكن إعادة تعيينه

// الدوال
function greet(name) {
    return 'Hello, ' + name;
}

// دالة السهم
const greet = (name) => 'Hello, ' + name;

// المصفوفات
const items = [1, 2, 3];
items.push(4);
items.forEach(item => console.log(item));
items.map(item => item * 2);
items.filter(item => item > 2);

// الكائنات
const person = {
    name: 'Ahmed',
    age: 25
};
console.log(person.name);

// القوالب النصية
const msg = `Hello, ${name}! You are ${age}.`;
```

### Fetch API

```javascript
// طلب GET
fetch('/api/posts/')
    .then(response => response.json())
    .then(data => console.log(data));

// Async/await
async function getPosts() {
    const response = await fetch('/api/posts/');
    const data = await response.json();
    return data;
}

// طلب POST
fetch('/api/posts/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
        title: 'New Post',
        content: 'Content here'
    })
});

// طلب DELETE
fetch('/api/posts/1/', {
    method: 'DELETE',
    headers: {
        'X-CSRFToken': csrftoken
    }
});
```

### التعامل مع DOM

```javascript
// تحديد العناصر
document.getElementById('id');
document.querySelector('.class');
document.querySelectorAll('div');

// تغيير المحتوى
element.textContent = 'Text';
element.innerHTML = '<b>HTML</b>';

// إنشاء العناصر
const div = document.createElement('div');
div.textContent = 'New!';
container.appendChild(div);

// الأحداث
button.addEventListener('click', () => {
    console.log('Clicked!');
});

// تحميل الصفحة
document.addEventListener('DOMContentLoaded', () => {
    // الصفحة جاهزة
});
```

---

## مشاريع تطبيقية

### ابنِ هذه المشاريع للتدرب

**1. واجهة برمجة بسيطة**
- أنشئ نقاط نهاية JSON يدويًا
- أعد عروض القائمة والتفاصيل
- تعامل مع الأخطاء

**2. واجهة برمجة مدونة مع DRF**
- نموذج Post مع مسلسل
- ViewSet كامل مع CRUD
- واجهة تصفح الـ API

**3. عارض منشورات JavaScript**
- اجلب المنشورات من الـ API
- اعرضها في بطاقات
- أضف حالة التحميل

**4. مدير المهام (مشروع الأسبوع)**
- واجهة برمجة المهام مع إجراء التبديل
- واجهة CRUD بـ JavaScript
- لوحة إحصائيات

**5. واجهة برمجة ملاحظات مع وسوم**
- نموذجا Note وTag
- مسلسلات متداخلة
- تصفية حسب الوسم

---

## الأنماط الشائعة

### نمط استجابة الـ API

```python
# بنية استجابة متسقة
{
    "status": "success",
    "data": {...},
    "message": "Post created"
}

# استجابة الخطأ
{
    "status": "error",
    "errors": {...},
    "message": "Validation failed"
}
```

### نمط JavaScript Fetch

```javascript
async function apiCall(url, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(url, options);

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    return method === 'DELETE' ? null : await response.json();
}
```

### نمط حالة التحميل

```javascript
async function loadData() {
    const container = document.getElementById('container');
    container.innerHTML = '<p>جارٍ التحميل...</p>';

    try {
        const data = await fetch('/api/data/').then(r => r.json());
        container.innerHTML = '';
        // عرض البيانات
    } catch (error) {
        container.innerHTML = '<p>خطأ في تحميل البيانات</p>';
    }
}
```

---

## أفضل ممارسات الأمان

**أمان الـ API:**
- استخدم المصادقة لعمليات الكتابة
- تحقق من جميع المدخلات عبر المسلسلات
- استخدم رموز حالة HTTP الصحيحة
- قيّد معدل الطلبات على نقاط النهاية
- لا تكشف البيانات الحساسة

**أمان JavaScript:**
- أدرج دائمًا رمز CSRF
- تحقق من مدخلات المستخدم وعقّمها
- لا تخزّن البيانات الحساسة في localStorage
- استخدم HTTPS في بيئة الإنتاج

---

## نصائح تصحيح الأخطاء

### تصحيح أخطاء الـ API

1. **استخدم واجهة التصفح** - اختبر مباشرة في المتصفح
2. **تحقق من تبويب Network** - راقب الطلبات والاستجابات
3. **اطبع serializer.errors** - اعرف مشاكل التحقق
4. **استخدم Postman/Insomnia** - اختبار API متقدم

### تصحيح أخطاء JavaScript

1. **console.log()** - اطبع القيم
2. **أدوات مطوري المتصفح** - Network وConsole وElements
3. **debugger;** - ضع نقاط توقف في الكود
4. **تبويب Network** - تحقق من استجابات الـ API

---

## موارد إضافية

- **Postman** - أداة اختبار الـ API
- **Insomnia** - بديل لـ Postman
- **HTTPie** - عميل HTTP من سطر الأوامر
- **JSON Formatter** - إضافة متصفح لتنسيق JSON
- **مميزات ES6** - دليل JavaScript الحديث
- **You Don't Know JS** - سلسلة كتب JavaScript مجانية

---

**تذكّر:** واجهات برمجة التطبيقات هي العمود الفقري لتطوير الويب الحديث. أتقنها!
