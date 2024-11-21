'''
L’algoritmo di compressione RLE (run length encoding)
prende una lista di numeri in ingresso e la sostituisce
con una sequenza (ripetizioni valore)
[1 1 1 1 2 2 2 3 3 4 4 4 4 4 4 5 6]
[4 1 3 2 2 3 6 4 1 5 1 6]

scrivere un programma che legga da file una sequenza di numeri (consecutivi)
e salvi in ouput le sequenze compresse (una per riga) dopo aver verificato che
la decompressione della stringa compressa sia uguale all'originale
Per ogni stringa, stampare a video il rapporto di compressione
(numero di valori iriginali/numero di valori compressi)

Algoritmo:
----------
per ogni riga
    comprimi elemento
        per ogni elemento
            se uguae al precedente incremeneta contatire,
            altrimenti 
                salva (occ, valore)
                occ = 1
        slava (occ,valore) ultimo elemento
    decomprimi elemento compresso
        per ogni coppia di dati
            crea occ ripetizioni di dato e aggiungi a stringa/lista
    se sonouguali, stampa compresso e CR
    altrimenti, stampa errore

'''


def compressRLE(originale):
    if len(originale) == 0:
        return ''
    compressa = ''
    occorrenze = 1
    valore = originale[0]

    for i in range(1, len(originale)):
        next = originale[i]
        if next == valore:
            occorrenze += 1
        else:
            compressa += f'{occorrenze}{valore}'
            occorrenze = 1
            valore = next

    compressa += f'{occorrenze}{valore}'
    return compressa
    


def decompressRLE(compressa):
    if len(compressa) % 2 != 0:
        return ''
    
    decompressa = ''
    for i in range(0,len(compressa), 2):
        occorrenze = int(compressa[i])
        sequenza = compressa[i+1] * occorrenze
        decompressa += sequenza

    return decompressa

def main():
    with open('stringhe.txt', 'r') as file:
        for line in file:
            originale = line.strip()
            compressa = compressRLE(originale)
            decompressa = decompressRLE(compressa)
            if originale == decompressa:
                print(f'CR: {len(originale)/len(compressa):.2f} output = {compressa}')


    pass

main()
