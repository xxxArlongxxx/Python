# Importa as bibliotecas necessárias
import csv               # Para escrever arquivos CSV
from faker import Faker  # Para gerar dados falsos

# Cria uma instância do gerador de dados falsos
fake = Faker()

# Define os nomes das colunas que serão usadas no arquivo CSV
fieldnames = ['id', 'nome', 'email', 'telefone', 'endereco']

# Abre (ou cria) o arquivo 'usuarios.csv' no modo escrita ('w')
# O 'with' garante que o arquivo será fechado corretamente após o uso
with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:

    # Cria um escritor de arquivos CSV baseado em dicionários
    escritor = csv.DictWriter(arquivo, fieldnames=fieldnames)

    # Escreve a primeira linha (cabeçalho) com os nomes das colunas
    escritor.writeheader()

    # Gera 100 registros falsos
    for i in range(1, 101):  # Começa do 1 para usar como ID

        # Escreve uma nova linha com dados falsos para cada usuário
        escritor.writerow({
            'id': i,
            'nome': fake.name(),               # Nome completo
            'email': fake.email(),             # Endereço de e-mail
            'telefone': fake.phone_number(),   # Número de telefone
            'endereco': fake.address().replace('\n', ', ')  # Endereço, formatado em uma linha só
        })
