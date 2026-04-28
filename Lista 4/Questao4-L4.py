quant_dias = int(input())

def malkuth():
    nomes = input().split()
    quant_nomes = len(nomes)
    quant_bubble = 0
    while quant_bubble < quant_nomes: #algoritmo do bubble sort
        quant_bubble += 1
        for i in range(quant_nomes):
            if i > 0:
                if len(nomes[i]) < len(nomes[i-1]):
                    nomes[i], nomes[i-1] = nomes[i-1], nomes[i]
    energia_coletada = (len(nomes[0]) + len(nomes[-1]))*20
    return energia_coletada #retorna o valor da energia pra somar depois

def yesod():
    sequencia = input()
    ultimo = 0
    quantidade = 0
    sequencia_resumida = []
    continuidade = True
    for atual in range(len(sequencia)):
        if continuidade: #verifica se o & já foi ou não
            if sequencia[atual] != "&":
                if sequencia[ultimo] != sequencia[atual]:
                    sequencia_resumida.append(str(quantidade))
                    sequencia_resumida.append(sequencia[ultimo])
                    quantidade = 1
                    ultimo = atual
                else:
                    quantidade += 1
                    ultimo = atual
            else:
                continuidade = False
    sequencia_resumida.append(str(quantidade))
    sequencia_resumida.append(sequencia[ultimo])
    resultado = ''.join(sequencia_resumida)
    print(resultado)
    if continuidade == True: #ajustar essa parte mas botei pra não esquecer :)
        dia_sucesso = True
    else:
        dia_sucesso = False



def binah():
    matriz_a = []
    matriz_b = []
    matriz_nova = []
    for i in range(3): #gerando matriz nova só com zeros
        linha = []
        for j in range(3):
            linha.append(0)
        matriz_nova.append(linha)
    for i in range(3):
        linha = input().split()
        matriz_a.append(linha)
    for i in range(3):
        linha = input().split()
        matriz_b.append(linha)
    for i in range(3): #linha matriz a
        for j in range(3): #coluna de a // linha de b
            for k in range(3): #coluna de b
                termo = int(matriz_a[i][j]) * int(matriz_b[j][k])
                matriz_nova[i][k] += termo
    print(matriz_nova)
    energia_resultante = matriz_nova[0][0] + matriz_nova[1][1] + matriz_nova[2][2]
    return energia_resultante
    

def dias():
    for i in range(quant_dias):
        sefirot = input()