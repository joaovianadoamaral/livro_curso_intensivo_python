# use todas as funções aprendidas sobre manipulação de listas
# irei trabalhar com uma lista de jogos que joguei na infância


# resumo
# instrução del
# métodos: .append(), .insert(i,'v'), .pop(), remove('v') 
# métodos: .sort(), .reverse() 
# funções: sorted(), len()

games = []

# criação do top 3 -> na ordem que adicionado
games.append('Resident Evil 4')
games.append('GTA san Andreas')
games.append('bomba patch')

print ('Top 3 criado :\n    ', games)

# poxa, mas eu acho que God of War seria primeiro colocado né
games.insert(0, 'God of War')
print('GoW assume top1:\n   ', games)

# nossa mas é só top 3, temos 4 jogos aqui
del games[3]
print('Novo Top 3 :\n   ', games)

# mas e se trocassemos o segundo pelo terceiro lugar, como ficaria
# 2° RE4 3° GTA
aux = games.pop()
games.insert(1, aux)
print ('Esse Top 3 é mais correto?\n    ', games )

# aconteceu um bug devastador que vai impedir de RE4 de ganhar o GoY -> precisaremos retira-lo da lista
RE4 = 'Resident Evil 4'.title()
games.remove(RE4)
print ('Concorrentes ao GoY: \n     ', games)

########################################################
# agora precisamos fazer um top 10 e ordena-los
#3
games.append(RE4)
#4
games.append('Bomba patch')
#5
games.append('Black')
#6
games.append('Bully')
#7
games.append('Need for speed: most wanted')
#8
games.append('Mortal Kombat')
#9
games.append('Shadow of the Colossus')
#10
games.append('Guitar Hero')

# veja os games na ordem de premiação
print('\nOrdem de premiação:')
cont = 1
for game in games:
    message = f'\t{cont}. \t{game}'
    print(message)
    cont += 1

# veja os games na ordem alfabetica
print('\nOrdem começando pelo top 10:')
games.reverse()
cont = 10
for game in games:
    message = f'\t{cont}. \t{game}'
    print(message)
    cont -= 1

#volta ao normal
games.reverse()

# por ordem alfabética crescente
print('\nOrdem alfabética crescente:')
games_sorted = sorted(games)
cont = 1
for game in games_sorted:
    message = f'\t{cont}. \t{game}'
    print(message)
    cont += 1

# por ordem alfabética crescente
print('\nOrdem alfabética decrescente:')
games.sort(reverse = True)
cont = 10
for game in games:
    message = f'\t{cont}. \t{game}'
    print(message)
    cont -= 1

# agradecemos x jogos participantes
len_games = len(games)
print(f'\nGostariamos de agradecer aos todos {len_games} jogos participantes\n')
