# crie uma lista de 1 a 1 milhão
list_numbers = [number for number in range(1, 1_000_000 + 1)]
min_list = min(list_numbers)
print(f'{min_list:_}')

max_list = max(list_numbers)
print(f'{max_list:_}')

# observe quanto tempo o python demora para somar 1 milhão de números
sum_list = sum(list_numbers)
print(f'{sum_list:_}')