import tkinter as tk
from tkinter import ttk
import requests
from webbrowser import open_new_tab

def fetch_headers():
    url = url_entry.get()
    try:
        response = requests.get(url)
        headers_text.delete('1.0', tk.END)
        headers_text.insert('1.0', str(response.headers))
    except Exception as e:
        result_display.config(text=str(e))

def send_headers():
    url = url_entry.get()
    headers = headers_text.get('1.0', tk.END)
    try:
        headers_dict = eval(headers)
        response = requests.get(url, headers=headers_dict)
        open_new_tab(response.url)
    except Exception as e:
        result_display.config(text=str(e))

root = tk.Tk()
root.title("HTTP Headers Tool")

url_label = tk.Label(root, text="URL:")
url_label.pack(side=tk.TOP, fill=tk.X)

url_entry = tk.Entry(root)
url_entry.pack(side=tk.TOP, fill=tk.X)

headers_label = tk.Label(root, text="Headers:")
headers_label.pack(side=tk.TOP, fill=tk.X)

headers_text = tk.Text(root, height=10)
headers_text.pack(side=tk.TOP, fill=tk.X)

fetch_button = tk.Button(root, text="Fetch Headers", command=fetch_headers)
fetch_button.pack(side=tk.LEFT, expand=True)

send_button = tk.Button(root, text="Send Headers", command=send_headers)
send_button.pack(side=tk.RIGHT, expand=True)

result_display = tk.Label(root, text="", relief=tk.SUNKEN)
result_display.pack(side=tk.BOTTOM, fill=tk.X)

signature_label = tk.Label(root, text="Made by DHX", font=("Arial", 8))
signature_label.pack(side=tk.BOTTOM, fill=tk.X)

roo
t.mainloop()
