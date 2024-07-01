# nomes próprios devem começar com letras maiúsculas
# mas como'bmw' é uma sigla -> deve ser escrita toda maiúscula

cars = ['audi','bmw','subaru','toyota']

# percorra a lista e mostre os nomes de acordo com a regra anterior
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
