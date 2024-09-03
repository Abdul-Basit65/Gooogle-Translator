import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to perform translation
def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

# Function to update the translation
def data():
    s = combo_sor.get()
    d = combo_dest.get()
    msg = sor_txt.get(1.0, tk.END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, tk.END)
    dest_txt.insert(tk.END, textget)

# Create main window
root = tk.Tk()
root.title("Google Translator")
root.geometry("500x700")
root.config(bg="black")

# Title label
lab_txt = tk.Label(root, text="Google Translator", font=("Time New Roman", 35, "bold"), bg="black", fg="white")
lab_txt.place(x=40, y=40, height=50, width=420)

# Frame for combobox and text widgets
frame = tk.Frame(root).pack(side=tk.BOTTOM)

# Get list of languages from googletrans
languages = list(LANGUAGES.values())

# Source language dropdown
combo_sor = ttk.Combobox(frame, values=languages)
combo_sor.place(x=40, y=125, height=50, width=150)
combo_sor.set("English")

# Destination language dropdown
combo_dest = ttk.Combobox(frame, values=languages)
combo_dest.place(x=290, y=125, height=50, width=150)
combo_dest.set("Hindi")

# Source text input
sor_txt = tk.Text(frame, font=("Time New Roman", 20, "bold"), wrap=tk.WORD)
sor_txt.place(x=10, y=190, height=200, width=480)

# Destination text output
dest_txt = tk.Text(frame, font=("Time New Roman", 20, "bold"), wrap=tk.WORD)
dest_txt.place(x=10, y=400, height=200, width=480)

# Translate button
translate_btn = tk.Button(frame, text="Translate", relief=tk.RAISED, command=data)
translate_btn.place(x=190, y=620, height=50, width=100)

# Run the main loop
root.mainloop()
