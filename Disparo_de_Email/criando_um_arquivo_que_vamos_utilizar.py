dados = """Vendedor, Produtos, Vendas
Ana, Computadores, 1500
Ana, Monitores, 400
Ana, Teclados, 500
Ana, Tables, 100
João, Monitores, 300
João, Impressoras, 200
João, Mouses, 200
Maria, Teclados, 500
Maria, Tablets, 100
Carlos, Mouses, 700
Carlos, Notebooks, 300
Carlos, Smartphones, 900
Carlos, Monitores, 400
Carlos, Impressoras, 600
Fernanda, Impressoras, 400
Fernanda, Smartphones, 150
Lucas, Notebooks, 800
Lucas, Computadores, 600
Julia, Tablets, 600
Julia, Mouses, 200
Roberto, Smartphones, 900
Roberto, Teclados, 250
"""

caminho_arquivo = 'vendas.txt'
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(dados)