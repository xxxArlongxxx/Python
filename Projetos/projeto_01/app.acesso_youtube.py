import pyautogui #importa a biblioteca pyautogui que é responsável por controlar o mouse e o teclado
import time #importa a biblioteca time que é responsável por controlar o tempo de execução do código em segundos
import pyperclip #importa a biblioteca pyperclip que é responsável por copiar e colar textos
import pandas as pd #importa a biblioteca pandas que é responsável por manipular arquivos excel
import sys #importa a biblioteca sys que é responsável por controlar o sistema

q = ' '.join(sys.argv[1:]) #pega o argumento passado pelo usuário e armazena na variável q


pyautogui.sleep(1) #aguarda 1 segundos
pyautogui.press('win') #pressiona a tecla do windows
pyautogui.sleep(1) #aguarda 1 segundos
pyautogui.typewrite('chrome') #escreve chrome
pyautogui.sleep(1) #aguarda 2 segundos
pyautogui.press('enter') #pressiona a tecla enterPython no Portal da Manuteno
pyautogui.sleep(2) #aguarda 2 segundos
pyautogui.moveTo(190, 70) #move o mouse para as coordenadas 150, 150
pyautogui.sleep(1) #aguarda 1 segundos
pyautogui.click(190, 70) #clica no campo de pesquisaPython no Portal da Manuteno
pyautogui.typewrite('https://www.youtube.com/@Portal_da_Manuten%C3%A7%C3%A3o/featured') #escreve o link do youtube
pyautogui.press('enter') #pressiona a tecla enter
pyautogui.sleep(7) #aguarda 5 segundos
pyautogui.click(400, 135) #clica no campo de pesquisa
pyautogui.sleep(2) #aguarda 2 segundos
pyautogui.click(400, 135) #clica no campo de pesquisa
pyautogui.typewrite('Python no Portal da Manutenção') #escreve o argumento passado pelo usuário
pyautogui.press('enter') #pressiona a tecla enter
pyautogui.sleep(2) #aguarda 2 segundos
pyautogui.moveTo(500, 500)
pyautogui.click(500, 500) #clica no vídeo

'''
print("Pressione Ctrl + C para parar.")
while True:
    x, y = pyautogui.position()
    print(f"Posição do mouse: X={x}, Y={y}", end="\r")  # Atualiza na mesma linha
    time.sleep(0.1)  # Reduz a taxa de atualização
'''