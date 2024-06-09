from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://www.google.com/')

input('Pressione Enter para fechar o navegador...')