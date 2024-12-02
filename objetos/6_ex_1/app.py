class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Olá galera!")

class Superheroi(Pessoa):
    def __init__(self, nome, idade, super_poder):
        super().__init__(nome, idade)
        self.super_poder = super_poder

    def utilizar_super_poder(self):
        print("O herói utilizou o superpoder da %s" % self.super_poder)

abraao = Pessoa("Abraão", 1)

abraao.falar()

aryman = Superheroi("Aryman", 38, "Paternidade")

aryman.utilizar_super_poder()

print(aryman.idade)

