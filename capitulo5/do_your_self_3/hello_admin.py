# Lista de usuários
usuarios = ['admin', 'alice', 'bob', 'charlie', 'david']

# Percorrendo a lista de usuários
for usuario in usuarios:
    if usuario == 'admin':
        print("Olá admin, gostaria de ver um relatório de status?")
    else:
        print(f"Olá {usuario.title()}, obrigado por fazer login novamente.")

# Verificando se a lista de usuários está vazia
if usuarios:
    # Percorrendo a lista de usuários
    for usuario in usuarios:
        if usuario == 'admin':
            print("Olá admin, gostaria de ver um relatório de status?")
        else:
            print(f"Olá {usuario.title()}, obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")

# Listas de usuários
current_users = ['admin', 'alice', 'bob', 'charlie', 'david']
new_users = ['eric', 'alice', 'john', 'DAVID', 'michael']

# Convertendo os nomes de usuários para minúsculas
current_users_lower = [user.lower() for user in current_users]

# Verificando os novos usuários
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"O nome de usuário '{new_user}' já está em uso. Por favor, forneça um novo nome.")
    else:
        print(f"O nome de usuário '{new_user}' está disponível.")

# Lista de números de 1 a 9
numeros = list(range(1, 10))

# Percorrendo a lista de números
for numero in numeros:
    if numero == 1:
        print(f"{numero}st")
    elif numero == 2:
        print(f"{numero}nd")
    elif numero == 3:
        print(f"{numero}rd")
    else:
        print(f"{numero}th")
