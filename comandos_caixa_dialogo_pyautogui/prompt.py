import pyautogui

# text = A mensagem que vai ser exibida na caixa de diálogo
# title = O título da caixa de diálogo
# default = Um valor padrão pré-preenchido na caixa de texto (LEMBRANDO É OPCIONAL) 

resposta = pyautogui.prompt(text='Qual é o seu nome?', title = 'Pergunta')

if resposta:
    pyautogui.alert(text= f'Olá, {resposta}', title = 'Caixinha de alerta')
else:
    pyautogui.alert(text= 'Você não digitou nada', title = 'Caixinha de alerta')