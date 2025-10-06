import tkinter as tk
from tkinter import ttk

fenetre = tk.Tk()
fenetre.title("MA première framework")
fenetre.geometry("400x300")

label = ttk.Label(fenetre, text="Bonjour")
label.pack(pady=20)

if __name__ == "__main__":
    fenetre.mainloop()

