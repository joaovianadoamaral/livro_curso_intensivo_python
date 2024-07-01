# convidados
guests = ["Julia", 'Adreia', 'Marcelo']

for guest in guests:
    message = "olá " + guest + ", você foi convidado para jantar comigo!"
    print ( message )
    
print ('-=-' * 10)

# descobri que a Julia vai faltar

missed_guest = 'Julia'
guests.remove(missed_guest) # retorna None -> não jogar para uma variável -> use a variável
message = "olá, acabo de descobrir que o convidado: " + missed_guest + " não irá comparecer"
print ( message )

# convidando outra pessoa no lugar

print ( '-=-' * 10 )
new_guest = 'Gustavo'
guests.append(new_guest)

for guest in guests:
    message = "olá " + guest + ", você está convidado para um jantar comigo!"
    print ( message )

# mesa maior! -> + 3 convidados 
print ( '-=-' * 10 )
print("olá, foi encontrado uma mesa maior. Portanto posso convidar mais 3 pessoas!")

new_guests = ['Laura', 'Pedro', 'Marcos']
#adicionado ao início
guests.insert(0, new_guests[0])

#adicionado ao meio
guests.insert(2, new_guests[1])

#adicionado ao final
guests.append(new_guests[2])



# minha mesa não chegará a temo -> so tenho 2 lugares :(
print('-=-' * 10 )
print ("olá infelizmente só poderei convidar duas pesssoa. :(")

removed_guests = []

removed_guests.append(guests.pop())
message = "olá " + removed_guests[0] + "sinto em lhe informar que não poderemos jantar mais. Vamos deixar para a próxima ok?"
print (message)

removed_guests.append(guests.pop())
message = "olá " + removed_guests[1] + "sinto em lhe informar que não poderemos jantar mais. Vamos deixar para a próxima ok?"
print (message)

removed_guests.append(guests.pop())
message = "olá " + removed_guests[2] + "sinto em lhe informar que não poderemos jantar mais. Vamos deixar para a próxima ok?"
print (message)

removed_guests.append(guests.pop())
message = "olá " + removed_guests[3] + "sinto em lhe informar que não poderemos jantar mais. Vamos deixar para a próxima ok?"
print (message)

# lista atual -> Laura, andreia 
print('-=-' * 10 )
for guest in guests:
    message = "olá " + guest + " você ainda está convidado para o meu jantar"
    print ( message )

# exclua as duas ultimas pessoas da lista
del guests[1]
del guests[0]

print ('Minha lista de convidados ao final: ', guests )

