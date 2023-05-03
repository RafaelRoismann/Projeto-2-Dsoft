frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

ocupado = []
for navios in frota_oponente.values():
    for navio in navios:
        for pos in navio:
            ocupado.append(pos)

livres = []
for linha in range(10):
    for coluna in range(10):
        pos = [linha, coluna]
        if pos not in ocupado:
            livres.append(pos)

saida = ''
for pos in livres:
    saida += f'{pos[0]}\n'
    saida += f'{pos[1]}\n'

#print(saida)

'''
0
0
0
1
0
2
0
3
0
4
0
7
0
8
0
9
1
0
1
1
1
2
1
3
1
4
1
8
1
9
2
0
2
1
2
2
2
3
2
4
2
5
2
6
2
8
2
9
3
0
3
1
3
2
3
3
3
4
3
5
3
8
3
9
4
0
4
1
4
2
4
4
4
5
4
6
4
7
4
8
4
9
5
0
5
1
5
2
5
4
5
5
5
6
5
7
5
8
5
9
6
4
6
5
6
6
6
7
6
8
6
9
7
0
7
1
7
9
5
9
6
9
8
9
9
'''

frota = {
    'porta-aviões': [
        [[1, 5], [1, 6], [1, 7], [1, 8]]
    ], 
    'navio-tanque': [
        [[6, 1], [6, 2], [6, 3]], [[4, 7], [5, 7], [6, 7]]], 
         'contratorpedeiro': [[[1, 1], [2, 1]], [[2, 3], [3, 3]], [[9, 1], [9, 2]]], 
         'submarino': [[[0, 3]], [[4, 5]], [[8, 9]], [[8, 4]]]}
posicoes = []
for navios in frota.values():
    for navio in navios:
        for pos in navio:
            posicoes.append(pos)

print(posicoes)
[[1, 5], [1, 6], [1, 7], [1, 8], [6, 1], [6, 2], [6, 3], [4, 7], [5, 7], [6, 7], [1, 1], [2, 1], [2, 3], [3, 3], [9, 1], [9, 2], [0, 3], [4, 5], [8, 9], [8, 4]]