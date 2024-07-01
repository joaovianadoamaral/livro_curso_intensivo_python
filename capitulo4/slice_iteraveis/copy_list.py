# usando o conceito de slice podemos:
# omitir o primeiro índice: inicia no começo
# omitir o segundo índice: termina ao final 

original_list = ['Joao', 'Julia', 'Andreia', 'Vitor', 'Gustavo']
copy_list = original_list [ : ]

# obs.: copy_list = original_list  -> não produz o resultado esperado
"""
a lista trabalha por referência, ou seja, pega o endereço do primeiro 
item da lista.
ao fazer
    lista1 = lista2

ambas recebem o mesmo endereço de lista na memória, ou seja, se tornam 
duas coisas totalmente iguais.

o que acontece com uma altera a outra.

basicamente se tornam duas coisas iguais com nomes diferentes.

podemos falar que estamos apelidando a lista
"""

print (copy_list)

copy_list.append('25/03')

print(original_list)
print(copy_list)
