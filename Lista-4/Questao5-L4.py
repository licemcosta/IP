def calcular_geradores(tempo): #calcular a quantidade de geradores
    quant_geradores = tempo // 100
    return quant_geradores

def nova_posicao(movimento, quem_anda): #determina a nova posição da pessoa
    if movimento == "c" or movimento == "d1" or movimento == "d2":
        posicoes_sobreviventes[quem_anda][1] -= 1
    elif movimento == "b" or movimento == "d3" or movimento == "d4":
        posicoes_sobreviventes[quem_anda][1] += 1
    if movimento == "e" or movimento == "d1" or movimento == "d3":
        posicoes_sobreviventes[quem_anda][0] -= 1
    elif movimento == "d" or movimento == "d2" or movimento == "d4":
        posicoes_sobreviventes[quem_anda][0] += 1
    return (0 <= posicoes_sobreviventes[quem_anda][0] < 9 and 0 <= posicoes_sobreviventes[quem_anda][1] < 9)

def estruturas(tempo): #avalia as estruturas percorridas e atualiza o tempo
    linha = posicoes_sobreviventes[quem_anda][0]
    coluna  = posicoes_sobreviventes[quem_anda][1]
    if matriz[linha][coluna] == "M":
        tempo += 5
        print("🌿 Correu pelo mapa.")
    elif matriz[linha][coluna] == "S":
        tempo += 40
        print("🏃 Usou a Shack!")
        matriz[linha][coluna] = "M"
    elif matriz[linha][coluna] == "J":
        tempo += 25
        print("🏃 Usou a Jungle!")
        matriz[linha][coluna] = "M"
    elif matriz[linha][coluna] == "LT":
        tempo += 20
        print("🏃 Usou a LT!")
    return tempo


def percurso():

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

lista_sobreviventes = ["Kate", "Dwight", "Ada", "Vee"]
sobrevivente = input()
while sobrevivente not in lista_sobreviventes:
    sobrevivente = input()

combate_acontecendo = True
while combate_acontecendo == True:
    lista_sobreviventes = ["Kate", "Dwight", "Ada", "Vee"]
    posicoes_sobreviventes = [coordenada_inicial, coordenada_inicial, coordenada_inicial, coordenada_inicial]
    sobrevivente = input()
    while sobrevivente not in lista_sobreviventes:
        sobrevivente = input()
    quem_anda = lista_sobreviventes.index(sobrevivente) #para saber quem vai fazer a movimentação e onde eu mexo na lista das posições
    movimento = input().split()
    pessoa_viva = nova_posicao(quem_anda)
    if pessoa_viva == False: #se ele tentar sair da matriz o assassino pega ele