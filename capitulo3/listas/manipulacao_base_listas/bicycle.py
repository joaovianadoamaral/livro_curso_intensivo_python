# João , 27/03/24

# [colchetes indicam listas]
# [itens, são , separados , por , virgulas]
# observe uma lista que contém tipos de bicicletas:
# apesar desta lista os dados terem uma correlação, isso não é uma obrigação das listas
# python mostra a lista do jeito que se escreve ela: isso inclui os colchetes

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print ( bicycles )

# elementos de uma lista
# para acessa-los informe o nome da lista e a posição que o item oculpa
# o primeiro item possuí posição (índice) 0

# item 1 da lista -> bicycles [ 0 ]
# item 3 da lista -> bicycles [ 2 ]
# item x da lista -> bicycles [ x - 1]

item1 = bicycles [ 0 ]
print (item1)

# ultimo item de uma lista
# acesse usando o indice -1
# o crescimento dos números negativos da lista significa andar para trás
# -2 = penultimo item, -3 = antepenúltimo item ...

# é possível pegar os itens dessa lista e trabalhar com eles como se fossem variáveis