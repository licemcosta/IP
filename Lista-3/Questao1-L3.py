quant_eventos = int(input())
nome = ""
print("Édipo: Inicializando sistema de embarque. Tripulantes atuais: Zaphod Beeblebrox, Ford Prefect, Arthur Dent, Marvin")
lista_tripulantes = ["Zaphod Beeblebrox", "Ford Prefect", "Arthur Dent", "Marvin"]
for i in range(quant_eventos):
    evento = input()
    if "embarcar" in evento:
        nome = evento.replace("embarcar ", "")
        lista_tripulantes.append(nome)
        if nome == "Trillian":
            print("Finalmente alguém sensata a bordo! Bem-vinda, Trillian!")
    elif "remover" in evento:
        nome = evento.replace("remover ", "")
        lista_tripulantes.remove(nome)
        if nome == "Marvin":
            print("Ninguem se importa comigo mesmo. Tchau")
        if nome == "Arthur Dent":
            print("Eu só queria poder tomar chá... vou descer no próximo planeta")
    elif "mover" in evento:
        evento = evento.replace("mover ", "")
        nome = evento.rsplit(" ", 1)[0]
        posicao = int(evento.rsplit(" ", 1)[1])
        lista_tripulantes.remove(nome)
        lista_tripulantes.insert(posicao, nome)
        if nome == "Zaphod Beeblebrox" and posicao == 0:
            print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")
        if nome == "Ford Prefect" and posicao == 0:
            print("Sou um escritor do Guia! Mereço destaque!")
    elif "priorizar" in evento:
        nome = evento.replace("priorizar ", "")
        lista_tripulantes.remove(nome)
        lista_tripulantes.insert(0, nome)
        if nome == "Zaphod Beeblebrox":
            print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")
        if nome == "Ford Prefect":
            print("Sou um escritor do Guia! Mereço destaque!")

if len(lista_tripulantes) == 1:
    print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {lista_tripulantes[0]}.")
if len(lista_tripulantes) == 2:
    print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {lista_tripulantes[0]} e {lista_tripulantes[1]}.") 
if len(lista_tripulantes) >= 3:
    print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {lista_tripulantes[0]}, {lista_tripulantes[1]} e {lista_tripulantes[2]}.")
    lista_tripulantes.pop(2)
    lista_tripulantes.pop(1)
    lista_tripulantes.pop(0)
    if len(lista_tripulantes) > 0:
        print("Convocando tripulantes:")
        for item in lista_tripulantes:
            print("- " + item)

