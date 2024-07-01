# 10 primeiros cubos com comprehension list
cube_list = [value ** 3 for value in range(1, 11)]

""" 
método tradicional de criação da lista
cube_list = []
for cube in range(1,11):
    cube ** = 3
    cube_list.append(cube)
"""

# exiba com laço for
for cube in cube_list:
    print(cube)
