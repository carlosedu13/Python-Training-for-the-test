num = int(input("Digite quantos números deseja: "))

i = 0
numeros = []

while len(numeros) < num:
    if i % 2 != 0 and i > 0:
        numeros.append(i)
    i+=1

print(numeros)
