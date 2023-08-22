import random

#Criando a lista
lista = []

# Randomizando os dados
for i in range(100):
    nome = random.choice(['Erick', 'Sarah', 'Fernanda', 'Renata', 'Fabio', 'Sheila', 'Renato', 'Victória', 'Gabriele', 'Mariana', 'Beatriz', 'Priscila', 'Gustavo', 'Bruno', 'Fabiano'])
    sobrenome = random.choice(['Monteiro', 'Alcaide', 'Fernandes', 'dos Anjos', 'Martins', 'de Souza', 'Souza', 'de Sousa', 'Sousa', 'Reis', 'Salim', 'Mendonça', 'José', 'Viviani', 'dos Santos', 'Rodrigues'])

    randomUser = {
        'nome': f'{nome} {sobrenome}',  
        'contato': f'+55 (11) 9{random.randrange(1000, 9999, 1)}-{random.randrange(1000, 9999, 1)}',
        'endereco':f'R. blablabla N.{random.randrange(10, 99, 1)}', 
        'rg': f'{random.randrange(10, 99, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}-{random.randrange(1, 9, 1)}', 
        'cpf': f'{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}.{random.randrange(100, 999, 1)}/{random.randrange(10, 99, 1)}'
    }

    # Aplicando cada dicionário de nome à lista
    lista.append(randomUser)

# Definindo o tamanho da lista
tamanhoLista = len(lista)

# Para cada nome na lisa ele imprime os dados
for i in range(tamanhoLista):
    print(f'Nome: {lista[i]["nome"]} | Contato: {lista[i]["contato"]} | Endereço: {lista[i]["endereco"]} | RG: {lista[i]["rg"]} | CPF: {lista[i]["cpf"]}')
