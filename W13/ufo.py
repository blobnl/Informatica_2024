'''
input
elenco dei singoli avvistamenti
paese, forma, durata, descrizione

ouput
- paese con > avvistamenti
- forma UFO > segnalata
- avvistamento di durata più lunga

paesi = {}
forme = {}
durataMax = 0

per ogni avvistamento:
    - aggiornare gli avvistamenti per paese avvistamento
    - aggiorna avvistamenti per forma avvistamento
    - se durata avvistamento > durataMax
        durataMax = durata avvistamento
        memorizza (forma, durata, descrizione)

stampa i dati richiesti

'''

import csv
from operator import itemgetter

def main():
    paesi = {}
    forme = {}
    maxAvvistamento = (0, '', '') # durata, descrizione, forma

    with open('ufo_sightings.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            (paese, forma, durata, descrizione) = (row[2], row[3], int(row[4]), row[5])
            if paese not in paesi:
                paesi[paese] = 1
            else:
                paesi[paese] += 1
            if forma not in forme:
                forme[forma] = 1
            else:
                forme[forma] += 1

            if durata > maxAvvistamento[0]:
                maxAvvistamento = (durata, descrizione, forma)

    maxPaese = max(paesi.items(), key = itemgetter(1))
    maxForma = max(forme.items(), key = itemgetter(1))

    print(f'Il paese con il maggiorn numero di avvistamenti è {maxPaese[0]}')
    print(f'Forma di UFO più comunemente segnalata: {maxForma[0]}')
    print(f'Avvistamento di durata più lunga: {maxAvvistamento[1]} (Durata: {maxAvvistamento[0]} Forma: {maxAvvistamento[2]})')

main()