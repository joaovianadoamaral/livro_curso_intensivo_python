# apesar da função min(list) já existir, vamos cria-la?
def min_list(numbers_list):
    # define o valor inicial como o primeiro da lista
    min_value = numbers_list[0]

    # verifica se existe outro menor que ele na lista
    for value in numbers_list:
        if value < min_value:
            min_value = value
    
    # retorna o menor valor encotrado na lista
    return min_value

numbers = [5, 3, 7 , 10 , 38, 94, -2, 40]
min_value = min_list( numbers )
print( min_value )