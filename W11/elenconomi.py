import csv
from operator import itemgetter

'''
elenco = []
per ogni nome:
    se nbome è in elenco -> aumenta occorrenza di 1
    altrimenti aggiungi nome con occorrenza 1

ordinare per occorrenze in ordine inverso
stampa i primi n

'''

def leggiElenco(filename):
    elenco = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for studente in reader:
            nome = studente['NOME']
            if nome in elenco:
                elenco[nome] += 1
            else:
                elenco[nome] = 1

    return elenco
    

def main():
    elenco = leggiElenco('14BHDWZ_2026.csv')
    ordinati = sorted(elenco.items(),
                      key = itemgetter(1),
                      reverse = True)
    
    N = 10
    for i in range(N):
        (nome, occorrenza) = ordinati[i]
        print(f'{nome:20s} {occorrenza: 6d}')

main()
