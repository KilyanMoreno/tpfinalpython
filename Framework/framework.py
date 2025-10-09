import tkinter as tk
from tkinter import ttk
from tkinter import *

fenetre = tk.Tk()
fenetre.title("MA première framework")
fenetre.geometry("400x300")

label = ttk.Label(fenetre, text="Bonjour")
label.pack(pady=20)

entry = ttk.Entry(fenetre)
entry.pack()

def click_button():
    Toplevel()
button = ttk.Button(fenetre, text="Fenetre 2", command=click_button)
button.pack(side="top", padx=10, pady=5)
button.place(x=5, y=5)

text_fenetre = tk.Text(fenetre, height=5)
text_fenetre.pack()




if __name__ == "__main__":
    fenetre.mainloop()