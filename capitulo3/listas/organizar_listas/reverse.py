# o método reverse simplismente inverte a ordem da lista
# alteração permanente
# podemos retornar a forma original fazendo um .reverse() de novo na lista

list = [1,5,3,8,9]
print('Here is the original list: ', list)

list.reverse()
print('Here is the reverse list: ',  list)

list.reverse()
print('Here is the original list again: ', list)
#list -> [9,8,3,5,1]

#o último passa a ser o primeiro e o primeiro o último,
#além das outras trocas de posiçãoS