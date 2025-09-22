import csv
import operator

def leggiFile(nomeFile):
    # apri il file e leggi il contenuto del csv con una funzione apposita che divide i campi
    file = open(nomeFile, 'r')
    reader = csv.reader(file)

    # crea un dizionario vuoto
    freq = {}
    primaRiga = True

    for line in reader:
        # salta la prima riga (che contiene l'intestazione del file)
        if primaRiga:
            primaRiga = False
        else:
            # estrazione nome dalla riga (ogni riga è una lista dei campi contenuti nel file)
            nome = line[2]
            # se il nome è nel dizionario, incrementa la frequenza, altrimenti aggiungilo con frequenza 1
            if nome in freq:
                freq[nome] += 1
            else:
                freq[nome] = 1

    file.close()
    return freq

def ordina(freq):
    # estrai una lista di item (chiave, valore) dal dizionario 
    lista = list(freq.items())
    # e ordinalo in ordine decrescente di valore (frequenze...) e nome (2 chiavi)
    lista.sort(key=operator.itemgetter(1), reverse = True)
    return lista


def stampa(lista, posizioni):
    for i in range(posizioni):
        print(f'{lista[i][0]:20s} {lista[i][1]:2d}')
        #print(lista[i])


def main():
    # dichiarazioni costanti
    FILENAME = "14BHDWZ_2026.csv"
    DA_STAMPARE = 10

    # leggi il file, calcolando le frequenze (contenute in un dizionario (nome, frequenza)
    frequenze = leggiFile(FILENAME)
    # ottieni una lista ordinata di coppie (nome, frequenza)
    lista = ordina(frequenze)
    # stampa i primi n elementi della lista
    stampa(lista, DA_STAMPARE)


main()
