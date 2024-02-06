from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

os.system("start chrome.exe --remote-debugging-port=9222")

input('teste: ')

chromeOptions = Options()

chromeOptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome = webdriver.Chrome(options=chromeOptions)

input("teste: ")

chrome.get('https://contas.acesso.gov.br/alteracao_cadastro')

input('teste: ')