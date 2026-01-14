'''
casate = {} chiave: lista
materie = {}
studenti = ()
per ogni record:
    aggiorna casata
    aggiorna materia
    aggiorna studente

calcola medie per
    casata
    materia
    studente

stampa casat per ordine chiave
trova max studente e stampa
trova max/min materia e stampa
'''
import csv
from operator import itemgetter

def aggiorna(diz, chiave, valore):
    if chiave in diz:
        diz[chiave].append(valore)
    else:
        diz[chiave] = [valore]

def calcolaMedie(diz):
    for (chiave, valori) in diz.items():
        media = sum(valori) / len(valori)
        diz[chiave] = media

def leggiRisultati(filename):
    casate = {}
    materie = {}
    studenti = {}
    # chiave: []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            voto = int(row['punti'])
            aggiorna(casate, row['casata'], voto)
            aggiorna(materie, row['materia'], voto)
            aggiorna(studenti, row['nome'] + ' ' + row['cognome'], voto)

    calcolaMedie(casate)
    calcolaMedie(materie)
    calcolaMedie(studenti)

    return (casate, materie, studenti)

def main():
    (casate, materie, studenti) = leggiRisultati('risultati.csv')

    # stampa per acasata
    print('Media dei punti per casata:')
    for casata in sorted(casate):
        print(f'- {casata}: {casate[casata]:.2f}')

    maxStudente = max(studenti.items(), key = itemgetter(1))
    print(f'\nStudente con la media più alta: {maxStudente[0]} ({maxStudente[1]:.2f})')

    minMateria = min(materie.items(), key = itemgetter(1))
    maxMateria = max(materie.items(), key = itemgetter(1))

    print(f'\nMateria più facile: {maxMateria[0]} ({maxMateria[1]:.2f})')
    print(f'\nMateria più difficile: {minMateria[0]} ({minMateria[1]:.2f})')

main()


