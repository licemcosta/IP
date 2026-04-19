objetivos_da_missao = ["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
itens_bonus = ["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixos = ["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]
lista_coleta = []
quantidade = []
pontuacao = 0
cont_objetivos = 0
quant_bubble = 0

#FASE 1
print("FASE 1:")
print("Marty McFly: Vamos buscar os Recursos que o Doc pediu.")
coleta = input()
while coleta != "Fim Da Coleta!": 
    if coleta not in lixos: #se o item não for lixo ele entra no meu inventário
        if coleta not in lista_coleta: #itens novos - não estão no inventário ainda
            lista_coleta.append(coleta) 
            quantidade.append(1)
            if coleta in itens_bonus:
                print("Marty McFly: Não podemos deixar uma raridade dessas pra trás né?!")
            if coleta in objetivos_da_missao:
                print("Marty McFly: Boa Embananado, estávamos precisando disso.")
                cont_objetivos += 1
        else: #itens "velhos" - já estão no inventário
            indice = lista_coleta.index(coleta)
            numero = quantidade[indice]
            quantidade[indice] += 1
            if coleta in itens_bonus:
                print("Marty McFly: Não podemos deixar uma raridade dessas pra trás né?!")
            if coleta in objetivos_da_missao:
                print("Marty McFly: Por via das dúvidas, vamos levar mais.")
    else:
        print("Marty McFly: Pra que eu preciso disso? Só vai encher meu inventário.")
    coleta = input()

quant_coleta = len(lista_coleta) #algoritmo do bubble sort
while quant_bubble < quant_coleta:
    quant_bubble += 1
    for i in range(quant_coleta): 
        if i > 0:
            if quantidade[i] > quantidade[i-1]:
                quantidade[i], quantidade[i-1] = quantidade[i-1], quantidade[i]
                lista_coleta[i], lista_coleta[i-1] = lista_coleta[i-1], lista_coleta[i]

for item in lista_coleta: #pontuação
    indice = lista_coleta.index(item)
    numero = quantidade[indice]
    if item in objetivos_da_missao:
        pontuacao += 30*numero
    elif item in itens_bonus:
        pontuacao += 10*numero
    else:
        pontuacao -= 5*numero
    if pontuacao > 100:
        pontuacao = 100
    elif pontuacao < 0:
        pontuacao = 0

print("Marty McFly: Nossa coleta termina aqui.")
if cont_objetivos == 0:
    print("Marty McFly: Infelizmente não encontramos nenhum dos objetivos, não poderemos continuar com a missão.")
else:
    print(f"PONTUAÇÃO DA COLETA = {pontuacao}")
    if pontuacao < 30:
        print("Marty McFly: Pontuação Insuficiente, não poderemos continuar com a missão.")
    else:
        #FASE 2
        print("")
        print("FASE 2:")
        print("Doc Brown: De onde estão vindo esses sinais de rádio-frequência dimensional? Eles formam uma matriz perfeita!")
        matriz = []
        quantidade_linhas = int(input())
        quantidade_colunas = int(input())

        percurso = []
        linha = []
        for i in range(quantidade_linhas):
            coluna_pontos = ["."]*quantidade_colunas
            percurso.append(coluna_pontos)

        for i in range(quantidade_linhas):
            linha = input().split(" - ")
            matriz.append(linha)


        for i in range(quantidade_linhas):
            for j in range(quantidade_colunas):
                matriz[i][j] = float(matriz[i][j])

        linha_atual = 0
        coluna_atual = 0
        maior_valor = 0
        maior_linha = 0
        maior_coluna = 0
        distancia_percorrida = 0
        posicao = " "
        progresso = True

        while progresso:

            if 0 <= linha_atual-1 < quantidade_linhas and 0 <= coluna_atual < quantidade_colunas: #Verificar o de cima
                valor = matriz[linha_atual-1][coluna_atual]
                if valor > maior_valor:
                    maior_valor = valor
                    maior_linha = linha_atual - 1
                    maior_coluna = coluna_atual
                    posicao = "^"
                

            if 0 <= linha_atual < quantidade_linhas and 0 <= coluna_atual+1 < quantidade_colunas: #Verificar o da direita
                valor = matriz[linha_atual][coluna_atual+1]
                if valor > maior_valor:
                    maior_valor = valor
                    maior_linha = linha_atual
                    maior_coluna = coluna_atual + 1
                    posicao = ">"

            if 0 <= linha_atual+1 < quantidade_linhas and 0 <= coluna_atual < quantidade_colunas: #Verificar o de baixo
                valor = matriz[linha_atual+1][coluna_atual]
                if valor > maior_valor:
                    maior_valor = valor
                    maior_linha = linha_atual + 1
                    maior_coluna = coluna_atual
                    posicao = "v"

            if 0 <= linha_atual < quantidade_linhas and 0 <= coluna_atual-1 < quantidade_colunas: #Verificar o da esquerda
                valor = matriz[linha_atual][coluna_atual-1]
                if valor > maior_valor:
                    maior_valor = valor
                    maior_linha = linha_atual 
                    maior_coluna = coluna_atual - 1
                    posicao = "<"

            if maior_valor > matriz[linha_atual][coluna_atual]:
                percurso[linha_atual][coluna_atual] = posicao
                distancia_percorrida += 1
                linha_atual = maior_linha
                coluna_atual = maior_coluna

            else:
                percurso[linha_atual][coluna_atual] = "X"
                progresso = False


        for i in range(quantidade_linhas):
            print("".join(percurso[i]))
        print(f"Doc Brown: Os sinais vêm da posição [{linha_atual}][{coluna_atual}]!")
        print(f"Localização triangulada com sucesso após {distancia_percorrida} movimentos pela grade dimensional.")


        #FASE 3
        print("")
        print("FASE 3:")
        print("Doc Brown: Está quase tudo pronto para voltarmos para casa!")
        string_binaria = str(input())
        numero_inicial = int(string_binaria, 2)
        quant_trocas = 0
        for i in range(numero_inicial, 88):
            numero_atual = format(i, "7b")
            numero_seguinte = format(i + 1, "7b")
            for j in range(7):
                if numero_atual[j] != numero_seguinte[j]:
                    quant_trocas += 1

        print("SISTEMA SINCRONIZADO!")
        print(f"Doc Brown: Marty, para acelerarmos de {numero_inicial} até 88 mph, o Capacitor teve que realizar {quant_trocas} trocas de estado nos bits de processamento!")
        print("--- #1 VICTORY ROYALE: Bem-Vindos a 1985! ---")