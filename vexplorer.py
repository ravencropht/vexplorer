#!/usr/bin/env python3

import subprocess
from os import environ


def vault_get(vault_path):
    list_command = subprocess.Popen(
        ["vault", "kv", "get", vault_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True
    )
    output, error = list_command.communicate()
    if output:
        return output
    elif error:
        raise


def vault_list(vault_path):
    list_command = subprocess.Popen(
        ["vault", "kv", "list", vault_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True
    )
    output, error = list_command.communicate()
    if output:
        return output
    elif error:
        raise


def vault_up(vault_path):
    vault_path = vault_path.split('/')
    for _ in vault_path:
        if _ == '':
            vault_path.remove(_)
    vault_path = vault_path[:-1]
    vault_path = f'/{"/".join(vault_path)}/'
    return vault_path


vault_path = '/secret/'

print('---------------------------------------')
print('Для выхода введите QUIT или quit')
print('Для перехода вверх введите up,UP или ..')
print('---------------------------------------')

while True:
# Check Vault env variables
    if 'VAULT_ADDR' not in environ or 'VAULT_TOKEN' not in environ:
        print('Не заданы переменные VAULT_ADDR или VAULT_TOKEN')
        break
#
    try:
        print(vault_list(vault_path))
    except:
        try:
            print(vault_get(vault_path))
        except:
            print('НЕВЕРНЫЙ ПУТЬ')
            print(vault_path)
        vault_path = vault_up(vault_path)
    else:
        if vault_path[-1] == '/':
            pass
        else:
            vault_path = f'{vault_path}/'

        argument = str(input(f'{vault_path} > '))

        if argument == 'QUIT' or argument == 'quit':
            print('ЗАВЕРШЕНИЕ РАБОТЫ')
            break
        elif argument == 'up' or argument == 'UP' or argument == '..':
            vault_path = vault_up(vault_path)
        else:
            vault_path = f'{vault_path}{argument}'
