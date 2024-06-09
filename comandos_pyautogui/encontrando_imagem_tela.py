import pyautogui

try:
   x, y = pyautogui.locateCenterOnScreen('Lixeira.png')
   pyautogui.moveTo(x=x, y=y, duration=1)
   pyautogui.doubleClick()
except Exception as erro:
    print(f' Error: {erro}')
    
    
