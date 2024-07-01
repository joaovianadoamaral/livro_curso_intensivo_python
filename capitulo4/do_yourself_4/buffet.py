# buffet oferece apenas 5 tipos de comida
# pense em 5 pratos para esse buffet
buffet = ('Macarronada', 'Churrasco', 'Japonês', 'Farofa', 'Mechicano')

print('Veja o cardápio do restaurante: ')
cont = 1
for food in buffet:
    print(f'\t{cont}.\t{food}')
    cont += 1
# tente modificar e veja a rejeição de python
# buffet[0] = 'Pizza'

# reescreva a tupla mudando dois pratos do restaurante
buffet = ('Macarronada', 'Churrasco', 'Japonês', 'Feijoada', 'Peixe')
print('Veja o cardápio do restaurante revisado: ')
cont = 1
for food in buffet:
    print(f'\t{cont}.\t{food}')
    cont += 1

print()
