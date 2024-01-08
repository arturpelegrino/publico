import os, shutil

class constantes():

    def __init__(self):
        self.rota_planilha = rota_planilha = r"C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_downloader\input_downloader\input.xlsx" # <-- define a rota da planilha
        self.rota_validador = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_downloader\download_validator'
        self.rota_coletor = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_downloader\coletor_gru_downloader'
        self.rota_gru_log = r'C:\Users\artur\OneDrive\Área de Trabalho\Codes\PythonCodes\GRU_bot\gru_bot_downloader\log_status_download'

    def rota_cvm (self, cnpj, cpf):
        return f'https://cvmweb.cvm.gov.br/SAR/FormGRUTabD.aspx?tpPFPJ=PJ&idPartic={cnpj}&cpfSolic={cpf}'
    
class funções():

    def limpar_pasta(self, pasta):
        if os.path.exists(pasta):
            for pdf in os.scandir(pasta):
                os.remove(f'{pasta}\{pdf.name}')
        else:    
            os.makedirs(pasta)

    def limpar_input(self, wb, ws, rows, cpf_obj, rota_planilha):
        cpf_obj.value = ""
        for i in range(2, rows+1):
            for j in range(1,8):
                ws.cell(row=i, column=j).value=""
        wb.save(filename=rota_planilha)

    def clicar (self, chrome, xpath):
        chrome.find_element('xpath', xpath).click()

    def digitar(self, chrome, xpath, info):
        chrome.find_element('xpath', xpath).send_keys(info)
    
    def processar_download(self, rota_validador, rota_coletor, status_download, cnpj):
        vazio = []
        if os.listdir(rota_validador) == vazio:
            status_download.value = "download não realizado"
            return False
        else:
            for pdf in os.scandir(rota_validador):
                shutil.copy(f'{rota_validador}/{pdf.name}', f'{rota_coletor}/GRU_{cnpj}.pdf')
                status_download.value = "download realizado"
                os.remove(f'{rota_validador}/{pdf.name}')
                return True