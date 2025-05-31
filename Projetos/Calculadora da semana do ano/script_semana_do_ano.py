# Importação das bibliotecas necessárias
import tkinter as tk                      # Biblioteca padrão para criação de interfaces gráficas
from tkinter import messagebox            # Módulo para exibir mensagens de erro e alertas
from datetime import datetime             # Classe para manipulação de datas

# Função para calcular o número da semana do ano com base na data informada
def calcular_semana(event=None):
    try:
        data_str = entry_data.get()  # Captura o texto digitado no campo de entrada

        # Validação simples do formato esperado da data: DD/MM/AAAA
        if len(data_str) != 10 or data_str[2] != '/' or data_str[5] != '/':
            raise ValueError("Formato inválido. Use DD/MM/AAAA.")

        # Converte a string para um objeto datetime
        data = datetime.strptime(data_str, "%d/%m/%Y")

        # Extrai o número da semana e o ano ISO usando o calendário ISO 8601
        semana = data.isocalendar()[1]
        ano_semana = data.isocalendar()[0]

        # Exibe o resultado no rótulo
        label_resultado.config(text=f"Semana {semana} de {ano_semana}")
    except ValueError as ve:
        # Em caso de erro (como data inválida), exibe uma janela de erro e limpa o resultado
        messagebox.showerror("Erro", str(ve))
        label_resultado.config(text="")

# Função que encerra o programa, associada à tecla Esc
def fechar_app(event=None):
    root.quit()

# === Configuração da Janela Principal ===
root = tk.Tk()                                  # Criação da janela principal
root.title("Calculadora das 52 Semanas")        # Título da janela
root.geometry("500x400")                        # Dimensões fixas da janela
root.config(bg="white")                         # Cor de fundo da janela
root.resizable(False, False)                    # Impede redimensionamento
root.bind("<Escape>", fechar_app)               # Associa a tecla Esc à função de fechamento

# === Cabeçalho ===
header_frame = tk.Frame(root, bg="#FF7F32", height=80)  # Área superior colorida (laranja)
header_frame.pack(fill="x")                             # Preenche horizontalmente
label_header = tk.Label(
    header_frame,
    text="Calculadora das 52 Semanas",
    font=("Helvetica", 20, "bold"),
    fg="white",
    bg="#FF7F32"
)
label_header.pack(expand=True)

# === Área de Conteúdo Principal ===
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Rótulo de instrução
label_instrucao = tk.Label(
    content_frame,
    text="Por favor, insira a data (DD/MM/AAAA):",
    font=("Helvetica", 14),
    fg="#333",
    bg="white"
)
label_instrucao.pack(pady=(20, 10))

# Campo de entrada para a data
entry_data = tk.Entry(
    content_frame,
    font=("Helvetica", 16),
    width=20,
    justify="center",
    bd=2,
    relief="solid"
)
entry_data.pack(pady=10)
entry_data.bind("<Return>", calcular_semana)  # Pressionar Enter chama a função calcular_semana

# Botão que executa o cálculo da semana
botao_calcular = tk.Button(
    content_frame,
    text="Calcular Semana",
    font=("Helvetica", 16),
    fg="white",
    bg="#FF7F32",
    bd=2,
    relief="raised",
    command=calcular_semana  # Chama a função ao clicar
)
botao_calcular.pack(pady=20)

# Rótulo onde o resultado será exibido
label_resultado = tk.Label(
    content_frame,
    text="",
    font=("Helvetica", 16),
    fg="#333",
    bg="white"
)
label_resultado.pack(pady=20)

# === Rodapé com Assinatura ===
footer_frame = tk.Frame(root, bg="white")
footer_frame.pack(fill="x", side="bottom", padx=10, pady=10)
label_assinatura = tk.Label(
    footer_frame,
    text="Desenvolvido por Dione Nascimento",
    font=("Helvetica", 10, "italic", "bold"),
    fg="#FF7F32",
    bg="white"
)
label_assinatura.pack(side="right")

# Inicia o loop principal da interface gráfica
root.mainloop()
