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
    for i in define_posicoes(linha, coluna, orientacao, tamanho):
        if i in frota.values():
            return False
        if i[0] < 0 or i[0] > 9 or i[1] < 0 or i[1] > 9:
            return False
    return True