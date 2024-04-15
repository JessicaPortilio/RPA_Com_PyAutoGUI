from pyautogui import hotkey, typewrite, press
from time import sleep

# Tempo de espera
sleep(1)

# abrindo o excutar do windows
hotkey('win', 'r')

sleep(1)

# Escrevendo calc
typewrite('calc')

sleep(1)

# apertando enter
press('enter')