import pyautogui as py
import time
import cv2 as cv
import os
import pyperclip
import webbrowser as wb

# Caminho absoluto ou relativo válido
start_publishing = 'C:/projetos_beeware/Python/Projetos/curso_de_python/Aula_05/assets/start_publishing.png'
chatgpt = 'C:/projetos_beeware/Python/Projetos/curso_de_python/Aula_05/assets/chatgpt.png'
publishing = 'C:/projetos_beeware/Python/Projetos/curso_de_python/Aula_05/assets/publishing.png'


py.PAUSE = 1
py.FAILSAFE = True


def localization_onClick(img):
    # Verifica se a imagem existe antes
    if not os.path.exists(img):
        print("Imagem não encontrada no caminho especificado!")
    else:
        localizacao = py.locateOnScreen(img, confidence=0.8)
        if localizacao:
            x, y = py.center(localizacao)
            py.moveTo(x, y, duration=0.5)
            py.click()
        else:
            print("Imagem não localizada na tela.")


py.press('win')
time.sleep(1)
py.write('linkedIn')
time.sleep(1)
py.press('enter')
time.sleep(1)
localization_onClick(img=start_publishing)
time.sleep(1)

mensagem = '''

Fala, pessoal!

Essa mensagem aqui foi escrita por Python.
Isso mesmo. Uma automação simples fez tudo sozinho.

A ideia foi mostrar como dá pra automatizar até post no LinkedIn.
Usei código pra abrir o navegador, escrever o texto e publicar.
Tudo no automático.

Dá pra aplicar isso em várias rotinas do dia a dia.
Simples, prático e direto ao ponto.

#PortalDosDados #Automação #Python #Produtividade #PowerBI

Quer aprender como faz isso?
Segue meu canal no YouTube que vou mostrar o passo a passo lá!

https://www.youtube.com/@Portal_dos_Dados


'''

# Copia o texto para a área de transferência
pyperclip.copy(mensagem)

# Cola o conteúdo com Ctrl + V
py.hotkey('ctrl', 'v')


#publica a mensagem
localization_onClick(img=publishing)

time.sleep(2)
py.hotkey('alt', 'f4')  # Fecha a janela do LinkedIn
time.sleep(1)

wb.open_new_tab('https://www.youtube.com/@Portal_dos_Dados')

