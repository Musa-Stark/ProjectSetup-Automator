# ⚡ ProjectSetup-Automator

### Automate your coding environment setup with a single Python script.

This script is designed to **instantly launch your development environments** (NLP, Jarvis, or OpenCV) by opening relevant folders in **VS Code**, starting **Chrome sessions**, and organizing your **Windows desktops** automatically.

Perfect for developers who juggle multiple projects and want a smooth, automated startup experience.

---

## 🚀 Features

- 🧠 **NLP Setup** — Opens your NLP project folder and associated ChatGPT workspace.  
- 🤖 **Jarvis Setup** — Launches your Jarvis AI project with a local server and ChatGPT session.  
- 👁️ **OpenCV Setup** — Loads your computer vision workspace and related YouTube tutorials.  
- 💻 **Multi-desktop Automation** — Automatically switches between Windows virtual desktops for cleaner workflow.  
- ⏰ **Timeout Fallback** — If no option is selected within 60 seconds, defaults to Jarvis setup.

---

## 🧩 Requirements

Make sure you have these Python packages installed:

```bash
pip install keyboard pyautogui inputimeout
