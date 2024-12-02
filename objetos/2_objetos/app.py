class Skate:
  def __init__(self, shape, truck, rodas, rolamentos):
    self.shape = shape
    self.truck = truck
    self.rodas = rodas
    self.rolamentos = rolamentos

longboard = Skate("Element", "Crail", "Bones", "Speed Fire")

print(longboard.shape, longboard.rolamentos)
print(longboard.truck)