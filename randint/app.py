import random

print(random.randint(1, 10))

aleatorio = random.randint(1, 2)

palpite = int(input("Advinhe o número: "))

if aleatorio == palpite:
  print("Você acertou!")
else:
  print("Você errou!")