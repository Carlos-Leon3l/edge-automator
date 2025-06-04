from tkinter import *
from tkinter import ttk
from main import inicializa_automator

#ESSE ARQUIVO E O QUE DEVE SER INICIALIZADO 
root = Tk()
root.title("Microsoft Rewards Automator")

frm = ttk.Frame(root, padding=30 )
frm.grid()

ttk.Label(frm, text="Microsoft Reward automator", font=("Arial", 15), background="lightgrey", foreground="blue", relief="sunken", padding=10).grid(column=0, row=0, columnspan=2, pady=(0,20))

ttk.Label(frm, text="Quantas palavras você quer buscar ?").grid(column=0, row=1, sticky=W)

quantidade = IntVar()

ttk.Spinbox(frm, textvariable=quantidade, from_=1, to=30, width=5, background="lightgrey", foreground="blue", justify="center").grid(column=1, row=1, padx=(10,0))

def iniciar_busca():
    btn_inicializar.config(text="Executando...", state=DISABLED)
    root.update_idletasks() 

    valor = int(quantidade.get())
    inicializa_automator(valor)

    btn_inicializar.config(text="Inicializar", state=NORMAL)

ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=2, pady=20)

btn_inicializar = ttk.Button(frm, text="Inicializar", command=iniciar_busca)
btn_inicializar.grid(column=1, row=2, pady=20,)

root.mainloop()