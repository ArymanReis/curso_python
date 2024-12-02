soma = lambda x: x + 10

print(soma(50))

soma_dois_numeros = lambda a, b: a + b

print(soma_dois_numeros(4, 5))

'''
def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num

    return soma

s = soma_todos(5,22,55,33,95,355)
print(s)

s2 = soma_todos(4,5,6)
print(s2)

def mult_todos(*mult):
    m = 1
    for multiplicar in mult:
        m *= multiplicar

    return m    

ml = mult_todos(2,6,3)
print(ml)


def reune_dados(nome, idade, profissao, func):
    apresentacao = func(nome, idade, profissao)
    return apresentacao

def apresenta_dados(nome, idade, profissao):
    frase = "O nome do usário é %s e sua idade é %d anos e ele é um %s" % (nome, idade, profissao)
    return frase

print(reune_dados("Aryman", 38, "Programador", apresenta_dados))

apresentacao = reune_dados("Abrãao", 1, "Pai da fé", apresenta_dados)

print(apresentacao)


def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def operacao(a, b, c):
    resultado = c(a, b)
    return resultado

a = operacao(5, 5, soma)

print(a)

b = operacao(10, 5, multiplicacao)

print(b)


def soma_numeros(a, b, c = 10):
    print(a + b + c)

soma_numeros(1, 2, 3)
soma_numeros(10, 20,)

def criar_escada(degraus):
    i = 1
    while i <= degraus:
        print("#" * i)
        i = i + 1

criar_escada(10)

def imprime_nome(nome = "Aryman"):
    print("Olá! %s" % nome)

imprime_nome()

imprime_nome("Marcus")


def soma_ate_100(n):
    if n < 100:
        n += 1
        print(n)
        return soma_ate_100(n)
    else:
        return n

numero = 94
nun_100 = soma_ate_100(numero)

print(nun_100)

escopo_global = "Tchau"

def teste():
    teste = "Olá"
    print(teste)
    print(escopo_global)

teste()

escopo_global = "Até logo"

teste()

# Devo evitar ao máximo usar variávél no escopo global, sempre declarar variáveis dentro das funções, devido as variáveis fora da função podem ser alteradas. Em funçoes diferentes posso usar o mesmo nome.



def digaOi(nome):
    print("Olá %s " % nome)

digaOi("Aryman")
digaOi("BRUNA")

def digaOla():
    print("Olá mundo!")
    print("Olá universo!")

digaOla()

def multiplicacao(a, b):
    print(a * b)

multiplicacao(2, 4)

nun_a = 10
nun_b = 20

multiplicacao(nun_a, nun_b)

def saudacao(nome):
    return "Olá %s" % nome

sds = saudacao("Aryman Reis")

print(sds)

print(sds + ". Tudo Bem?")

def soma(a, b):
    return a + b

nun = soma(5, 8)

print(nun)
print(nun + 10)

def profissao(nome):

    p = ""

    if nome == "Aryman":
        p = "Programador"
    else:
        p = "Não identificado"

    return p

n = profissao("Aryman")
print(n)'''

