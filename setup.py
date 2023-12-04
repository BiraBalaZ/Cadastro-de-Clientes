import random
from functions import middle_line
import fake_data as fake
from time import sleep
from tqdm import tqdm
from os import system

# Cleaning Terminal
system('cls')

# Requesting the number of Data
request_number = int(input('Number of lines\n>>> '))

# Cleaning Terminal
system('cls')

# Loading Bar
print(f'Loading {request_number} Lines')
for i in tqdm(range(request_number)):
    if (i < 6):
        sleep(.5)
    elif (i >= 6 and i <= 85):
        sleep(.1)
    elif (i > 85 and i <= 90):
        sleep(.75)
    elif (i > 90 and i <= 100):
        sleep(.2)
    else:
        sleep(.05)
sleep(1)

# Creating client_list
client_list = []

# Randomizing data
for i in range(request_number):
    name = f'{random.choice(fake.first_name)} {random.choice(fake.second_name)}'

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

# Printing the Client Data in a table
for i in range(client_list_len):
    middle_line()
    print(f'|{client_list[i]["name"] :^20}|', end=' ')
    print(f'{client_list[i]["contact"]} |', end=' ')
    print(f'{client_list[i]["email"] :^32}|', end=' ')
    print(f'{client_list[i]["address"]} |', end=' ')
    print(f'{client_list[i]["rg"]} |', end=' ')
    print(f'{client_list[i]["cpf"]} |')

# Final middle line
middle_line()
