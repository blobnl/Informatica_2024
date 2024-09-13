import csv
import operator

def leggiFile(nomeFile):
    # apri il file e leggi il contenuto del csv con una funzione apposita che divide i campi
    file = open(nomeFile, 'r')
    reader = csv.reader(file)

    # crea un dizionario vuoto (nomi,occorrenze)
    freq = {}
    primaRiga = True

    for line in reader:
        # salta la prima riga (che contiene l'intestazione del file)
        if primaRiga:
            primaRiga = False
        else:
            # estrazione nome dalla riga (ogni riga è una lista dei campi contenuti nel file)
            nome = line[2]
            # se il nome è nel dizionario, incrementa la frequenza
            if nome in freq:
                freq[nome] = freq[nome] + 1
            else:
                # altrimenti aggiungilo con frequenza 1    
                freq[nome] = 1

    file.close()
    return freq

def ordina(freq):
    # estrai una lista di item dal dizionario e ordinalo in ordine crescente
    lista = list(freq.items())
    #lista.sort(key=lambda x:x[1], reverse = True)
    lista.sort(key=operator.itemgetter(1), reverse = True)
    return lista


def stampa(lista, posizioni):
    for i in range(posizioni):
        print(f'{lista[i][0]:20} {lista[i][1]}')
        #print(lista[i])

# Press the green button in the gutter to run the script.
def main():
    # dichiarazioni costanti
    FILENAME = "14BHDLZ_2022.csv"
    DA_STAMPARE = 10

    # leggi il file, calcolando le frequenze (contenute in un dizionario (nome, frequenza)
    frequenze = leggiFile(FILENAME)
    # ottieni una lista ordinata di coppie (nome, frequenza)
    lista = ordina(frequenze)
    # stampa i primi n elementi della lista
    stampa(lista, DA_STAMPARE)


main()
