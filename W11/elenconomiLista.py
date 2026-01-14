import csv
from operator import itemgetter

'''
spoluzione con lista: NON OTTIMALE (da non seguire...)

'''

def leggiElenco(filename):
    elenco = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for studente in reader:
            nome = studente['NOME']
            # creo record (nome, occorrenze)
            # {'nome': x, 'occorrenze': y}
            trovato = False
            for elemento in elenco:
                if elemento['nome'] == nome:
                    elemento['occorrenze'] += 1
                    trovato = True
                    break
            if not trovato:
                record = {'nome': nome, 'occorrenze': 1}
                elenco.append(record)

    return elenco
    

def main():
    elenco = leggiElenco('14BHDWZ_2026.csv')
    ordinati = sorted(elenco,
                      key = itemgetter('occorrenze'),
                      reverse = True)
    
    N = 10
    for i in range(N):
        (nome, occorrenza) = (ordinati[i]['nome'], ordinati[i]['occorrenze'])
        print(f'{nome:20s} {occorrenza: 6d}')

main()
