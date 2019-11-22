def exercicio2():
    velocidades = []
    continuar = 0

    while True:
        velocidades.append(velocidade(int(input("Digite a distância percorrida por seu veiculo: ")), int(input("Digite o tempo que levou para percorrer esta distância: "))))

        continuar = int(input("Quer adicionar outro valor? Digite o valor númerico dentro dos colchetes ( NÃO[0] e SIM[1] ): "))
        
        if continuar == 0:
            break

    media = velocidadeMedia(velocidades)
    print(f'A média de velocidade foi {media}')

def velocidade(distancia, tempo):
    return distancia / tempo

def velocidadeMedia(velocidades):
    return sum(velocidades) / len(velocidades)

exercicio2()
