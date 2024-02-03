from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")

options.add_experimental_option("excludeSwitches", ["enable-automation"])

# options.add_experimental_option("useAutomationExtension", False)

service = webdriver.ChromeService(executable_path=r'C:\Users\%username%\AppData\Roaming\undetected_chromedriver\undetected_chromedriver.exe')

chrome = webdriver.Chrome(service=service, options=options)

# chrome.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# useragentarray = [ 
# 	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
# 	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
# ] 

# for i in range(len(useragentarray)): 
# 	# Setting user agent iteratively as Chrome 108 and 107 
# 	chrome.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
# 	print(chrome.execute_script("return navigator.userAgent;")) 
# 	chrome.get("https://www.httpbin.org/headers")

chrome.get('https://sso.acesso.gov.br/login?client_id=www.gov.br&authorization_id=18d629b8bdb')

input('teste: ')