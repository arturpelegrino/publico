class rotas():

    def __init__(self):
        self.dados = 'fundos.xlsx'

class xpaths():

    def __init__(self):
        self.cnpj_fundo = '//*[@id="containerView"]/div[2]/div/div[2]/table/thead/tr[2]/th[4]/input'
        self.buscar_fundo = '//*[@id="containerView"]/div[2]/div/div[2]/table/tbody/tr/td[8]/a'
        self.participantes = '//*[@id="containerView"]/div[2]/div[2]/fieldset/div/div[3]/div/div/div'
        self.alterar_auditor = '//*[@id="containerView"]/div/fieldset/div/div[3]/div/fieldset/div[1]/div/div/table/tbody/tr/td[5]/a[1]'
        self.cnpj_auditor = '//*[@id="inputNumeroRegistroPessoaJuridica"]'
        self.data_alteracao = '//*[@id="inputDataInicioAuditorIndependente"]'
        self.cancelar_alteracao = '//*[@id="popupAlterarAuditorIndependenteFundo"]/div[2]/div/div/div[2]/form/div[8]/div/a[1]'
        self.voltar_perfil = '//*[@id="containerView"]/div/div[3]/div/a'
        self.voltar_buscador = '//*[@id="containerView"]/div[2]/div[2]/div[1]/div/a'