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

class Login(ctk.CTk):

    def __init__(self):
        super().__init__()

        logoItau = imagens().logoItau

        self.title('DISO | Dados Fiduciários > CVM Driver > Entrar')
        self.iconbitmap(logoItau)

        self.resizable(0, 0)

        escala = self._get_window_scaling()

        xTela = self.winfo_screenwidth()
        yTela = self.winfo_screenheight()

        xLogin = 850
        yLogin = 650

        centroX = int(((xTela-xLogin)/2)*escala)
        centroY = int(((yTela-yLogin)/2)*escala)

        self.geometry(f'{xLogin}x{yLogin}+{centroX}+{centroY}')

        self.grid_rowconfigure(index=(0,1,2,3,4,5), weight=1)
        self.grid_columnconfigure(index=(0,1), weight=1, uniform="colunasLogin")

        janelas.login(self)


if __name__ == "__main__":

    login = Login()

    login.mainloop()

# -------------- mudança de root --------------

# def sair(app):
#     app.destroy()

# app = ctk.CTk()

# app.geometry("500x500")

# button = tk.Button(master=app, text="sair", command=lambda app=app: sair(app))
# button.pack()

# app.mainloop()

# app = ctk.CTk()

# app.geometry("1000x1000")

# app.mainloop()








