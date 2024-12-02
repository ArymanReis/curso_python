'''lista = [1,2,3,4,5]

print(lista)

for n in lista:
    print(n)

numeros = [100, 200, 300, 400, 500, 700]

qual_numero_procura = int (input("Que número deseja buscar?"))

for i in numeros:
    if i == qual_numero_procura:
        print("O número %d foi encontrado" % i)

for x in range(10):
    print(x)
    if x == 5:
        print("Aconteceu alguma coisa!")

for a in range(5, 26, 2):
    print(a)

for b in range(3, 100, 18):
    print(b)

lista = [13, 55, 90, 12, 33, 44, 1000, 5, 7]

maior_valor = 0

for n in lista:
    if n > maior_valor:
        maior_valor = n

print(maior_valor)

menor_valor = lista[0]

for i in lista:
    if i < menor_valor:
        menor_valor = i

print("O menor valor é o %d " % menor_valor)

carro_a = ["BMW", 60000]
carro_b = ["Ferrari", 90000]
carro_c = ["VW", 120000]

carros = [carro_a, carro_b, carro_c]

print(carros[0][0])
print(carros[0][1])

for carro in carros:
    print("A marca do carro é: %s " % carro[0])'''

produto_a = ["Camisa", "Azul", 25.63]
produto_b = ["Bermuda", "Marrom", 123.63]
produto_c = ["Casaco", "Bege", 250.63]

lista_produtos = [produto_a, produto_b, produto_c]

print(lista_produtos)

for produto in lista_produtos:
    print("O produto é: %s e tem a cor %s e o seu preço é: R$ %.2f " % (produto[0], produto[1], produto[2]))
