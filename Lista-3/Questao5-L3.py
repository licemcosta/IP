lista_todos_primos = []
lista_primos = []
lista_primos_crescente = []
quant_bubble = 0
numero_secao = int(input())
if numero_secao < 9:
    print("Essa seção foi excluída por motivos que não podem ser revelados. Entre no labirinto e corra novamente.")
else:
    for termo in range(2, numero_secao + 1): #defino a seção
        for numero in range (termo, 2*termo): #defino os números que compõem a seção
            if termo < numero < 2*termo:
                lista_todos_primos.append(numero) #adiciono todos eles na lista para depois remover os não primos
                for k in range (2, numero): #verificação de primos
                    if numero%k == 0 and numero in lista_todos_primos: #se ele for divisível por algum outro ele é removido
                        lista_todos_primos.remove(numero)

    for numero in lista_todos_primos: #lista com 1 repetição de cada primo
        if numero not in lista_primos:
            lista_primos.append(numero)
            lista_primos_crescente = lista_primos.copy()

    quant_primos = len(lista_primos) #algoritmo do bubble sort
    while quant_bubble < quant_primos:
        quant_bubble += 1
        for i in range(quant_primos): 
            if i > 0:
                if lista_primos[i] > lista_primos[i-1]:
                    lista_primos[i], lista_primos[i-1] = lista_primos[i-1], lista_primos[i]
    lista_primos_decrescente = [str(x) for x in lista_primos]
    print(" ".join(lista_primos_decrescente))

    for numero in lista_primos_crescente: #conta a quantidade de vezes que cada primo aparece
        ocorrencia = lista_todos_primos.count(numero)
        print(f"O número {numero} apareceu {ocorrencia} vezes.")

    print("")

    maior_primo = lista_primos[0] #define a seção de destino
    maior_primo = int(maior_primo)
    secao_destino = (maior_primo + 1)//2
    if secao_destino == numero_secao:
        print("Thomas: O cálculo apontou para a seção que você estava! Isso é uma armadilha.")
        print("Minho: O Thomas tem razão.")
    elif secao_destino - numero_secao == 1 or numero_secao - secao_destino == 1:
        print("Thomas: A decodificação diz que a saída está na seção imediatamente anterior a que você estava.")
        print("Minho: Se isso realmente for válido, então restam 2 opções de saída.")
    else:
        print("De todos os cálculos feitos, a única seção que apresentou diferença maior do que 1 foi essa.")