import subprocess


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


if __name__ == '__main__':
    print(vault_get('/secret/ansible/clients/sbt/backend/init/users/vendor'))
