quant_removidos = 0

print("Bem vindos, exploradores! Começaremos à Missão Lazarus!")
planetas_candidatos = input().split(", ") #separar cada planeta e suas características

print("Planetas armazenados. Fim da Missão Lazarus.")
for item in planetas_candidatos[::-1]: #faz uma lista de cada item e separa os termos com cada característica como um novo item
    termo = item.split(" - ") 
    if termo[2] == "falha" or int(termo[1]) < 6:
        planetas_candidatos.remove(item)
        quant_removidos += 1


print("Hora de escolher os melhores planetas para habitarmos!")

numero_planetas = len(planetas_candidatos)
for i in range (numero_planetas): #rankeia os planetas
    planetas_candidatos[i] = planetas_candidatos[i].split(" - ")
    planetas_candidatos[i][1] = int(planetas_candidatos[i][1])
for j in range(numero_planetas):
    for i in range(numero_planetas-j-1):
        if(planetas_candidatos[i][1] < planetas_candidatos[i+1][1]):
            planetas_candidatos[i], planetas_candidatos[i+1] = planetas_candidatos[i+1], planetas_candidatos[i]
        elif(planetas_candidatos[i][1] == planetas_candidatos[i+1][1]):
            if(planetas_candidatos[i][0] > planetas_candidatos[i+1][0]):
                planetas_candidatos[i], planetas_candidatos[i+1] = planetas_candidatos[i+1], planetas_candidatos[i]

planetas = [planeta[0] for planeta in planetas_candidatos]
nomes = ", ".join(planetas)
if numero_planetas != 0:
    print(f"Planetas habitáveis encontrados: {nomes}.")
else:
    print("Planetas habitáveis encontrados: nenhum.")

print(f"Quantidade de planetas desconsiderados: {quant_removidos}.")