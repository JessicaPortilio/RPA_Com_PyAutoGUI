import pyautogui
import time
import keyboard

IMAGEM = {
    'BlueStacks': 'BlueStacks.png',
    'meusjogos': 'meusjogos.png',
    'Cafemania': 'CafeMania.png',
    'Jogar': 'Jogar.png'
}

def image_game():
    imagens_encontradas = {'BlueStacks' : False, 'meusjogos': False, 'Cafemania': False, 'Jogar': False}
    while not all(imagens_encontradas.values()):
        
        if not imagens_encontradas['BlueStacks']:
            try:
                posicao_da_imagem_localizada = pyautogui.locateCenterOnScreen(IMAGEM['BlueStacks'],grayscale= True , confidence=0.8)
                print(f'BlueStacks: {posicao_da_imagem_localizada}')
                if posicao_da_imagem_localizada != None:
                    pyautogui.doubleClick(posicao_da_imagem_localizada)
                    imagens_encontradas['BlueStacks'] = True
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'BlueStacks': {e}")
        
        if not imagens_encontradas['meusjogos']:
            try:
                posicao_da_imagem_localizada = pyautogui.locateCenterOnScreen(IMAGEM['meusjogos'],grayscale= True , confidence=0.8)
                print(f'meusjogos: {posicao_da_imagem_localizada}')
                if posicao_da_imagem_localizada != None:
                    pyautogui.click(posicao_da_imagem_localizada)
                    imagens_encontradas['meusjogos'] = True
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'meusjogos': {e}")
    
        if not imagens_encontradas['Cafemania']:
            try:
                posicao_da_imagem_localizada = pyautogui.locateCenterOnScreen(IMAGEM['Cafemania'],grayscale= True , confidence=0.8)
                print(f'Cafemania: {posicao_da_imagem_localizada}')
                if posicao_da_imagem_localizada != None:
                    pyautogui.click(posicao_da_imagem_localizada)
                    imagens_encontradas['Cafemania'] = True
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'Cafemania': {e}")
        
        if not imagens_encontradas['Jogar']:
            try:
                posicao_da_imagem_localizada = pyautogui.locateCenterOnScreen(IMAGEM['Jogar'],grayscale= True , confidence=0.8)
                print(f'Jogar: {posicao_da_imagem_localizada}')
                if posicao_da_imagem_localizada != None:
                    pyautogui.click(posicao_da_imagem_localizada)
                    imagens_encontradas['Jogar'] = True
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'Jogar': {e}")
        
        time.sleep(0.1)


keyboard.add_hotkey('i', image_game)

print(f"Pressione 'i' para inicializar a busca pelas imagens ou pressione 's' para sair.")

while True:
    if keyboard.is_pressed('s'):
        print('Saindo...')
        break
    time.sleep(0.1)
        