# função range ()
# facilita gerar uma série de números

# sequência com range()

for value in range(1,5):
    print(value)

# imprime de 1 a 4 (5 - 1)
# começa no primeiro número e para um número antes do último
    
# usado para criar uma lista de números
# função list() -> converte um conjunto de números para uma lista
    
numbers = list (range(1,6))
print ( numbers )

# range(x, y, z) -> use para ignorar números intercalados
# x -> inicio incluso
# y -> final não incluso (vai até o anterior)
# z -> passo / intervalo que progride 

# 10 primeiros quadrados perfeitos em uma lista
perfect_squares = []
for value in range(1,11): 
    square = value ** 2
    perfect_squares.append(square)

print ( perfect_squares )

