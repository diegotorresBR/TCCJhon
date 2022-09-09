M_adj_ex1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
for i in range(0, 6):
    for j in range(0, 6):
        M_adj_ex1[i][j] = int(input(f'Informe o valor do elemento [{i},{j}]: '))
print('-=' * 30)
for i in range(0, 6):
    for j in range(0, 6):
        print(f'[{M_adj_ex1[i][j]}]', end='')
    print()

for i in range(0, 6):
    grau = 0
    for j in range(0, 6):
        if (M_adj_ex1[i][j] == 1):
            grau = grau + 1
    print(f'O vértice [{i}] tem grau [{grau}]')

AB == BA == 6
AC == CA == 7
AD == DA == 5
AE == EA == 2
BC == CB == 4
BD == DB == 7
BF == FB == BC / 2
CD == DC == 6
CF == FC == CB / 2
DE == ED == 2

Aresta
de
G = [AB, AC, AD, AE, BA, BC, BD, BF, CA, CB,
     CD, CF, DA, DB, DC, DE, EA, ED, FB, FC]

comp_c_Euler = 0
circuito_Euler = []
for i in range(0, 6):
    grau = 0
    for j in range(0, 6):
        if (M_adj_ex1[i][j] == 1):
            grau = grau + 1
    if (i == 0):
        comp_c_Euler = i
    elif

