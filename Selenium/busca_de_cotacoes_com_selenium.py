from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from time import sleep

import os

abrindoNavegador = webdriver.Chrome()

abrindoNavegador.get('https://www.google.com/')

sleep(2)

campo_busca = abrindoNavegador.find_element(By.NAME, 'q')

campo_busca.send_keys('Dolar hoje')

sleep(1)

campo_busca.send_keys(Keys.RETURN)

sleep(1)

valorDolarHoje = abrindoNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

print(f'Dolar: {valorDolarHoje}')

sleep(1)

campo_busca = abrindoNavegador.find_element(By.NAME, 'q')
campo_busca.clear()

sleep(1)

campo_busca.send_keys('Euro hoje')

sleep(1)

campo_busca.send_keys(Keys.RETURN)

sleep(1)

valorEuroHoje = abrindoNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

print(f'Euro: {valorEuroHoje}')

nomeCaminhoArquivo = 'Valores_Dolar_Euro.txt'

with open(nomeCaminhoArquivo, 'w') as arquivo:
    arquivo.write(f'Dolar: {valorDolarHoje} \n')
    arquivo.write(f'Euro: {valorEuroHoje} \n')

os.startfile(nomeCaminhoArquivo)    
# input('Pressione Enter para fechar o navegador...')