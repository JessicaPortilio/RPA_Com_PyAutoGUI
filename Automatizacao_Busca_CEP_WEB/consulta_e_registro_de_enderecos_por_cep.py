import requests
import itertools
import threading
import time

def pesquisar_endereco_por_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        if 'erro' not in dados:
            rua = dados.get('logradouro', 'Não encontrado')
            bairro = dados.get('bairro', 'Não encontrado')
            cidade = dados.get('localidade', 'Não encontrado')
            cep_retornado = dados.get('cep', 'Não encontrado')
        else:
            rua, bairro, cidade, cep_retornado = 'Não encontrado', 'Não encontrado', 'Não encontrado', 'Não encontrado'
    except requests.RequestException as e:
        print(f'Erro ao conultar o CEP {cep}: {e}')
        
    return rua, bairro, cidade, cep_retornado


# Função para mostrar a animação de carregamento.
def mostrar_loading():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if feito:
            break
        print(f'\rCarregando {c}', end='', flush=True)
        time.sleep(0.1)

def main():
    nome_arquivo_cep = 'ceps.txt'
    global feito
    feito = False
    
    try:
        with open(nome_arquivo_cep, 'r', encoding='utf-8') as arquivo:
            ceps = arquivo.readlines()
    except FileNotFoundError:
           print(f'O arquivo {nome_arquivo_cep} não foi encontrado.')
    
    if not ceps:
        print('O arquivo de CEPs está vazio')
        return
    
    # Inicia o thread para a animação de carregamento.
    t = threading.Thread(target=mostrar_loading)
    t.start()
    
    nome_arquivo_resultado = 'resultados_ceps.txt'
    
    
    with open(nome_arquivo_resultado, 'w', encoding='utf-8') as arquivo:
        arquivo.write('Endereço,Bairro,Cidade,CEP\n')
        
        for cep in ceps[1:]:
            cep = cep.strip()
            if cep:
                rua, bairro, cidade, cep_retornado = pesquisar_endereco_por_cep(cep)
                arquivo.write(f'{rua},{bairro},{cidade},{cep_retornado}\n')
    
    feito = True
    t.join()
    
    print(f'\nOs resultados foram salvos em {nome_arquivo_cep}')
    

if __name__ == '__main__':
    main()