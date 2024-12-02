if 10 > 5:
    verdura = "Cenoura"
    print("Entrou no if")
    print(verdura)

    nome = "Aryman"

    if nome == "Aryman":
        print("Olá %s" % nome )

idade = int(input("Qual a sua idade?"))

if idade >= 18:
    print("Sua idade é: %d pode entrar na balada" % idade)

numero_rodas = int(input("Quantas rodas tem seu carro?"))

if numero_rodas >= 4:
    print("Pague o pedágio")

if numero_rodas < 4:
    print("Pode passar livremente")

# Estrutura condicional if 

poupanca = 200

saque = 200

if saque <= poupanca:
    print("Você sacou R$%d " % saque)
else:
    print("Você não tem saldo para sacar R$%d " % saque)
    print("Sua poupança te no momento tem R$%d " % poupanca)

salario = float(input("Qual seu salário?"))

if salario > 1800:
    print("Você precisa pagar o imposto de renda")
else:
    print("Você NÃO precisa pagar o imposto de renda")

numero_um = int(input("Digite primeiro número: "))
numero_dois = int(input("Digite segundo número: "))

multiplicacao = numero_um * numero_dois

if multiplicacao <= 100:
    print("O número é baixo")
else:
    print("O número é alto")

# if aninhado

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Você pode entrar na festa")

    metodo_de_pagamento = input("Como você vai pagar a entrada")

    if metodo_de_pagamento == "dinheiro":
        print("A fila do dinheiro é a número 1 ")
    else:
        print("A fila do cartão é a número 2")

else:
    print("Você NÂO pode entrar na festa")


nome = input("Digite o seu nome: ")

if nome == "Aryman":
    print("Você é um usuário admin")
elif nome == "João":
    print("Olá, você é um produtor de conteúdo")
else:
    print("Você é um usuário comum!")

numero = int(input("Digite um número: "))

if numero > 0 and numero <= 5:
    print("Maior que 0")
elif numero > 5 and numero <= 10:
    print("Maior que 5")
elif numero > 10 and numero <= 5:
    print("Maior que 10")
else: 
    print("Maior que 20")