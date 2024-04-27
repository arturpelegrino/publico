from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.firefox.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = browser.new_page()

    # page.goto("https://cvmweb.cvm.gov.br/swb/default.asp?sg_sistema=sic")

    # page.goto("https://cvmweb.cvm.gov.br/SWB/Sistemas/SIC/Home.asp?SWBPILHAMENU=sic")

    page.goto("https://sso.acesso.gov.br/login")

    # mainFrame = page.frame(name='SubMain')

    # mainFrame.locator('xpath=//*[@id="linkGovBr"]').click()

    # page.locator('xpath=//*[@id="linkGovBr"]').click()

    page.locator('xpath=/html/body/div[1]/main/form/div[1]/div[2]/input').fill('') # <- CPF
    page.locator('xpath=/html/body/div[1]/main/form/div[1]/div[2]/div/button').click()
    page.locator('xpath=/html/body/div[1]/main/form/div[1]/div[1]/input').fill('') # <- Senha
    page.locator('xpath=/html/body/div[1]/main/form/div[1]/div[2]/button[2]').click()

    input('teste: ')

    page.goto("https://cvmweb.cvm.gov.br/SWB/Sistemas/SIC/Fundos/fundos.asp")
    page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/div/select').select_option(value='9888')
    # page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/form/div[2]/div/select/option[3]').click()
    page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[2]/form/div[3]/div/a').click()
    page.locator('xpath=/html/body/div[1]/div[1]/div[7]/div/div/div[2]/div[3]/div[4]/div/div/div').click()
    input('test: ')
    page.locator('/html/body/div[1]/div[1]/div[7]/div[2]/div/div[2]/table/thead/tr[2]/th[4]/input').fill('') # <- cnpj fundo
    
    input('teste: ')
    browser.close()