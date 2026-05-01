quant_dias = int(input())

def classificar_alvo():
    alvo[1] = int(alvo[1])
    if alvo[1] >= 7:
        if alvo[2] == "sim":
            tipo_alvo = "Elite"
        else:
            tipo_alvo = "Executor"
    elif 7 > alvo[1] >= 4:
        if alvo[2] == "sim":
            tipo_alvo = "Veterano"
        else:
            tipo_alvo = "Operador"
    else:
        tipo_alvo = "Iniciante"
    print(f"Analisando alvo: {alvo[0]}... Classificação: {tipo_alvo}")
    return tipo_alvo

def analisar_tentativas():
    fracassos = 0
    soma = 0 
    for termo in range(len(tentativas)):
        tentativas[termo] = int(tentativas[termo])
        soma += tentativas[termo]
    if soma % len(tentativas) == 0:
        print(f"Missão Completa. | Manipulação temporal: {len(tentativas)} tentativa(s)")
    else:
        print("Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.")
        fracassos += 1
    return fracassos


favoritos = [3, 5]
def ataques_refletidos(ataques_inimigos):
    quant_refletidos = 0
    for termo in range(len(ataques_inimigos)):
        ataques_inimigos[termo] = int(ataques_inimigos[termo])
        if ataques_inimigos[termo] % 3 == 0 or ataques_inimigos[termo] % 5 == 0:
            quant_refletidos += 1
    print(f"Dragão refletiu {quant_refletidos} ataque(s)!")

fracasso = 0
dias_passados = 0
print("Entendo… Vamos começar do começo.")
print()
for i in range(quant_dias + 1):
    if fracasso == 0:
        musica = input().split(" - ") #nome da música - autor
        alvo = input().split(" - ") #nome - nivel de ameaça - armado
        print(f"====== Restam {(quant_dias - dias_passados)} dias. ======")
        dias_passados += 1
        print(f"Escutando: {musica[0]} - {musica[1]}")
        if musica[1] != "DJ Electrohead" or alvo[0] != "DJ Electrohead": #código roda normalmente
            tentativas = input().split()
            classificar_alvo()
            fracasso = analisar_tentativas()
            if fracasso == 0:
                ataques_inimigos = input().split()
                ataques_refletidos(ataques_inimigos)
                print()
        else: #caso especial
            print("DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.")

if fracasso == 0:
    print("====== FIM DAS MISSÕES ======")
    print("Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.")

