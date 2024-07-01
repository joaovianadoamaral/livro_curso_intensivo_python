# uma tupla é uma lista imutável 
# -> não se pode alterar os elementos definidos

# se em um programa temos que um retângulo 
# que representa a hitbox de um personagem
# e se esse retângulo deve possuir dimensões constantes

dimensions = (200, 50)
print(dimensions)
# dimensions.append(0) 
# error -> tuple has no atrribute 'append'

# embora não possamos alterar uma tupla, podemos redfini-la
dimensions = (400, 100)
print(dimensions)

