objetivos_da_missao = ["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
itens_bonus = ["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixos = ["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]
lista_coleta = []
quantidade = []
pontuacao = 0
cont_objetivos = 0
quant_bubble = 0

#FASE 1
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

#FASE 2