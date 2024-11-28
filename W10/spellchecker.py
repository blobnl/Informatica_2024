'''
scrivere un programma che dato un dizionario (che contiene l'elenco di parole scritte correttamente
in una determinata lingua, con ogni parola scritta in un'unica riga) legga un testo, e 
stampi in output l'elenco di parole del testo che non sono scritte in maniera corretta 
(i.e., che non appartengono al dizionario)

ALGORITMO:
----------

??

'''

def estraiParole(riga):
    parole = [parola.strip(',.;:-_!?"()') for parola in riga.strip().split()]
    '''    
    parole = []
    words = riga.strip().split()
    for parola in words:
        parola = parola.strip(',.;:-_!?"')
        parole.append(parola)
    '''

    return parole

def leggiDizionario(filename):
    dizionario = set()
    with open(filename, 'r') as file:
        for parola in file:
            dizionario.add(parola.strip().lower())

    return dizionario

def main():
    # leggo dizionario in set
    dizionario = leggiDizionario('words')
    # opzione a cerco parole nel testo e le confronto col dizionario
    '''
    with open('alice30.txt', 'r') as file:
        for line in file:
            parole = estraiParole(line)
            for parola in parole:
                if parola.lower() not in dizionario:
                    print(parola)
    '''
    testo = set()
    with open('alice30.txt', 'r') as file:
        for line in file:
            parole = estraiParole(line)
            for parola in parole:
                testo.add(parola.lower())

    sbagliate = testo.difference(dizionario)
    for parola in sbagliate:
        print(parola)

    pass

main()