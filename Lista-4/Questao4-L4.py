def compra_de_plantas():
    print("O quintal está sendo invadido! Prepare a melhor linha de defesa possível!")
    posicao = 0
    quantidade_sois = int(input())
    nome_planta = ""
    compra = False
    while nome_planta != "FIM": #fazendo a compra das plantas
        nome_planta = input()
        if nome_planta == "Disparervilha":
            if quantidade_sois >= 50:
                quantidade_sois -= 50
                quantidade_plantas[0] += 1
                compra = True
            else:
                print("Você não tem sóis suficientes para isso!")
                compra = False
        elif nome_planta == "Noz-Obstáculo":
            if quantidade_sois >= 75:
                quantidade_sois -= 75
                quantidade_plantas[1] += 1
                compra = True
            else:
                print("Você não tem sóis suficientes para isso!")
                compra = False
        elif nome_planta == "Gelervilha":
            if quantidade_sois >= 100:
                quantidade_sois -= 100
                quantidade_plantas[2] += 1
                compra = True
            else:
                print("Você não tem sóis suficientes para isso!")
                compra = False
        if compra == True and nome_planta != "FIM":
            linha_de_combate[posicao] = nome_planta
        posicao += 1

def batalha():  
    tipo_zumbi = input()
    vida = 10
    velocidade = 2
    vida_noz = 2
    passagem = False
    if tipo_zumbi == "Zumbi Cabeça-de-Cone":
        vida = 14
    print("Lá vem o zumbi... espero que suas plantas estejam preparadas!")
    combate_acontecendo = True
    posicao = 0
    linha_de_combate.reverse() #inverte a linha de combate, logo, o zumbi vai percorrer da direita pra esquerda, já que as plantas tão da direita pra esquerda
    while combate_acontecendo == True and posicao < 18:
        parada = True
        for i in range(velocidade): #verificador de quantas casas ele avança
            if parada == True and posicao < 18:
                    if linha_de_combate[posicao] != "":
                        parada = False
                    else:
                        posicao += 1
        if posicao < 18:
            vida -= quantidade_plantas[0] + quantidade_plantas[2]
            velocidade -= quantidade_plantas[2]
            if velocidade < 1:
                velocidade = 1
            if tipo_zumbi == "Zumbi do Jornal":
                if vida <= 5 and passagem == False:
                    passagem = True
                    velocidade = 3
                if quantidade_plantas[1] > 0 and passagem == True:
                        velocidade = 2
            if vida <= 0:
                print("Bom trabalho! Dave Doidão nunca esteve tão feliz...")
                combate_acontecendo = False
            else:
                if linha_de_combate[posicao] == "Noz-Obstáculo":
                    if tipo_zumbi == "Zumbi Saltador":
                        posicao += 1
                    if tipo_zumbi != "Zumbi Saltador":
                        if vida_noz == 2:
                            vida_noz = 1
                        elif vida_noz == 1:
                            vida_noz = 2
                            linha_de_combate[posicao] = ""
                            posicao += 1
                            quantidade_plantas[1] -= 1
                            print("NOMNOMNOM!")
                elif linha_de_combate[posicao] == "Disparervilha":
                    linha_de_combate[posicao] = ""
                    quantidade_plantas[0] -= 1
                    posicao += 1
                    print("NOMNOMNOM!")
                elif linha_de_combate[posicao] == "Gelervilha":
                    linha_de_combate[posicao] = ""
                    quantidade_plantas[2] -= 1
                    posicao += 1
                    print("NOMNOMNOM!")
    if combate_acontecendo == True:
        print("O zumbi chegou à porta! Você perdeu!")
  
linha_de_combate = []
quantidade_plantas = [0, 0, 0] #disparervilha, noz-obstáculo, gelervilha

for i in range(18):
    linha_de_combate.append("")

compra_de_plantas()
batalha()