import os
import subprocess

HTML_FILE = "how_to_use.html"
PORT = 8080

print("\n=== Tinyevil_url HTML Server with Cloudflared ===\n")

# Step 1: Check if HTML file exists
if not os.path.exists(HTML_FILE):
    print(f"[!] {HTML_FILE} not found. Place it in the same folder as this script.")
    exit(1)

# Step 2: Instructions for Python HTTP server
print("[1] Starting local server with Python:")
print(f"    python3 -m http.server {PORT}\n")
print(f"    -> Open in browser: http://localhost:{PORT}/{HTML_FILE}\n")

# Step 3: Instructions for installing Cloudflared (Kali Linux)
print("[2] On Kali Linux, install cloudflared:")
print("    sudo apt update && sudo apt upgrade -y")
print("    sudo apt install cloudflared -y\n")

# Step 4: Instructions for Termux (Android)
print("[3] On Termux, install packages:")
print("    pkg update && pkg upgrade -y")
print("    pkg install python -y")
print("    pkg install cloudflared -y\n")

# Step 5: Cloudflared command
print("[4] After starting the server, run Cloudflared tunnel:")
print(f"    cloudflared tunnel --url http://localhost:{PORT}\n")

print("This will give you a public URL (https://randomstring.trycloudflare.com) to share your HTML page.\n")
