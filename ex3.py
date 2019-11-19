cont = 1
numeros = []]
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
