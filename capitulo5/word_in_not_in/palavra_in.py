# maneira já descoberta antes de usar 'in'
# desa maneira temos:
# 'para todo num em nums faça:'
nums = (1,2,3,4,5,6,7,8)
for num in nums:
    print(num)

# para saber se um valor em particular está na lista
fruit = 'maçã'
fruits = ['maçã', 'pera', 'melancia', 'banana']

fruit_in_fruits = fruit in fruits
print(fruit_in_fruits) # True

fruit = 'uva'
fruit_in_fruits = fruit in fruits
print(fruit_in_fruits) # False
