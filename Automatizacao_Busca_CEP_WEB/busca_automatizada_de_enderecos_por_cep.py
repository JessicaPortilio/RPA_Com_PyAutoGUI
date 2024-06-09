from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

def buscar_dados_por_cep(cep):

    abrirNavegador = webdriver.Chrome()
    abrirNavegador.get('https://www2.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm')

    sleep(3)

    campo_endereco = abrirNavegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/input')
    campo_endereco.clear()
    campo_endereco.send_keys(cep)

    sleep(1)

    abrirNavegador.find_element(By.XPATH, '//*[@id="Geral"]/div/div/div[6]/input').click()

    sleep(1)

    try:
        rua = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]').text
        bairro = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]').text
        cidade = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[3]').text
        cep = abrirNavegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]').text

        abrirNavegador.quit()
        
        return rua, bairro, cidade, cep
        
    except:
        abrirNavegador.quit()
        return 'Não encotrado', 'Não encontrado', 'Não encontrado', cep


def buscar_dados_por_arquivo(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        ceps = arquivo.readlines()
    
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        for cep in ceps[1:]:
            cep = cep.strip()
            rua, bairro, cidade, cep_retornado = buscar_dados_por_cep(cep)
            arquivo.write(f'CEP: {cep}, Rua: {rua}, Bairro: {bairro}, Cidade: {cidade}, CEP Retornado: {cep_retornado}\n')

arquivo_entrada = 'ceps.txt'
arquivo_saida = 'dados_ceps.txt'

buscar_dados_por_arquivo(arquivo_entrada, arquivo_saida)

print(f'Processo concluído. Verifique o arquivo {arquivo_saida} para os resultados!')
