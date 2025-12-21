# Week 1 Setup Instructions

Complete guide for setting up your development environment for Python programming.

---

## Table of Contents

1. [Overview](#overview)
2. [Install Python](#install-python)
3. [Install VS Code](#install-vs-code)
4. [Install Git](#install-git)
5. [Create GitHub Account](#create-github-account)
6. [Verify Installation](#verify-installation)
7. [Troubleshooting](#troubleshooting)

---

## Overview

### What You'll Install

**Python**: The programming language we'll use
- Version: 3.11 or higher
- Time: 10-15 minutes

**VS Code**: The code editor
- Latest version
- Time: 5-10 minutes

**Git**: Version control system
- Latest version
- Time: 5-10 minutes

**GitHub**: Online code storage (account creation)
- Time: 5 minutes

**Total Time**: 30-45 minutes

### System Requirements

**Minimum Requirements**:
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: 4GB
- **Disk Space**: 10GB free
- **Internet**: Stable connection for downloads

---

## Install Python

### Windows

#### Step 1: Download Python

1. Open your web browser
2. Go to [python.org/downloads](https://www.python.org/downloads/)
3. Click the yellow **"Download Python 3.x.x"** button
4. Save the installer file (e.g., `python-3.11.5-amd64.exe`)

#### Step 2: Run the Installer

1. Find and double-click the downloaded installer
2. **CRITICAL**: Check the box **"Add Python to PATH"** at the bottom
3. Click **"Install Now"**
4. Wait for installation to complete
5. Click **"Close"**

#### Step 3: Verify Installation

1. Press `Win + R`
2. Type `cmd` and press Enter
3. In the command prompt, type:
```bash
python --version
```
4. You should see: `Python 3.11.x` or similar
5. Also check pip:
```bash
pip --version
```

If you see version numbers, you're done!

**Screenshot Checkpoints**:
- [ ] "Add Python to PATH" is checked
- [ ] Installation successful message
- [ ] Version command shows Python 3.11+

---

### macOS

#### Step 1: Check if Python is Already Installed

1. Open **Terminal** (Applications → Utilities → Terminal)
2. Type:
```bash
python3 --version
```
3. If you see Python 3.11+, skip to [Install VS Code](#install-vs-code)

#### Step 2: Install Using Official Installer

**Option A: Official Python Installer**

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download the macOS installer (e.g., `python-3.11.5-macos11.pkg`)
3. Double-click the downloaded file
4. Follow the installation wizard
5. Click "Continue" → "Agree" → "Install"
6. Enter your password when prompted
7. Click "Close"

**Option B: Using Homebrew (Recommended for developers)**

1. Open Terminal
2. Install Homebrew if you don't have it:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Install Python:
```bash
brew install python3
```

#### Step 3: Verify Installation

```bash
python3 --version
pip3 --version
```

**Note**: On macOS, use `python3` and `pip3` instead of `python` and `pip`.

---

### Linux (Ubuntu/Debian)

#### Step 1: Update Package List

Open Terminal and run:
```bash
sudo apt update
```

#### Step 2: Install Python

```bash
sudo apt install python3 python3-pip python3-venv
```

Enter your password when prompted.

#### Step 3: Verify Installation

```bash
python3 --version
pip3 --version
```

**For Other Linux Distributions**:

**Fedora/CentOS/RHEL**:
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux**:
```bash
sudo pacman -S python python-pip
```

---

## Install VS Code

### Windows

#### Step 1: Download VS Code

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Click **"Download for Windows"**
3. Save the installer (e.g., `VSCodeUserSetup-x64-1.x.x.exe`)

#### Step 2: Run the Installer

1. Double-click the downloaded installer
2. Accept the license agreement
3. **Important**: Check these boxes:
   - ✓ Add "Open with Code" action to Windows Explorer file context menu
   - ✓ Add "Open with Code" action to Windows Explorer directory context menu
   - ✓ Add to PATH
4. Click "Next" → "Install"
5. Click "Finish"

#### Step 3: Launch VS Code

1. Press `Win` key
2. Type "Visual Studio Code"
3. Click to open

---

### macOS

#### Step 1: Download VS Code

1. Go to [code.visualstudio.com](https://code.visualstudio.com/)
2. Click **"Download for Mac"**
3. Save the file (`VSCode-darwin-universal.zip`)

#### Step 2: Install

1. Open Downloads folder
2. Double-click the ZIP file (if not already extracted)
3. Drag **Visual Studio Code.app** to the **Applications** folder

#### Step 3: Launch VS Code

1. Open **Applications** folder
2. Double-click **Visual Studio Code**
3. If you see a security warning, click **"Open"**

---

### Linux

#### Using Package Manager (Ubuntu/Debian)

```bash
# Download and install the key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

# Add repository
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

# Install
sudo apt update
sudo apt install code
```

Or download the `.deb` package from [code.visualstudio.com](https://code.visualstudio.com/) and install with:
```bash
sudo dpkg -i <filename>.deb
```

---

## Configure VS Code for Python

### Install Python Extension

1. Open VS Code
2. Click the **Extensions** icon (left sidebar) or press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS)
3. In the search box, type: **Python**
4. Find **"Python"** by Microsoft (should be first result)
5. Click **"Install"**

### Recommended Additional Extensions

While in Extensions, also install:

1. **Pylance** (by Microsoft)
   - Better Python IntelliSense
   - Usually installed with Python extension

2. **Python Indent** (by Kevin Rose)
   - Helps with Python indentation

3. **Code Runner** (by Jun Han)
   - Run code with a single click

### Configure Python Path

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type: **Python: Select Interpreter**
3. Choose the Python version you installed

---

## Install Git

### Windows

#### Step 1: Download Git

1. Go to [git-scm.com](https://git-scm.com/)
2. Click **"Download for Windows"**
3. Save the installer (e.g., `Git-2.x.x-64-bit.exe`)

#### Step 2: Run the Installer

1. Double-click the installer
2. Use default options (just keep clicking "Next")
3. **Important selections**:
   - Default editor: Choose "Use Visual Studio Code as Git's default editor"
   - PATH environment: "Git from the command line and also from 3rd-party software"
   - Line ending conversions: "Checkout Windows-style, commit Unix-style"
4. Click "Install"
5. Click "Finish"

#### Step 3: Verify Installation

1. Open Command Prompt (Win + R → type `cmd`)
2. Type:
```bash
git --version
```
3. You should see: `git version 2.x.x`

---

### macOS

#### Option A: Using Homebrew (Recommended)

```bash
brew install git
```

#### Option B: Using Official Installer

1. Go to [git-scm.com](https://git-scm.com/)
2. Download macOS installer
3. Follow installation steps

#### Step 3: Verify Installation

```bash
git --version
```

---

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install git
```

Verify:
```bash
git --version
```

---

## Configure Git

After installing Git, configure it with your information:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Example:
```bash
git config --global user.name "Ahmed Mohammed"
git config --global user.email "ahmed.mohammed@example.com"
```

Verify configuration:
```bash
git config --list
```

---

## Create GitHub Account

### Step 1: Sign Up

1. Go to [github.com](https://github.com/)
2. Click **"Sign up"** (top right)
3. Enter your email address
4. Click **"Continue"**
5. Create a password
6. Choose a username (lowercase, can include numbers and hyphens)
7. Complete the verification puzzle
8. Click **"Create account"**

### Step 2: Verify Email

1. Check your email inbox
2. Find email from GitHub
3. Click the verification link

### Step 3: Complete Setup

1. Answer the onboarding questions (or skip)
2. Choose the Free plan
3. Complete the setup

### Step 4: Optional - Set Up SSH Keys

SSH keys make it easier to push/pull code without entering password every time.

#### Generate SSH Key

**Windows/macOS/Linux**:
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Press Enter to accept default location.
Press Enter twice for no passphrase (or create one for extra security).

#### Add SSH Key to GitHub

1. Copy your public key:

**Windows**:
```bash
type %USERPROFILE%\.ssh\id_ed25519.pub
```

**macOS/Linux**:
```bash
cat ~/.ssh/id_ed25519.pub
```

2. Go to GitHub → Settings (profile icon → Settings)
3. Click **"SSH and GPG keys"** (left sidebar)
4. Click **"New SSH key"**
5. Title: "My Computer" (or any name)
6. Paste the key in the "Key" field
7. Click **"Add SSH key"**

---

## Verify Installation

### Complete Verification Checklist

Open a new terminal/command prompt and run these commands:

```bash
# Python
python --version
# Should show: Python 3.11.x or higher

# Pip
pip --version
# Should show: pip 23.x.x or similar

# Git
git --version
# Should show: git version 2.x.x

# VS Code (from command line)
code --version
# Should show version number
```

**On macOS/Linux**, use `python3` and `pip3`:
```bash
python3 --version
pip3 --version
```

### Create Test Project

1. Create a folder called `test-python`
2. Open VS Code
3. File → Open Folder → Select `test-python`
4. Create new file: `test.py`
5. Type:
```python
print("Setup complete!")
print(f"Python version: {__import__('sys').version}")
```
6. Right-click in editor → "Run Python File in Terminal"
7. You should see output in the terminal

If you see the message, congratulations! Setup is complete!

---

## Troubleshooting

### Python Issues

#### Issue: "python is not recognized" (Windows)

**Solution**:
1. Uninstall Python
2. Reinstall and **check "Add Python to PATH"**
3. Restart computer

**Or manually add to PATH**:
1. Search "Environment Variables" in Start menu
2. Click "Environment Variables"
3. Under "System variables", find "Path"
4. Click "Edit"
5. Click "New"
6. Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311`
7. Add: `C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts`
8. Click OK
9. Restart Command Prompt

#### Issue: Permission Denied when installing packages

**Windows**: Run Command Prompt as Administrator
**macOS/Linux**: Don't use `sudo` with pip; use virtual environments instead

---

### VS Code Issues

#### Issue: Python extension not working

**Solution**:
1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
3. Type: **Python: Select Interpreter**
4. Choose your Python installation
5. Restart VS Code

#### Issue: Terminal not opening in VS Code

**Solution**:
1. View → Terminal (or `Ctrl+``)
2. If still not working, reinstall VS Code

---

### Git Issues

#### Issue: "git is not recognized"

**Windows**:
1. Reinstall Git
2. Make sure to select "Git from the command line and also from 3rd-party software"
3. Restart computer

**macOS/Linux**:
- Verify installation: `which git`
- If empty, reinstall Git

#### Issue: Git asking for username/password repeatedly

**Solution**: Set up SSH keys (see [Create GitHub Account](#create-github-account) section)

---

### General Issues

#### Issue: Antivirus blocking installation

**Solution**:
- Temporarily disable antivirus
- Install software
- Re-enable antivirus
- Add Python, VS Code, and Git folders to antivirus exceptions

#### Issue: Not enough disk space

**Solution**:
- Free up at least 10GB
- Delete temporary files
- Uninstall unused programs

#### Issue: Installation hanging/freezing

**Solution**:
- Close all other programs
- Restart computer
- Try installation again
- Download installer again (might be corrupted)

---

## Post-Installation Setup

### Create Project Folder Structure

Create a dedicated folder for your Python learning:

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

### VS Code Settings (Optional but Recommended)

1. Open VS Code
2. File → Preferences → Settings (or `Ctrl+,`)
3. Search for these settings and modify:

**Format on Save**:
- Search: "format on save"
- Check the box

**Auto Save**:
- Search: "auto save"
- Select "afterDelay"

**Python Linting**:
- Search: "python linting enabled"
- Check the box

---

## Quick Reference Commands

### Terminal/Command Prompt Basics

**Windows (Command Prompt)**:
```bash
dir                  # List files
cd foldername        # Change directory
cd ..                # Go up one directory
mkdir foldername     # Create directory
cls                  # Clear screen
```

**macOS/Linux (Terminal)**:
```bash
ls                   # List files
cd foldername        # Change directory
cd ..                # Go up one directory
mkdir foldername     # Create directory
clear                # Clear screen
pwd                  # Show current directory
```

### Running Python

**Windows**:
```bash
python script.py
python              # Interactive mode
```

**macOS/Linux**:
```bash
python3 script.py
python3             # Interactive mode
```

### Git Basics

```bash
git --version       # Check Git version
git config --list   # View configuration
git status          # Check repository status
```

---

## Next Steps

After completing setup:

1. ✓ Verify all installations work
2. ✓ Create your project folder
3. ✓ Configure VS Code settings
4. ✓ Test Python by running a simple script
5. → Proceed to **lessons.md** to start learning Python!

---

## Getting Help

If you encounter issues:

1. **Read error messages carefully** - they often tell you what's wrong
2. **Google the error** - someone else has likely had the same issue
3. **Check official documentation**:
   - Python: [docs.python.org](https://docs.python.org/)
   - VS Code: [code.visualstudio.com/docs](https://code.visualstudio.com/docs)
   - Git: [git-scm.com/doc](https://git-scm.com/doc)
4. **Ask your trainer** - that's what they're there for!

---

## Video Tutorials (If Needed)

If you prefer video guides:

- **Python Installation**: Search YouTube for "Install Python [Your OS] 2024"
- **VS Code Setup**: Search "VS Code Python Setup Tutorial"
- **Git Installation**: Search "Install Git [Your OS]"

---

**Congratulations on completing the setup!** You're now ready to start your Python programming journey!
