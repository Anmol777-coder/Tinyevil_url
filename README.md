# 🕶️ Evil-Terminal v3.0  

**TinyURL GPT Edition – Created by Anmol**  
A modern, terminal-based Python tool to shorten, manage and organize links with style ⚡  

---

## 📖 Introduction  

**Evil-Terminal v3.0** is a Python-powered terminal utility designed for:  
- Developers running local servers  
- Pentesters working with **ngrok** / **cloudflared** tunnels  
- Users who want a simple yet powerful **link shortener**  

It provides:  
- Beautiful **ASCII banner**  
- System & Network info (Local + Public IP detection)  
- TinyURL API integration  
- Link history logging  
- Random Session ID generator  
- Clean interactive menu  

---

## ✨ Features  

- ✅ ASCII Banner – Stylish startup screen  
- ✅ Internet Check + Local & Public IP detection  
- ✅ Shorten links from:  
  - `http://localhost:8080`  
  - `https://<ngrok>.ngrok.io`  
  - `https://trycloudflare.com`  
- ✅ Auto history logging with timestamps  
- ✅ Random 12-character Session ID generator  
- ✅ Ctrl+C exit handler  
- ❌ QR Code removed (legacy feature)  

---

## 📂 Project Structure  

Tinyevil_url/
│
├── evil_terminal.py # Main Script (Terminal Edition)
├── Tinyevil-G.py # GUI Edition
├── requirements.txt # Dependencies
├── README.md # Documentation
├── LICENSE # License File
├── .gitignore # Git Ignore Rules
└── link_history.* # Auto-generated History (txt/html/csv/json)

yaml
Copy code

---

## ⚡ Installation  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/Anmol777-coder/Tinyevil_url.git
cd Tinyevil_url
2️⃣ Setup Virtual Environment (Recommended)
bash
Copy code
python -m venv venv
Activate venv:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

3️⃣ Install Requirements
bash
Copy code
pip install -r requirements.txt
4️⃣ Run Evil-Terminal
bash
Copy code
python evil_terminal.py
📜 Menu Preview
csharp
Copy code
============================================================
[1] Shorten localhost link
[2] Shorten cloudflared/ngrok link
[3] View history
[4] Generate random session ID
[5] Exit
============================================================
⚙️ Dependencies
Listed in requirements.txt:

nginx
Copy code
requests
Built-in modules used: os, time, platform, socket, signal, sys, random, string, datetime

🎯 Use Cases
👨‍💻 Developers → shorten localhost URLs

🛡️ Pentesters → manage ngrok/cloudflared tunnels

🌐 Everyday Users → shorten and save long links

🔑 Security Testers → generate random session IDs

🖼️ Banner Preview
When you run the script:

diff
Copy code
             .           .           
             M.          .M          
              MMMMMMMMMMM.           
           .MMM\MMMMMMM/MMM.         
          .MMM.7MMMMMMM.7MMM.        
         .MMMMMMMMMMMMMMMMMMM        
         MMMMMMM.......MMMMMMM       
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
    MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  
         MMMMMMMMMMMMMMMMMMMMM       
         MMMMMMMMMMMMMMMMMMMMM       
             MMMMM   MMMMM  v3.0     
             MMMMM   MMMMM           
             MMMMM   MMMMM           
             MMMMM   MMMMM           
             .MMM.   .MMM.           
          TinyURL GPT - Evil Terminal
============================================================
🎨 Tinyevil-G (GUI Version)
Tinyevil-G is the GUI Edition of Evil-Terminal.
It uses Tkinter to provide a Dark Droid/Matrix-style interface, supports exporting history, and makes link shortening easier with buttons and tables.

✨ Features
🌐 Link Shortener

Shortens localhost, ngrok, and trycloudflare URLs.

🎨 Dark Droid/Matrix GUI

Tkinter + custom theme styling.

📜 History Manager

Auto-save history in link_history.txt and link_history_gui.html.

View history in the GUI (table view).

📂 Export Options

Export history as HTML, CSV, JSON.

🖥 System Info

Auto-detects Local IP + Public IP.

🔑 Session ID Generator

Generates random alphanumeric IDs.

🚀 Splash Screen Loader

▶️ How to Run
bash
Copy code
python Tinyevil-G.py
📂 Files Created
link_history.txt → Simple text log

link_history_gui.html → Styled HTML history

Export options:

history.csv

history.json

history.html

📜 License
This project is licensed under the MIT License – free to use, modify, and distribute.

🧑‍💻 Author
Created by: Anmol Yadav

Powered by: Python 🐍

🌟 Support
If you like this project:

⭐ Star it on GitHub

🔁 Fork & Contribute

🐞 Report issues / Pull Requests welcome

✨💗 Thank you for visiting!
