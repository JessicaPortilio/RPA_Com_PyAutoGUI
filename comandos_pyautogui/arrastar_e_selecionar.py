import pyautogui
from time import sleep

# Tempe de espera
# sleep(5)

# Pega a posição do mouse
# print(pyautogui.position())

# Move o mouse até as coordenadas
pyautogui.moveTo(x=117, y=123, duration=1)

# Pressiona o botão do mouse
pyautogui.mouseDown()

# Arrasta o mouse até a possição desejada
pyautogui.dragTo(x=21, y=123, duration=1)

# Solta o botão do mouse
pyautogui.mouseUp()