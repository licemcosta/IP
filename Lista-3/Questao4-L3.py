quant_removidos = 0

print("Bem vindos, exploradores! Começaremos à Missão Lazarus!")
planetas_candidatos = input().split(", ") #separar cada planeta e suas características

print("Planetas armazenados. Fim da Missão Lazarus.")
for item in planetas_candidatos: #faz uma lista de cada item e separa os termos com cada característica como um novo item
    termo = item.split("-") 
    if termo[2] == "falha":
        planetas_candidatos.remove(item)
        quant_removidos += 1
    if termo[1]:
        termo[1] = int(termo[1])
        if termo[1] < 6:
            planetas_candidatos.remove(item)
            quant_removidos += 1

print("Hora de escolher os melhores planetas para habitarmos!")

numero_planetas = len(planetas_candidatos)
for i in range (numero_planetas): #rankeia os planetas
    planeta[i] = planeta.split("-")
for j in range(numero_planetas):
    for i in range(numero_planetas-i-1):
        if(planeta[i][1] < planeta[i+1][1]):
            planeta[i], planeta[i+1] = planeta[i+1], planeta[i]
        elif(planeta[i][1] == planeta[i+1][1]):
            if(planeta[i][0] > planeta[i+1][0]):
                planeta[i], planeta[i+1] = planeta[i+1], planeta[i]

print(f"Quantidade de planetas desconsiderados: {quant_removidos}.")