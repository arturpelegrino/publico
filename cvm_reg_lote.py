from cvm_reg_class import constantes, funções
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    firefox = p.firefox.launch(headless=False)
    pag = firefox.new_page()
    pag.goto('https://sso.acesso.gov.br/login?client_id=www.gov.br&authorization_id=18d629b8bdb')
    pag.get_by_
    input('teste: ')
    firefox.close()

pag.locator('teste')

