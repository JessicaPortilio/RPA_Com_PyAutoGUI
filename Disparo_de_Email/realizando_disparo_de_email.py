import win32com.client as win32
import os

outlook = win32.Dispatch('outlook.application')

nome_arquivo = 'vendedores_emails.txt'

with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    dados = linha.strip().split(', ')
    nome = dados[0]
    email = dados[1]
    
    emailOutlook = outlook.CreateItem(0)
    
    emailOutlook.To = email
    
    emailOutlook.HTMLBody = emailOutlook.HTMLBody = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 20px auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 8px;
                background-color: #f9f9f9;
            }}
            .header {{
                background-color: #007bff;
                color: #fff;
                text-align: center;
                padding: 10px;
                border-radius: 8px 8px 0 0;
            }}
            .content {{
                padding: 20px;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>Relatório de Vendas</h2>
            </div>
            <div class="content">
                <p>Olá <b>{nome}</b>,</p>
                <p>Espero que esteja bem. Segue abaixo o relatório com suas vendas mais recentes:</p>
                <p>Atenciosamente,</p>
            </div>
            <div class="footer">
                <p>Este é um e-mail automático. Por favor, não responda.</p>
            </div>
        </div>
    </body>
    </html>
"""

    anexoEmail = f'D:\\RPA_Com_PyAutoGUI\\Arquvios_Vendedores_Separados\\{nome}.txt'
    
    if os.path.exists(anexoEmail):
        emailOutlook.Attachments.Add(anexoEmail)
    else:
        print(f'Arquivo {anexoEmail} não encontrado.')

    emailOutlook.Save()  # emailOutlook.Send()