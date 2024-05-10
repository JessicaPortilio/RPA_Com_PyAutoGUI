import pyautogui

# text = A mensagem que vai ser exibida na caixa de diálogo
# title = O título da caixa de diálogo

senha = pyautogui.password(text='Digite sua senha:', title='Senha')

if len(senha) >= 6:
    pyautogui.alert(text='Sua senha tem mais de 6 caracteres')
else:
    pyautogui.alert(text='Sua senha é muito pequena')