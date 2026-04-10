total_moedas = 0
dia = 1
numero_desculpa = 1

print("Ô promessa sem jeito…")
print()
for i in range(7):
    print(f"Dia {dia}: Quantas moedas João Grilo conseguiu arrecadar hoje?")
    moedas = int(input())
    total_moedas += moedas
    print(f"No dia {dia}, o baú já tem R$ {total_moedas}")
    dia += 1
print()
print(f"Total arrecadado após o plano: R$ {total_moedas}")
print()

if total_moedas == 0:
    print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")
    print()
    print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
    print()
    quant_desculpas = int(input())
    for i in range (quant_desculpas):
        print(f"Digite a {numero_desculpa}ª desculpa:")
        numero_desculpa += 1
        desculpa = input()
        print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")
else:
    print("João Grilo começa a despedida da cachorra:")
    print("'Canis Mortus, Dinherus no Bolsus'")
    print("'Caro nostra quae in patina eius est, canis.'")
    print()
    print("João Grilo, o padeiro acreditou?")
    resposta = input()
    if resposta.lower() == "sim":
        print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
        print("Como o padeiro acreditou?")
    else:
        print("O padeiro não acreditou... João Grilo parte para o Plano B!")
        print()
        print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
        print()
        quant_desculpas = int(input())
        for i in range (quant_desculpas):
            print(f"Digite a {numero_desculpa}ª desculpa:")
            numero_desculpa += 1
            desculpa = input()
            print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")

print("Chicó: 'Não sei, só sei que foi assim!'")