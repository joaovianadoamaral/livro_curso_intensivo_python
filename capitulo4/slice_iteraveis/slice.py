# slice = fatia
"""
Você fatia iteráveis assim:
especifique onde começa: primeiro índice
especifique onde termina (não incluso): segundo índice

iteravel[0:3]

lista = [0,1,2,3,4,5,6,7,8,9,10]

lista_fatiada = lista[0:5]
print(lista_fatiada)
    -> 0,1,2,3,4

Obs.: uma lista fatiada de 0 a N -> corta N números  -> 0 a N -1
Obs.2: uma lista fatiada de 1 a N -> corta N - 1 números -> 1 a N - 1

N vai indicar qual o item na contagem ordinal
N = 5 -> quinto item da lista

            x : y : z
omissão do x-> começa no primeiro índice
ex: lista[:5] -> primeiro ao quarto item

omissão do y -> vai até o fim da lista
ex.: lista [ 2 : ] -> terceiro ao último item

omissão do z -> por padrão o passo é igual à 1

valores negativos representam quanto que falta chegar ao fim.
fim = -1

quanto MENOR o número negativo mais longe está do fim

lista [-3: ]  -> exibe os últimos 3 itens de uma lista
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# imprime somentes os 3 primeiros jogadores
for player in players[:3]:
    print(player.title())

