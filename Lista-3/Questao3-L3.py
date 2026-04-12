usuario_terminal = input()
dimensao_alvo = input()
fluido_portal = input()
status_federacao = input()
acao_historico = input()
dimensao_alvo_novo = "" #verificacão do dimensão alvo (numeros e letras maiúsculas)
lista_dimensoes = ["C-137", "Planeta Squanch"]

print("Sistema Operacional RickOS v3.14 - Inicializando Arma de Portais...")

if fluido_portal == "Suco de Limão":
    print("BURP Morty, você colocou Suco de Limão onde devia ter número! O sistema pifou!")
else:
    fluido_portal = int(fluido_portal) #se não for suco de limão tem que ser inteiro
    if usuario_terminal == "Rick Prime" or usuario_terminal == "Evil Morty":
        print("Alerta Vermelho: Variante perigosa detectada no terminal!")
    for letra in dimensao_alvo: #retirar os espaços para poder usar o isalpha.()
        if letra != " ":
            dimensao_alvo_novo += letra
    if dimensao_alvo_novo.isalpha() and dimensao_alvo_novo.isupper():
        print("Não precisa gritar, Morty! O painel da arma não é surdo!")
    if acao_historico == "anexar":
        lista_dimensoes.append(dimensao_alvo)
        print("Rastro anexado ao final do histórico.")
    elif acao_historico == "esconder":
        lista_dimensoes.pop()
        print("Apagando o último rastro... Federação idiota.")
    elif acao_historico == "priorizar":
        lista_dimensoes.insert(0, dimensao_alvo)
        print("Sobrescrevendo prioridades. Nova dimensão no topo da lista!")
    if fluido_portal >= 50 and status_federacao == "alta" and len(lista_dimensoes) > 2:
        print("Fuga tática ativada! Saltando por múltiplas dimensões para despistar os insetos!")
    elif  fluido_portal < 15:
        print("Ferrou! A Arma de Portais tá quase vazia. Pega a nave, Morty!")
    elif status_federacao == "baixa" and dimensao_alvo in lista_dimensoes:
        print(f"Ah, já estivemos na dimensão {dimensao_alvo}. Bora encher a cara no Blips and Chitz!")
    else:
        print("Preparando salto interdimensional... Wubba Lubba Dub Dub!")
