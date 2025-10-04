# ⚡ ProjectSetup-Automator

### Automate your coding environment setup with a single Python script.

This script is designed to **instantly launch your development environments** (NLP, Jarvis, or OpenCV) by opening relevant folders in **VS Code**, starting **Chrome sessions**, and organizing your **Windows desktops** automatically.

Perfect for developers who juggle multiple projects and want a smooth, automated startup experience.

---

## 🚀 Features

* 🧠 **NLP Setup** — Opens your NLP project folder and associated ChatGPT workspace.
* 🤖 **Jarvis Setup** — Launches your Jarvis AI project with a local server and ChatGPT session.
* 👁️ **OpenCV Setup** — Loads your computer vision workspace and related YouTube tutorials.
* 💻 **Multi-desktop Automation** — Automatically switches between Windows virtual desktops for cleaner workflow.
* ⏰ **Timeout Fallback** — If no option is selected within 60 seconds, defaults to Jarvis setup.
* ⚙️ **Windows Startup Integration** — Optionally run the setup automatically when your PC boots.

---

## 🧩 Requirements

Make sure you have these Python packages installed:

```bash
pip install keyboard pyautogui inputimeout
```

Also ensure:

* **VS Code (`code`)** is available in your system path
* **Google Chrome** is installed
* You’re on **Windows** (since this script uses Windows-specific desktop shortcuts)

---

## 🧠 How It Works

The script waits for your selection:

```text
Select one within 60 seconds or I setup Jarvis project!
1. NLP Setup
2. Jarvis Setup
3. OpenCV
> 
```

Then:

* Opens the corresponding project folder in VS Code
* Launches a new Chrome session (ChatGPT, local host, or YouTube)
* Positions everything neatly across virtual desktops

---

## 🛠️ Setup Paths

In the script, update these folder paths to match your local setup:

```python
NLP_folder = r"E:\code_playground\python\Jarvis_NLP\phase_3"
Jarvis_folder = r"E:\code_playground\Jarvis\jarvis_v1"
OpenCV_folder = r"E:\code_playground\python\openCV"
```

---

## 🧰 Usage

Run the script directly from the terminal:

```bash
python setup_projects.py
```

If you don’t select anything within 60 seconds, it will automatically launch the **Jarvis** setup.

---

## ⚙️ Optional: Run on Windows Startup

If you want your setup to run automatically every time your computer starts, you can use a **batch file (`.bat`)**.

### 🧾 Example `.bat` file

Create a new file named `start_setup.bat` and paste the following:

```bat
@echo off
python "E:\code_playground\automate_setup\setup_nlp.py"
exit
```

> 💡 Replace the Python script path with your actual `.py` file path.

### 🪄 To make it run at startup:

1. Press **Win + R**, type `shell:startup`, and hit **Enter**.
   This opens your **Windows Startup folder**.
2. Copy your `.bat` file into this folder.
3. Restart your computer — your Python setup will launch automatically after login!

This is great if you want your dev environment ready as soon as your system boots.

---

## 📂 Project Structure

```
ProjectSetup-Automator/
│
├── setup_projects.py     # Main automation script
├── start_setup.bat       # Optional Windows startup launcher
├── README.md             # Documentation
└── requirements.txt      # Dependencies
```

---

## ✨ Demo (Example Flow)

1. Run the script
2. Select **1** for NLP
3. Watch it:

   * Jump desktops
   * Open VS Code
   * Launch ChatGPT and setup pages
4. All ready for coding within seconds 🚀

---

## 💡 Future Ideas

* 🔧 Add cross-platform (macOS/Linux) support
* 🌐 Add customizable environment configs via JSON
* 🗂️ GUI-based selection menu

---

## 🧑‍💻 Author

**Musa Stark**<br/>
📧 [musa.fullstack08@gmail.com](mailto:musa.fullstack08@gmail.com)<br/>
🐙 [GitHub Profile](https://github.com/Musa-Stark)

---

## 🪄 License

This project is licensed under the **MIT License** — feel free to use and modify.

---

> “Automate the boring stuff. Focus on building cool things.” 💡