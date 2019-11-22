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
