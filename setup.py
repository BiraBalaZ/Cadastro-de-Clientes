import random

#Criando a lista
lista = []

# Randomizando os dados
for i in range(100):

    primeiro_nome = random.choice(['Erick', 'Sarah', 'Fernanda', 'Renata', 'Fabio', 'Sheila', 'Renato', 'Victória', 'Gabriele', 'Mariana', 'Beatriz', 'Priscila', 'Gustavo', 'Bruno', 'Fabiano'])
    segundo_nome = random.choice(['Monteiro', 'Alcaide', 'Fernandes', 'dos Anjos', 'Martins', 'de Souza', 'Souza', 'de Sousa', 'Sousa', 'Reis', 'Salim', 'Mendonça', 'José', 'Viviani', 'dos Santos', 'Rodrigues'])
    nome = f'{primeiro_nome} {segundo_nome}'
    email = random.choice(['@gmail.com', '@outlook', '@hotmail.com', '@yahoo.com'])

    four_digits = random.randrange(1000, 9999, 1)
    three_digits = random.randrange(100, 999, 1)
    two_digits = random.randrange(10, 99, 1)
    one_digit = random.randrange(1, 9, 1)

    random_user = {
        'nome': f'{nome}', 
        'contato': f'+55 (11) 9{four_digits}-{four_digits}',
        'email': f'{primeiro_nome}.{segundo_nome.replace(" ", ".")}{email}'.lower(),
        'endereco':f'R. blablabla N.{two_digits}', 
        'rg': f'{two_digits}.{three_digits}.{three_digits}-{one_digit}', 
        'cpf': f'{three_digits}.{three_digits}.{three_digits}/{two_digits}'
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
