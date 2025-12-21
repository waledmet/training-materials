# تعليمات الإعداد للأسبوع الأول

دليل شامل لإعداد بيئة التطوير الخاصة بك لبرمجة Python.

---

## جدول المحتويات

1. [نظرة عامة](#نظرة-عامة)
2. [تثبيت Python](#تثبيت-python)
3. [تثبيت VS Code](#تثبيت-vs-code)
4. [تثبيت Git](#تثبيت-git)
5. [إنشاء حساب GitHub](#إنشاء-حساب-github)
6. [التحقق من التثبيت](#التحقق-من-التثبيت)
7. [حل المشكلات](#حل-المشكلات)

---

## نظرة عامة

### ما الذي ستقوم بتثبيته

**Python**: لغة البرمجة التي سنستخدمها
- الإصدار: 3.11 أو أعلى
- الوقت: 10-15 دقيقة

**VS Code**: محرر الأكواد
- أحدث إصدار
- الوقت: 5-10 دقائق

**Git**: نظام التحكم في الإصدار
- أحدث إصدار
- الوقت: 5-10 دقائق

**GitHub**: تخزين الأكواد عبر الإنترنت (إنشاء حساب)
- الوقت: 5 دقائق

**الوقت الإجمالي**: 30-45 دقيقة

### متطلبات النظام

**الحد الأدنى من المتطلبات**:
- **نظام التشغيل**: Windows 10+, macOS 10.14+, أو Linux (Ubuntu 18.04+)
- **الذاكرة RAM**: 4GB
- **مساحة القرص**: 10GB متاحة
- **الإنترنت**: اتصال مستقر للتنزيلات

---

## تثبيت Python

### Windows

#### الخطوة 1: تنزيل Python

1. افتح متصفح الويب الخاص بك
2. انتقل إلى [python.org/downloads](https://www.python.org/downloads/)
3. انقر على الزر الأصفر **"Download Python 3.x.x"**
4. احفظ ملف التثبيت (مثل `python-3.11.5-amd64.exe`)

#### الخطوة 2: تشغيل المثبت

1. ابحث عن ملف التثبيت المنزل وانقر عليه نقراً مزدوجاً
2. **مهم جداً**: ضع علامة في مربع **"Add Python to PATH"** في الأسفل
3. انقر على **"Install Now"**
4. انتظر حتى يكتمل التثبيت
5. انقر على **"Close"**

#### الخطوة 3: التحقق من التثبيت

1. اضغط `Win + R`
2. اكتب `cmd` واضغط Enter
3. في موجه الأوامر، اكتب:
```bash
python --version
```
4. يجب أن ترى: `Python 3.11.x` أو ما شابه
5. تحقق أيضاً من pip:
```bash
pip --version
```

إذا رأيت أرقام الإصدار، فقد انتهيت!

**نقاط التحقق من لقطات الشاشة**:
- [ ] تم وضع علامة على "Add Python to PATH"
- [ ] رسالة نجاح التثبيت
- [ ] أمر الإصدار يُظهر Python 3.11+

---

### macOS

#### الخطوة 1: التحقق من تثبيت Python مسبقاً

1. افتح **Terminal** (Applications → Utilities → Terminal)
2. اكتب:
```bash
python3 --version
```
3. إذا رأيت Python 3.11+، انتقل إلى [تثبيت VS Code](#تثبيت-vs-code)

#### الخطوة 2: التثبيت باستخدام المثبت الرسمي

**الخيار أ: المثبت الرسمي لـ Python**

1. انتقل إلى [python.org/downloads](https://www.python.org/downloads/)
2. نزّل مثبت macOS (مثل `python-3.11.5-macos11.pkg`)
3. انقر نقراً مزدوجاً على الملف المنزل
4. اتبع معالج التثبيت
5. انقر "Continue" → "Agree" → "Install"
6. أدخل كلمة المرور الخاصة بك عند الطلب
7. انقر "Close"

**الخيار ب: استخدام Homebrew (موصى به للمطورين)**

1. افتح Terminal
2. ثبّت Homebrew إذا لم يكن لديك:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. ثبّت Python:
```bash
brew install python3
```

#### الخطوة 3: التحقق من التثبيت

```bash
python3 --version
pip3 --version
```

**ملاحظة**: على macOS، استخدم `python3` و `pip3` بدلاً من `python` و `pip`.

---

### Linux (Ubuntu/Debian)

#### الخطوة 1: تحديث قائمة الحزم

افتح Terminal وقم بتشغيل:
```bash
sudo apt update
```

#### الخطوة 2: تثبيت Python

```bash
sudo apt install python3 python3-pip python3-venv
```

أدخل كلمة المرور الخاصة بك عند الطلب.

#### الخطوة 3: التحقق من التثبيت

```bash
python3 --version
pip3 --version
```

**لتوزيعات Linux الأخرى**:

**Fedora/CentOS/RHEL**:
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux**:
```bash
sudo pacman -S python python-pip
```

---

## تثبيت VS Code

### Windows

#### الخطوة 1: تنزيل VS Code

1. انتقل إلى [code.visualstudio.com](https://code.visualstudio.com/)
2. انقر على **"Download for Windows"**
3. احفظ المثبت (مثل `VSCodeUserSetup-x64-1.x.x.exe`)

#### الخطوة 2: تشغيل المثبت

1. انقر نقراً مزدوجاً على المثبت المنزل
2. اقبل اتفاقية الترخيص
3. **مهم**: ضع علامة على هذه المربعات:
   - ✓ Add "Open with Code" action to Windows Explorer file context menu
   - ✓ Add "Open with Code" action to Windows Explorer directory context menu
   - ✓ Add to PATH
4. انقر "Next" → "Install"
5. انقر "Finish"

#### الخطوة 3: تشغيل VS Code

1. اضغط مفتاح `Win`
2. اكتب "Visual Studio Code"
3. انقر للفتح

---

### macOS

#### الخطوة 1: تنزيل VS Code

1. انتقل إلى [code.visualstudio.com](https://code.visualstudio.com/)
2. انقر على **"Download for Mac"**
3. احفظ الملف (`VSCode-darwin-universal.zip`)

#### الخطوة 2: التثبيت

1. افتح مجلد Downloads
2. انقر نقراً مزدوجاً على ملف ZIP (إذا لم يتم استخراجه بالفعل)
3. اسحب **Visual Studio Code.app** إلى مجلد **Applications**

#### الخطوة 3: تشغيل VS Code

1. افتح مجلد **Applications**
2. انقر نقراً مزدوجاً على **Visual Studio Code**
3. إذا رأيت تحذيراً أمنياً، انقر **"Open"**

---

### Linux

#### استخدام مدير الحزم (Ubuntu/Debian)

```bash
# تنزيل وتثبيت المفتاح
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

# إضافة المستودع
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

# التثبيت
sudo apt update
sudo apt install code
```

أو نزّل حزمة `.deb` من [code.visualstudio.com](https://code.visualstudio.com/) وثبّتها بـ:
```bash
sudo dpkg -i <filename>.deb
```

---

## إعداد VS Code لـ Python

### تثبيت إضافة Python

1. افتح VS Code
2. انقر على أيقونة **Extensions** (الشريط الجانبي الأيسر) أو اضغط `Ctrl+Shift+X` (Windows/Linux) أو `Cmd+Shift+X` (macOS)
3. في مربع البحث، اكتب: **Python**
4. ابحث عن **"Python"** من Microsoft (يجب أن يكون النتيجة الأولى)
5. انقر على **"Install"**

### إضافات إضافية موصى بها

أثناء وجودك في Extensions، قم أيضاً بتثبيت:

1. **Pylance** (من Microsoft)
   - IntelliSense أفضل لـ Python
   - عادةً ما يتم تثبيته مع إضافة Python

2. **Python Indent** (من Kevin Rose)
   - يساعد في المسافات البادئة في Python

3. **Code Runner** (من Jun Han)
   - تشغيل الكود بنقرة واحدة

### إعداد مسار Python

1. اضغط `Ctrl+Shift+P` (Windows/Linux) أو `Cmd+Shift+P` (macOS)
2. اكتب: **Python: Select Interpreter**
3. اختر إصدار Python الذي ثبّته

---

## تثبيت Git

### Windows

#### الخطوة 1: تنزيل Git

1. انتقل إلى [git-scm.com](https://git-scm.com/)
2. انقر على **"Download for Windows"**
3. احفظ المثبت (مثل `Git-2.x.x-64-bit.exe`)

#### الخطوة 2: تشغيل المثبت

1. انقر نقراً مزدوجاً على المثبت
2. استخدم الخيارات الافتراضية (فقط استمر في النقر على "Next")
3. **اختيارات مهمة**:
   - المحرر الافتراضي: اختر "Use Visual Studio Code as Git's default editor"
   - بيئة PATH: "Git from the command line and also from 3rd-party software"
   - تحويلات نهاية السطر: "Checkout Windows-style, commit Unix-style"
4. انقر "Install"
5. انقر "Finish"

#### الخطوة 3: التحقق من التثبيت

1. افتح Command Prompt (Win + R → اكتب `cmd`)
2. اكتب:
```bash
git --version
```
3. يجب أن ترى: `git version 2.x.x`

---

### macOS

#### الخيار أ: استخدام Homebrew (موصى به)

```bash
brew install git
```

#### الخيار ب: استخدام المثبت الرسمي

1. انتقل إلى [git-scm.com](https://git-scm.com/)
2. نزّل مثبت macOS
3. اتبع خطوات التثبيت

#### الخطوة 3: التحقق من التثبيت

```bash
git --version
```

---

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

التحقق:
```bash
git --version
```

---

## إعداد Git

بعد تثبيت Git، قم بإعداده بمعلوماتك:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

مثال:
```bash
git config --global user.name "Ahmed Mohammed"
git config --global user.email "ahmed.mohammed@example.com"
```

التحقق من الإعداد:
```bash
git config --list
```

---

## إنشاء حساب GitHub

### الخطوة 1: التسجيل

1. انتقل إلى [github.com](https://github.com/)
2. انقر **"Sign up"** (أعلى اليمين)
3. أدخل عنوان بريدك الإلكتروني
4. انقر **"Continue"**
5. أنشئ كلمة مرور
6. اختر اسم مستخدم (أحرف صغيرة، يمكن أن يتضمن أرقاماً وواصلات)
7. أكمل لغز التحقق
8. انقر **"Create account"**

### الخطوة 2: التحقق من البريد الإلكتروني

1. تحقق من صندوق الوارد لبريدك الإلكتروني
2. ابحث عن بريد إلكتروني من GitHub
3. انقر على رابط التحقق

### الخطوة 3: إكمال الإعداد

1. أجب على أسئلة الإعداد الأولي (أو تخطّها)
2. اختر الخطة المجانية (Free plan)
3. أكمل الإعداد

### الخطوة 4: اختياري - إعداد مفاتيح SSH

مفاتيح SSH تجعل من الأسهل دفع/سحب الكود دون إدخال كلمة المرور في كل مرة.

#### إنشاء مفتاح SSH

**Windows/macOS/Linux**:
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

اضغط Enter لقبول الموقع الافتراضي.
اضغط Enter مرتين لعدم وجود عبارة مرور (أو أنشئ واحدة لمزيد من الأمان).

#### إضافة مفتاح SSH إلى GitHub

1. انسخ مفتاحك العام:

**Windows**:
```bash
type %USERPROFILE%\.ssh\id_ed25519.pub
```

**macOS/Linux**:
```bash
cat ~/.ssh/id_ed25519.pub
```

2. انتقل إلى GitHub → Settings (أيقونة الملف الشخصي → Settings)
3. انقر **"SSH and GPG keys"** (الشريط الجانبي الأيسر)
4. انقر **"New SSH key"**
5. العنوان: "My Computer" (أو أي اسم)
6. الصق المفتاح في حقل "Key"
7. انقر **"Add SSH key"**

---

## التحقق من التثبيت

### قائمة التحقق الكاملة

افتح طرفية/موجه أوامر جديداً وقم بتشغيل هذه الأوامر:

```bash
# Python
python --version
# يجب أن يُظهر: Python 3.11.x أو أعلى

# Pip
pip --version
# يجب أن يُظهر: pip 23.x.x أو ما شابه

# Git
git --version
# يجب أن يُظهر: git version 2.x.x

# VS Code (من سطر الأوامر)
code --version
# يجب أن يُظهر رقم الإصدار
```

**على macOS/Linux**، استخدم `python3` و `pip3`:
```bash
python3 --version
pip3 --version
```

### إنشاء مشروع اختبار

1. أنشئ مجلداً يسمى `test-python`
2. افتح VS Code
3. File → Open Folder → اختر `test-python`
4. أنشئ ملفاً جديداً: `test.py`
5. اكتب:
```python
print("Setup complete!")
print(f"Python version: {__import__('sys').version}")
```
6. انقر بزر الماوس الأيمن في المحرر → "Run Python File in Terminal"
7. يجب أن ترى الإخراج في الطرفية

إذا رأيت الرسالة، تهانينا! اكتمل الإعداد!

---

## حل المشكلات

### مشاكل Python

#### المشكلة: "python is not recognized" (Windows)

**الحل**:
1. إلغاء تثبيت Python
2. إعادة التثبيت و**ضع علامة على "Add Python to PATH"**
3. إعادة تشغيل الكمبيوتر

**أو إضافة إلى PATH يدوياً**:
1. ابحث عن "Environment Variables" في قائمة ابدأ
2. انقر على "Environment Variables"
3. تحت "System variables"، ابحث عن "Path"
4. انقر على "Edit"
5. انقر على "New"
6. أضف: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311`
7. أضف: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts`
8. انقر OK
9. أعد تشغيل Command Prompt

#### المشكلة: رفض الإذن عند تثبيت الحزم

**Windows**: قم بتشغيل Command Prompt كمسؤول
**macOS/Linux**: لا تستخدم `sudo` مع pip؛ استخدم البيئات الافتراضية بدلاً من ذلك

---

### مشاكل VS Code

#### المشكلة: إضافة Python لا تعمل

**الحل**:
1. افتح VS Code
2. اضغط `Ctrl+Shift+P` (أو `Cmd+Shift+P` على macOS)
3. اكتب: **Python: Select Interpreter**
4. اختر تثبيت Python الخاص بك
5. أعد تشغيل VS Code

#### المشكلة: الطرفية لا تفتح في VS Code

**الحل**:
1. View → Terminal (أو `Ctrl+``)
2. إذا كانت لا تزال لا تعمل، أعد تثبيت VS Code

---

### مشاكل Git

#### المشكلة: "git is not recognized"

**Windows**:
1. أعد تثبيت Git
2. تأكد من تحديد "Git from the command line and also from 3rd-party software"
3. أعد تشغيل الكمبيوتر

**macOS/Linux**:
- تحقق من التثبيت: `which git`
- إذا كان فارغاً، أعد تثبيت Git

#### المشكلة: Git يطلب اسم المستخدم/كلمة المرور بشكل متكرر

**الحل**: قم بإعداد مفاتيح SSH (راجع قسم [إنشاء حساب GitHub](#إنشاء-حساب-github))

---

### مشاكل عامة

#### المشكلة: برنامج مكافحة الفيروسات يمنع التثبيت

**الحل**:
- عطّل برنامج مكافحة الفيروسات مؤقتاً
- ثبّت البرنامج
- أعد تفعيل برنامج مكافحة الفيروسات
- أضف مجلدات Python و VS Code و Git إلى استثناءات مكافحة الفيروسات

#### المشكلة: لا توجد مساحة كافية على القرص

**الحل**:
- وفّر ما لا يقل عن 10GB
- احذف الملفات المؤقتة
- إلغاء تثبيت البرامج غير المستخدمة

#### المشكلة: التثبيت معلق/متجمد

**الحل**:
- أغلق جميع البرامج الأخرى
- أعد تشغيل الكمبيوتر
- جرب التثبيت مرة أخرى
- نزّل المثبت مرة أخرى (قد يكون تالفاً)

---

## إعداد ما بعد التثبيت

### إنشاء هيكل مجلد المشروع

أنشئ مجلداً مخصصاً لتعلم Python الخاص بك:

**Windows**:
```bash
mkdir %USERPROFILE%\python-training
cd %USERPROFILE%\python-training
```

**macOS/Linux**:
```bash
mkdir ~/python-training
cd ~/python-training
```

### إعدادات VS Code (اختياري ولكن موصى به)

1. افتح VS Code
2. File → Preferences → Settings (أو `Ctrl+,`)
3. ابحث عن هذه الإعدادات وعدّلها:

**التنسيق عند الحفظ (Format on Save)**:
- ابحث عن: "format on save"
- ضع علامة في المربع

**الحفظ التلقائي (Auto Save)**:
- ابحث عن: "auto save"
- اختر "afterDelay"

**Python Linting**:
- ابحث عن: "python linting enabled"
- ضع علامة في المربع

---

## أوامر مرجعية سريعة

### أساسيات Terminal/Command Prompt

**Windows (Command Prompt)**:
```bash
dir                  # سرد الملفات
cd foldername        # تغيير الدليل
cd ..                # الرجوع مستوى واحد
mkdir foldername     # إنشاء دليل
cls                  # مسح الشاشة
```

**macOS/Linux (Terminal)**:
```bash
ls                   # سرد الملفات
cd foldername        # تغيير الدليل
cd ..                # الرجوع مستوى واحد
mkdir foldername     # إنشاء دليل
clear                # مسح الشاشة
pwd                  # عرض الدليل الحالي
```

### تشغيل Python

**Windows**:
```bash
python script.py
python              # الوضع التفاعلي
```

**macOS/Linux**:
```bash
python3 script.py
python3             # الوضع التفاعلي
```

### أساسيات Git

```bash
git --version       # التحقق من إصدار Git
git config --list   # عرض الإعداد
git status          # التحقق من حالة المستودع
```

---

## الخطوات التالية

بعد إكمال الإعداد:

1. ✓ تحقق من عمل جميع التثبيتات
2. ✓ أنشئ مجلد مشروعك
3. ✓ قم بإعداد إعدادات VS Code
4. ✓ اختبر Python بتشغيل نص بسيط
5. → تابع إلى **lessons.md** لبدء تعلم Python!

---

## الحصول على المساعدة

إذا واجهت مشاكل:

1. **اقرأ رسائل الخطأ بعناية** - غالباً ما تخبرك بما هو الخطأ
2. **ابحث في Google عن الخطأ** - من المحتمل أن شخصاً آخر واجه نفس المشكلة
3. **تحقق من الوثائق الرسمية**:
   - Python: [docs.python.org](https://docs.python.org/)
   - VS Code: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)
   - Git: [git-scm.com/doc](https://git-scm.com/doc)
4. **اسأل مدربك** - هذا هو ما هم موجودون من أجله!

---

## دروس الفيديو (إذا لزم الأمر)

إذا كنت تفضل أدلة الفيديو:

- **تثبيت Python**: ابحث في YouTube عن "Install Python [Your OS] 2024"
- **إعداد VS Code**: ابحث عن "VS Code Python Setup Tutorial"
- **تثبيت Git**: ابحث عن "Install Git [Your OS]"

---

**تهانينا على إكمال الإعداد!** أنت الآن جاهز لبدء رحلتك في برمجة Python!
