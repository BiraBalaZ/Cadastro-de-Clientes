import random
import fake_data as fake

# Creating client_list
client_list = []

# Randomizing data
for i in range(150):
    #first_name = random.choice(['Erick', 'Sarah', 'Fernanda', 'Renata', 'Fabio', 'Sheila', 'Renato', 'Victória', 'Gabriele', 'Mariana', 'Beatriz', 'Priscila', 'Gustavo', 'Bruno', 'Fabiano', 'Murilo', 'Gabriel', 'Pedro', 'Fagner', 'Luiz', 'João', 'Kleber', 'Rebeca', 'Victor', 'Lívia', 'Carol', 'Ana', 'Anna', 'Júlia', 'Heitor', 'Paulo', 'Letícia'])
    #second_name = random.choice(['Monteiro', 'Alcaide', 'Fernandes', 'dos Anjos', 'Martins', 'de Souza', 'Souza', 'de Sousa', 'Sousa', 'Reis', 'Salim', 'Mendonça', 'José', 'Viviani', 'dos Santos', 'Rodrigues', 'Henrique', 'Potter', 'Brás', 'Araújo', 'Emanoel', 'Carolina', 'Carolyna', 'Carvalho', 'Medeiros', 'Marin', 'Vieira', 'Falcão', 'Silva', 'da Silva'])
    #email = random.choice(['@gmail.com', '@outlook', '@hotmail.com', '@yahoo.com'])

    name = f'{random.choice(fake.first_name)} {random.choice(fake.second_name)}'

    # Dictionary
    client_dict = {
        'name': name, 
        'contact': f'+55 (11) 9{random.randrange(1000, 9999, 1)}-{random.randrange(1000, 9999, 1)}',
        'email': f'{name.lower()}{random.choice(fake.email)}'.replace(" ", "."),
        'address':f'R. blablabla N.{random.randrange(10, 99, 1)}', 
        'rg': f'{random.randrange(10, 99, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}-{random.randrange(1, 9, 1)}', 
        'cpf': f'{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}/{random.randrange(10, 99, 1)}'
    }
 
    # Adding every dictionary at the client_list
    client_list.append(client_dict)

# Defining client_list lenght
client_list_len = len(client_list)

# Printing the Client Data in a tabble
for i in range(client_list_len):
    print(f'Name: {client_list[i]["name"] :<20}|', end=' ')
    print(f'Contact: {client_list[i]["contact"]} |', end=' ')
    print(f'E-Mail: {client_list[i]["email"] :<30} |', end=' ')
    print(f'Address: {client_list[i]["address"]} |', end=' ')
    print(f'RG: {client_list[i]["rg"]} |', end=' ')
    print(f'CPF: {client_list[i]["cpf"]}')
