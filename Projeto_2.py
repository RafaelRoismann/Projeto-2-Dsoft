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
