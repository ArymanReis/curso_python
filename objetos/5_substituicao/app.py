
class Pessoa:
    def fala(self):
        print("Olá pessoal!")

class Aryman(Pessoa):
    def fala(self):
        print("Olá pessoal, eu sou Aryman")


class Abraao(Pessoa):
    pass

ary = Aryman()

ary.fala()

abraao = Abraao()

abraao.fala()