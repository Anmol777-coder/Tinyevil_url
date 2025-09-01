import os
import time
import platform
import requests
import socket
import signal
import sys
import random
import string
from datetime import datetime

# 🎨 Colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# 🖼 Banner
def ascii_banner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    ver = "v3.0"
    print(Colors.OKGREEN + "             .           .           " + Colors.ENDC)
    print(Colors.OKGREEN + "             M.          .M          " + Colors.ENDC)
    print(Colors.OKGREEN + "              MMMMMMMMMMM.           " + Colors.ENDC)
    print(Colors.OKGREEN + "           .MMM\\\\MMMMMMM/MMM.         " + Colors.ENDC)
    print(Colors.OKGREEN + "          .MMM.7MMMMMMM.7MMM.        " + Colors.ENDC)
    print(Colors.OKGREEN + "         .MMMMMMMMMMMMMMMMMMM        " + Colors.ENDC)
    print(Colors.OKGREEN + "         MMMMMMM.......MMMMMMM       " + Colors.ENDC)
    print(Colors.OKGREEN + "         MMMMMMMMMMMMMMMMMMMMM       " + Colors.ENDC)
    print(Colors.OKGREEN + "    MMMM MMMMMMMMMMMMMMMMMMMMM MMMM  " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD " + Colors.ENDC)
    print(Colors.OKGREEN + "    MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  " + Colors.ENDC)
    print(Colors.OKGREEN + "         MMMMMMMMMMMMMMMMMMMMM       " + Colors.ENDC)
    print(Colors.OKGREEN + "         MMMMMMMMMMMMMMMMMMMMM       " + Colors.ENDC)
    print(Colors.OKGREEN + f"             MMMMM   MMMMM  {ver}     " + Colors.ENDC)
    print(Colors.OKGREEN + "             MMMMM   MMMMM           " + Colors.ENDC)
    print(Colors.OKGREEN + "             MMMMM   MMMMM           " + Colors.ENDC)
    print(Colors.OKGREEN + "             MMMMM   MMMMM           " + Colors.ENDC)
    print(Colors.OKGREEN + "             .MMM.   .MMM.           " + Colors.ENDC)
    print(Colors.OKCYAN + "          TinyURL GPT - Evil Terminal" + Colors.ENDC)
    print(Colors.OKCYAN + "============================================================" + Colors.ENDC)

# 🌐 Internet Check + IPs
def check_internet():
    print(Colors.OKBLUE + "[*] Checking Internet Connection..." + Colors.ENDC)
    response = os.system("ping -c 1 -W 2 google.com > /dev/null 2>&1")
    if response == 0:
        print(Colors.OKGREEN + "[+] Internet: CONNECTED ✅" + Colors.ENDC)
        try:
            lanip = socket.gethostbyname(socket.gethostname())
        except:
            lanip = "Unavailable"
        print(Colors.WARNING + "[i] Local IP: " + Colors.OKGREEN + lanip + Colors.ENDC)
        try:
            publicip = requests.get("https://api.ipify.org").text
        except:
            publicip = "Unavailable"
        print(Colors.WARNING + "[i] Public IP: " + Colors.OKGREEN + publicip + Colors.ENDC)
        return lanip, publicip
    else:
        print(Colors.FAIL + "[!] Internet: FAILED ❌" + Colors.ENDC)
        sys.exit()

# 🔗 Link Shortener
def shorten_link(url):
    try:
        api = f"https://tinyurl.com/api-create.php?url={url}"
        short = requests.get(api).text
        save_history(url, short)
        return short
    except:
        return Colors.FAIL + "[!] Failed to shorten link" + Colors.ENDC

# 📜 Save History (TXT + HTML)
def save_history(original, short):
    # Save to text file (old system)
    with open("link_history.txt", "a") as f:
        f.write(f"{datetime.now()} | {original} -> {short}\n")

    # Save to HTML file (new system)
    html_file = "link_history.html"
    entry = f"<tr><td>{datetime.now()}</td><td>{original}</td><td><a href='{short}' target='_blank'>{short}</a></td></tr>\n"

    if not os.path.exists(html_file):
        with open(html_file, "w") as f:
            f.write("""<html>
<head>
<title>Link History - Evil Terminal</title>
<style>
    body { font-family: Arial, sans-serif; background: #111; color: #eee; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th, td { border: 1px solid #444; padding: 10px; text-align: left; }
    th { background: #333; }
    tr:nth-child(even) { background: #222; }
    a { color: #4CAF50; text-decoration: none; }
</style>
</head>
<body>
<h2>🔗 Evil-Terminal Link History</h2>
<table>
<tr><th>Date & Time</th><th>Original Link</th><th>Shortened Link</th></tr>
""")
            f.write(entry)
    else:
        with open(html_file, "a") as f:
            f.write(entry)


    # 📜 Show History
def show_history():
    if os.path.exists("link_history.html"):
        print(Colors.OKCYAN + "\n=== Link History (HTML file) ===" + Colors.ENDC)
        print(Colors.OKGREEN + "[i] Saved in: link_history.html" + Colors.ENDC)
    elif os.path.exists("link_history.txt"):
        print(Colors.OKCYAN + "\n=== Link History (TXT file) ===" + Colors.ENDC)
        with open("link_history.txt", "r") as f:
            print(f.read())
    else:
        print(Colors.WARNING + "[!] No history found." + Colors.ENDC)
        

# 📋 Menu
def show_menu():
    print("\n" + Colors.WARNING + "[1] Shorten localhost link")
    print("[2] Shorten cloudflared/ngrok link")
    print("[3] View history")
    print("[4] Generate random session ID")
    print("[5] Exit" + Colors.ENDC)
    return input(Colors.OKCYAN + "[+] Choose option: " + Colors.ENDC)

# 🎬 Loading Animation
def loading(msg, sec=2):
    print(Colors.OKBLUE + msg + Colors.ENDC, end="", flush=True)
    for _ in range(sec * 3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

# 🛑 Ctrl+C Handler
def ctrl_c_handler(sig, frame):
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(Colors.FAIL + "[*] (Ctrl + C) Detected, Exiting..." + Colors.ENDC)
    time.sleep(1)
    print(Colors.WARNING + "[*] Thanks For Using Evil-Terminal :)" + Colors.ENDC)
    sys.exit(0)

signal.signal(signal.SIGINT, ctrl_c_handler)

# 🏁 Main
def main():
    ascii_banner()
    lanip, publicip = check_internet()
    time.sleep(1)
    while True:
        choice = show_menu()
        if choice == "1":
            link = input(Colors.OKBLUE + "[+] Enter localhost link (e.g. http://localhost:8080): " + Colors.ENDC)
            if "localhost" in link:
                loading("[*] Shortening link")
                print(Colors.OKGREEN + f"[🔗] Shortened Link: {shorten_link(link)}" + Colors.ENDC)
            else:
                print(Colors.FAIL + "[!] Invalid localhost link" + Colors.ENDC)
        elif choice == "2":
            link = input(Colors.OKBLUE + "[+] Enter tunnel link (cloudflared/ngrok): " + Colors.ENDC)
            if "trycloudflare" in link or ".ngrok.io" in link:
                loading("[*] Shortening tunnel link")
                print(Colors.OKGREEN + f"[🔗] Shortened Tunnel Link: {shorten_link(link)}" + Colors.ENDC)
            else:
                print(Colors.FAIL + "[!] Invalid tunnel link format" + Colors.ENDC)
        elif choice == "3":
            show_history()
        elif choice == "4":
            sid = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            print(Colors.OKGREEN + f"[i] Generated Session ID: {sid}" + Colors.ENDC)
        elif choice == "5":
            loading("[*] Exiting Evil-Terminal", sec=1)
            print(Colors.WARNING + "👋 Goodbye, MONU! Stay safe." + Colors.ENDC)
            break
        else:
            print(Colors.FAIL + "❌ Invalid option. Try again." + Colors.ENDC)

if __name__ == "__main__":
    main()
