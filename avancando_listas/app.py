lista = [10, 20, 30, 40]

print(lista)

del lista[0]

print(lista)

del lista[len(lista) - 1]

print(lista)

lista_dois = []

i = 0

while i <= 10:
    lista_dois.append(i)
    i = i + 1

print(lista_dois)

j = 0

while j < len(lista_dois):
    if lista_dois[j] == 4:
        del lista_dois[j]
    j = j + 1

print(lista_dois)