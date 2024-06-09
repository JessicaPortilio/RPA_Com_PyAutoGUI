from pyautogui import moveTo, doubleClick, locateCenterOnScreen
from time import sleep

# Imagens
BLUESTACKS = 'BlueStacks.png'
MEUSJOGOS = 'meusjogos.png'
CAFEMANIA = 'CafeMania.png'
JOGAR = 'Jogar.png'

# Constantes
MAX_TENTATIVAS = 15
MAX_TENTATIVAS_IMAGEM = 10 
TEMPO_ESPERA = 0.5
TEMPO_JOGAR = 50

def localizar_e_clicar(imagem, max_tentativas = MAX_TENTATIVAS_IMAGEM, tempo_espera = TEMPO_ESPERA):
    tentativas = 0
    while tentativas < max_tentativas:
        try:
            localizao = locateCenterOnScreen(imagem, confidence=0.8)
            if localizao:
                moveTo(localizao, duration=tempo_espera)
                doubleClick()
                return True
        except Exception as e:
            print(f'Error ao tentar localizar {imagem}: {e}')
        tentativas +=1 
    print(f'Não foi possível localizar {imagem} após {max_tentativas} tentativas')
    return False


indice = 0
local_jogo_flag = False
finalizou_flag = False
while indice < MAX_TENTATIVAS and not local_jogo_flag:
    try:
        local_jogo = locateCenterOnScreen(BLUESTACKS, confidence=0.8)
        if local_jogo:
            local_jogo_flag = True
            
            moveTo(local_jogo, duration=TEMPO_ESPERA)
            doubleClick()
            
            x = 0
            meusjogos_flag = False
            while x < MAX_TENTATIVAS_IMAGEM and not meusjogos_flag:
                if localizar_e_clicar(MEUSJOGOS):
                    meusjogos_flag = True
                    n1 = 0
                    cafemania_flag = False
                    while n1 < MAX_TENTATIVAS_IMAGEM and not cafemania_flag:
                        if localizar_e_clicar(CAFEMANIA):
                            cafemania_flag = True
                            sleep(TEMPO_JOGAR)
                            if localizar_e_clicar(JOGAR):
                                finalizou_flag = True
                                break
                        n1 += 1
                x +=1    
            
    except Exception as e:
        print(f'Erro inesperado: {e}')

    indice += 1


if finalizou_flag:
    print("Tarefa concluída com sucesso!")
else:
    print("Imagem não encontrada.")