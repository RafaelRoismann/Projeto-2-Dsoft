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
def posiciona_frota(dicionario):
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
    for navio, valor in dicionario.items():
        for i in valor:
            for x in i:
                tabuleiro[x[0]][x[1]] = 1
    return tabuleiro