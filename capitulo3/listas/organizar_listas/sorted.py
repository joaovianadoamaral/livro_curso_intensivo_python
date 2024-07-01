# a funçaõ sorted () permite ordenar uma lista, mas não altera a lista original

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list: ', cars)

# a função sorted pega uma lista referência e retorna OUTRA lista organizada
cars_sorted = sorted ( cars )

# parâmetro reverse = True -> torna a organição decrescente
cars_sorted_reverse = sorted ( cars, reverse = True)

print ('Here is the sorted list: ', cars_sorted)
print ('Here is the sorted reverse list: ',cars_sorted_reverse)
print ('Here is the orignial list again: ', cars)
