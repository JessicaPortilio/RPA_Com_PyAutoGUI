import pyautogui  # Biblioteca para automação de controle do mouse e teclado
import time  # Biblioteca para manipulação de tempo
import keyboard  # Biblioteca para detecção de teclas pressionadas

# Dicionário que mapeia nomes de ações para os arquivos de imagem correspondentes
IMAGEM = {
    'BlueStacks': 'BlueStacks.png',
    'meusjogos': 'meusjogos.png',
    'CafeMania': 'CafeMania.png',
    'Jogar': 'Jogar.png'
}

# Função que imprime a posição atual do mouse na tela
def get_mouse():
    try:
        print(pyautogui.position())  # Imprime a posição do mouse
    except Exception as e:
        print(f"Erro ao obter a posição do mouse: {e}")  # Captura e imprime erros

# Função que procura e clica nas imagens especificadas
def image_game():
    # Dicionário para rastrear quais imagens já foram encontradas
    found_images = {'BlueStacks': False, 'meusjogos': False, 'CafeMania': False, 'Jogar': False}
    
    # Loop que continua até que todas as imagens sejam encontradas
    while not all(found_images.values()):
        # Se a imagem 'BlueStacks' ainda não foi encontrada
        if not found_images['BlueStacks']:
            try:
                # Procura a imagem na tela
                image_location = pyautogui.locateCenterOnScreen(IMAGEM['BlueStacks'], grayscale=True, confidence=0.8)
                print(f'BlueStacks: {image_location}')  # Imprime a posição da imagem encontrada
                if image_location is not None:
                    pyautogui.doubleClick(image_location)  # Dá um duplo clique na posição da imagem
                    found_images['BlueStacks'] = True  # Marca como encontrada
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'BlueStacks': {e}")  # Captura e imprime erros
        
        # Se a imagem 'meusjogos' ainda não foi encontrada
        if not found_images['meusjogos']:
            try:
                image_location = pyautogui.locateCenterOnScreen(IMAGEM['meusjogos'], grayscale=True, confidence=0.8)
                print(f'Meus Jogos: {image_location}')
                if image_location is not None:
                    pyautogui.click(image_location)  # Clica na posição da imagem
                    found_images['meusjogos'] = True  # Marca como encontrada
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'Meus Jogos': {e}")
        
        # Se a imagem 'CafeMania' ainda não foi encontrada
        if not found_images['CafeMania']:
            try:
                image_location = pyautogui.locateCenterOnScreen(IMAGEM['CafeMania'], grayscale=True, confidence=0.8)
                print(f'CafeMania: {image_location}')
                if image_location is not None:
                    pyautogui.click(image_location)  # Clica na posição da imagem
                    found_images['CafeMania'] = True  # Marca como encontrada
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'CafeMania': {e}")
        
        # Se a imagem 'Jogar' ainda não foi encontrada
        if not found_images['Jogar']:
            try:
                image_location = pyautogui.locateCenterOnScreen(IMAGEM['Jogar'], grayscale=True, confidence=0.8)
                print(f'Jogar: {image_location}')
                if image_location is not None:
                    pyautogui.click(image_location)  # Clica na posição da imagem
                    found_images['Jogar'] = True  # Marca como encontrada
            except Exception as e:
                print(f"Erro ao localizar ou clicar em 'Jogar': {e}")
        
        time.sleep(0.1)  # Pequeno atraso para evitar uso excessivo da CPU

# Adiciona um atalho de teclado: 'p' para obter a posição do mouse
keyboard.add_hotkey('p', get_mouse)
# Adiciona um atalho de teclado: 'i' para iniciar a função de procura das imagens
keyboard.add_hotkey('i', image_game)

# Loop infinito para manter o script ativo
print("Pressione 'p' ou 'i' para obter a posição do mouse ou iniciar o jogo. Pressione 'q' para sair.")
while True:
    if keyboard.is_pressed('q'):
        print("Saindo...")  # Imprime mensagem de saída
        break
    time.sleep(0.1)  # Pequeno atraso para evitar uso excessivo da CPU
