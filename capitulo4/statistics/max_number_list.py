# apesar da função max(list) já existir, vamos cria-la?
def max_value_list ( numbers_list ):
    # define o primeiro valor da lista como maior
    max_value = numbers_list[0]

    # compara com os outros valores da lista
    for max in numbers_list:
        if max > max_value:
            max_value = max
    
    return max_value

numbers = [5, 3, 7 , 10 , 38, 94, -2, 40]
max = max_value_list (numbers)
print(max)