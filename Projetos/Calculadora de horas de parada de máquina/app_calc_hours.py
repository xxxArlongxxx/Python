import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def calcular_diferenca(event=None):
    try:
        data1_str = entry_data1.get().strip()
        data2_str = entry_data2.get().strip()

        formato = "%d/%m/%Y %H:%M:%S"
        data1 = datetime.strptime(data1_str, formato)
        data2 = datetime.strptime(data2_str, formato)

        diferenca_segundos = abs((data2 - data1).total_seconds())
        diferenca_horas = diferenca_segundos / 3600
        diferenca_minutos = diferenca_segundos / 60

        label_resultado_horas.config(
            text=f"Total de: {diferenca_horas:.2f}".replace('.', ',') + " horas")
        label_resultado_minutos.config(
            text=f"Total de: ({diferenca_minutos:.2f}".replace('.', ',') + " minutos)")
    except ValueError:
        messagebox.showerror(
            "Erro", "Formato inválido. Use DD/MM/AAAA HH:MM:SS.")
        label_resultado_horas.config(text="")
        label_resultado_minutos.config(text="")


def fechar_app(event=None):
    root.destroy()


# Janela principal
root = tk.Tk()
root.title("Calculadora Horas de Parada")
root.geometry("500x400")
root.config(bg="white")
root.resizable(False, False)
root.bind("<Escape>", fechar_app)

# --- Cabeçalho ---
header_frame = tk.Frame(root, bg="#FF7F32", height=80)
header_frame.pack(fill="x")
label_header = tk.Label(header_frame, text="Calculadora Horas de Parada", font=(
    "Helvetica", 18, "bold"), fg="white", bg="#FF7F32")
label_header.pack(expand=True)

# --- Área de Conteúdo ---
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand=True, padx=20, pady=20)

label_instrucao = tk.Label(content_frame, text="Digite data e hora (DD/MM/AAAA HH:MM:SS):",
                           font=("Helvetica", 14), fg="#333", bg="white")
label_instrucao.pack(pady=(10, 5))

entry_data1 = tk.Entry(content_frame, font=(
    "Helvetica", 14), width=25, justify="center", bd=2, relief="solid")
entry_data1.pack(pady=5)
entry_data1.bind("<Return>", calcular_diferenca)

entry_data2 = tk.Entry(content_frame, font=(
    "Helvetica", 14), width=25, justify="center", bd=2, relief="solid")
entry_data2.pack(pady=5)
entry_data2.bind("<Return>", calcular_diferenca)

botao_calcular = tk.Button(content_frame, text="Calcular Diferença", font=(
    "Helvetica", 16), fg="white", bg="#FF7F32", bd=2, relief="raised", command=calcular_diferenca)
botao_calcular.pack(pady=15)

label_resultado_horas = tk.Label(content_frame, text="", font=(
    "Helvetica", 16), fg="#333", bg="white")
label_resultado_horas.pack()

label_resultado_minutos = tk.Label(
    content_frame, text="", font=("Helvetica", 16), fg="#333", bg="white")
label_resultado_minutos.pack()

# --- Rodapé ---
footer_frame = tk.Frame(root, bg="white")
footer_frame.pack(fill="x", side="bottom", padx=10, pady=10)
label_assinatura = tk.Label(footer_frame, text="Desenvolvido por Dione Nascimento", font=(
    "Helvetica", 10, "italic", "bold"), fg="#FF7F32", bg="white")
label_assinatura.pack(side="right")

root.mainloop()
