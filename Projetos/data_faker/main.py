import csv
from faker import Faker

fake = Faker()

# Criando dados falsos para um banco de dados de usuários
with open('fakeusers.csv', 'w', newline='') as csvfile:
    fieldnames = ['nome', 'email', 'data_nascimento', 'endereço', 'telefone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for _ in range(1000):
        writer.writerow({
            'nome': fake.name(),
            'email': fake.email(),
            'data_nascimento': fake.date_of_birth(),
            'endereço': fake.address(),
            'telefone': fake.phone_number()

        })

