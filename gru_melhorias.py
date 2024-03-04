#class
class funções():
    @staticmethod
    def criar_tbl_log (i, rows, cnpj, status_download):
        tbl_log = ""

        if i == 2:

            tbl_log = f'<style> th {{background-color: orange; color: white;}} \
table, th, td {{border: 1px solid grey; border-collapse: collapse;padding: 5px;}} \
table tr:nth-child(odd) {{background-color: rgb(237, 237, 237);}} </style> \
<table><tr><th>cnpj</th><th>status_download</th></tr>'
            
        elif i == rows:

            tbl_log = f'<tr><td>{cnpj}</td><td>{status_download}</td></tr></table>'

        else:
            
            tbl_log = f'<tr><td>{cnpj}</td><td>{status_download}</td></tr>'

        return tbl_log
    
#main
tbl_log = "" # <--- tabela de registro fica fora para não zerar seu valor a cada iteração
try:
    tbl_log += f.criar_tbl_log(i, rows, cnpj, status_download.value)
except:
    tbl_log += f.criar_tbl_log(i, rows, cnpj, status_download.value)
