from tkinter import *
from tkinter import ttk
from main import repeticao_de_busca_aleatoria

root = Tk()
frm = ttk.Frame(root, padding=30 )

frm.grid()
ttk.Label(frm, text="Microsoft Reward automator", font=("Arial", 16), background="lightgrey", foreground="blue", relief="sunken").grid(column=0, row=1)

ttk.Label(frm, text="Quantas palavras você quer buscar ?").grid(column=0, row=10)

ttk.Spinbox(frm, from_=1, to=30, width=3, background="lightgrey", foreground="blue").grid(column=1, row=10)

ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=30)

def ola():
    print("hello world")

btn_inicializa = ttk.Button(frm, text="Inicializar", command=repeticao_de_busca_aleatoria)
btn_inicializa.grid(column=0, row=30)

root.mainloop()