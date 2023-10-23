import random

# Criando a lista
lista = []

# Randomizando os dados
for i in range(100):

    primeiro_nome = random.choice(['Erick', 'Sarah', 'Fernanda', 'Renata', 'Fabio', 'Sheila', 'Renato', 'Victória', 'Gabriele', 'Mariana', 'Beatriz', 'Priscila', 'Gustavo', 'Bruno', 'Fabiano', 'Murilo', 'Gabriel', 'Pedro', 'Fagner', 'Luiz', 'João', 'Kleber', 'Rebeca', 'Victor', 'Lívia', 'Carol', 'Ana', 'Anna', 'Júlia', 'Heitor', 'Paulo', 'Letícia'])
    segundo_nome = random.choice(['Monteiro', 'Alcaide', 'Fernandes', 'dos Anjos', 'Martins', 'de Souza', 'Souza', 'de Sousa', 'Sousa', 'Reis', 'Salim', 'Mendonça', 'José', 'Viviani', 'dos Santos', 'Rodrigues', 'Henrique', 'Potter', 'Brás', 'Araújo', 'Emanoel', 'Carolina', 'Carolyna', 'Carvalho', 'Medeiros', 'Marin', 'Vieira', 'Falcão', 'Silva', 'da Silva'])
    nome = f'{primeiro_nome} {segundo_nome}'
    email = random.choice(['@gmail.com', '@outlook', '@hotmail.com', '@yahoo.com'])

    random_user = {
        'nome': f'{nome}', 
        'contato': f'+55 (11) 9{random.randrange(1000, 9999, 1)}-{random.randrange(1000, 9999, 1)}',
        'email': f'{primeiro_nome}.{segundo_nome.replace(" ", ".")}{email}'.lower(),
        'endereco':f'R. blablabla N.{random.randrange(10, 99, 1)}', 
        'rg': f'{random.randrange(10, 99, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}-{random.randrange(1, 9, 1)}', 
        'cpf': f'{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}/{random.randrange(10, 99, 1)}'
    }

    # Aplicando cada dicionário de nome à lista
    lista.append(random_user)

# Definindo o tamanho da lista
tamanho_lista = len(lista)

# Para cada nome na lisa ele imprime os dados
for i in range(tamanho_lista):
    print(f'Nome: {lista[i]["nome"] :<20}|', end=' ')
    print(f'Contato: {lista[i]["contato"]} |', end=' ') 
    print(f'E-Mail: {lista[i]["email"] :<30} |', end=' ') 
    print(f'Endereço: {lista[i]["endereco"]} |', end=' ') 
    print(f'RG: {lista[i]["rg"]} |', end=' ')
    print(f'CPF: {lista[i]["cpf"]}')
