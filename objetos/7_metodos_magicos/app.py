class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return "O nome do usuário %s e tem %d anos e é um %s" % (self.nome, self.idade, self.profissao)
    
ary = Pessoa("Aryman", 38, "Programador")

print(ary.__str__())
        