# تعليمات إعداد الأسبوع الثاني

دليل شامل لإعداد البيئات الافتراضية لـ Python وإدارة الحزم للأسبوع الثاني.

---

## جدول المحتويات

1. [نظرة عامة](#نظرة-عامة)
2. [إعداد البيئة الافتراضية](#إعداد-البيئة-الافتراضية)
3. [تثبيت الحزم باستخدام pip](#تثبيت-الحزم-باستخدام-pip)
4. [إنشاء requirements.txt](#إنشاء-requirementstxt)
5. [المشاكل الشائعة واستكشاف الأخطاء](#المشاكل-الشائعة-واستكشاف-الأخطاء)
6. [اختبار الإعداد](#اختبار-الإعداد)

---

## نظرة عامة

### ما ستتعلمه في إعداد الأسبوع الثاني

**البيئات الافتراضية**: بيئات Python معزولة لمشاريعك
- الحفاظ على التبعيات منظمة
- تجنب تعارضات الحزم
- جعل المشاريع قابلة للنقل

**pip**: مثبت حزم Python
- تثبيت الحزم من الجهات الخارجية
- إدارة إصدارات الحزم
- إنشاء ملفات المتطلبات

**الوقت الإجمالي**: 20-30 دقيقة

### المتطلبات الأساسية

قبل بدء إعداد الأسبوع الثاني، يجب أن يكون لديك:
- [ ] Python 3.11+ مثبت
- [ ] VS Code مثبت
- [ ] إعداد الأسبوع الأول مكتمل
- [ ] معرفة أساسية بالطرفية/موجه الأوامر

---

## إعداد البيئة الافتراضية

### ما هي البيئة الافتراضية؟

فكر في البيئة الافتراضية كمساحة عمل منفصلة لكل مشروع:

```
جهاز الكمبيوتر الخاص بك
├── المشروع A (venv)
│   ├── Python 3.11
│   └── الحزم: Django 4.2, requests
│
├── المشروع B (venv)
│   ├── Python 3.11
│   └── الحزم: Flask 2.3, numpy
│
└── Python النظام
    └── الحزم الأساسية
```

كل مشروع له مجموعة معزولة خاصة به من الحزم دون التدخل مع الآخرين.

---

### إنشاء بيئة افتراضية

#### Windows

**الخطوة 1: فتح الطرفية في VS Code**
1. افتح VS Code
2. اضغط `Ctrl+` ` (علامة التنصيص الخلفية) لفتح الطرفية
3. أو: View → Terminal

**الخطوة 2: إنشاء مجلد المشروع**
```bash
# الانتقال إلى حيث تريد المشروع
cd D:\CCDS\repositories\training

# إنشاء مجلد للتمرين
mkdir week-2-practice
cd week-2-practice
```

**الخطوة 3: إنشاء البيئة الافتراضية**
```bash
# إنشاء بيئة افتراضية باسم 'venv'
python -m venv venv
```

هذا ينشئ مجلداً يسمى `venv` مع:
- نسخة من Python
- مدير حزم pip
- دليل حزم معزول

**الخطوة 4: تفعيل البيئة الافتراضية**
```bash
# PowerShell
venv\Scripts\Activate.ps1

# Command Prompt
venv\Scripts\activate.bat
```

**سترى (venv) في طرفيتك:**
```
(venv) PS D:\CCDS\repositories\training\week-2-practice>
```

**الخطوة 5: التحقق من التفعيل**
```bash
# التحقق من موقع Python
where python
# يجب أن يظهر المسار إلى venv\Scripts\python.exe

# التحقق من موقع pip
where pip
# يجب أن يظهر المسار إلى venv\Scripts\pip.exe
```

---

#### macOS/Linux

**الخطوة 1: فتح الطرفية**
1. افتح VS Code
2. اضغط `Cmd+` ` (علامة التنصيص الخلفية)
3. أو: View → Terminal

**الخطوة 2: إنشاء مجلد المشروع**
```bash
# الانتقال إلى مجلد المشاريع
cd ~/Documents

# إنشاء مجلد التمرين
mkdir week-2-practice
cd week-2-practice
```

**الخطوة 3: إنشاء البيئة الافتراضية**
```bash
# إنشاء بيئة افتراضية
python3 -m venv venv
```

**الخطوة 4: تفعيل البيئة الافتراضية**
```bash
source venv/bin/activate
```

**سترى (venv) في طرفيتك:**
```
(venv) user@computer:~/Documents/week-2-practice$
```

**الخطوة 5: التحقق من التفعيل**
```bash
# التحقق من موقع Python
which python
# يجب أن يظهر: .../venv/bin/python

# التحقق من موقع pip
which pip
# يجب أن يظهر: .../venv/bin/pip
```

---

### إلغاء تفعيل البيئة الافتراضية

عندما تنتهي من العمل:

**جميع المنصات**:
```bash
deactivate
```

يختفي بادئة `(venv)` من طرفيتك.

---

### تكامل VS Code

**تكوين VS Code لاستخدام بيئتك الافتراضية:**

1. افتح لوحة الأوامر: `Ctrl+Shift+P` (Windows/Linux) أو `Cmd+Shift+P` (macOS)
2. اكتب: **Python: Select Interpreter**
3. اختر: `Python 3.11.x ('venv': venv)`
4. سيستخدم VS Code الآن هذه البيئة

**سيقوم VS Code تلقائياً بتفعيل venv عند فتح الطرفية!**

---

## تثبيت الحزم باستخدام pip

### ما هو pip؟

pip هو مدير حزم Python - ينزل ويثبت الحزم من [PyPI.org](https://pypi.org/).

### أوامر pip الأساسية

**تأكد من تفعيل بيئتك الافتراضية!**
ابحث عن `(venv)` في طرفيتك.

#### تثبيت الحزم

**تثبيت حزمة:**
```bash
pip install package_name

# مثال
pip install requests
```

**تثبيت إصدار محدد:**
```bash
pip install package_name==version

# مثال
pip install django==4.2.0
```

**تثبيت أحدث إصدار متوافق:**
```bash
pip install package_name>=version

# مثال
pip install numpy>=1.20.0
```

**تثبيت حزم متعددة:**
```bash
pip install package1 package2 package3

# مثال
pip install requests beautifulsoup4 pillow
```

#### عرض الحزم المثبتة

**قائمة بجميع الحزم:**
```bash
pip list
```

الإخراج:
```
Package         Version
--------------- -------
pip             23.2.1
requests        2.31.0
setuptools      68.0.0
```

**عرض تفاصيل الحزمة:**
```bash
pip show package_name

# مثال
pip show requests
```

الإخراج:
```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
License: Apache 2.0
Location: /path/to/venv/lib/python3.11/site-packages
Requires: charset-normalizer, idna, urllib3, certifi
```

#### ترقية الحزم

**ترقية حزمة:**
```bash
pip install --upgrade package_name

# مثال
pip install --upgrade requests
```

**ترقية pip نفسه:**
```bash
# Windows
python -m pip install --upgrade pip

# macOS/Linux
python3 -m pip install --upgrade pip
```

#### إلغاء تثبيت الحزم

**إلغاء تثبيت حزمة:**
```bash
pip uninstall package_name

# مثال
pip uninstall requests
```

سيُطلب منك التأكيد:
```
Found existing installation: requests 2.31.0
Uninstalling requests-2.31.0:
  Proceed (Y/n)? Y
```

---

## إنشاء requirements.txt

### ما هو requirements.txt؟

ملف يسرد جميع الحزم التي يحتاجها مشروعك:

```
requests==2.31.0
beautifulsoup4==4.12.2
pillow==10.0.0
```

الفوائد:
- مشاركة تبعيات المشروع مع الآخرين
- إعادة إنشاء البيئة على جهاز كمبيوتر آخر
- تتبع الإصدارات المحددة المستخدمة

### إنشاء requirements.txt

**الطريقة 1: تلقائي (موصى به)**

بعد تثبيت جميع حزمك:
```bash
pip freeze > requirements.txt
```

هذا ينشئ ملفاً بجميع الحزم والإصدارات المثبتة.

**الطريقة 2: يدوي**

إنشاء ملف `requirements.txt` يدوياً:
```
# استخراج الويب
requests==2.31.0
beautifulsoup4==4.12.2

# معالجة الصور
pillow==10.0.0

# تحليل البيانات
pandas==2.0.3
numpy==1.25.0
```

التعليقات مع `#` تساعد في تنظيم الحزم.

### التثبيت من requirements.txt

**على جهاز كمبيوتر آخر أو بيئة جديدة:**

```bash
# أولاً، إنشاء وتفعيل البيئة الافتراضية
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# ثم تثبيت جميع الحزم
pip install -r requirements.txt
```

هذا يثبت جميع الحزم المدرجة في الملف بالإصدارات المحددة.

---

## الحزم الشائعة للأسبوع الثاني

بينما يركز الأسبوع الثاني على ميزات Python المدمجة، إليك بعض الحزم التي قد تستكشفها:

```bash
# لتحسينات المشروع الصغير
pip install colorama  # نص طرفية ملون
pip install prettytable  # جداول جميلة في الطرفية
```

**مثال: استخدام colorama**
```python
from colorama import Fore, Style, init

# تهيئة colorama
init()

# إخراج ملون
print(Fore.GREEN + "Task completed!" + Style.RESET_ALL)
print(Fore.RED + "Error occurred!" + Style.RESET_ALL)
```

**مثال: استخدام prettytable**
```python
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
table.add_row(["Ahmed", 25, "Cairo"])
table.add_row(["Sara", 22, "Dubai"])
print(table)
```

الإخراج:
```
+--------+-----+-------+
|  Name  | Age |  City |
+--------+-----+-------+
| Ahmed  |  25 | Cairo |
|  Sara  |  22 | Dubai |
+--------+-----+-------+
```

---

## المشاكل الشائعة واستكشاف الأخطاء

### المشكلة 1: "venv غير معروف"

**المشكلة**: `python -m venv venv` لا يعمل

**الحل**:
```bash
# Windows - استخدم المسار الكامل
C:\Python311\python.exe -m venv venv

# أو تحقق من تثبيت Python
where python

# macOS/Linux - استخدم python3
python3 -m venv venv
```

---

### المشكلة 2: سكريبت التفعيل لا يعمل (Windows PowerShell)

**المشكلة**:
```
venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled
```

**الحل**:

**الخيار A: استخدم Command Prompt بدلاً من ذلك**
1. أغلق PowerShell
2. افتح Command Prompt
3. استخدم: `venv\Scripts\activate.bat`

**الخيار B: تغيير سياسة تنفيذ PowerShell**
```powershell
# شغّل PowerShell كمسؤول
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# ثم حاول التفعيل مرة أخرى
venv\Scripts\Activate.ps1
```

---

### المشكلة 3: pip غير موجود

**المشكلة**: `pip: command not found` أو `pip is not recognized`

**الحل**:

**تحقق مما إذا كان pip مثبتاً:**
```bash
# Windows
python -m pip --version

# macOS/Linux
python3 -m pip --version
```

**إذا كان pip مفقوداً، أعد التثبيت:**
```bash
# قم بتنزيل get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# ثبّت pip
python get-pip.py
```

---

### المشكلة 4: الإذن مرفوض (macOS/Linux)

**المشكلة**: أخطاء الأذونات عند تثبيت الحزم

**الحل**:

**لا تستخدم sudo مع pip في البيئات الافتراضية!**

بدلاً من ذلك:
```bash
# تأكد من تفعيل البيئة الافتراضية
source venv/bin/activate

# ثم ثبّت بشكل طبيعي
pip install package_name
```

إذا كنت لا تزال تواجه مشاكل:
```bash
# تحقق من ملكية venv
ls -la venv

# إذا كان مملوكاً لـ root، أعد إنشاء venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

---

### المشكلة 5: فشل تثبيت الحزمة

**المشكلة**: خطأ في تثبيت حزمة

**الحلول الشائعة**:

**1. ترقية pip أولاً:**
```bash
python -m pip install --upgrade pip
```

**2. مسح ذاكرة التخزين المؤقت لـ pip:**
```bash
pip cache purge
```

**3. التثبيت مع --no-cache-dir:**
```bash
pip install --no-cache-dir package_name
```

**4. تحقق من توافق إصدار Python:**
- بعض الحزم تتطلب إصدارات محددة من Python
- تحقق من توثيق الحزمة على PyPI.org

---

### المشكلة 6: استخدام Python/pip الخطأ

**المشكلة**: ثبّتت الحزمة لكن لا يمكن استيرادها

**الحل**:

**تحقق من أي Python قيد التشغيل:**
```bash
# في الطرفية
python --version
which python  # macOS/Linux
where python  # Windows

# في Python
import sys
print(sys.executable)
```

**تأكد من:**
- تفعيل البيئة الافتراضية `(venv)` يظهر في الطرفية
- VS Code يستخدم المفسر الصحيح
- كلاً من Python و pip من نفس venv

---

### المشكلة 7: فشل تثبيت requirements.txt

**المشكلة**: بعض الحزم تفشل عند التثبيت من requirements.txt

**الحل**:

**ثبّت الحزم واحدة تلو الأخرى للعثور على المشكلة:**
```bash
# بدلاً من
pip install -r requirements.txt

# افعل هذا
pip install package1
pip install package2
# إلخ.
```

**أو ثبّت بدون قيود الإصدار أولاً:**
```bash
# عدّل requirements.txt لإزالة أرقام الإصدار
requests
beautifulsoup4
pillow

# ثم ثبّت
pip install -r requirements.txt
```

---

## اختبار الإعداد

### التحقق من البيئة الافتراضية

**الاختبار 1: التحقق من التفعيل**
```bash
# Windows
where python
# يجب أن يظهر: ...\venv\Scripts\python.exe

# macOS/Linux
which python
# يجب أن يظهر: .../venv/bin/python
```

**الاختبار 2: التحقق من العزل**
```bash
# قائمة الحزم (يجب أن تكون قليلة)
pip list
# يجب أن يظهر فقط: pip, setuptools, (ربما wheel)
```

**الاختبار 3: اختبار التثبيت والاستيراد**
```bash
# ثبّت حزمة اختبار
pip install requests

# شغّل Python
python

# حاول الاستيراد
>>> import requests
>>> print(requests.__version__)
2.31.0
>>> exit()
```

إذا عملت جميعها بدون أخطاء، إعدادك صحيح!

---

### إنشاء مشروع اختبار

**اختبار سير العمل الكامل:**

```bash
# 1. إنشاء مجلد المشروع
mkdir test-project
cd test-project

# 2. إنشاء بيئة افتراضية
python -m venv venv

# 3. تفعيل
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 4. تثبيت الحزم
pip install requests colorama

# 5. إنشاء requirements.txt
pip freeze > requirements.txt

# 6. إنشاء سكريبت اختبار
# أنشئ test.py مع:
```

**test.py:**
```python
import requests
from colorama import Fore, Style, init

init()

print(Fore.GREEN + "Testing virtual environment..." + Style.RESET_ALL)

response = requests.get("https://api.github.com")
print(f"GitHub API Status: {response.status_code}")

print(Fore.GREEN + "All tests passed!" + Style.RESET_ALL)
```

**شغّل الاختبار:**
```bash
python test.py
```

**الإخراج المتوقع:**
```
Testing virtual environment...
GitHub API Status: 200
All tests passed!
```

إذا رأيت هذا، كل شيء يعمل!

---

## أفضل الممارسات

### إرشادات البيئة الافتراضية

**افعل:**
- ✓ أنشئ venv جديداً لكل مشروع
- ✓ فعّل venv قبل تثبيت الحزم
- ✓ أضف `venv/` إلى `.gitignore`
- ✓ استخدم `requirements.txt` للمشاركة
- ✓ احتفظ بـ venv في مجلد المشروع

**لا تفعل:**
- ✗ تثبيت الحزم عالمياً (بدون venv)
- ✗ رفع مجلد venv إلى Git
- ✗ مشاركة مجلدات venv بين المشاريع
- ✗ نسيان تفعيل venv قبل البرمجة

### إرشادات requirements.txt

**requirements.txt جيد:**
```
# إطار الويب
django==4.2.0

# قاعدة البيانات
psycopg2-binary==2.9.6

# API
djangorestframework==3.14.0

# التطوير
pytest==7.4.0
black==23.7.0
```

**التعليقات تجمع الحزم ذات الصلة**
**أرقام الإصدار تضمن الاتساق**
**منظم وقابل للقراءة**

### بنية المشروع مع Venv

```
my-project/
├── venv/                 # البيئة الافتراضية (لا ترفع)
├── src/                  # كود المصدر
│   ├── __init__.py
│   └── main.py
├── tests/                # ملفات الاختبار
│   └── test_main.py
├── requirements.txt      # التبعيات (ارفع هذا)
├── .gitignore           # تجاهل مجلد venv
└── README.md            # توثيق المشروع
```

**ملف .gitignore:**
```
# البيئة الافتراضية
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDE
.vscode/
.idea/
*.swp
```

---

## مرجع سريع

### الأوامر الشائعة

**الإنشاء والتفعيل:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**إدارة الحزم:**
```bash
pip install package_name          # تثبيت
pip install -r requirements.txt   # تثبيت من ملف
pip list                          # قائمة المثبتة
pip freeze > requirements.txt     # حفظ التبعيات
pip uninstall package_name        # إزالة
```

**إلغاء التفعيل:**
```bash
deactivate
```

---

## الخطوات التالية

بعد إكمال إعداد الأسبوع الثاني:

1. ✓ البيئة الافتراضية منشأة
2. ✓ pip يعمل بشكل صحيح
3. ✓ يمكن تثبيت الحزم
4. ✓ يمكن إنشاء requirements.txt
5. → تدرب مع تمارين الأسبوع الثاني!
6. → ابنِ مشروع قائمة المهام الصغير
7. → جرب حزم مختلفة

---

## تمارين تطبيق الأسبوع الثاني

**جرب هذه للتحقق من إعدادك:**

**التمرين 1: ممارسة البيئة**
```bash
# إنشاء مشروع جديد
mkdir calculator-project
cd calculator-project

# إنشاء وتفعيل venv
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# التحقق من العزل
pip list
```

**التمرين 2: ممارسة الحزمة**
```bash
# تثبيت بعض الحزم
pip install colorama prettytable

# إنشاء requirements.txt
pip freeze > requirements.txt

# التحقق من محتوى الملف
cat requirements.txt  # macOS/Linux
type requirements.txt  # Windows
```

**التمرين 3: إعادة إنشاء البيئة**
```bash
# إلغاء تفعيل البيئة الحالية
deactivate

# حذف venv
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# إنشاء venv جديد
python -m venv venv
venv\Scripts\activate

# التثبيت من المتطلبات
pip install -r requirements.txt

# التحقق من تثبيت الحزم
pip list
```

---

## الحصول على المساعدة

إذا واجهت مشاكل:

1. **اقرأ رسائل الخطأ بعناية** - غالباً ما تخبرك بما هو الخطأ
2. **تحقق من التفعيل** - هل `(venv)` يظهر في الطرفية؟
3. **تحقق من إصدار Python** - `python --version`
4. **ابحث عن الخطأ في Google** - من المحتمل أن يكون شخص آخر واجه نفس المشكلة
5. **تحقق من التوثيق الرسمي**:
   - venv: [docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
   - pip: [pip.pypa.io](https://pip.pypa.io/)
6. **اسأل مدربك** - هم هنا للمساعدة!

---

## موارد إضافية

**التوثيق الرسمي:**
- Python venv: [docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
- توثيق pip: [pip.pypa.io/en/stable](https://pip.pypa.io/en/stable/)
- PyPI (فهرس الحزم): [pypi.org](https://pypi.org/)

**دروس الفيديو:**
- "Python Virtual Environments" - Corey Schafer
- "pip Tutorial" - Tech With Tim
- "requirements.txt" - Real Python

**المقالات:**
- Real Python - البيئات الافتراضية
- Python.org - تثبيت الحزم
- pip - دليل المستخدم

---

**تهانينا على إعداد بيئة تطوير Python الخاصة بك!** أنت الآن جاهز للعمل على مشاريع معزولة مع تبعيات نظيفة. هذه مهارة احترافية ستستخدمها طوال مسيرتك البرمجية!
