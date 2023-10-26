import random

# Criando a client_list
client_list = []

# Randomizando os dados
for i in range(100):

    primeiro_nome = random.choice(['Erick', 'Sarah', 'Fernanda', 'Renata', 'Fabio', 'Sheila', 'Renato', 'Victória', 'Gabriele', 'Mariana', 'Beatriz', 'Priscila', 'Gustavo', 'Bruno', 'Fabiano', 'Murilo', 'Gabriel', 'Pedro', 'Fagner', 'Luiz', 'João', 'Kleber', 'Rebeca', 'Victor', 'Lívia', 'Carol', 'Ana', 'Anna', 'Júlia', 'Heitor', 'Paulo', 'Letícia'])
    segundo_nome = random.choice(['Monteiro', 'Alcaide', 'Fernandes', 'dos Anjos', 'Martins', 'de Souza', 'Souza', 'de Sousa', 'Sousa', 'Reis', 'Salim', 'Mendonça', 'José', 'Viviani', 'dos Santos', 'Rodrigues', 'Henrique', 'Potter', 'Brás', 'Araújo', 'Emanoel', 'Carolina', 'Carolyna', 'Carvalho', 'Medeiros', 'Marin', 'Vieira', 'Falcão', 'Silva', 'da Silva'])
    email = random.choice(['@gmail.com', '@outlook', '@hotmail.com', '@yahoo.com'])

    # Dictionary
    client_dict = {
        'nome': f'{primeiro_nome} {segundo_nome}', 
        'contato': f'+55 (11) 9{random.randrange(1000, 9999, 1)}-{random.randrange(1000, 9999, 1)}',
        'email': f'{primeiro_nome}.{segundo_nome.replace(" ", ".")}{email}'.lower(),
        'endereco':f'R. blablabla N.{random.randrange(10, 99, 1)}', 
        'rg': f'{random.randrange(10, 99, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}-{random.randrange(1, 9, 1)}', 
        'cpf': f'{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}/{random.randrange(10, 99, 1)}'
    }
 
    # Aplicando cada dicionário de nome à client_list
    client_list.append(client_dict)

# Definindo o tamanho da client_list
client_list_len = len(client_list)

# Para cada nome na lisa ele imprime os dados
for i in range(client_list_len):
    print(f'Nome: {client_list[i]["nome"] :<20}|', end=' ')
    print(f'Contato: {client_list[i]["contato"]} |', end=' ') 
    print(f'E-Mail: {client_list[i]["email"] :<30} |', end=' ') 
    print(f'Endereço: {client_list[i]["endereco"]} |', end=' ') 
    print(f'RG: {client_list[i]["rg"]} |', end=' ')
    print(f'CPF: {client_list[i]["cpf"]}')
