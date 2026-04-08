# دروس الأسبوع السادس – النماذج، التحقق والمصادقة

مرحبًا بك في الأسبوع السادس! هذا الأسبوع سنتعلم كيفية التعامل مع مدخلات المستخدم من خلال النماذج وتنفيذ مصادقة المستخدم. بنهاية هذا الأسبوع، ستكون قادرًا على إنشاء النماذج، والتحقق من البيانات، وبناء نظام تسجيل دخول/تسجيل متكامل.

---

## جدول المحتويات

1. [مقدمة إلى النماذج](#1-مقدمة-إلى-النماذج)
2. [أساسيات نماذج Django](#2-أساسيات-نماذج-django)
3. [ModelForm](#3-modelform)
4. [التحقق من النماذج](#4-التحقق-من-النماذج)
5. [معالجة النماذج في العروض](#5-معالجة-النماذج-في-العروض)
6. [حماية CSRF](#6-حماية-csrf)
7. [نظام مصادقة Django](#7-نظام-مصادقة-django)
8. [تسجيل الدخول والخروج](#8-تسجيل-الدخول-والخروج)
9. [تسجيل المستخدم](#9-تسجيل-المستخدم)
10. [حماية العروض](#10-حماية-العروض)
11. [العروض المبنية على الفئات](#11-العروض-المبنية-على-الفئات)
12. [إطار عمل الرسائل](#12-إطار-عمل-الرسائل)
13. [مشروع مصغّر: مدونة مع مصادقة](#13-مشروع-مصغّر-مدونة-مع-مصادقة)

---

## 1. مقدمة إلى النماذج

### لماذا النماذج؟

تتيح النماذج للمستخدمين **التفاعل** مع تطبيقك عبر إرسال البيانات.

**حالات الاستخدام الشائعة:**
- تسجيل الدخول / إنشاء الحساب
- إنشاء / تعديل منشورات المدونة
- نماذج التواصل
- وظيفة البحث
- التعليقات
- التقييمات

**بدون نماذج:**
```python
# بيانات مُضمَّنة في الكود
post = Post.objects.create(title="Hardcoded", content="Not flexible")
```

**مع نماذج:**
```html
<!-- يمكن للمستخدم إدخال بياناته الخاصة -->
<form method="post">
    <input type="text" name="title">
    <textarea name="content"></textarea>
    <button type="submit">إرسال</button>
</form>
```

### نماذج HTML مقابل نماذج Django

**نموذج HTML عادي:**
```html
<form method="post" action="/submit/">
    <input type="text" name="email">
    <input type="password" name="password">
    <button type="submit">تسجيل الدخول</button>
</form>
```

**المشكلات:**
- لا يوجد تحقق
- لا يوجد أمان (CSRF)
- معالجة الأخطاء متكررة
- كتابة HTML يدويًا

**نماذج Django تحل هذه المشكلات:**
- ✅ توليد HTML تلقائي
- ✅ تحقق مدمج
- ✅ حماية CSRF
- ✅ معالجة الأخطاء
- ✅ تنظيف البيانات

---

## 2. أساسيات نماذج Django

### إنشاء نموذج

**forms.py:**
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

**حقول النماذج:**
- `CharField` - إدخال نصي
- `EmailField` - التحقق من البريد الإلكتروني
- `IntegerField` - أرقام
- `BooleanField` - مربعات الاختيار
- `ChoiceField` - قوائم منسدلة
- `DateField` - منتقي التاريخ

### معاملات الحقول

```python
class ContactForm(forms.Form):
    # حقل مطلوب (افتراضي)
    name = forms.CharField(max_length=100)

    # حقل اختياري
    phone = forms.CharField(required=False)

    # مع نص مساعد
    email = forms.EmailField(help_text="لن نشارك بريدك الإلكتروني أبدًا")

    # مع قيمة أولية
    subject = forms.CharField(initial="مرحبًا")

    # مع تسمية مخصصة
    message = forms.CharField(
        label="رسالتك",
        widget=forms.Textarea(attrs={'rows': 5})
    )
```

### الودجات (Widgets)

**الودجات تتحكم في كيفية عرض حقول النموذج:**

```python
from django import forms

class ExampleForm(forms.Form):
    # إدخال نصي (افتراضي)
    name = forms.CharField()

    # منطقة نص
    bio = forms.CharField(widget=forms.Textarea)

    # إدخال كلمة مرور
    password = forms.CharField(widget=forms.PasswordInput)

    # إدخال البريد الإلكتروني
    email = forms.EmailField(widget=forms.EmailInput)

    # قائمة منسدلة
    country = forms.ChoiceField(choices=[
        ('us', 'United States'),
        ('uk', 'United Kingdom'),
        ('sa', 'Saudi Arabia'),
    ])

    # مربعات الاختيار
    subscribe = forms.BooleanField(widget=forms.CheckboxInput)

    # أزرار الاختيار
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[('m', 'ذكر'), ('f', 'أنثى')]
    )
```

### خصائص الودجة المخصصة

```python
class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'أدخل اسمك',
            'id': 'name-input'
        })
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 40,
            'class': 'form-control'
        })
    )
```

---

## 3. ModelForm

### ما هو ModelForm؟

**ModelForm** يُنشئ نموذجًا تلقائيًا من النموذج (Model).

**بدون ModelForm:**
```python
class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.TextField()
    status = forms.ChoiceField(choices=[...])
    # يجب المطابقة يدويًا مع حقول النموذج
```

**مع ModelForm:**
```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
    # يطابق النموذج تلقائيًا!
```

### إنشاء ModelForm

```python
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
```

### خيارات Meta في ModelForm

```python
class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # تحديد الحقول المضمّنة
        fields = ['title', 'content', 'status']

        # أو استخدام جميع الحقول (غير موصى به)
        # fields = '__all__'

        # أو استثناء حقول معينة
        # exclude = ['created_at', 'author']

        # تسميات مخصصة
        labels = {
            'title': 'عنوان المنشور',
            'content': 'محتوى المنشور',
        }

        # نصوص مساعدة
        help_texts = {
            'status': 'اختر مستوى ظهور المنشور',
        }

        # ودجات مخصصة
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
```

### متى تستخدم ModelForm مقابل Form

**استخدم ModelForm عندما:**
- إنشاء/تعديل نسخ من النموذج
- حقول النموذج تتطابق مع حقول النموذج (Model)
- تريد تحققًا تلقائيًا

**استخدم Form عندما:**
- لا توجد علاقة مباشرة بنموذج
- نماذج التواصل
- نماذج البحث
- نماذج تسجيل الدخول (لا تُنشئ/تُعدّل نموذجًا)

---

## 4. التحقق من النماذج

### التحقق المدمج

تتحقق نماذج Django تلقائيًا:

```python
form = ContactForm(data={'email': 'invalid-email'})
if form.is_valid():
    # معالجة البيانات
    pass
else:
    # عرض الأخطاء
    print(form.errors)
```

**محققات الحقول:**
```python
class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20
    )

    email = forms.EmailField()  # يتحقق من صيغة البريد الإلكتروني

    age = forms.IntegerField(
        min_value=18,
        max_value=100
    )

    url = forms.URLField()  # يتحقق من صيغة الرابط
```

### التحقق المخصص للحقول

**الطريقة 1: clean_<fieldname>**

```python
class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # التحقق من وجود اسم المستخدم
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("اسم المستخدم مستخدم بالفعل")

        # التحقق من عدم وجود مسافات
        if ' ' in username:
            raise forms.ValidationError("لا يمكن أن يحتوي اسم المستخدم على مسافات")

        return username

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("كلمتا المرور غير متطابقتين")

        return password_confirm
```

### التحقق على مستوى النموذج

**الطريقة 2: clean()**

```python
class BookingForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError(
                    "يجب أن يكون تاريخ الانتهاء بعد تاريخ البداية"
                )

        return cleaned_data
```

### محققات مخصصة

```python
from django.core.exceptions import ValidationError

def validate_even_number(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} ليس عددًا زوجيًا')

class NumberForm(forms.Form):
    number = forms.IntegerField(validators=[validate_even_number])
```

---

## 5. معالجة النماذج في العروض

### GET مقابل POST

**طلب GET:** عرض النموذج الفارغ
**طلب POST:** معالجة البيانات المُرسَلة

### عرض النموذج الأساسي

```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        # تم إرسال النموذج
        form = ContactForm(request.POST)

        if form.is_valid():
            # معالجة البيانات
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # فعل شيء بالبيانات
            # إرسال بريد إلكتروني، حفظ في قاعدة البيانات، إلخ

            return redirect('success')
    else:
        # عرض النموذج الفارغ
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

### عرض ModelForm (إنشاء)

```python
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            # الحفظ في قاعدة البيانات
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})
```

### عرض ModelForm (تعديل)

```python
from django.shortcuts import get_object_or_404

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'post_form.html', {
        'form': form,
        'post': post
    })
```

### قالب النموذج

```html
<!-- templates/contact.html -->
<form method="post">
    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">إرسال</button>
</form>
```

**خيارات عرض النموذج:**

```html
<!-- كفقرات (الأكثر شيوعًا) -->
{{ form.as_p }}

<!-- كجدول -->
<table>{{ form.as_table }}</table>

<!-- كقائمة غير مرتبة -->
<ul>{{ form.as_ul }}</ul>

<!-- عرض يدوي (تحكم كامل) -->
<div>
    {{ form.name.label_tag }}
    {{ form.name }}
    {% if form.name.errors %}
        <div class="error">{{ form.name.errors }}</div>
    {% endif %}
</div>
```

### عرض أخطاء النموذج

```html
<form method="post">
    {% csrf_token %}

    <!-- عرض جميع أخطاء النموذج -->
    {% if form.errors %}
        <div class="alert alert-danger">
            يرجى تصحيح الأخطاء أدناه.
        </div>
    {% endif %}

    <!-- عرض أخطاء الحقول -->
    <div>
        {{ form.email.label_tag }}
        {{ form.email }}
        {% if form.email.errors %}
            <div class="error">
                {{ form.email.errors }}
            </div>
        {% endif %}
    </div>

    <button type="submit">إرسال</button>
</form>
```

---

## 6. حماية CSRF

### ما هو CSRF؟

**CSRF (تزوير الطلبات عبر المواقع):** هجوم يخدع المستخدمين لإرسال طلبات إلى موقعك عبر موقع خبيث.

**مثال على الهجوم:**
```html
<!-- موقع خبيث -->
<form action="https://yoursite.com/delete-account" method="post">
    <button>اضغط للحصول على جائزة مجانية!</button>
</form>
```

### حماية Django من CSRF

**Django يحميك تلقائيًا:**

1. **في القالب:**
```html
<form method="post">
    {% csrf_token %}  <!-- مطلوب! -->
    {{ form.as_p }}
    <button type="submit">إرسال</button>
</form>
```

2. **Django يضيف رمزًا مخفيًا:**
```html
<input type="hidden" name="csrfmiddlewaretoken" value="...رمز طويل...">
```

3. **Django يتحقق من الرمز عند POST**

**مهم:**
- استخدم دائمًا `{% csrf_token %}` في نماذج POST
- يرفض Django النماذج التي لا تحتوي على رمز CSRF صالح
- طلبات GET لا تحتاج إلى رمز CSRF

---

## 7. نظام مصادقة Django

### نموذج المستخدم المدمج

يوفر Django نموذج `User`:

```python
from django.contrib.auth.models import User

# حقول المستخدم:
# - username
# - password (مُشفَّر)
# - email
# - first_name
# - last_name
# - is_active
# - is_staff
# - is_superuser
# - date_joined
# - last_login
```

### إنشاء المستخدمين

```python
from django.contrib.auth.models import User

# إنشاء مستخدم عادي
user = User.objects.create_user(
    username='ahmed',
    email='ahmed@example.com',
    password='secure_password'  # يُشفَّر تلقائيًا
)

# إنشاء مستخدم خارق (عبر الصدفة أو أمر createsuperuser)
user = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin_password'
)
```

**لا تخزن كلمات المرور بنص صريح أبدًا:**
```python
# ❌ خطأ
user.password = 'mypassword'
user.save()

# ✅ صحيح
user.set_password('mypassword')
user.save()
```

### التحقق من كلمات المرور

```python
from django.contrib.auth import authenticate

# مصادقة المستخدم
user = authenticate(
    username='ahmed',
    password='secure_password'
)

if user is not None:
    # بيانات الاعتماد صحيحة
    print("تسجيل الدخول ناجح")
else:
    # بيانات اعتماد غير صالحة
    print("اسم المستخدم أو كلمة المرور غير صحيحة")
```

---

## 8. تسجيل الدخول والخروج

### عرض تسجيل الدخول

```python
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': 'اسم المستخدم أو كلمة المرور غير صحيحة'
            })

    return render(request, 'login.html')
```

### قالب تسجيل الدخول

```html
<!-- templates/login.html -->
<h2>تسجيل الدخول</h2>

{% if error %}
    <div class="error">{{ error }}</div>
{% endif %}

<form method="post">
    {% csrf_token %}

    <div>
        <label>اسم المستخدم:</label>
        <input type="text" name="username" required>
    </div>

    <div>
        <label>كلمة المرور:</label>
        <input type="password" name="password" required>
    </div>

    <button type="submit">دخول</button>
</form>
```

### عرض تسجيل الخروج

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

### استخدام عروض Django المدمجة

**يوفر Django عروض مصادقة جاهزة:**

```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
```

### الوصول إلى المستخدم الحالي

**في العروض:**
```python
def profile_view(request):
    user = request.user

    if user.is_authenticated:
        username = user.username
        email = user.email
    else:
        # مستخدم مجهول
        pass
```

**في القوالب:**
```html
{% if user.is_authenticated %}
    <p>مرحبًا، {{ user.username }}!</p>
    <a href="{% url 'logout' %}">تسجيل الخروج</a>
{% else %}
    <a href="{% url 'login' %}">تسجيل الدخول</a>
{% endif %}
```

---

## 9. تسجيل المستخدم

### نموذج التسجيل

```python
# forms.py
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label="تأكيد كلمة المرور"
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("اسم المستخدم موجود بالفعل")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("كلمتا المرور غير متطابقتين")

        return cleaned_data
```

### عرض التسجيل

```python
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            # إنشاء المستخدم
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # تسجيل دخوله مباشرة
            login(request, user)

            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
```

### استخدام UserCreationForm

**يوفر Django نموذجًا مدمجًا:**

```python
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
```

### UserCreationForm مخصص

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
```

---

## 10. حماية العروض

### مُزخرف @login_required

**طلب المصادقة للعروض:**

```python
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    # يمكن للمستخدمين المسجلين فقط الوصول
    form = PostForm()
    return render(request, 'post_form.html', {'form': form})
```

**مع إعادة توجيه مخصصة:**
```python
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')
```

**في settings.py:**
```python
LOGIN_URL = '/accounts/login/'  # إعادة التوجيه الافتراضية لـ @login_required
LOGIN_REDIRECT_URL = '/dashboard/'  # الوجهة بعد تسجيل الدخول
LOGOUT_REDIRECT_URL = '/'  # الوجهة بعد تسجيل الخروج
```

### التحقق من الصلاحيات في العروض

```python
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # المؤلف فقط يمكنه التعديل
    if post.author != request.user:
        return redirect('post_detail', post_id=post_id)

    # ... بقية العرض
```

### حماية عناوين URL

```python
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create/', login_required(views.post_create), name='post_create'),
]
```

---

## 11. العروض المبنية على الفئات

### لماذا العروض المبنية على الفئات؟

**عروض مبنية على دوال:**
```python
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
```

**عروض مبنية على فئات (CBV):**
```python
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
```

**المزايا:**
- كود أقل
- قابل لإعادة الاستخدام
- وظائف مدمجة
- منظّم

### ListView

**عرض قائمة من الكائنات:**

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10  # ترقيم الصفحات (اختياري)
```

**URL:**
```python
from .views import PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
]
```

**القالب (post_list.html):**
```html
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
```

### DetailView

**عرض كائن واحد:**

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
```

**URL:**
```python
path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
```

### CreateView

**نموذج لإنشاء كائن:**

```python
from django.views.generic import CreateView
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

### UpdateView

**نموذج لتعديل كائن:**

```python
from django.views.generic import UpdateView

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
```

### DeleteView

**تأكيد الحذف:**

```python
from django.views.generic import DeleteView

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
```

**القالب (post_confirm_delete.html):**
```html
<form method="post">
    {% csrf_token %}
    <p>هل أنت متأكد من حذف "{{ post.title }}"؟</p>
    <button type="submit">نعم، احذف</button>
    <a href="{% url 'post_detail' post.pk %}">إلغاء</a>
</form>
```

### LoginRequiredMixin

**حماية العروض المبنية على الفئات:**

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = '/login/'
```

---

## 12. إطار عمل الرسائل

### ما هو إطار عمل الرسائل؟

عرض إشعارات مرة واحدة للمستخدمين (نجاح، خطأ، تحذير، معلومات).

**الإعداد (مُفعَّل بالفعل افتراضيًا):**
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.messages',  # موجود بالفعل
]

MIDDLEWARE = [
    'django.contrib.messages.middleware.MessageMiddleware',  # موجود بالفعل
]
```

### إضافة الرسائل

```python
from django.contrib import messages

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'تم إنشاء المنشور بنجاح!')
            return redirect('post_list')
        else:
            messages.error(request, 'يرجى تصحيح الأخطاء أدناه.')
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})
```

### مستويات الرسائل

```python
from django.contrib import messages

messages.debug(request, 'معلومات تصحيح')
messages.info(request, 'للمعلومة')
messages.success(request, 'نجاح!')
messages.warning(request, 'تحذير!')
messages.error(request, 'حدث خطأ')
```

### عرض الرسائل

**base.html:**
```html
{% if messages %}
    <div class="messages">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    </div>
{% endif %}
```

**مع Bootstrap:**
```html
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="close" data-dismiss="alert">
                <span>&times;</span>
            </button>
        </div>
    {% endfor %}
{% endif %}
```

---

## 13. مشروع مصغّر: مدونة مع مصادقة

### نظرة عامة على المشروع

بناء مدونة متكاملة تتضمن:
- تسجيل المستخدمين وتسجيل الدخول
- إنشاء/تعديل المنشورات (للمستخدمين المسجلين فقط)
- عرض المنشورات (للجميع)
- رسائل للتغذية الراجعة

### الخطوة 1: النماذج (Models)

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
```

### الخطوة 2: النماذج (Forms)

```python
# blog/forms.py
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

### الخطوة 3: العروض (Views)

```python
# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm, RegisterForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'تم إنشاء المنشور بنجاح!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, 'يمكنك تعديل منشوراتك فقط.')
        return redirect('post_detail', post_id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث المنشور بنجاح!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'post': post})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'مرحبًا! تم إنشاء حسابك بنجاح.')
            return redirect('post_list')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'مرحبًا بعودتك، {username}!')
            return redirect('post_list')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'تم تسجيل خروجك.')
    return redirect('post_list')
```

### الخطوة 4: عناوين URL

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

### الخطوة 5: القوالب

**base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}مدونتي{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'post_list' %}">الرئيسية</a>
        {% if user.is_authenticated %}
            <a href="{% url 'post_create' %}">منشور جديد</a>
            <span>مرحبًا، {{ user.username }}</span>
            <a href="{% url 'logout' %}">تسجيل الخروج</a>
        {% else %}
            <a href="{% url 'login' %}">تسجيل الدخول</a>
            <a href="{% url 'register' %}">إنشاء حساب</a>
        {% endif %}
    </nav>

    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}

    {% block content %}{% endblock %}
</body>
</html>
```

**post_list.html:**
```html
{% extends 'base.html' %}

{% block content %}
    <h1>جميع المنشورات</h1>
    {% for post in posts %}
        <article>
            <h2><a href="{% url 'post_detail' post.id %}">{{ post.title }}</a></h2>
            <p>بقلم {{ post.author.username }} في {{ post.created_at|date:"j F Y" }}</p>
            <p>{{ post.content|truncatewords:30 }}</p>
        </article>
    {% empty %}
        <p>لا توجد منشورات حتى الآن.</p>
    {% endfor %}
{% endblock %}
```

---

## ملخص

هذا الأسبوع تعلّمت:

1. **النماذج** - نماذج Django و ModelForms
2. **التحقق** - التحقق المدمج والمخصص
3. **معالجة النماذج** - التعامل مع طلبات GET و POST
4. **CSRF** - حماية تزوير الطلبات عبر المواقع
5. **المصادقة** - تسجيل دخول/خروج المستخدمين وتسجيلهم
6. **الحماية** - مُزخرف @login_required
7. **العروض المبنية على الفئات** - ListView، DetailView، CreateView، UpdateView، DeleteView
8. **الرسائل** - نظام التغذية الراجعة للمستخدم

### النقاط الأساسية

- استخدم دائمًا `{% csrf_token %}` في نماذج POST
- استخدم ModelForm للنماذج المرتبطة بالنماذج (Models)
- تحقق من البيانات قبل معالجتها
- لا تخزن كلمات المرور بنص صريح أبدًا
- احمِ العروض الحساسة بـ @login_required
- استخدم الرسائل للتغذية الراجعة للمستخدم

### معاينة الأسبوع القادم

الأسبوع السابع سيغطي:
- واجهات برمجة التطبيقات REST
- إطار عمل Django REST
- JavaScript و AJAX
- بناء نقاط نهاية API
- استهلاك APIs

---

## موارد إضافية

- [توثيق نماذج Django](https://docs.djangoproject.com/en/stable/topics/forms/)
- [توثيق مصادقة Django](https://docs.djangoproject.com/en/stable/topics/auth/)
- [العروض المبنية على الفئات](https://docs.djangoproject.com/en/stable/topics/class-based-views/)
- [إطار عمل الرسائل](https://docs.djangoproject.com/en/stable/ref/contrib/messages/)
