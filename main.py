import tkinter as tk
from tkinter import messagebox
import webbrowser

def search_place():
    keyword = keyword_entry.get().strip()
    if not keyword:
        messagebox.showinfo("Info", "Please write what you'd like to search for ")
        return
    url = f"https://www.google.com/maps/search/{keyword}"
    webbrowser.open(url)

window = tk.Tk()
window.title("Place Finder")
window.resizable(False, False)  # Prevent maximizing
width = 600
height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))
window.geometry(f"{width}x{height}+{x}+{y}")

window.configure(bg="#e6f2ff")

title_label = tk.Label(
    window,
    text="Welcome!\nWhat are you looking for?",
    bg="#e6f2ff",
    fg="#085078",
    font=("Arial", 18, "bold"),
    justify="center"
)
title_label.pack(pady=(60, 12))

info_label = tk.Label(
    window,
    text="Restaurant, cafe, park, pharmacy...\nWrite anything that comes to your mind!",
    bg="#e6f2ff",
    fg="#008892",
    font=("Arial", 13),
    justify="center"
)
info_label.pack(pady=(0, 36))

frame = tk.Frame(window, bg="#e6f2ff")
frame.pack(pady=5)
frame.pack_propagate(0)
frame.place(relx=0.5, rely=0.4, anchor="center")

keyword_entry = tk.Entry(frame, width=32, font=("Arial", 14), justify="center")
keyword_entry.grid(row=0, column=0, padx=(0,12))
keyword_entry.focus()

search_button = tk.Button(
    frame,
    text="🔍 Search",
    font=("Arial", 12, "bold"),
    bg="#51c4d3",
    fg="#ffffff",
    relief=tk.FLAT,
    padx=12, pady=6,
    activebackground="#126e82",
    command=search_place
)
search_button.grid(row=0, column=1)

frame.update_idletasks()
frame_width = frame.winfo_width()
frame.place(relx=0.5, rely=0.5, anchor="center")

hint_label = tk.Label(
    window,
    text="You can also press Enter to search.",
    bg="#e6f2ff",
    fg="#2e2e2e",
    font=("Arial", 10),
    justify="center"
)
hint_label.place(relx=0.5, rely=0.57, anchor="center")

window.bind("<Return>", lambda event: search_place())

window.mainloop()