# sort == organizar
# primeiro é preciso ter uma lista

cars = ['bmw', 'audi', 'toyota', 'subaru']
print ('lista original : ' ,  cars )

# método .sort() -> alteração permanente da lista
# ordenação alfabética

cars.sort()
print ('Ordenação crescente: ',  cars )

# ordenação decrescente -> adicione : reverse = True  ao método
cars.sort(reverse = True ) 
print ('Ordenação decrescente: ',  cars )

print ("Lembre-se -> todas as altereações com o método .sort são permanentes")