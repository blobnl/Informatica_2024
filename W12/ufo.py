'''
input:
data - ora - paese - forma - durata - descrizione

output:
paese con + avvistamenti
forma con + avvistamenti
avvistamento durata + lunga

'''
import csv
from operator import itemgetter

def analizzaAvvistamenti(filename):
    nazioni = {}
    forme = {}
    avvPiuLungo = ('', -1, '')

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            (paese, forma, durata, desc) = (row[2],
                    row[3], int(row[4]), row[5])
            nazioni[paese] = nazioni.get(paese, 0) + 1
            forme[forma] = forme.get(forma, 0) + 1

            avvPiuLungo = max(avvPiuLungo, (forma, durata, desc), key = itemgetter(1))
            '''
            if durata > avvPiuLungo[1]:
                avvPiuLungo = (forma, durata, desc)
            '''
    
    nazioniOrdinate = sorted(nazioni.items(), key = itemgetter(1), reverse = True)
    # la lista contiene tuple (nazione, avv) --> quindi mi serve il primo campo della tupla
    nazioneMA = nazioniOrdinate[0][0]
    formeOrdinate = sorted(forme.items(), reverse = True, key = itemgetter(1))
    formaMA = formeOrdinate[0][0]

    return (nazioneMA, formaMA, avvPiuLungo)

def main():
    (nazioneMA, formaMA, avvPiuLungo) = analizzaAvvistamenti('ufo_sightings.csv')
    print(f'Paese con il maggior numero di avvistamenti: {nazioneMA}')
    print(f'Forma di UFO più comunemente segnalata: {formaMA}')
    print(f'Avvistamento di durata più lunga: {avvPiuLungo[2]} (Durata: {avvPiuLungo[1]} secondi, Forma: {avvPiuLungo[0]})')


main()