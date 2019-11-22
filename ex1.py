contador0 = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contadorGeral = 0

acumulador0 = 0
acumulador1 = 0
acumulador2 = 0

while True:
    opcao = input("Continuar... S(SIM), N(Não): ")
    if opcao == "N":
        break
    numero = int(input("Digite o número: "))
    if numero < 35:
        contador0 = contador0 + 1
    if numero > 0:
        contador1 = contador1 + 1
        acumulador0=acumulador0 + numero
    else:
        contador2 = contador2 + 1
        acumulador1 = acumulador1 + numero
    if numero % 2==0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        contador3 = contador3 + 1
        acumulador2 = acumulador2 + numero
    if numero > 49 and numero < 101:
        # acm4 = acm4 + 1
        contador4 = contador4 + 1
    if numero > 9 and numero < 21:
        contador5 = contador5 + 1
        # acm5 = acm5 + 1
    contadorGeral = contadorGeral + 1

print("QTD num inferiores a 35,", contador0)
print("Media num Positivo,", acumulador0/contador1)
print("Media num negativo,", acumulador1/contador2)
print("Media num div 2/3/5/7,", acumulador2/contador3)
print("A porcentagem de numero,",(contador4*100/contadorGeral))
print("A porcentagem é,", (contador5*100)/contadorGeral)
