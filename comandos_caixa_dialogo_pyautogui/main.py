from pyautogui import alert, confirm, password, prompt

alert(text='Bem-vindo ao programa de interação com PyAutoGUI!', title='Mensagem')

confirmacao = confirm(text='Você gostaria de participar de uma pesquisa rápida?', title='Confirmação', buttons=['Sim', 'Não'])

if confirmacao == 'Sim':
    nome = prompt(text='Por favor, digite seu nome:', title='Pergunta')
    idade = prompt(text='Por favor, digite sua idade:', title='Pergunta')
    senha = password(text='Por favor, digite sua senha:', title='Pergunta')
    
    if len(senha) > 12:
        alert(text= f'Obrigada por participar, {nome}! Você tem {idade} anos e sua senha é forte', title='Mensagem')
    else:
        alert(text= f'Obrigada por participar, {nome}! Você tem {idade} anos e sua senha é fraca', title='Mensagem')
else:
   alert(text='Tudo bem, talvez na próxima!', title='Mensagem') 