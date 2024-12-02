'''l = ["Sofá", "Televisão", "Barco", "Poltrona"]

i = 0

item_procurado = input("O que deseja buscar na casa?")
achou = False

while i < len(l):
    if l[i] == item_procurado:
        print("Encontramos um %s!" % item_procurado)
        achou = True
    i = i + 1


if achou == False:
    print("Não encontrado %s!" % item_procurado)'''

itens_carro = ["Porta", "Pneu", "Estepe", "Maçaneta", "Janela", "Chave", "Motor", "Marcha"]

iten_um = input("O que deseja procurar?")
iten_dois = input("O que deseja procurar depois?")

i = 0

while i < len(itens_carro):
    if itens_carro[i] == iten_um:
        print("O primeiro objeto foi encontrado antes! %s " % iten_um)
        break
    elif itens_carro[i] == iten_dois:
        print("O segundo objeto foi encontrado antes! %s " % iten_dois)
        break

    i = i + 1