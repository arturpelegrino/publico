import time
from selenium.webdriver.common.by import By
class constantes():

    def __init__(self):
        self.name = "teste"
        self.nome_completo = self.name + ' mais'

class funções(constantes):

    def esperar(constantes):
        time.sleep(5)
        print(constantes.name)
    
    def printar(self, x: str):
        print(x)

    @staticmethod
    def pintar(x):
        print(x)