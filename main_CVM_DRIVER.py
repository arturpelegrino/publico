# ------------------------------------ processos e recursos ----------------------------------------
from recursos import rotas, imagens
from processos import janelas

# ----------------------------------------- bibliotecas --------------------------------------------
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import time
import sys

# --------------------------------------------- drivers config -------------------------------------
# from ctypes import windll
# windll.shcore.SetProcessDpiAwareness(1) #<-- desembaçar a tela

# ------------------------------------------------ execução ----------------------------------------

class App():
    
    def __init__(self) -> None:
        self.statusLogin = 0
        self.concluir = 0

    def abrirLogin(self) -> None:
        janelas.login(self)

    def abrirEventos(self) -> None:
        janelas.eventos(self)

if __name__ == "__main__":

    app = App()

    app.abrirLogin()

    if app.statusLogin == 1:

        app.abrirEventos()
        print('logado')

    if app.concluir == 1:

        sys.exit()

# -------------- mudança de root --------------

# def sair(event, app):
#     app.destroy()
#     print('ola')

# app = ctk.CTk()

# app.geometry("500x500")

# # button = tk.Button(master=app, text="sair", command=lambda app=app: sair(app))

# button = ttk.Button(master=app, text="sair")
# button.bind("<Button>", lambda event="<Button>", app=app: sair(event, app))
# button.pack()

# app.mainloop()

# app = ctk.CTk()

# app.geometry("1000x1000")

# app.mainloop()