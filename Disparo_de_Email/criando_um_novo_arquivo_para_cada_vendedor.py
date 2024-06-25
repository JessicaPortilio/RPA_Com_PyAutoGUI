
def organizar_dados_por_vendedores(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    
    cabecalho = linhas[0]
    linhas_dados = linhas[1:]
    
    dados_por_vendedores = {}
    
    for linha in linhas_dados:
        vendedor, produto, vendas = linha.strip().split(', ')
        if vendedor not in dados_por_vendedores:
            dados_por_vendedores[vendedor] = []
        dados_por_vendedores[vendedor].append(f'{vendedor}, {produto}, {vendas}')
    
    return cabecalho, dados_por_vendedores

def criar_arquivo_por_vendedor(cabecalho, dados_por_vendedores):
    arquivos_criados = []
    for vendedor, dados in dados_por_vendedores.items():
        caminho_arquivo_vendedor = f'D:\\RPA_Com_PyAutoGUI\\Arquvios_Vendedores_Separados\\{vendedor}.txt'
        with open(caminho_arquivo_vendedor, 'w', encoding='utf-8') as arquivo:
            arquivo.write(cabecalho)
            for dado in dados:
                arquivo.write(f'{dado}\n')
            arquivos_criados.append(caminho_arquivo_vendedor)
    return arquivos_criados

caminho_arquivo = 'vendas.txt'

cabecalho, dados_por_vendedores = organizar_dados_por_vendedores(caminho_arquivo)

arquivos_criados = criar_arquivo_por_vendedor(cabecalho, dados_por_vendedores)

print(arquivos_criados)