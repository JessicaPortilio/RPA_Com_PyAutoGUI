from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

abrirNavegador = webdriver.Chrome()
abrirNavegador.get('https://www2.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm')

sleep(3)

campo_endereco = abrirNavegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/input')
campo_endereco.clear()
campo_endereco.send_keys('01517100')

sleep(1)

abrirNavegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input').click()

sleep(1)

try:
    rua = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]').text
    bairro = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text
    cidade = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]').text
    cep = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]').text
except:
    rua, bairro, cidade, cep = 'Não encotrado', 'Não encontrado', 'Não encontrado', '01517100'


print(f' Rua: {rua}, Bairro: {bairro}, Cidade: {cidade}, Cep: {cep}')
input('Pressione Enter para fechar o navegador...')