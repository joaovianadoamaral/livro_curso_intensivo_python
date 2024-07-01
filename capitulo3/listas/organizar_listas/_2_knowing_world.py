# 5 lugares do mundo que eu gostaria de conhecer:
places = ['caribe', 'everest', 'japão', 'alemanha', 'itália']
print('Sua lista original : ', places)

# ordenados na ordem do alfabeto
sorted_places = sorted ( places )
print('Sua lista em ordem alfabética: ', sorted_places)

# ordenados de forma inversa
sorted_places_reverse = sorted ( places , reverse = True ) 
print ('Sua lista em ordem decrescente: ', sorted_places_reverse)

# veja que sua lista original não tem alterações
print ('Veja sua lista: ', places)

# mude a ordem da lista -> isso altera a lista original
places.reverse()
print ('Veja sua lista ao contrário: ', places ) 

# veja a lista voltando ao normal
places.reverse()
print ('Veja sua lista na forma original novamente: ', places)

# lista mudada e armazenada em forma alfabética
places.sort()
print('Veja como ficou a lista original: ', places)

# lista mudada e amarzenada de forma inversa
places.sort(reverse = True ) 
print ('Lista armazenada em ordem alfabética inversa: ',places)

# veja a quantidade de lugares que eu quero conhecer
number_places = len(places)
print('A quantidade de lugares que quero conhecer é: ', number_places)