'''carro = {
    "Portas": 4,
    "Janelas": 4,
    "Motor": 2.0,
    "Teto_solar": True,
    "Cambio": "Automático"
}

print(carro)

print(carro["Portas"])

livros = {
    "Erogon": 400,
    "Mente milhonária": 360,
    "Sherlock": 600
}

for livro in livros:
    print("O livro %s tem %d páginas" % (livro, livros[livro]))

dicionario = {
    "testando": 2,
    "nome": "Aryman",
    "idade": 29
}

print(dicionario)

print("nome" in dicionario)
print("sobrenome" in dicionario)

if "nome" in dicionario:
    print("O seu nome é %s" % dicionario["nome"])

if "sobrenome" in dicionario:
    print("O seu sobrenome é %s" % dicionario["sobrenome"])

dic = {}

print(dic)

dic["nome"] = "Aryman"

print(dic)

del dic["nome"]

print(dic)'''

carro = {
    "pneus": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4
}

print(carro)

carro["Teto solar"] = 1

print(carro)

del carro["motor"]
del carro["janelas"]

print(carro)