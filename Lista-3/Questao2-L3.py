lista_carol = input().split(", ") #itens que carol quer
itens_carol_atual = [] #itens que carol quer que estão no caminhão atual
itens_carol_restantes = lista_carol.copy() #itens que ainda faltam para carol

print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")

lista_caminhao = input().split(", ") #lista dos itens atuais do caminhão
while lista_caminhao != ["--"]:
    itens_carol_atual = [] #reseta a lista
    for item in lista_caminhao:
        if item in lista_carol:
            itens_carol_atual.append(item) #adiciona os itens do caminhão atual que carol quer nessa lista
    for item in itens_carol_atual:
        if item in lista_carol and item in itens_carol_restantes:
            itens_carol_restantes.remove(item) #itens restante começa com todos os itens e vai removendo a cada caminhão
    if len(itens_carol_atual) > 0: #se tiver itens é porque o caminhão trazia algum item que ela queria
        print(f"Ótimo, esse caminhão trouxe {itens_carol_atual}!")
    else: #se não tiver é porque o caminhão não trazia nada que ela queria
        print("Não encontramos nada que a Carol pediu nesse caminhão.")
    if len(itens_carol_restantes) != 0:
        print(f"Ainda precisamos de {itens_carol_restantes}.")
    lista_caminhao = input().split(", ") #recebe o novo caminhão

if len(itens_carol_restantes) == 0: #achou todos os itens
    print("Conseguimos! A Carol ficará muito feliz :)")
else: #não achou todos os itens
    print("Não conseguimos reunir todos os itens que a Carol precisa :(") 