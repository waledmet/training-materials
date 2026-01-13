# Week 2 Setup Instructions

Complete guide for setting up Python virtual environments and package management for Week 2.

---

## Table of Contents

1. [Overview](#overview)
2. [Virtual Environment Setup](#virtual-environment-setup)
3. [Package Installation with pip](#package-installation-with-pip)
4. [Creating requirements.txt](#creating-requirementstxt)
5. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
6. [Testing Your Setup](#testing-your-setup)

---

## Overview

### What You'll Learn in Week 2 Setup

**Virtual Environments**: Isolated Python environments for your projects
- Keep dependencies organized
- Avoid package conflicts
- Make projects portable

**pip**: Python's package installer
- Install third-party packages
- Manage package versions
- Create requirements files

**Total Time**: 20-30 minutes

### Prerequisites

Before starting Week 2 setup, you should have:
- [ ] Python 3.11+ installed
- [ ] VS Code installed
- [ ] Week 1 setup completed
- [ ] Basic terminal/command prompt knowledge

---

## Virtual Environment Setup

### What is a Virtual Environment?

Think of a virtual environment as a separate workspace for each project:

```
Your Computer
├── Project A (venv)
│   ├── Python 3.11
│   └── Packages: Django 4.2, requests
│
├── Project B (venv)
│   ├── Python 3.11
│   └── Packages: Flask 2.3, numpy
│
└── System Python
    └── Basic packages
```

Each project has its own isolated set of packages without interfering with others.

---

### Creating a Virtual Environment

#### Windows

**Step 1: Open Terminal in VS Code**
1. Open VS Code
2. Press `Ctrl+` ` (backtick) to open terminal
3. Or: View → Terminal

**Step 2: Create Project Folder**
```bash
# Navigate to where you want the project
cd D:\CCDS\repositories\training

# Create a folder for practice
mkdir week-2-practice
cd week-2-practice
```

**Step 3: Create Virtual Environment**
```bash
# Create virtual environment named 'venv'
python -m venv venv
```

This creates a folder called `venv` with:
- Copy of Python
- pip package manager
- Isolated package directory

**Step 4: Activate Virtual Environment**
```bash
# PowerShell
venv\Scripts\Activate.ps1

# Command Prompt
venv\Scripts\activate.bat
```

**You'll see (venv) in your terminal:**
```
(venv) PS D:\CCDS\repositories\training\week-2-practice>
```

**Step 5: Verify Activation**
```bash
# Check Python location
where python
# Should show path to venv\Scripts\python.exe

# Check pip location
where pip
# Should show path to venv\Scripts\pip.exe
```

---

#### macOS/Linux

**Step 1: Open Terminal**
1. Open VS Code
2. Press `Cmd+` ` (backtick)
3. Or: View → Terminal

**Step 2: Create Project Folder**
```bash
# Navigate to projects folder
cd ~/Documents

# Create practice folder
mkdir week-2-practice
cd week-2-practice
```

**Step 3: Create Virtual Environment**
```bash
# Create virtual environment
python3 -m venv venv
```

**Step 4: Activate Virtual Environment**
```bash
source venv/bin/activate
```

**You'll see (venv) in your terminal:**
```
(venv) user@computer:~/Documents/week-2-practice$
```

**Step 5: Verify Activation**
```bash
# Check Python location
which python
# Should show: .../venv/bin/python

# Check pip location
which pip
# Should show: .../venv/bin/pip
```

---

### Deactivating Virtual Environment

When you're done working:

**All Platforms**:
```bash
deactivate
```

The `(venv)` prefix disappears from your terminal.

---

### VS Code Integration

**Configure VS Code to Use Your Virtual Environment:**

1. Open Command Palette: `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type: **Python: Select Interpreter**
3. Choose: `Python 3.11.x ('venv': venv)`
4. VS Code will now use this environment

**VS Code will automatically activate the venv when you open the terminal!**

---

## Package Installation with pip

### What is pip?

pip is Python's package manager - it downloads and installs packages from [PyPI.org](https://pypi.org/).

### Basic pip Commands

**Make sure your virtual environment is activated!**
Look for `(venv)` in your terminal.

#### Installing Packages

**Install a package:**
```bash
pip install package_name

# Example
pip install requests
```

**Install specific version:**
```bash
pip install package_name==version

# Example
pip install django==4.2.0
```

**Install latest compatible version:**
```bash
pip install package_name>=version

# Example
pip install numpy>=1.20.0
```

**Install multiple packages:**
```bash
pip install package1 package2 package3

# Example
pip install requests beautifulsoup4 pillow
```

#### Viewing Installed Packages

**List all packages:**
```bash
pip list
```

Output:
```
Package         Version
--------------- -------
pip             23.2.1
requests        2.31.0
setuptools      68.0.0
```

**Show package details:**
```bash
pip show package_name

# Example
pip show requests
```

Output:
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

#### Upgrading Packages

**Upgrade a package:**
```bash
pip install --upgrade package_name

# Example
pip install --upgrade requests
```

**Upgrade pip itself:**
```bash
# Windows
python -m pip install --upgrade pip

# macOS/Linux
python3 -m pip install --upgrade pip
```

#### Uninstalling Packages

**Uninstall a package:**
```bash
pip uninstall package_name

# Example
pip uninstall requests
```

You'll be asked to confirm:
```
Found existing installation: requests 2.31.0
Uninstalling requests-2.31.0:
  Proceed (Y/n)? Y
```

---

## Creating requirements.txt

### What is requirements.txt?

A file that lists all packages your project needs:

```
requests==2.31.0
beautifulsoup4==4.12.2
pillow==10.0.0
```

Benefits:
- Share project dependencies with others
- Recreate environment on another computer
- Track exact versions used

### Creating requirements.txt

**Method 1: Automatic (Recommended)**

After installing all your packages:
```bash
pip freeze > requirements.txt
```

This creates a file with all installed packages and versions.

**Method 2: Manual**

Create `requirements.txt` file manually:
```
# Web scraping
requests==2.31.0
beautifulsoup4==4.12.2

# Image processing
pillow==10.0.0

# Data analysis
pandas==2.0.3
numpy==1.25.0
```

Comments with `#` help organize packages.

### Installing from requirements.txt

**On another computer or new environment:**

```bash
# First, create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Then install all packages
pip install -r requirements.txt
```

This installs all packages listed in the file with exact versions.

---

## Common Packages for Week 2

While Week 2 focuses on built-in Python features, here are some packages you might explore:

```bash
# For mini-project enhancements
pip install colorama  # Colored terminal text
pip install prettytable  # Pretty tables in terminal
```

**Example: Using colorama**
```python
from colorama import Fore, Style, init

# Initialize colorama
init()

# Colored output
print(Fore.GREEN + "Task completed!" + Style.RESET_ALL)
print(Fore.RED + "Error occurred!" + Style.RESET_ALL)
```

**Example: Using prettytable**
```python
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]
table.add_row(["Ahmed", 25, "Cairo"])
table.add_row(["Sara", 22, "Dubai"])
print(table)
```

Output:
```
+--------+-----+-------+
|  Name  | Age |  City |
+--------+-----+-------+
| Ahmed  |  25 | Cairo |
|  Sara  |  22 | Dubai |
+--------+-----+-------+
```

---

## Common Issues and Troubleshooting

### Issue 1: "venv is not recognized"

**Problem**: `python -m venv venv` doesn't work

**Solution**:
```bash
# Windows - Use full path
C:\Python311\python.exe -m venv venv

# Or check Python installation
where python

# macOS/Linux - Use python3
python3 -m venv venv
```

---

### Issue 2: Activation Script Not Running (Windows PowerShell)

**Problem**:
```
venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled
```

**Solution**:

**Option A: Use Command Prompt instead**
1. Close PowerShell
2. Open Command Prompt
3. Use: `venv\Scripts\activate.bat`

**Option B: Change PowerShell Execution Policy**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
venv\Scripts\Activate.ps1
```

---

### Issue 3: pip Not Found

**Problem**: `pip: command not found` or `pip is not recognized`

**Solution**:

**Check if pip is installed:**
```bash
# Windows
python -m pip --version

# macOS/Linux
python3 -m pip --version
```

**If pip is missing, reinstall:**
```bash
# Download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

# Install pip
python get-pip.py
```

---

### Issue 4: Permission Denied (macOS/Linux)

**Problem**: Permission errors when installing packages

**Solution**:

**DON'T use sudo with pip in virtual environments!**

Instead:
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Then install normally
pip install package_name
```

If still having issues:
```bash
# Check venv ownership
ls -la venv

# If owned by root, recreate venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
```

---

### Issue 5: Package Install Fails

**Problem**: Error installing a package

**Common Solutions**:

**1. Upgrade pip first:**
```bash
python -m pip install --upgrade pip
```

**2. Clear pip cache:**
```bash
pip cache purge
```

**3. Install with --no-cache-dir:**
```bash
pip install --no-cache-dir package_name
```

**4. Check Python version compatibility:**
- Some packages require specific Python versions
- Check package documentation on PyPI.org

---

### Issue 6: Wrong Python/pip Being Used

**Problem**: Installed package but can't import it

**Solution**:

**Check which Python is running:**
```bash
# In terminal
python --version
which python  # macOS/Linux
where python  # Windows

# In Python
import sys
print(sys.executable)
```

**Make sure:**
- Virtual environment is activated `(venv)` shows in terminal
- VS Code is using correct interpreter
- Both Python and pip are from the same venv

---

### Issue 7: requirements.txt Install Fails

**Problem**: Some packages fail when installing from requirements.txt

**Solution**:

**Install packages one by one to find the problem:**
```bash
# Instead of
pip install -r requirements.txt

# Do this
pip install package1
pip install package2
# etc.
```

**Or install without version constraints first:**
```bash
# Edit requirements.txt to remove version numbers
requests
beautifulsoup4
pillow

# Then install
pip install -r requirements.txt
```

---

## Testing Your Setup

### Verify Virtual Environment

**Test 1: Check Activation**
```bash
# Windows
where python
# Should show: ...\venv\Scripts\python.exe

# macOS/Linux
which python
# Should show: .../venv/bin/python
```

**Test 2: Check Isolation**
```bash
# List packages (should be minimal)
pip list
# Should show only: pip, setuptools, (maybe wheel)
```

**Test 3: Install and Import Test**
```bash
# Install a test package
pip install requests

# Run Python
python

# Try importing
>>> import requests
>>> print(requests.__version__)
2.31.0
>>> exit()
```

If all work without errors, your setup is correct!

---

### Create a Test Project

**Full workflow test:**

```bash
# 1. Create project folder
mkdir test-project
cd test-project

# 2. Create virtual environment
python -m venv venv

# 3. Activate
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# 4. Install packages
pip install requests colorama

# 5. Create requirements.txt
pip freeze > requirements.txt

# 6. Create test script
# Create test.py with:
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

**Run the test:**
```bash
python test.py
```

**Expected output:**
```
Testing virtual environment...
GitHub API Status: 200
All tests passed!
```

If you see this, everything is working!

---

## Best Practices

### Virtual Environment Guidelines

**DO:**
- ✓ Create a new venv for each project
- ✓ Activate venv before installing packages
- ✓ Add `venv/` to `.gitignore`
- ✓ Use `requirements.txt` for sharing
- ✓ Keep venv in project folder

**DON'T:**
- ✗ Install packages globally (without venv)
- ✗ Commit venv folder to Git
- ✗ Share venv folders between projects
- ✗ Forget to activate venv before coding

### requirements.txt Guidelines

**Good requirements.txt:**
```
# Web framework
django==4.2.0

# Database
psycopg2-binary==2.9.6

# API
djangorestframework==3.14.0

# Development
pytest==7.4.0
black==23.7.0
```

**Comments group related packages**
**Version numbers ensure consistency**
**Organized and readable**

### Project Structure with Venv

```
my-project/
├── venv/                 # Virtual environment (don't commit)
├── src/                  # Source code
│   ├── __init__.py
│   └── main.py
├── tests/                # Test files
│   └── test_main.py
├── requirements.txt      # Dependencies (commit this)
├── .gitignore           # Ignore venv folder
└── README.md            # Project documentation
```

**.gitignore file:**
```
# Virtual environment
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

## Quick Reference

### Common Commands

**Create and Activate:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Package Management:**
```bash
pip install package_name          # Install
pip install -r requirements.txt   # Install from file
pip list                          # List installed
pip freeze > requirements.txt     # Save dependencies
pip uninstall package_name        # Remove
```

**Deactivate:**
```bash
deactivate
```

---

## Next Steps

After completing Week 2 setup:

1. ✓ Virtual environment created
2. ✓ pip working correctly
3. ✓ Can install packages
4. ✓ Can create requirements.txt
5. → Practice with Week 2 exercises!
6. → Build the to-do list mini-project
7. → Experiment with different packages

---

## Week 2 Practice Exercises

**Try these to verify your setup:**

**Exercise 1: Environment Practice**
```bash
# Create a new project
mkdir calculator-project
cd calculator-project

# Create and activate venv
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# Verify isolation
pip list
```

**Exercise 2: Package Practice**
```bash
# Install some packages
pip install colorama prettytable

# Create requirements.txt
pip freeze > requirements.txt

# Verify file contents
cat requirements.txt  # macOS/Linux
type requirements.txt  # Windows
```

**Exercise 3: Recreate Environment**
```bash
# Deactivate current environment
deactivate

# Delete venv
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Create new venv
python -m venv venv
venv\Scripts\activate

# Install from requirements
pip install -r requirements.txt

# Verify packages installed
pip list
```

---

## Getting Help

If you encounter issues:

1. **Read error messages carefully** - They often tell you what's wrong
2. **Check activation** - Is `(venv)` showing in terminal?
3. **Verify Python version** - `python --version`
4. **Google the error** - Someone else has likely had the same issue
5. **Check official docs**:
   - venv: [docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
   - pip: [pip.pypa.io](https://pip.pypa.io/)
6. **Ask your trainer** - They're here to help!

---

## Additional Resources

**Official Documentation:**
- Python venv: [docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
- pip Documentation: [pip.pypa.io/en/stable](https://pip.pypa.io/en/stable/)
- PyPI (Package Index): [pypi.org](https://pypi.org/)

**Video Tutorials:**
- "Python Virtual Environments" - Corey Schafer
- "pip Tutorial" - Tech With Tim
- "requirements.txt" - Real Python

**Articles:**
- Real Python - Virtual Environments
- Python.org - Installing Packages
- pip - User Guide

---

**Congratulations on setting up your Python development environment!** You're now ready to work on isolated projects with clean dependencies. This is a professional skill that you'll use throughout your programming career!
