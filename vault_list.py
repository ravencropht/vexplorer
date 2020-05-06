import subprocess


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


if __name__ == '__main__':
    # print(vault_list('/secret/ansible/clients/sbt/backend/init/users/vendor'))
    print(vault_list('/secret/'))
