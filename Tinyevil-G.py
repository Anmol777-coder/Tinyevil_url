#!/usr/bin/env python3
"""
Tinyevil-G.py
Tkinter GUI for TinyEvil URL shortener (Tinyevil)
Features:
 - Shorten localhost/ngrok/cloudflared links (TinyURL API)
 - Show Local/Public IP
 - Session ID generator
 - History table (in-GUI)
 - Export history to HTML / CSV / JSON
 - Dark / Droid (cyan) themed UI with splash screen
"""

import os
import sys
import time
import json
import csv
import random
import string
import socket
import platform
import threading
from datetime import datetime

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
except Exception as e:
    print("Tkinter is required to run this GUI. Install python-tk package.")
    sys.exit(1)

import requests

# ---------- Configuration ----------
APP_TITLE = "Tinyevil-G v3.0"
HISTORY_HTML = "link_history_gui.html"
HISTORY_CSV = "link_history.csv"
HISTORY_JSON = "link_history.json"

# ---------- Utils ----------

def get_public_ip(timeout=3):
    try:
        return requests.get("https://api.ipify.org", timeout=timeout).text
    except Exception:
        return "Unavailable"

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "Unavailable"

def shorten_with_tinyurl(url):
    try:
        api = f"https://tinyurl.com/api-create.php?url={url}"
        r = requests.get(api, timeout=8)
        if r.status_code == 200:
            return r.text.strip()
        return None
    except Exception:
        return None

def gen_session_id(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ---------- History manager ----------
class HistoryManager:
    def __init__(self):
        self.entries = []  # each entry: {date, original, short}

    def add(self, original, short):
        entry = {"date": datetime.now().isoformat(sep=' ', timespec='seconds'),
                 "original": original,
                 "short": short}
        self.entries.append(entry)
        self._append_txt(entry)
        self._append_html(entry)

    # persist simple txt for backwards compatibility
    def _append_txt(self, entry):
        try:
            with open('link_history.txt', 'a', encoding='utf-8') as f:
                f.write(f"{entry['date']} | {entry['original']} -> {entry['short']}\n")
        except Exception:
            pass

    def _append_html(self, entry):
        row = f"<tr><td>{entry['date']}</td><td>{entry['original']}</td><td><a href=\"{entry['short']}\" target=\"_blank\">{entry['short']}</a></td></tr>\n"
        if not os.path.exists(HISTORY_HTML):
            with open(HISTORY_HTML, 'w', encoding='utf-8') as f:
                f.write(f"<html><head><meta charset=\"utf-8\"><title>Link History</title><style>body{{background:#06121a;color:#dff7fb;font-family:Arial}}table{{width:100%;border-collapse:collapse}}th,td{{border:1px solid #123; padding:8px}}th{{background:#032a33}}</style></head><body><h2>Link History</h2><table><tr><th>Date</th><th>Original</th><th>Short</th></tr>{row}</table></body></html>")
        else:
            # insert before closing table tag - simple approach: append new row then replace closing tags
            try:
                with open(HISTORY_HTML, 'r', encoding='utf-8') as f:
                    data = f.read()
                # naive insertion before </table></body></html>
                data = data.replace('</table></body></html>', row + '</table></body></html>')
                with open(HISTORY_HTML, 'w', encoding='utf-8') as f:
                    f.write(data)
            except Exception:
                # fallback: append to file (may break structure but still contains rows)
                with open(HISTORY_HTML, 'a', encoding='utf-8') as f:
                    f.write(row)

    def export_csv(self, path=None):
        path = path or HISTORY_CSV
        try:
            with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['date', 'original', 'short'])
                writer.writeheader()
                writer.writerows(self.entries)
            return path
        except Exception:
            return None

    def export_json(self, path=None):
        path = path or HISTORY_JSON
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self.entries, f, indent=2, ensure_ascii=False)
            return path
        except Exception:
            return None

    def export_html(self, path=None):
        path = path or HISTORY_HTML
        # if file already exists we already update during add; copy to path if different
        if os.path.exists(HISTORY_HTML) and path != HISTORY_HTML:
            try:
                with open(HISTORY_HTML, 'r', encoding='utf-8') as src, open(path, 'w', encoding='utf-8') as dst:
                    dst.write(src.read())
                return path
            except Exception:
                return None
        elif path == HISTORY_HTML:
            return path if os.path.exists(path) else None
        else:
            # generate minimal html from entries
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write('<html><head><meta charset="utf-8"><title>Link History</title></head><body><table border="1"><tr><th>Date</th><th>Original</th><th>Short</th></tr>')
                    for e in self.entries:
                        f.write(f"<tr><td>{e['date']}</td><td>{e['original']}</td><td><a href='{e['short']}'>{e['short']}</a></td></tr>")
                    f.write('</table></body></html>')
                return path
            except Exception:
                return None

# ---------- GUI ----------
class TinyevilGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry('900x600')
        self.configure(bg='#071016')
        self.resizable(True, True)

        self.history = HistoryManager()
        self._build_styles()
        self._build_splash()
        # load main UI after splash
        self.after(1200, self._build_main_ui)

    # style setup
    def _build_styles(self):
        style = ttk.Style(self)
        # Use default theme but configure colors for treeview
        style.configure('Treeview', background='#0b1620', foreground='#c8ffff', fieldbackground='#0b1620')
        style.map('Treeview', background=[('selected', '#03454b')], foreground=[('selected', '#ffffff')])

    # splash screen animation (simple)
    def _build_splash(self):
        self.splash = tk.Frame(self, bg='#04202a')
        self.splash.place(relx=0, rely=0, relwidth=1, relheight=1)
        title = tk.Label(self.splash, text='TINYEVIL-URL', font=('Segoe UI', 28, 'bold'), fg='#00ffcc', bg='#04202a')
        title.pack(pady=40)
        sub = tk.Label(self.splash, text='Loading... please wait', font=('Segoe UI', 12), fg='#9fdde0', bg='#04202a')
        sub.pack(pady=10)
        self.splash_progress = ttk.Progressbar(self.splash, mode='indeterminate', length=400)
        self.splash_progress.pack(pady=20)
        self.splash_progress.start(10)

    def _destroy_splash(self):
        try:
            self.splash_progress.stop()
        except Exception:
            pass
        self.splash.destroy()

    def _build_main_ui(self):
        self._destroy_splash()
        # top frame: info
        top = tk.Frame(self, bg='#071016')
        top.pack(fill='x', padx=12, pady=(8,4))

        lbl_title = tk.Label(top, text='⚡ Tinyevil-G v3.0', font=('Segoe UI', 16, 'bold'), fg='#00ffd6', bg='#071016')
        lbl_title.pack(side='left')

        # ip info
        self.ip_label = tk.Label(top, text='IP: checking...', font=('Segoe UI', 10), fg='#9fdde0', bg='#071016')
        self.ip_label.pack(side='right')
        threading.Thread(target=self._load_ip, daemon=True).start()

        main = tk.Frame(self, bg='#071016')
        main.pack(fill='both', expand=True, padx=12, pady=8)

        # left controls
        left = tk.Frame(main, bg='#071016')
        left.pack(side='left', fill='y', padx=(0,8))

        # url entry
        tk.Label(left, text='Enter URL to shorten:', fg='#c8ffff', bg='#071016').pack(pady=(6,2))
        self.url_var = tk.StringVar()
        url_entry = tk.Entry(left, textvariable=self.url_var, width=40, font=('Segoe UI', 11))
        url_entry.pack(pady=(0,8))

        btn_shorten = tk.Button(left, text='Shorten Link', bg='#00c2b8', fg='#041018', width=20, command=self.on_shorten)
        btn_shorten.pack(pady=6)

        btn_short_local = tk.Button(left, text='Shorten Localhost', bg='#00918a', fg='white', width=20, command=self.on_shorten_local)
        btn_short_local.pack(pady=6)

        btn_short_tunnel = tk.Button(left, text='Shorten Ngrok / Cloudflared', bg='#006b66', fg='white', width=20, command=self.on_shorten_tunnel)
        btn_short_tunnel.pack(pady=6)

        # session id
        tk.Label(left, text='Session ID:', fg='#c8ffff', bg='#071016').pack(pady=(12,2))
        self.sid_var = tk.StringVar()
        sid_entry = tk.Entry(left, textvariable=self.sid_var, width=30, font=('Segoe UI', 11))
        sid_entry.pack(pady=(0,6))
        tk.Button(left, text='Generate Session ID', bg='#00a89e', fg='white', command=self.on_gen_sid).pack(pady=6)

        # export buttons
        tk.Label(left, text='Export History:', fg='#c8ffff', bg='#071016').pack(pady=(14,4))
        tk.Button(left, text='Export HTML', bg='#0a8580', fg='white', width=20, command=self.on_export_html).pack(pady=4)
        tk.Button(left, text='Export CSV', bg='#0b6f6b', fg='white', width=20, command=self.on_export_csv).pack(pady=4)
        tk.Button(left, text='Export JSON', bg='#095d5a', fg='white', width=20, command=self.on_export_json).pack(pady=4)

        tk.Button(left, text='Open HTML History', bg='#033c39', fg='white', width=20, command=self.on_open_html).pack(pady=12)

        tk.Button(left, text='Exit', bg='#661111', fg='white', width=20, command=self.quit).pack(side='bottom', pady=12)

        # right: history table
        right = tk.Frame(main, bg='#071016')
        right.pack(side='left', fill='both', expand=True)

        cols = ('date', 'original', 'short')
        self.tree = ttk.Treeview(right, columns=cols, show='headings')
        self.tree.heading('date', text='Date')
        self.tree.heading('original', text='Original Link')
        self.tree.heading('short', text='Short Link')
        self.tree.column('date', width=160)
        self.tree.column('original', width=320)
        self.tree.column('short', width=240)
        self.tree.pack(fill='both', expand=True, padx=(0,6))

        # bottom status
        self.status = tk.Label(self, text='Ready', anchor='w', bg='#041016', fg='#9fdde0')
        self.status.pack(fill='x')

    # threaded ip loader
    def _load_ip(self):
        lan = get_local_ip()
        pub = get_public_ip()
        self.ip_label.config(text=f"LAN: {lan} | WAN: {pub}")

    # UI callbacks
    def on_shorten(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning('Input', 'Enter a URL first')
            return
        self.status.config(text='Shortening...')
        self.after(100, lambda: threading.Thread(target=self._shorten_and_add, args=(url,), daemon=True).start())

    def on_shorten_local(self):
        url = self.url_var.get().strip()
        if 'localhost' not in url:
            messagebox.showwarning('Localhost', 'Please enter a localhost URL (e.g. http://localhost:8080)')
            return
        self.on_shorten()

    def on_shorten_tunnel(self):
        url = self.url_var.get().strip()
        if not ('trycloudflare' in url or '.ngrok.io' in url):
            messagebox.showwarning('Tunnel', 'Enter a ngrok or trycloudflare link')
            return
        self.on_shorten()

    def _shorten_and_add(self, url):
        short = shorten_with_tinyurl(url)
        if short:
            self.history.add(url, short)
            self._insert_row({'date': datetime.now().isoformat(sep=' ', timespec='seconds'), 'original': url, 'short': short})
            self.status.config(text=f'Shortened: {short}')
        else:
            self.status.config(text='Failed to shorten')
            messagebox.showerror('Error', 'Could not shorten the provided URL')

    def _insert_row(self, e):
        self.tree.insert('', 0, values=(e['date'], e['original'], e['short']))

    def on_gen_sid(self):
        sid = gen_session_id()
        self.sid_var.set(sid)
        self.status.config(text=f'Generated SID: {sid}')

    def on_export_csv(self):
        path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files','*.csv')], initialfile=HISTORY_CSV)
        if not path:
            return
        ok = self.history.export_csv(path)
        if ok:
            messagebox.showinfo('Export', f'CSV saved: {ok}')
        else:
            messagebox.showerror('Export', 'Failed to save CSV')

    def on_export_json(self):
        path = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON files','*.json')], initialfile=HISTORY_JSON)
        if not path:
            return
        ok = self.history.export_json(path)
        if ok:
            messagebox.showinfo('Export', f'JSON saved: {ok}')
        else:
            messagebox.showerror('Export', 'Failed to save JSON')

    def on_export_html(self):
        path = filedialog.asksaveasfilename(defaultextension='.html', filetypes=[('HTML files','*.html')], initialfile=HISTORY_HTML)
        if not path:
            return
        ok = self.history.export_html(path)
        if ok:
            messagebox.showinfo('Export', f'HTML saved: {ok}')
        else:
            messagebox.showerror('Export', 'Failed to save HTML')

    def on_open_html(self):
        if os.path.exists(HISTORY_HTML):
            try:
                if platform.system() == 'Windows':
                    os.startfile(HISTORY_HTML)
                elif platform.system() == 'Darwin':
                    os.system(f'open "{HISTORY_HTML}"')
                else:
                    os.system(f'xdg-open "{HISTORY_HTML}"')
            except Exception:
                messagebox.showinfo('Open', f'Open the file manually: {os.path.abspath(HISTORY_HTML)}')
        else:
            messagebox.showwarning('Open', 'HTML history not found. Export first or create entries.')

# ---------- Run ----------

def main():
    app = TinyevilGUI()
    app.mainloop()

if __name__ == '__main__':
    main()
