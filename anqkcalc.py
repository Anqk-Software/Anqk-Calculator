import tkinter as tk
from tkinter import messagebox
import math
from cryptography.fernet import Fernet

# Encrypting and decrypting history
def save_history(data, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data.encode())
    with open("history.enc", "wb") as f:
        f.write(encrypted)

def load_history(key):
    cipher = Fernet(key)
    try:
        with open("history.enc", "rb") as f:
            encrypted = f.read()
            return cipher.decrypt(encrypted).decode()
    except FileNotFoundError:
        return ""

# Setting up the calculator
class AnqkCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("AnqkCalc")
        self.root.geometry("350x450")  # Initial window size
        self.root.config(bg="#f0f0f0")  # Optional: Set background color
        self.root.wm_attributes('-fullscreen', True)  # Start in fullscreen mode
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Define the buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("sqrt", 5, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=3, font=("Arial", 12), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Make sure rows and columns expand evenly
        for i in range(6):  # 6 rows (including the entry)
            self.root.grid_rowconfigure(i, weight=1)

        for i in range(4):  # 4 columns
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            current = self.result_var.get()
            self.result_var.set(current + text)

# Setting up the main app window
def run_app():
    root = tk.Tk()
    app = AnqkCalc(root)
    root.mainloop()

run_app()

