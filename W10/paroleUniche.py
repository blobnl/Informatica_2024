'''
Problema: contare il numero di parole uniche (indipendentemente
da maisucolo/minuscolo) nel file in input:
NOTA: una parola è una qualsiasi sequenza di
caratteri alfabetici (quindi NON include segni di punteggiatura/spazi)

ALGPRITMO
crea iinsieme vuoto parole
per ogni riga del filr in ingresso
    per ogni parola nella riga
        aggiungi parola a insieme parole

stampa numero di elementi in insieme

'''

def leggiParoleUniche(filename):
    parole = set()
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            parti = line.strip().split()
            for parte in parti:
                parola = parte.lower().strip(',;.:?!"')
                if parola != '':
                    parole.add(parola)

    return parole



def main():
    FILENAME = 'nurseryrhyme.txt'
    parole = leggiParoleUniche(FILENAME)
    print(f'Il numero di parole uniche in {FILENAME} è {len(parole)}')


main()
