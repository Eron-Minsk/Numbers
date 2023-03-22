import tkinter as tk
from num2words import num2words
import clipboard

def convert_number():
    number = int(entry.get())
    words = num2words(number, lang=language.get()).split("-")
    words = "\n".join(words)
    result_label.config(text=words, font=("Arial", 7))

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

def copy():
    clipboard.copy(result_label.cget("text"))

root = tk.Tk()
root.title("Number to Words Converter")
root.geometry("300x300")
root.configure(bg="white")

label = tk.Label(root, text="Please enter a number", font=("Arial", 12), bg="white")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

language = tk.StringVar(root)
language.set("en")
language_dropdown = tk.OptionMenu(root, language, "en", "fr", "es", "de", "it", "pt", "ru", "tr", "id", "ar", "hi", "bn", "fa", "ja", "ko", "zh-CN", "zh-TW")
language_dropdown.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_number, bg="blue", fg="white", font=("Arial", 12), bd=0)
convert_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear, bg="red", fg="white", font=("Arial", 12), bd=0)
clear_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy", command=copy, bg="green", fg="white", font=("Arial", 12), bd=0)
copy_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 7), bg="white")
result_label.pack(pady=10)

root.mainloop()