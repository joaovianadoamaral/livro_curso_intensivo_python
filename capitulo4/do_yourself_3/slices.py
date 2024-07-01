# 10 primeiros cubos com comprehension list
cube_list = [value ** 3 for value in range(1, 11)]

# os 3 primeiros itens da lista
trhee_firts_cube = cube_list[:3]
print('Os três primeiros itens da lista são:')
for cube in trhee_firts_cube:
    print(cube)

# os 3 itens do meio -> 4 - 6
trhee_mid_cube = cube_list[3:6]
print('Os três itens do meio são: ')
for cube in trhee_mid_cube:
    print(cube)

# os 3 últimos itens da lista são
trhee_end_cube = cube_list[-3:]
print('Os últimos 3 itens da lista são:')
for cube in trhee_end_cube:
    print(cube)

