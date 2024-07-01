# cria uma lista onde a variável temporária 'value'
# faz a operação value**2 e guarda para cada valor do range()
squares = [value**2 for value in range(1,11)]
print ( squares )

# aqui a variável value é inútil -> todo valor da lista será 3
# eu só quiz que esse valor se repetisse n vezes
n = 15
numbers_3 = [3 for value in range(0,n)]
print ( numbers_3 )

# sintaxe:
# [valor_a_ser_preenchido_lista laço_for + range()/lista]
list_numbers = list(range(0,26))
squares2 = [number**2 for number in list_numbers]
print(squares2)

# observação -> não use 2 pontos