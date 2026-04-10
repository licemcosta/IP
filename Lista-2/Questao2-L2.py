din_inicial = int(input())
custo = 0
quant_compras = 0
custo_total = 0
print(f"A família possui {din_inicial} ainda, talvez ele fique tranquilo hoje")

while din_inicial > 0:
    compra = input()
    if compra == "Amauri":
        din_inicial = 0
        print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
    else:
        custo = int(input())
        if din_inicial < custo:
            print ("Enlouqueceram? Vocês estão falidos")
            din_inicial = 0
        else:
            din_inicial -= custo
            quant_compras += 1
            custo_total += custo
            if custo < 1000:
                print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')
            elif custo > 500000:
                print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")
            else:
                print(f"Gastaram {custo} reais para comprar um(a) {compra}")

            if compra == "carro":
                modelo = input()
                if modelo == "chevette":
                    print("chevette : Relembrando as origens será?")
                elif modelo == "jeep":
                    print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
                elif modelo == "bmw":
                    print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")    
            if din_inicial == 0:
                print("Enlouqueceram? Vocês estão falidos")

            
    
print(f"{quant_compras} - {custo_total} reais")