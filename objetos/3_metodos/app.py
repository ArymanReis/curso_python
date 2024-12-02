class Skate:
  def __init__(self, shape, truck, rodas, rolamentos):
    self.shape = shape
    self.truck = truck
    self.rodas = rodas
    self.rolamentos = rolamentos

  def manobra(self):
    print("Flip")

  def novo_rolamento(self, novo_rolamento):
    self.rolamentos = novo_rolamento


longboard = Skate("Element", "Crail", "Bones", "Speed Fire")

longboard.novo_rolamento("Back11")

print(longboard.rolamentos)

longboard.manobra()

