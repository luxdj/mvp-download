import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser

LICENSE_SERVER = "http://localhost:8001"

def check_and_download():
    url = entry.get().strip()

    if not url:
        messagebox.showerror("Greška", "Ubaci SoundCloud link")
        return

    try:
        r = requests.get(LICENSE_SERVER)
        data = r.json()

        if data.get("download_allowed"):
            messagebox.showinfo(
                "Dozvoljeno",
                "Autor je dozvolio download.\nOtvoriće se zvanični link."
            )
            webbrowser.open(url)
        else:
            messagebox.showwarning(
                "Nije dozvoljeno",
                "Download nije dozvoljen.\nKontaktiraj autora."
            )

    except Exception as e:
        messagebox.showerror("Greška", f"Licencni server nije dostupan\n{e}")

# GUI
root = tk.Tk()
root.title("Legal Music Downloader")

tk.Label(root, text="SoundCloud link:").pack(pady=5)
entry = tk.Entry(root, width=60)
entry.pack(padx=10)

tk.Button(root, text="Check & Download", command=check_and_download).pack(pady=15)

root.mainloop()