# EP2

# Importando a biblioteca random
import random

random.seed(1)
# Define o posicionamento dos navios
def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicoes = []

    for i in range(tamanho):

        # Define a posição na direção vertical
        if orientacao == "vertical":
            lista_posicoes.append([linha, coluna])
            linha += 1 
        
        # Define a posição na direção horizontal
        if orientacao == "horizontal":
            lista_posicoes.append([linha, coluna])
            coluna += 1 

    return lista_posicoes

# Preenche frota
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    # Define a posição de um novo navio a ser adicionado à frota do jogador
    novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if navio not in frota:
        frota[navio] = []

    # Adiciona o novo navio à frota do jogador
    frota[navio].append(novo_navio)

    return frota

# Faz jogada 
def faz_jogada(tabuleiro, linha, coluna):
    # Determina a posicao que será atacada
    posicao = tabuleiro[linha][coluna]

    # Caso de acerto de um navio
    if posicao == 1:
        tabuleiro[linha][coluna] = 'X'
    
    # Caso de erro do alvo
    if posicao == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro 

# Posiciona Frota 
def posiciona_frota(frota):
    # Cria tabuleiro 10x10
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
    # Marca a posição dos navios no tabuleiro
    for nome_navio, navios in frota.items():
        for navio in navios:
            for parte_do_navio in navio:
                tabuleiro[parte_do_navio[0]][parte_do_navio[1]] = 1
    return tabuleiro 

# Quantas embarcações afundadas?
def afundados(frota, tabuleiro):
    navios_afundados = 0

    for nome_navio, navios in frota.items():
        for navio in navios:
            t = True 
            for parte_do_navio in navio:

                # Verifica afundamento dos navios
                if tabuleiro[parte_do_navio[0]][parte_do_navio[1]] != 'X':
                    t = False

            # Registra afundamento
            if t == True:
                navios_afundados += 1

    return navios_afundados

# Posição válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_ja_ocupadas = []

    for navios in frota.values():
        for navio in navios:
            for posicao in navio:
                # Registra posições já ocupadas
                posicoes_ja_ocupadas.append(posicao)

    # Valida posição para os navios 
    for i in define_posicoes(linha, coluna, orientacao, tamanho):
        # Verifica o caso da posição ficar fora do tabuleiro
        if i[0] < 0 or i[0] > 9 or i[1] < 0 or i[1] > 9:
            return False
        # Verifica o caso da posição do novo navio conflitar com a posição de algum outro navio já posicionado
        if i in posicoes_ja_ocupadas:
            return False
    return True

# Monta tabuleiros
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    # Formata tabuleiro
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    # Atualiza tabuleiro
    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


lista_teste = [] 
ponteiro_teste = 0

# É um número inteiro?
def eh_inteiro(valor):
    # Verifica se dá erro ao tentar converter string para int
    try:
         int(valor)
    # Caso de erro
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
            # Utiliza input
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
frota_jogador = {'porta-aviões': [], 'navio-tanque': [], 'contratorpedeiro': [], 'submarino': []}

# Define tipo do navio
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

    # Imprime informações do navio
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))

    # Pergunta uma linha para o posicionamento do navio
    linha = input_interno('Em qual linha deseja colocar o seu navio? (De 0 a 9) ', 'Linha inválida!')
    # Pergunta uma coluna para o posicionamento do navio
    coluna = input_interno('Em qual coluna deseja colocar o seu navio? (De 0 a 9) ', 'Coluna inválida!')

    # Perguntar a orientação caso o tipo do navio não seja um submarino
    if navio != 'submarino':
        orientacao = int(input_interno('Em qual orientacao deseja colocar o seu navio? (1-vertical ou 2-horizontal) ', 'Orientação inválida!'))
        # Define orientação vertical
        if orientacao == 1:
            orientacao = 'vertical'
        # Define orientação horizontal
        elif orientacao == 2:
            orientacao = 'horizontal'

    # Valida posicionamento do navio
    while posicao_valida(frota_jogador, linha, coluna, orientacao, tamanho) == False:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio, tamanho))
        linha = input_interno('Em qual linha deseja colocar o seu navio? (De 0 a 9) ', 'Linha inválida!')
        coluna = input_interno('Em qual coluna deseja colocar o seu navio? (De 0 a 9) ', 'Coluna inválida!')
        if navio != 'submarino':
            orientacao = input_interno('Em qual orientacao deseja colocar o seu navio? (1-vertical ou 2-horizontal) ', 'Orientação inválida!')
            # Define orientação vertical
            if orientacao == 1:
                orientacao = 'vertical'
            # Define orientação horizontal
            elif orientacao == 2:
                orientacao = 'horizontal'

    # Adiciona novo navio à frota
    frota_jogador = preenche_frota(frota_jogador, navio, linha, coluna, orientacao, tamanho)

# Jogadas do jogador

# Cria frota oponente
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

# Posiciona a frota do oponente no tabuleiro do oponente
tabuleiro_oponente = posiciona_frota(frota_oponente)

# Posiciona a frota do jogador no tabuleiro do jogador
tabuleiro_jogador = posiciona_frota(frota_jogador)

# Cria lista de posições anteriores
posicoes_anteriores = []

jogando = True
while jogando:
    # Imprime os tabuleiros formatados
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # Pergunta a linha que o jogador deseja atacar
    linha_de_ataque = input_interno('Qual a linha que você deseja atacar? (De 0 a 9) ','Linha inválida!')
    # Pergunta a coluna que o jogador deseja atacar
    coluna_de_ataque = input_interno('Qual a coluna que você deseja atacar? (De 0 a 9) ','Coluna inválida!')
    
    # Verifica se o ataque já foi feito antes
    if [linha_de_ataque, coluna_de_ataque] in posicoes_anteriores:
        print('A posição linha', linha_de_ataque, 'e coluna', coluna_de_ataque, 'já foi informada anteriormente!')
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_de_ataque, coluna_de_ataque)
        
    # Acrescenta o novo ataque à lista de ataques anteriores
    posicoes_anteriores.append([linha_de_ataque, coluna_de_ataque])

    # Quantos navios foram afundados?
    navios_afundados = afundados(frota_oponente, tabuleiro_oponente)

    # Verifica se todos os navios do oponente já foram afundados
    if navios_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False


# Jogada do oponente 
    
    # Define jogada do oponente
    else:
        # Cria lista de ataque do oponente
        lista_posicoes_sorteadas = []
        t = True
        while t:
            # Sorteia jogada do oponente
            linha_sorteada = random.randint(0, 9)
            coluna_sorteada = random.randint(0, 9)
            posicao_sorteada = [linha_sorteada, coluna_sorteada]

            # Valida jogada do oponente
            if posicao_sorteada not in lista_posicoes_sorteadas:
                t = False
                

        # Salvar jogada do oponente na lista de ataques anteriores do oponente
        lista_posicoes_sorteadas.append(posicao_sorteada)

        # Imprimir a string informando o ataque do oponente 
        print("Seu oponente está atacando na linha {0} e coluna {1}".format(linha_sorteada, coluna_sorteada))

        # Atualizando o tabuleiro do jogador após a jogada do oponente
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_sorteada, coluna_sorteada)

        # Verificar se o oponente derrubou todas as embarcações do jogador
        n_afundados = afundados(frota_jogador, tabuleiro_jogador)
        if n_afundados == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False 