
#importa a biblioteca OpenCV, ela é usada para capturar a imagem da webcam.
import cv2 

#importa a biblioteca time, ela é usada para gerar um nome único para a foto com base na data e hora.
import time 

#importa a biblioteca tkinter, ela é usada para criar a interface gráfica do aplicativo.
import tkinter as tk 

#importa a função messagebox da biblioteca tkinter, ela é usada para exibir mensagens de erro e sucesso.
from tkinter import messagebox 

#importa as bibliotecas Image e ImageTk da biblioteca PIL, elas são usadas para exibir a imagem da webcam na interface.
from PIL import Image, ImageTk 

#importa a biblioteca os, ela é usada para criar a pasta "fotos" caso não exista.
import os 

# Cria a variável pasta_fotos com o nome da pasta onde as fotos serão salvas
pasta_fotos = "fotos"

#Se a pasta "fotos" não existir, ela é criada.
if not os.path.exists(pasta_fotos):
    os.makedirs(pasta_fotos)

# Função para tirar a foto, ela é chamada quando o botão "Tirar Foto" é clicado.

def tirar_foto():

#O método cap.read() retorna dois valores: ret e frame. O valor ret é um booleano que indica se a imagem foi capturada com sucesso. O valor frame é a imagem capturada pela webcam    
    ret, frame = cap.read()
    
    # Se a imagem foi capturada com sucesso
    if ret:
        # Gera um nome único para a foto com base na data e hora
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(pasta_fotos, f"foto_{timestamp}.jpg")  # Foto salva na pasta 'fotos'
        
        # Salva a foto com o nome gerado
        cv2.imwrite(filename, frame)
        print(f"Foto salva como {filename}")
        
        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Foto Tirada", f"Foto salva como {filename}")
    else:
        messagebox.showerror("Erro", "Não foi possível capturar a foto.")

# Função para fechar o aplicativo
def fechar_aplicativo():
    cap.release()  # Libera a câmera
    root.quit()    # Encerra o aplicativo

# Cria a janela principal do Tkinter
root = tk.Tk()
root.title("Aplicativo de Captura de Foto")

# Define o tamanho da janela e a cor de fundo
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Inicia a captura de vídeo pela webcam
cap = cv2.VideoCapture(0)

# Função para atualizar a imagem da webcam na interface
def atualizar_imagem():
    ret, frame = cap.read()
    if ret:
        # Converte o frame para o formato que o Tkinter consegue exibir
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imagem = Image.fromarray(frame_rgb)
        imagem = imagem.resize((400, 300))  # Redimensiona a imagem para caber na tela
        imagem_tk = ImageTk.PhotoImage(imagem)
        
        # Atualiza o painel de imagem
        painel_imagem.config(image=imagem_tk)
        painel_imagem.image = imagem_tk
    
    # Chama a função de atualização a cada 20ms
    painel_imagem.after(20, atualizar_imagem)

# Painel para exibir a imagem da webcam
painel_imagem = tk.Label(root, bd=2, relief="solid", padx=5, pady=5)
painel_imagem.pack(pady=20)

# Título da interface
titulo = tk.Label(root, text="Bem-vindo ao Aplicativo de Captura de Foto", font=("Helvetica", 16), bg="#f0f0f0")
titulo.pack(pady=10)

# Frame para organizar os botões
frame_botoes = tk.Frame(root, bg="#f0f0f0")
frame_botoes.pack(pady=10)

# Botão para tirar a foto
botao_tirar_foto = tk.Button(frame_botoes, text="Tirar Foto", width=20, height=2, bg="#4CAF50", fg="white", font=("Helvetica", 12), command=tirar_foto)
botao_tirar_foto.grid(row=0, column=0, padx=10)

# Botão para fechar o aplicativo
botao_fechar = tk.Button(frame_botoes, text="Fechar", width=20, height=2, bg="#f44336", fg="white", font=("Helvetica", 12), command=fechar_aplicativo)
botao_fechar.grid(row=0, column=1, padx=10)

# Inicia a atualização da imagem da webcam
atualizar_imagem()

# Inicia o loop principal do Tkinter
root.mainloop()
