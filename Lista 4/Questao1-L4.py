lista_chefe = [140] #vida do chefe
lista_hornet = [5, 0, 0, 0, 0, 0] #máscaras totais, mascaras perdidas, mascaras recuperadas, sedas atuais, sedas geradas, sedas perdidas 
def chefe(acao_chefe):
    if acao_chefe == "Acerto":
        lista_hornet[0] -= 1 #máscaras totais
        lista_hornet[1] += 1 #máscaras perdidas
    elif acao_chefe == "Acerto Duplo":
        lista_hornet[0] -= 2 #máscaras totais
        lista_hornet[1] += 2 #máscaras perdidas
    
def hornet(acao_hornet):
    if acao_hornet == "Ferrão":
        lista_chefe[0] -= 10 #dano
        lista_hornet[3] += 2 #sedas atuais
        if lista_hornet[3] > 8: #para não passar do limite do carretel
            lista_hornet[3] = 8
        lista_hornet[4] += 2 #sedas geradas
    elif acao_hornet == "Ataque de Seda" and lista_hornet[3] >= 3:
        lista_chefe[0] -= 20 #dano
        lista_hornet[3] -= 3 #sedas atuais
    elif acao_hornet == "Vincular" and lista_hornet[3] == 8:
        lista_hornet[3] -= 8 #sedas atuais
        lista_hornet[2] += 3 #mascaras recuperadas
        if lista_hornet[0] > 2:
            lista_hornet[0] = 5
        else:
            lista_hornet[0] += 3

nome_chefe = input()
if nome_chefe == "Tessela":
    print("Tessela: Ha Ha Ha! Parece que a aranha retornou.")
elif nome_chefe == "Grande Mãe Seda":
    print("Hornet: Monarca, seu reino de tirania acaba aqui!")
elif nome_chefe == "A Última Juíza":
    print("Hornet: Não posso recuar agora, a cidadela está logo ali.")
else:
    print(f"Hornet: {nome_chefe}, levante sua lâmina!")
print("")
    
def combate(combate_acontecendo):
    acao_hornet = input()
    hornet(acao_hornet)
    if lista_chefe[0] > 0:
        acao_chefe = input()
        chefe(acao_chefe)
        if lista_hornet[0] <= 0:
            combate_acontecendo = False
    else:
        combate_acontecendo = False
    return combate_acontecendo

combate_acontecendo = True
while combate_acontecendo:
    combate(combate_acontecendo)

if lista_chefe[0] == 0:
    print("RESULTADOS DA BATALHA")
    print(f"Máscaras restantes: {lista_hornet[0]}")
    print(f"Máscaras recuperadas: {lista_hornet[2]}")
    print(f"Seda restante: {lista_hornet[3]}")
    print(f"Seda desperdiçada: {lista_hornet[4] - lista_hornet[5]}")
    print()
    print("Hornet: Não cairei tão fácil.")
else:
    print("Hornet: Hm?")
    print(f"Vida Restante: {lista_chefe[0]}")
