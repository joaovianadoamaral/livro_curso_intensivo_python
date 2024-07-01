import random

# Gerar uma lista aleatória de 20 números inteiros entre 1 e 100
list_point = [random.randint(1, 100) for _ in range(20)]

# a lista anterior representa as pontuações de um jogador
# vamos descobrir qual a lista gerada?
print ( list_point )

# vamos ver qual as 3 maiores pontuações do jogador?
sorted_list_point = sorted(list_point, reverse = True)
for max_point in sorted_list_point[:3]:
    print(max_point)
