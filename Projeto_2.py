# EP2

# Define posições
def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicoes = []

    for i in range(tamanho): 
        if orientacao == "vertical":
            lista_posicoes.append([linha, coluna])
            linha += 1 
            
        if orientacao == "horizontal":
            lista_posicoes.append([linha, coluna])
            coluna += 1 

    return lista_posicoes

# Preenche frota
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if navio not in frota:
        frota[navio] = []

    frota[navio].append(novo_navio)

    return frota

# Faz jogada 
def faz_jogada(tabuleiro, linha, coluna):
    posicao = tabuleiro[linha][coluna]
    if posicao == 1:
        tabuleiro[linha][coluna] = 'X'
    if posicao == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro 

# Posiciona Frota 
def posiciona_frota(frota):
    tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio, posicao in frota.items():
        for i in posicao:
            for x in i:
                tabuleiro[x[0]][x[1]] = 1
    return tabuleiro 

# Quantas embarcações afundadas?
def afundados(embarcacoes, tabuleiro):
    navios_afundados = 0
    for navio, valor in embarcacoes.items():
        for i in valor:
            t = True 
            for x in i:
                if tabuleiro[x[0]][x[1]] != 'X':
                    t = False 
            if t == True:
                navios_afundados += 1
    return navios_afundados

# Posição válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_ja_ocupadas = []
    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                posicoes_ja_ocupadas.append(posicao)

    for i in define_posicoes(linha, coluna, orientacao, tamanho):
        if i[0] < 0 or i[0] > 9 or i[1] < 0 or i[1] > 9:
            return False
        if i in posicoes_ja_ocupadas:
            return False
    return True

# Posicionando frota
frota = {'porta-aviões': [], 'navio-tanque': [], 'contratorpedeiro': [], 'submarino': []}

for embarcacoes in range(10):
    if embarcacoes < 1:
        navio = 'porta-aviões'
        tamanho = 4
    elif embarcacoes < 3:
        navio = 'navio-tanque'
        tamanho = 3
    elif embarcacoes < 6:
        navio = 'contratorpedeiro'
        tamanho = 2
    elif embarcacoes >= 6:
        navio = 'submarino'
        tamanho = 1

    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))

    linha = int(input('Em qual linha deseja colocar o seu navio? (De 0 a 9) '))
    coluna = int(input('Em qual coluna deseja colocar o seu navio? (De 0 a 9) '))
    if navio != 'submarino':
        orientacao = int(input('Em qual orientacao deseja colocar o seu navio? (1-vertical ou 2-horizontal) '))

        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'

    while posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
        linha = int(input('Em qual linha deseja colocar o seu navio? (De 0 a 9) '))
        coluna = int(input('Em qual coluna deseja colocar o seu navio? (De 0 a 9) '))
        if navio != 'submarino':
            orientacao = int(input('Em qual orientacao deseja colocar o seu navio? (1-vertical ou 2-horizontal) '))

            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'

    frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)
    
print(frota)