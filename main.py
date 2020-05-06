#!/usr/bin/env python3

import vault_list
import vault_get
import vault_up

vault_path = '/secret/'

print('---------------------------------------')
print('Для выхода введите QUIT или quit')
print('Для перехода вверх введите up,UP или ..')
print('---------------------------------------')

while True:
    try:
        print(vault_list.vault_list(vault_path))
    except:
        try:
            print(vault_get.vault_get(vault_path))
        except:
            print('НЕВЕРНЫЙ ПУТЬ')
            print(vault_path)
        vault_path = vault_up.vault_up(vault_path)
    else:
        if vault_path[-1] == '/':
            # vault_path = f'{vault_path}{argument}'
            pass
        else:
            vault_path = f'{vault_path}/'

        argument = str(input(f'{vault_path} > '))

        if argument == 'QUIT' or argument == 'quit':
            print('ЗАВЕРШЕНИЕ РАБОТЫ')
            break
        elif argument == 'up' or argument == 'UP' or argument == '..':
            vault_path = vault_up.vault_up(vault_path)
        else:
            vault_path = f'{vault_path}{argument}'
