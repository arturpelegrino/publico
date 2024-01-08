import os, shutil

class constantes():

    def __init__(self):
        self.rota_sample = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_manager\sample_status_transf.xlsx'
        self.rota_input = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_manager\input_transf'
        self.rota_fundos = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\Efetivações'
        self.rota_erros = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_manager\erro_transf'
        self.rota_transf_log = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_manager\log_status_transf'

class funções():
    
    def limpar_pasta(self, pasta):
        if os.path.exists(pasta):
            for pdf in os.scandir(pasta):
                os.remove(os.path.join(pasta, pdf.name))
        else:
            os.makedirs(pasta)

    def pasta_existente(self, rota_fundo, cnpj_pnl, cnpj, status_transf, rota_pdf, pdf):
        pasta_mais_rct = None
        tmp_mais_rct = 0
        num_pastas = 0
        
        for pasta in os.scandir(rota_fundo):
            if status_transf.value != None:
                break
            else:
                if os.path.isdir(f"{rota_fundo}/{pasta.name}"):
                    num_pastas += 1
                    if os.path.exists(f"{rota_fundo}/{pasta.name}/GRU_{cnpj}.pdf"):
                        cnpj_pnl.value = cnpj
                        status_transf.value = f"transferência já realizada: para {pasta.name}"
                        break
                    else: 
                        tmp_mod = pasta.stat().st_mtime_ns
                        if tmp_mod > tmp_mais_rct:
                            pasta_mais_rct = f"{rota_fundo}/{pasta.name}"
                            tmp_mais_rct = tmp_mod
        
        if status_transf.value == None:        
            if num_pastas == 0:
                if os.path.exists(os.path.join(rota_fundo, pdf)):
                    cnpj_pnl.value = cnpj
                    status_transf.value = "transferência já realizada: pasta do fundo"
                else:
                    cnpj_pnl.value = cnpj
                    status_transf.value = "transferência realizada: pasta do fundo"
                    shutil.copy(rota_pdf, os.path.join(rota_fundo, pdf))
            else:
                cnpj_pnl.value = cnpj
                status_transf.value = "transferência realizada: pasta recentemente modificada"
                shutil.copy(rota_pdf, os.path.join(pasta_mais_rct, pdf))

    def pasta_inexistente(self, cnpj_pnl, cnpj, status_transf, rota_erros, pdf, rota_pdf):
        cnpj_pnl.value = cnpj
        status_transf.value = "transferência não realizada: pasta não encontrada"
        rota_erro = os.path.join(rota_erros, pdf)
        shutil.copy(rota_pdf, rota_erro)
