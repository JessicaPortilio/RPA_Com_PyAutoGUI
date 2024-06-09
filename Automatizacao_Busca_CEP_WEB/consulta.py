import requests  # Importa a biblioteca 'requests', que é usada para fazer solicitações HTTP (pedidos de informações na web).
import itertools  # Importa 'itertools' para criar ciclos de caracteres para a animação de carregamento.
import threading  # Importa 'threading' para criar e controlar threads (linhas de execução paralelas).
import time  # Importa 'time' para controlar o tempo da animação de carregamento.

# Função que consulta o endereço correspondente a um CEP usando a API do ViaCEP.
def pesquisar_endereco_por_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'  # Monta a URL da API do ViaCEP com o CEP fornecido.
    try:
        response = requests.get(url)  # Faz a solicitação à API ViaCEP usando o CEP.
        response.raise_for_status()  # Verifica se a resposta da solicitação não teve erros.
        dados = response.json()  # Converte a resposta em formato JSON para um dicionário Python.
        
        # Verifica se a resposta não contém erros.
        if 'erro' not in dados:
            rua = dados.get('logradouro', 'Não encontrado')  # Pega o nome da rua ou define 'Não encontrado' se não existir.
            bairro = dados.get('bairro', 'Não encontrado')  # Pega o nome do bairro ou define 'Não encontrado' se não existir.
            cidade = dados.get('localidade', 'Não encontrado')  # Pega o nome da cidade ou define 'Não encontrado' se não existir.
            cep_retornado = dados.get('cep', 'Não encontrado')  # Pega o CEP ou define 'Não encontrado' se não existir.
        else:
            rua, bairro, cidade, cep_retornado = 'Não encontrado', 'Não encontrado', 'Não encontrado', 'Não encontrado'
    except requests.RequestException as e:
        # Define as variáveis como 'Erro na consulta' se houver um erro na solicitação.
        rua, bairro, cidade, cep_retornado = 'Erro na consulta', 'Erro na consulta', 'Erro na consulta', 'Erro na consulta'
        print(f"Erro ao consultar o CEP {cep}: {e}")  # Imprime uma mensagem de erro no console.
    
    # Retorna as informações obtidas (rua, bairro, cidade e CEP).
    return rua, bairro, cidade, cep_retornado

# Função para mostrar a animação de carregamento.
def mostrar_loading():
    # Inicia um loop infinito que clica entre os caracteres: '|', '/', '-', '\'
    for c in itertools.cycle(['|', '/', '-', '\\']):
        # Verifica se a variável 'feito' foi definida como True para sair do loop
        if feito:
            break
        # Imprime o caractere de carregamento atual no mesmo local do terminal (substituindo o anterior)
        print(f'\rCarregando {c}', end='', flush=True)
        # Pausa por 0.1 segundo para criar a animação de carregamento
        time.sleep(0.1)


# Função principal do programa.
def main():
    global feito
    feito = False
    nome_arquivo_cep = 'ceps.txt'  # Nome do arquivo que contém a lista de CEPs a serem pesquisados.
    
    try:
        # Tenta abrir o arquivo de CEPs e ler seu conteúdo.
        with open(nome_arquivo_cep, 'r', encoding='utf-8') as arquivo:
            ceps = arquivo.readlines()  # Lê todas as linhas do arquivo e as armazena na lista 'ceps'.
    except FileNotFoundError:
        # Imprime uma mensagem de erro se o arquivo de CEPs não for encontrado e termina a execução.
        print(f"O arquivo {nome_arquivo_cep} não foi encontrado.")
        return
    
    # Verifica se o arquivo de CEPs está vazio.
    if not ceps:
        print("O arquivo de CEPs está vazio.")  # Imprime uma mensagem de erro se o arquivo estiver vazio.
        return

    # Inicia o thread para a animação de carregamento.
    t = threading.Thread(target=mostrar_loading)
    t.start()

    nome_arquivo_resultados = 'resultados_ceps.txt'  # Nome do arquivo onde os resultados serão salvos.
    
    # Abre o arquivo de resultados para escrita.
    with open(nome_arquivo_resultados, 'w', encoding='utf-8') as file:
        file.write('Endereco,Bairro,Cidade,CEP\n')  # Escreve o cabeçalho das colunas no arquivo de resultados.
        
        # Itera sobre cada linha de CEP no arquivo, ignorando o cabeçalho.
        for cep in ceps[1:]:
            cep = cep.strip()  # Remove espaços em branco ao redor do CEP.
            if cep:  # Verifica se a linha não está vazia.
                rua, bairro, cidade, cep_retornado = pesquisar_endereco_por_cep(cep)  # Pesquisa o endereço para o CEP.
                file.write(f'{rua},{bairro},{cidade},{cep_retornado}\n')  # Escreve os resultados no arquivo de resultados.

    feito = True  # Indica que o carregamento terminou.
    t.join()  # Aguarda o thread da animação terminar.

    # Imprime uma mensagem informando que os resultados foram salvos com sucesso.
    print(f"\nOs resultados foram salvos em {nome_arquivo_resultados}")

# Executa a função principal se este arquivo for executado diretamente.
if __name__ == "__main__":
    main()
