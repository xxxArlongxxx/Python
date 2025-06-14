import csv
from faker import Faker

fake = Faker('pt_BR')  # Configurando o Faker para o português do Brasil

# Criando dados falsos para um banco de dados de usuários
with open('fakeusers.csv', 'w', newline='') as csvfile:
    fieldnames = ['nome', 'email', 'data_nascimento', 'estado', 'cidade', 'telefone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(10000):
        writer.writerow({
            'nome': fake.name(),
            'email': fake.email(),
            'data_nascimento': fake.date_of_birth(),
            'estado': fake.state(),
            'cidade': fake.city(),
            'telefone': fake.phone_number()

        })

