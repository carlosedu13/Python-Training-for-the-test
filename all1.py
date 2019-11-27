# EX 2

num = int(input("Digite quantos números deseja: "))

i = 0
numeros = []

while len(numeros) < num:
    if i % 2 != 0 and i > 0:
        numeros.append(i)
    i+=1

print(numeros)

# EX 3

cont = 1
numeros = []
pares = []
impares = []

while cont <= 20:
    numeros.append(int(input(f'Digite {cont}º numero dos vinte: ')))
    cont+=1

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Todos os números digitados: {numeros.sort()}')
print(f'Todos os números pares: {pares.sort()}')
print(f'Todos os números impares: {impares}')

# EX 4

notas = []

while True:
    nota = float(input("Digite uma nota ou o valor -1 para encerrar a entrada de notas: "))
    if nota == -1:
        break
    notas.append(nota)

# Letra A do exercício

print(len(notas))

# Letra B do exercício

print(notas)

# Letra C do exercício

for nota in notas[::-1]:
    print(nota)

# Letra D do exercício

print(f'A soma de todos os valores digitados é: {sum(notas)}')

# Letra E do exercício

print(f'A média dos valores na lista é: {sum(notas) / len(notas)}')

# Letra F do exercício
media = sum(notas) / len(notas)
print(f'Os valores a cima da média são: {list(filter(lambda valor: valor > media, notas))}')

# Letra G do exercício
print(f'Os valores abaixo de 7 são: {list(filter(lambda valor: valor < 7, notas))}')

print('------------------------Programa encerrado------------------------')


# EX 5

numeros = []
contador = 1

while contador <= 10:
    numero = float(input("Digite um numero: "))
    numeros.append(numero)
    contador += 1

print(f'A soma dos quadrados é {sum(list(map(lambda valor: valor * valor, numeros)))}')
