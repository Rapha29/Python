import tkinter as tk
from tkinter import font

def button1_click():
    label.config(text="Eu também te amo ♥!")

def button2_click():
    label.config(text="Não mente, clica em sim logo!")

root = tk.Tk()
root.title("Exemplo com 2 Botões")

root.geometry("400x200")

font_size = font.nametofont("TkDefaultFont")
font_size.configure(size=14)

label = tk.Label(root, text="Me ama?", font=font_size)
label.pack()

button1 = tk.Button(root, text="Sim", command=button1_click, font=font_size)
button1.pack()

button2 = tk.Button(root, text="Não", command=button2_click, font=font_size)
button2.pack()

root.mainloop()
