def calcular_geradores(tempo): #calcular a quantidade de geradores
    quant_geradores = tempo // 100
    return quant_geradores

def nova_posicao(movimento): #determina a nova posição da pessoa
    if movimento == "c" or movimento == "d1" or movimento == "d2":
        posicao_sobreviventes[1] -= 1
    elif movimento == "b" or movimento == "d3" or movimento == "d4":
        posicao_sobreviventes[1] += 1
    if movimento == "e" or movimento == "d1" or movimento == "d3":
        posicao_sobreviventes[0] -= 1
    elif movimento == "d" or movimento == "d2" or movimento == "d4":
        posicao_sobreviventes[0] += 1
    return (0 <= posicao_sobreviventes[0] < 9 and 0 <= posicao_sobreviventes[1] < 9)

def estruturas(): #avalia as estruturas percorridas e atualiza o tempo
    linha = posicao_sobreviventes[0]
    coluna  = posicao_sobreviventes[1]
    if matriz[linha][coluna] == "M":
        tempo_ganho += 5
        print("🌿 Correu pelo mapa.")
    elif matriz[linha][coluna] == "S":
        tempo_ganho += 40
        print("🏃 Usou a Shack!")
        matriz[linha][coluna] = "M"
    elif matriz[linha][coluna] == "J":
        tempo_ganho += 25
        print("🏃 Usou a Jungle!")
        matriz[linha][coluna] = "M"
    elif matriz[linha][coluna] == "LT":
        tempo_ganho += 20
        print("🏃 Usou a LT!")
    return tempo_ganho


def percurso(tempo, ganchos): #faz o percurso (botar todas as funções aqui dentro)
    quant_geradores = calcular_geradores(tempo)
    print(f"--- STATUS: {quant_geradores}/5 Geradores | {ganchos}/12 Ganchos ---")
    if vantagem_adicionada == False: #tempo da vantagem
        adicao_tempo += (60 + distancia * 10)
        vantagem_adicionada = True
    tempo = percurso(tempo)
    sobrevivente = input() #até sair um sobrevivente que exista
    while sobrevivente not in lista_sobreviventes:
        sobrevivente = input()
    movimentos = input().split(", ")
    for movimento in movimentos: #para cada movimento em movimentos
        novo_local = nova_posicao(movimento)
        if novo_local == True: #se for um local válido
            tempo_ganho += estruturas(tempo)
        else: #se não for válido
            print("❌ Travou na parede! Deixou fácil pro killer!")
            ganchos += 1
    ganchos += 1
    tempo += adicao_tempo
    print(f"Fim da Chase! O/A {sobrevivente} ganhou {tempo_ganho} segundos.")
    print(f"O {assassino} alcançou o/a {sobrevivente} e colocou-o no gancho.")


print("DBCin x DBIp, que a melhor equipe vença! 🏆")

lista_assassinos = ["Spirit", "Singularidade", "Huntress"]
assassino = "" #escolha do assassino
while assassino not in lista_assassinos:
    assassino = input()
    if assassino in lista_assassinos:
        print("Killer de acordo com o previsto! Boa partida!")
    else:
        print("Killer não previsto! Jogo será atrasado, até que a outra equipe escolha um válido!")

tipo_mapa = input() #criando o mapa
matriz = []
for i in range(9):
    linha = []
    for j in range(9):
        linha.append("M")
    matriz.append(linha)
if tipo_mapa == "MacMillan":
    matriz[5][1] = "S" #Shack
    matriz[3][7] = "J" #Jungle
    matriz[1][5] = "LT" #LT
elif tipo_mapa == "Autohaven":
    matriz[1][6] = "S" #Shack
    matriz[2][2] = "J" #Jungle
    matriz[6][3] = "LT" #LT
else:
    matriz[6][7] = "S" #Shack
    matriz[2][2] = "J" #Jungle
    matriz[7][1] = "LT" #LT

coordenada_inicial = input().split(",")
for termo in coordenada_inicial:
    termo = int(termo)
coordenada_assassino = [0,0] #definindo a coordenada do assassino e a distância
if abs(coordenada_inicial[0] - 8) > coordenada_inicial[0]:
    coordenada_assassino[0] = 8
if abs(coordenada_inicial[1] - 8) > coordenada_inicial[1]:
    coordenada_assassino[1] = 8
distancia = abs(coordenada_inicial[0] - coordenada_assassino[0]) + abs(coordenada_inicial[1] - coordenada_assassino[1])
print(f"O(A) {assassino} nasceu na posição [{coordenada_assassino[0]}, {coordenada_assassino[1]}].")
print(f"A vossa vantagem inicial de distância é de {distancia} espaços!")

combate_acontecendo = True
ganchos = 0
tempo = 0
lista_sobreviventes = ["Kate", "Dwight", "Ada", "Vee"]
posicao_sobreviventes = [coordenada_inicial[0], coordenada_inicial[1]]
vantagem_adicionada = False

#CHASE
while combate_acontecendo == True:
    percurso()

