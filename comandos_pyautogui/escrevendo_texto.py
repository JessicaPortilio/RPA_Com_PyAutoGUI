import pyautogui
from time import sleep

# Tempo de espera
# sleep(4)

# Pegando a posição do mouse
# print(pyautogui.position())

# Move o mouse para as coordenadas x e y em 1 segundo
pyautogui.moveTo(x=356, y=1050, duration=1)

# Clica no local atual do mouse
pyautogui.click()

# Digita algo com um intervalo de meio segundo entre cada caractere
pyautogui.typewrite('Calculadora', interval=1)
