import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from recursos import imagens
from PIL import Image, ImageTk
        
class janelas:
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def login(janelaPrincipal):
        # -------------------------------------- Login Background -----------------------------------------
        rotaLoginBgItau = imagens().loginBgItau
        
        loginBgItau = ctk.CTkImage(light_image=Image.open(rotaLoginBgItau),
                                    dark_image=Image.open(rotaLoginBgItau),
                                    size=(425, 650))
        
        labelBgItau = ctk.CTkLabel(master=janelaPrincipal, text="", image=loginBgItau)
        labelBgItau.grid_configure(row=0, column=0, rowspan=6, sticky="nw")

        # -------------------------------------- Msg de Boas-Vindas ----------------------------------
        boasVindasFrame = ctk.CTkFrame(master=janelaPrincipal, fg_color="white", corner_radius=0, border_width=0)
        boasVindasFrame.grid_configure(row=0, column=1, sticky="nswe")

        boasVindasFonte = ctk.CTkFont(family="Arial Rounded MT Bold", weight="normal", size=40)
        
        boasVindas = ctk.CTkLabel(master=boasVindasFrame, text="Seja bem-vindo,\nItuber!", text_color="#E97132",
                                  font=boasVindasFonte, justify="left")
        boasVindas.grid_configure(row=0, column=1, sticky="nw", padx=(60, 0), pady=(50, 0))

        # --------------------------------- Subtítulo de Boas-Vindas ----------------------------------
        comandoFrame = ctk.CTkFrame(master=janelaPrincipal, fg_color="white", corner_radius=0, border_width=0)
        comandoFrame.grid_configure(row=1, column=1, sticky="nswe")

        comandoFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        comando = ctk.CTkLabel(master=comandoFrame, text="Acesse sua conta:", text_color="#E97132", font=comandoFonte)
        comando.grid_configure(row=1, column=1, sticky="nw", padx=(60, 0), pady=(25, 0))

        # ----------------------------------------- Funcional ----------------------------------------
        funcionalFrame = ctk.CTkFrame(master=janelaPrincipal, fg_color="white", corner_radius=0, border_width=0)
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
        senhaFrame = ctk.CTkFrame(master=janelaPrincipal, fg_color="white", corner_radius=0, border_width=0)
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
        ambienteFrame = ctk.CTkFrame(master=janelaPrincipal, fg_color="white", corner_radius=0, border_width=0)
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
        entrarFrame = ctk.CTkFrame(master=janelaPrincipal, fg_color="white", corner_radius=0, border_width=0)
        entrarFrame.grid_columnconfigure(index=0, weight=1)
        entrarFrame.grid_configure(row=5, column=1, sticky="nswe")

        entrarFonte = ctk.CTkFont(family="Arial", weight="bold", size=16)

        entrar = ctk.CTkLabel(master=entrarFrame, text="Entrar", text_color="#E97132", font=entrarFonte)
        entrar.grid_configure(row=0, column=0, sticky="we", padx=0, pady=(25, 50))
        

        