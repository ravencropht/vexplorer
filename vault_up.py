def vault_up(vault_path):
    vault_path = vault_path.split('/')
    for _ in vault_path:
        if _ == '':
            vault_path.remove(_)
    vault_path = vault_path[:-1]
    vault_path = f'/{"/".join(vault_path)}/'
    return vault_path


if __name__ == '__main__':
    vault_path = '/secret/1121/ololo/qwerty/'
    print(vault_up(vault_path))
