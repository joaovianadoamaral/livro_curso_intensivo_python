# apesar da função max(list) já existir, vamos cria-la?
def sum_numbers_list ( numbers_list):
    # define 0 para que a soma seja feita com os outros números
    sum = 0

    # obs.: 0 não interfere na soma com outros números 
    # -> por isso da escolha
    for num in numbers_list:
        sum += num

    return sum

list_numbers = [number for number in range(1, 1_000_000 + 1)]
sum = sum_numbers_list(list_numbers)
print (f'{sum:_}' )

