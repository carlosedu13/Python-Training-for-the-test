def media(alunos, notas):
    alunoENota = []

    alunosNomes = open(alunos, 'r')
    alunosNotas = open(notas, 'r')

    while True:
        nome = alunosNomes.readline()
        nota = alunosNotas.readline()
        alunoENota.append(nome, nota)
    
    alunos = open('final.txt', 'w')
    alunos.writelines(alunoENota)

media("alunos.txt", "notas.txt")
