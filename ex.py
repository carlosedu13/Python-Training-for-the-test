crescente = open('assets/crescente.txt', 'r')
numerosCrescentes = crescente.readlines()
numerosCrescentes = []

i = 0

while i <=100:
    numerosCrescentes.append(f'{i}; ')
    i+=1
    
crescente = open('assets/crescente.txt', 'w')
crescente.writelines(numerosCrescentes)
crescente.close()


# -------------------------------------------------------------------------------------------

decrescente = open('assets/decrescente.txt', 'r')
numerosDecrescentes = decrescente.readlines()
numerosDecrescentes = []

Imenos = 100

while Imenos >= 0:
    numerosDecrescentes.append(f'{Imenos}; ')
    Imenos-=1
    
decrescente = open('assets/decrescente.txt', 'w')
decrescente.writelines(numerosDecrescentes)
decrescente.close()

# -------------------------------------------------------------------------------------------

