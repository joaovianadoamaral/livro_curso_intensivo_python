# sempre supomos até agora que as listas não estavam vazias
# é interessante não partir desse pressupostos sempre

# como testar se a lista está vazia
lista_nao_vazia = ['joao', 'maria', 'andreia', 'vitor', 'viana']
lista_vazia = []

if lista_nao_vazia: # True
    print('True')
else:
    print('False')

if lista_vazia: # False
    print('True')
else:
    print('False')

string_vazia = ''
string_nao_vazia = 'oi'

if string_vazia: # False
    print('True')
else:
    print('False')

if string_nao_vazia: # True
    print('True')
else:
    print('False')

"""
Uma lista quando usada como teste de condição
-> se possuí algum item == True
-> se vazia == False

A mesma coisa serve para strings
-> string vazia '' == false
-> string não vazia == True
"""
