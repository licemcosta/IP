def malkuth(nomes):
    quant_nomes = len(nomes)
    quant_bubble = 0
    while quant_bubble < quant_nomes: #algoritmo do bubble sort
        quant_bubble += 1
        for i in range(quant_nomes):
            if i > 0:
                if len(nomes[i]) < len(nomes[i-1]):
                    nomes[i], nomes[i-1] = nomes[i-1], nomes[i]
    energia_coletada = (len(nomes[0]) + len(nomes[-1]))*20
    print(f"Energia Coletada: {energia_coletada} / {energia_necessaria}")
    if energia_coletada >= energia_necessaria:
        print("Malkuth: O treino vespertino de hoje foi um sucesso! Estarei esperando vocês no período noturno, pessoal!")
        print()
        sucesso = True
    else:
        print("Malkuth: Ah não.. não conseguimos energia suficiente... amanhã eu dobrarei a carga horária para que a gente possa concluir o expediente com excelência!")
        print()
        sucesso = False
    return sucesso #retorna o valor da energia pra somar depois

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
    if continuidade == True:
        print(f"Yesod: Aqui está a lista de caracteres comprimidos: '{resultado}'")
        print()
        sucesso = True
    else:
        print("Yesod: Os caracteres de hoje estavam corrompidas... devemos encerrar o dia mais cedo e investigar.")
        print()
        sucesso = False
    return sucesso



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
    energia_resultante = matriz_nova[0][0] + matriz_nova[1][1] + matriz_nova[2][2]
    print(matriz_nova)
    print()
    print(f"Energia Coletada: {energia_resultante} / {energia_necessaria}")
    if energia_resultante >= energia_necessaria:
        print("Binah: O expediente foi concluído. Não cometa os mesmos erros amanhã.")
        print("Binah: É realmente uma sensação única te ver falhando...")
        print()
        sucesso = True
    else:
        print("Binah: É realmente uma sensação única te ver falhando...")
        print()
    return sucesso


def dias():
    energia_necessaria = 60
    for dia in range(quant_dias):
        energia_necessaria += 40
        print(f"Angela: Hoje é o dia {dia} de {quant_dias}. Espero mais um expediente concluído com excelência.")
        sefirot = input()
        if sefirot == "Malkuth":
            print("Hoje é o dia da Malkuth!")
            print("Malkuth: Ah, onde estão meus modos! Malkuth se apresentando!")
            print("Malkuth: Estamos responsáveis hoje por organizar por tamanho nossa lista de funcionários do time de controle, vamos entregar com resultados perfeitos!")
            print()
            nomes = input().split()
            if nomes == []:
                print("Malkuth: Pessoal?! Onde está todo mundo?! Isso é inaceitável!")
                print()
                sucesso = False
            else:
                sucesso = malkuth(nomes)

        elif sefirot == "Yesod":
            print("Hoje é dia do Yesod!")
            print("Yesod: Você é a cabeça dessa corporação, você deve agir como um exemplo para os outros e fazer certeza que esse dia passe coordialmente seguindo as regras.")
            print("Yesod: Hoje estamos com um problema a resolver. Você é um progamador, não é? Hoje recebemos vários caracteres, e você terá de as comprimir para facilitar as informações.")
            print()
            sucesso = yesod()
        elif sefirot == "Binah":
            print("Hoje é o dia da Binah.")
            print("Binah: ...Você chegou.")
            print("Binah: Você já deve saber o que fazer. Espero um bom resultado vindo de você.")
            print()
            sucesso = binah()
        else:
            print("Angela: Essa sefirot não está disponível hoje.")
            print()
        print("Angela: O relatório dessa semana está pronto.")
        if sucesso == True:
            print(f"Dia {dia} | Status: Energia necessária adquirida.")
        else:
            print(f"Dia {dia} | Status: Energia necessária não adquirida.")
    
quant_dias = int(input())
print("Hoje é o dia da Lobotomy CinCorporation!")
print()
dias()