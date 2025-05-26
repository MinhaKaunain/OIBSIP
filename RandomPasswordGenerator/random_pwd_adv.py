import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password():
    length = length_var.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")
        return

    length = int(length)
    chars = ''
    if letters_var.get():
        chars += string.ascii_letters
    if numbers_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Password Length:").pack()
length_var = tk.StringVar()
tk.Entry(root, textvariable=length_var).pack()

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=('Arial', 14), justify='center').pack()

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
