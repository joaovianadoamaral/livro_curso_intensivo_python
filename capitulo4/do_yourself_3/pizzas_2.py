# 3 tipos de pizza favoritas
pizzas = ['calabresa', 'catupiry', 'portuguesa']

# cópia do gosto das pizzas para um amigo
friend_pizzas = pizzas[:]

# Eu gosto de uma pizza diferente do meu amigo
pizzas.append('chocolate')

# meu amigo gosta de uma pizza diferente de mim:
friend_pizzas.append('peperone')

# prove que são duas pizzas diferentes:
print('Minhas pizzas favoritas são: ')
for pizza in pizzas:
    print(pizza)

print('\nAs pizzas favoritas de meu amigo são:')
for pizza in friend_pizzas:
    print(pizza)

print()
