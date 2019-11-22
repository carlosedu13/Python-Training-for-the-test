numeros = []
contador = 1

while contador <= 10:
    numero = float(input("Digite um numero: "))
    numeros.append(numero)
    contador += 1

print(f'A soma dos quadrados é {sum(list(map(lambda valor: valor * valor, numeros)))}')
