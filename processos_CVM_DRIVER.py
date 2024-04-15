import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from recursos import imagens
from PIL import Image, ImageTk
import time
        
class janelas:
    
    def __init__(self) -> None:
        pass
    
    
    def login(app):

# ------------------------------------- tela config -----------------------------------------

        telaLogin = ctk.CTk()

        logoItau = imagens().logoItau

        telaLogin.title('DISO - Reportes Regulatórios > CVM Driver > Entrar')
        telaLogin.iconbitmap(logoItau)

        telaLogin.resizable(0, 0)

        escala = telaLogin._get_window_scaling()

        xTela = telaLogin.winfo_screenwidth()
        yTela = telaLogin.winfo_screenheight()

        xLogin = 850
        yLogin = 650

        centroX = int(((xTela-xLogin)/2)*escala)
        centroY = int(((yTela-yLogin)/2)*escala)

        telaLogin.geometry(f'{xLogin}x{yLogin}+{centroX}+{centroY}')

        telaLogin.grid_rowconfigure(index=(0,1,2,3,4,5), weight=1)
        telaLogin.grid_columnconfigure(index=(0,1), weight=1, uniform="colunasLogin")

        # -------------------------------------- Login Background -----------------------------------------

        def clicar(event, telaLogin, seletorAmbiente):
            print(seletorAmbiente.get())
            telaLogin.destroy()
            

        rotaLoginBgItau = imagens().loginBgItau
        
        loginBgItau = ctk.CTkImage(light_image=Image.open(rotaLoginBgItau),
                                    dark_image=Image.open(rotaLoginBgItau),
                                    size=(425, 650))
        
        labelBgItau = ctk.CTkLabel(master=telaLogin, text="", image=loginBgItau)
        labelBgItau.grid_configure(row=0, column=0, rowspan=6, sticky="nw")

        # -------------------------------------- Msg de Boas-Vindas ----------------------------------
        boasVindasFrame = ctk.CTkFrame(master=telaLogin, fg_color="white", bg_color="white", corner_radius=0, border_width=0)
        boasVindasFrame.grid_configure(row=0, column=1, sticky="nswe")

        boasVindasFonte = ctk.CTkFont(family="Arial Rounded MT Bold", weight="normal", size=40)
        
        boasVindas = ctk.CTkLabel(master=boasVindasFrame, text="Seja bem-vindo,\nItuber!", text_color="#E97132",
                                  font=boasVindasFonte, justify="left")
        boasVindas.grid_configure(row=0, column=1, sticky="nw", padx=(60, 0), pady=(50, 0))

        # --------------------------------- Subtítulo de Boas-Vindas ----------------------------------
        comandoFrame = ctk.CTkFrame(master=telaLogin, fg_color="white", bg_color="white", corner_radius=0, border_width=0)
        comandoFrame.grid_configure(row=1, column=1, sticky="nswe")

        comandoFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        comando = ctk.CTkLabel(master=comandoFrame, text="Acesse sua conta:", text_color="#E97132", font=comandoFonte)
        comando.grid_configure(row=1, column=1, sticky="nw", padx=(60, 0), pady=(25, 0))

        # ----------------------------------------- Funcional ----------------------------------------
        funcionalFrame = ctk.CTkFrame(master=telaLogin, fg_color="white", bg_color="white", corner_radius=0, border_width=0)
        funcionalFrame.grid_columnconfigure(index=0, weight=1)
        funcionalFrame.grid_rowconfigure(index=(0, 1), weight=0)
        funcionalFrame.grid_configure(row=2, column=1, sticky="nswe")

        funcionalFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        tituloFuncional = ctk.CTkLabel(master=funcionalFrame, text="Funcional:", text_color="#3A3A3A", font=funcionalFonte)
        tituloFuncional.grid_configure(row=0, column=0, sticky="nw", padx=(60, 0), pady=(25, 0))

        entradaFuncional = ctk.CTkEntry(master=funcionalFrame, text_color="#3A3A3A", font=funcionalFonte, border_width=2.5,
                                        fg_color="white", placeholder_text_color="#AEAEAE", placeholder_text="", 
                                        border_color="#AEAEAE", height=50)
        entradaFuncional.grid_configure(row=1, column=0, sticky="ew", padx=60, pady=(5, 0))

        # ------------------------------------------ Senha --------------------------------------------------
        senhaFrame = ctk.CTkFrame(master=telaLogin, fg_color="white", bg_color="white", corner_radius=0, border_width=0)
        senhaFrame.grid_columnconfigure(index=0, weight=1)
        senhaFrame.grid_rowconfigure(index=(0, 1), weight=0)
        senhaFrame.grid_configure(row=3, column=1, sticky="nswe")

        senhaFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        tituloSenha = ctk.CTkLabel(master=senhaFrame, text="Senha:", text_color="#3A3A3A", font=senhaFonte)
        tituloSenha.grid_configure(row=0, column=0, sticky="nw", padx=(60, 0), pady=(25, 0))

        entradaSenha = ctk.CTkEntry(master=senhaFrame, text_color="#3A3A3A", font=senhaFonte, border_width=2.5,
                                        fg_color="white", placeholder_text_color="#AEAEAE", placeholder_text="", 
                                        border_color="#AEAEAE", height=50, show="*")
        entradaSenha.grid_configure(row=1, column=0, sticky="ew", padx=60, pady=(5, 0))

        # ----------------------------------------- Ambiente ------------------------------------------------
        ambienteFrame = ctk.CTkFrame(master=telaLogin, fg_color="white", bg_color="white", corner_radius=0, border_width=0)
        ambienteFrame.grid_columnconfigure(index=0, weight=1)
        ambienteFrame.grid_rowconfigure(index=(0, 1), weight=0)
        ambienteFrame.grid_configure(row=4, column=1, sticky="nswe")

        ambienteFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        tituloAmbiente = ctk.CTkLabel(master=ambienteFrame, text="Ambiente:", text_color="#3A3A3A", font=ambienteFonte)
        tituloAmbiente.grid_configure(row=0, column=0, sticky="nw", padx=(60, 0), pady=(25, 0))

        seletorAmbiente = ctk.CTkComboBox(master=ambienteFrame, border_width=2.5, height=50, text_color="#3A3A3A",
                                          font=ambienteFonte, fg_color="white", border_color="#AEAEAE", button_color="#AEAEAE",
                                          values=("Normal", "Estruturados"), dropdown_hover_color="#E97132")
        seletorAmbiente.grid_configure(row=1, column=0, sticky="ew", padx=60, pady=(5, 0))

        # ---------------------------------------- Botão de entrar --------------------------------------------
        entrarFrame = ctk.CTkFrame(master=telaLogin, fg_color="white", bg_color="white", corner_radius=0, border_width=0)
        entrarFrame.grid_columnconfigure(index=0, weight=1)
        entrarFrame.grid_configure(row=5, column=1, sticky="nswe")

        entrarFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        entrar = ctk.CTkLabel(master=entrarFrame, text="Entrar", text_color="#E97132", font=entrarFonte)
        entrar.bind('<Button>', lambda event="<Button>", telaLogin=telaLogin, seletorAmbiente=seletorAmbiente: clicar(event, telaLogin, seletorAmbiente))
        entrar.grid_configure(row=0, column=0, sticky="we", padx=0, pady=(40, 50))

        app.statusLogin = 1


        telaLogin.mainloop()

    def eventos(app):
        
        # ---------------------------------- tela config ------------------------------------------

        telaEventos = ctk.CTk()

        logoItau = imagens().logoItau

        telaEventos.title('DISO - Reportes Regulatórios > CVM Driver > Eventos')
        telaEventos.iconbitmap(logoItau)

        telaEventos.after(1, telaEventos.wm_state, 'zoomed')

        btn = ctk.CTkButton(telaEventos, text="ola")
        btn.pack_configure(side=ctk.BOTTOM)


        telaEventos.mainloop()