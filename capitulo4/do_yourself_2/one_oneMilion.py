# crie uma lista de itens de 1 a 1 milhão
list_numbers = [value for value in range(1, 1_000_000 + 1)]

# exiba os números usando for
for num in list_numbers:
    print(f'{num:_}')
