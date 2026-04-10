quant_pen = int(input())
numero_pen = 0
letras_tentativa = ""
senha = "a"
senha_crip = ""
pen_abertos = 0
num_tentativa = 0

print("Avenida Brasil: A Vingança de Nina!")

for i in range(quant_pen):
    senha = input()
    num_tentativa = 0
    for letra in senha:
        if letra != " ":
            num_tentativa += 2
    numero_pen += 1
    letras_tentativa = ""
    print(f"Descriptografando pendrive {numero_pen} de {quant_pen}...")
    while senha != senha_crip and num_tentativa > 0:
            letra_atual = input()
            if letra_atual in senha and letra_atual not in letras_tentativa:
                print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")
            elif letra_atual not in senha and letra_atual not in letras_tentativa :
                print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")
            elif letra_atual in letras_tentativa:
                print("Max: Ele já tentou isso, Carminha...")
            if letra_atual not in letras_tentativa:
                letras_tentativa += letra_atual
            senha_crip = ""
            for letra in senha:
                if letra not in letras_tentativa and letra != " ":
                    senha_crip += "_"
                else:
                    senha_crip += letra
            print(f"Senha: {senha_crip}")
            num_tentativa -= 1
    if senha == senha_crip and num_tentativa >= 0:
        print(f"Tufão: Agora eu sei de toda a verdade! O pendrive {numero_pen} está aberto.")
        pen_abertos += 1
    else:
        print(f"Carminha: Consegui! As fotos do pendrive {numero_pen} estão a salvo comigo.")
print(f"Conseguimos abrir {pen_abertos} de {quant_pen} pendrives!")
if pen_abertos == 0:
    print("Tufão continuará sendo enganado para sempre...")
elif 0 < pen_abertos <= quant_pen*0.5:
    print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")
elif quant_pen*0.5 < pen_abertos < quant_pen:
    print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")
else:
    print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")