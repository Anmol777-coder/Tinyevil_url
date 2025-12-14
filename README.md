# 🕶️ Evil-Terminal v3.0
https://www.freepik.com/premium-photo/illustration-skilled-pro-player-shooter_235253156.htm#fromView=search&page=1&position=16&uuid=a878126f-7af3-4182-b423-e7b2dfe13c70&query=2D+game+art+player++action

**TinyURL GPT Edition – Created by Anmol**
A modern, terminal-based Python tool to shorten, manage, and organize links with style ⚡

---

## 📖 Introduction

**Evil-Terminal v3.0** is a Python-powered terminal utility designed for:

* 👨‍💻 Developers running local servers
* 🛡️ Pentesters working with ngrok / cloudflared tunnels
* 🌐 Users who want a simple yet powerful link shortener

### It provides:

* Beautiful ASCII banner
* System & Network info (Local + Public IP detection)
* TinyURL API integration
* Link history logging
* Random Session ID generator
* Clean interactive menu

---

## ✨ Features

* ✅ ASCII Banner – Stylish startup screen
* ✅ Internet Check + Local & Public IP detection
* ✅ Shorten links from localhost, ngrok, cloudflared
* ✅ Auto history logging with timestamps
* ✅ Random 12-character Session ID generator
* ✅ Ctrl+C exit handler
* ❌ QR Code feature removed (legacy)

---

## 📂 Project Structure

```
Tinyevil_url/
├── evil_terminal.py      # Main Script (Terminal Edition)
├── Tinyevil-G.py         # GUI Edition
├── requirements.txt      # Dependencies
├── README.md             # Documentation
├── LICENSE               # License File
├── .gitignore            # Git Ignore Rules
└── link_history.*        # Auto-generated History (txt/html/csv/json)
```

---

## ⚡ Installation

```bash
# 1️⃣ Clone Repository
git clone https://github.com/Anmol777-coder/Tinyevil_url.git
cd Tinyevil_url

# 2️⃣ Setup Virtual Environment (Recommended)
python -m venv venv

# Activate venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 3️⃣ Install Requirements
pip install -r requirements.txt

# 4️⃣ Run Evil-Terminal
python evil_terminal.py
```

---

## 📜 Menu Preview

```
============================================================
[1] Shorten localhost link
[2] Shorten cloudflared/ngrok link
[3] View history
[4] Generate random session ID
[5] Exit
============================================================
```

---

## ⚙️ Dependencies

Listed in `requirements.txt`:

* requests

Built-in modules: `os`, `time`, `platform`, `socket`, `signal`, `sys`, `random`, `string`, `datetime`

---

## 🎯 Use Cases

* 👨‍💻 Developers → shorten localhost URLs
* 🛡️ Pentesters → manage ngrok/cloudflared tunnels
* 🌐 Everyday Users → shorten and save long links
* 🔑 Security Testers → generate random session IDs

---

## 🖼️ Banner Preview

```
           .           .           
          M.          .M          
           MMMMMMMMMMM.           
        .MMM\MMMMMMM/MMM.         
      .MMM.🔥MMMMMMM.🔥MMM.        
      .MMMMMMMMMMMMMMMMMMM        
      MMMMMM\......./MMMMMM       
      MMMMMMMMMMMMMMMMMMMMM       
 MMMM MMMMMMMMMMMMMMMMMMMMM MMMM
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD
MMM8  MMMMMMMMMMMMMMMMMMMMM 8MMM  
      MMMMMMMMMMMMMMMMMMMMM      
      MMMMMMMMMMMMMMMMMMMMM       
          MMMMM   MMMMM  v3.0     
          MMMMM   MMMMM           
          MMMMM   MMMMM           
          MMMMM   MMMMM           
          .MMM.   .MMM.           
          TinyURL GPT - Evil Terminal
===================================
```

---

## 🎨 Tinyevil-G (GUI Version)

Tinyevil-G is the GUI Edition of Evil-Terminal.

### Features

* 🌐 Link Shortener (localhost, ngrok, cloudflared)
* 🎨 Dark Droid/Matrix GUI (Tkinter custom theme)
* 📜 History Manager with auto-save (txt/html)
* 📂 Export Options (HTML, CSV, JSON)
* 🖥 System Info (Local + Public IP)
* 🔑 Session ID Generator
* 🚀 Splash Screen Loader

### Run

```bash
python Tinyevil-G.py
```

### Files Created

* `link_history.txt` → Simple text log
* `link_history_gui.html` → Styled HTML history
* Export: `history.csv`, `history.json`, `history.html`

---

## 📜 License

MIT License – free to use, modify, and distribute.

---

## 🧑‍💻 Author

Created by: **Anmol Yadav**
Powered by: **Python 🐍**

---

## 🌟 Support

* ⭐ Star this project on GitHub
* 🔁 Fork & Contribute
* 🐞 Report issues / PRs welcome

✨💗 Thank you for visiting!
