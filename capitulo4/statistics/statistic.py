# algumas funções de estatísticas para listas
numbers = list (range ( 1,10 ))
numbers.append(0)

# 1,2,3,4,5,6,7,8,9,0
# função min() -> menor número da lista
min_numbers = min(numbers)

# função max() -> maior número da lista
max_numbers = max(numbers)

# função sum() -> soma de todos os dígitos da lista
sum_numbers = sum ( numbers )

print (min_numbers, max_numbers, sum_numbers)