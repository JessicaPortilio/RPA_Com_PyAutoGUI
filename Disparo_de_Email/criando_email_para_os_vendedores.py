vendedores_emails = {
    "Ana": "ana@example.com",
    "João": "joao@example.com",
    "Maria": "maria@example.com",
    "Carlos": "carlos@example.com",
    "Fernanda": "fernanda@example.com",
    "Lucas": "lucas@example.com",
    "Julia": "julia@example.com",
    "Roberto": "roberto@example.com"
}

def criar_arquivo_vendedores_emails(vendedores_emails, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        for vendedor, email in vendedores_emails.items():
            arquivo.write(f'{vendedor}, {email}\n')

caminho_arquivo = 'vendedores_emails.txt'

criar_arquivo_vendedores_emails(vendedores_emails, caminho_arquivo)