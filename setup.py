import random
from functions import middle_line
import fake_data as fake
from time import sleep
from tqdm import tqdm
from os import system
from colors import color_ini, color_end, c_blue

# Cleaning Terminal
system('cls')

# Requesting the number of Data
request_number = int(input('Number of lines\n>>> '))

# Cleaning Terminal
system('cls')

# Loading Bar
print(f'Loading {request_number} Lines', end='')
color_ini(c_blue)
for i in tqdm(range(request_number)):
    if (i <= request_number * .1):
        sleep(.65)
    elif (i > request_number * .1 and i <= request_number * .25):
        sleep(.25)
    elif (i > request_number * .25 and i <= request_number * .5):
        sleep(.1)
    elif (i > request_number * .5 and i <= request_number * .75):
        sleep(.4)
    elif (i > request_number * .75 and i <= request_number):
        sleep(.1)
sleep(1)
color_end()
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

# Final (middle) line
middle_line()
