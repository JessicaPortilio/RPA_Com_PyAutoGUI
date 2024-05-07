import pyautogui

# text = A mensagem que vai ser exibida na caixa de diálogo
# title = O título da caixa de diálogo

confirmacao = pyautogui.confirm(text ='Você está gostando de apreender sobre PyAutoGUI?', title = 'Confirmação', buttons=['Sim', 'Não'])
print(confirmacao)