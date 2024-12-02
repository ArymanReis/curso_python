print("Antes do loop")

numero = 0

while numero < 5:
    print(numero)

    if numero == 3:
        print("O número é 3!")

    numero = numero + 1

print("Depois do loop")

num = 1

while num <= 50:
    if num % 2 == 0:
        print(num)
    num = num + 1

number = 1

while number <= 10:

    print(number)

    if number == 5:
        
        break

    number = number + 1

print("Após o loop")

n = 20

while n >= 0:
    print(n)

    if n == 5:
        break

    n = n -1

print("Pós loop")

x = 0

while x < 1:
    new_number = int(input("Digite um número: "))

    print(new_number)

    if new_number == 0:
        print("Saindo do loop!")
        break
    