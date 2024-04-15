from pyautogui import moveTo, click, typewrite
from time import sleep

menu_inicial = 468,1049
barra_pesquisa = 772,154
calculadora = 590,347


# Tempo de espera para o computador pensar
sleep(1)
#print(pyautogui.position())

# Mover o mouse até o menu inicial
moveTo(menu_inicial, duration=0.5)

# Vou clicar no menu inical
click(menu_inicial, duration=0.5)

# Mover o mouse até a barra de pesquisa
moveTo(barra_pesquisa, duration=0.5)
# Vou clicar na barra de pesquisa
click(barra_pesquisa, duration=0.5)

# Vou digitar calculadora
typewrite('Calculadora')
# Vou mover o mouse até a calculadora
moveTo(calculadora, duration=0.5)
# Vou clicar na calculadora
click(calculadora, duration=0.5)