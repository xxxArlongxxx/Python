import pyautogui as py
import time
import webbrowser
import subprocess

# Caminho correto da imagem a ser localizada
url_comece = 'C:/projetos_beeware/Python/Projetos/preditiva/assets/comece.png'

# Configurações do pyautogui
py.FAILSAFE = False  # Evita que o script pare se o mouse for para o canto superior esquerdo
py.PAUSE = 0.5       # Pausa de 0,5s entre cada comando do pyautogui


# Função que procura uma imagem na tela com confiança de 80%

def localizar_imagem(imagem):
    while True:
        try:
            posicao = py.locateOnScreen(imagem, confidence=0.8)
            if posicao is not None:
                print(f"Imagem localizada em: {posicao}")
                break
        except Exception as e:
            print(f"Erro ao localizar imagem: {e}")
        time.sleep(1)


# Abre o menu iniciar, digita "linkedin" e aperta Enter
py.press('win')
py.write('linkedin')
time.sleep(1)
py.press('enter')

# Aguarda o carregamento do LinkedIn e tenta localizar a imagem
position = localizar_imagem(url_comece)
# Clica na imagem localizada
py.click(position)
