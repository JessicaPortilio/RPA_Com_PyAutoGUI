import pyautogui
import numpy as np
from PIL import ImageGrab
import cv2
import time

# Função para encontrar a região com a cor específica na tela
def encontrar_cor(cor_alvo):
    # Captura a tela
    imagem = np.array(ImageGrab.grab())

    # Define os limites inferior e superior para a cor alvo
    limiar = 20
    cor_inferior = np.array([max(0, cor - limiar) for cor in cor_alvo])
    cor_superior = np.array([min(255, cor + limiar) for cor in cor_alvo])

    # Converte a imagem para o espaço de cores HSV
    hsv_imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)

    # Cria uma máscara para filtrar os pixels que estão dentro do intervalo de cor desejado
    mascara = cv2.inRange(hsv_imagem, cor_inferior, cor_superior)

    # Encontra os contornos na máscara
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Se houver contornos encontrados, encontra o centro do maior contorno
    if contornos:
        maior_contorno = max(contornos, key=cv2.contourArea)
        momento = cv2.moments(maior_contorno)
        if momento["m00"] != 0:
            centro_x = int(momento["m10"] / momento["m00"])
            centro_y = int(momento["m01"] / momento["m00"])
            return centro_x, centro_y

    return None

# Função para clicar na região com a cor específica
def clicar_cor(cor_alvo):
    posicao = encontrar_cor(cor_alvo)
    if posicao:
        pyautogui.moveTo(posicao, duration=2)
        print("Moveu para a região com a cor específica em:", posicao)
    else:
        print("Não encontrou a região com a cor específica.")

# Cor alvo
cor_alvo = [181, 232, 34]

# Loop para clicar na região com a cor específica repetidamente
while True:
    clicar_cor(cor_alvo)
    # Aguarda um segundo antes de verificar novamente
    time.sleep(1)



# import pyautogui
# import time

# time.sleep(10)

# # Obtém a posição atual do mouse
# posicao_mouse = pyautogui.position()
# print("Posição atual do mouse:", posicao_mouse)

# # Obtém a cor do pixel na posição atual do mouse
# cor_pixel = pyautogui.pixel(posicao_mouse[0], posicao_mouse[1])
# print("Cor do pixel na posição do mouse:", cor_pixel)
