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

# Monta tabuleiros
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


lista_teste = [] 
ponteiro_teste = 0

# É um número inteiro?
def eh_inteiro(valor):
    try:
         int(valor)
    except ValueError:
         return False
    return True

# Valida input
def input_interno(questao, erro):
    resp = 0
    global ponteiro_teste
    
    if lista_teste == []:
        t = True
        while t:
            resp = input(questao)
            if eh_inteiro(resp):
                resp = int(resp)
                if resp >= 0 and resp <= 9:
                    t = False
                else:  
                    print(erro)
            else:
                print(erro)
    else:
        resp = lista_teste[ponteiro_teste]
        ponteiro_teste += 1
    return resp

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

    linha = input_interno('Em qual linha deseja colocar o seu navio? (De 0 a 9) ', 'Linha inválida!')
    coluna = input_interno('Em qual coluna deseja colocar o seu navio? (De 0 a 9) ', 'Coluna inválida!')

    if navio != 'submarino':
        orientacao = int(input_interno('Em qual orientacao deseja colocar o seu navio? (1-vertical ou 2-horizontal) ', 'Orientação inválida!'))

        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'

    while posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
        linha = input_interno('Em qual linha deseja colocar o seu navio? (De 0 a 9) ', 'Linha inválida!')
        coluna = input_interno('Em qual coluna deseja colocar o seu navio? (De 0 a 9) ', 'Coluna inválida!')
        if navio != 'submarino':
            orientacao = input_interno('Em qual orientacao deseja colocar o seu navio? (1-vertical ou 2-horizontal) ', 'Orientação inválida!')

            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'

    frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)

# Jogadas do jogador
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

tabuleiro_oponente = posiciona_frota(frota_oponente)

tabuleiro_jogador = posiciona_frota(frota)

posicoes_anteriores = []

jogando = True

while jogando:
    linha_de_ataque = input_interno('Qual a linha que você deseja atacar? (De 0 a 9) ','Linha inválida!')
    coluna_de_ataque = input_interno('Qual a coluna que você deseja atacar? (De 0 a 9) ','Coluna inválida!')
    
    if [linha_de_ataque, coluna_de_ataque] in posicoes_anteriores:
        print('A posição linha', linha_de_ataque, 'e coluna', coluna_de_ataque, 'já foi informada anteriormente!')
    else:
        tabuleiro_atualizado_do_oponente = faz_jogada(tabuleiro_oponente, linha_de_ataque, coluna_de_ataque)
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_atualizado_do_oponente))

    posicoes_anteriores.append([linha_de_ataque, coluna_de_ataque])

    navios_afundados = afundados(frota_oponente, tabuleiro_oponente)

    if navios_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
