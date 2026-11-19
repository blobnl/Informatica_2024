'''
Controllare il corretto ‘spelling’ di un documento, stampando tutte le parole 
che non compaiono in un apposito dizionario
Dati:
words: file di testo contenente le parole corrette (una per riga)
alice30.txt: file di testo libero contenente un racconto (in questo caso 
il libro Alice nel Paese delle Meraviglie)
Stampare tutte le parole del documento che non si trovano tra 
le parole corrette

ALGORITMO:
- leggi dizionario
- leggin insieme parole
- aprle scorrette = differnza tra insiemi
- stampat parole scorrette (ordinate)

'''

import string

#print(string.punctuation)

def leggiDizionario(filename):
    dizionario = set()
    with open(filename) as file:
        for parola in file:
            parola = parola.strip()
            dizionario.add(parola.lower())
            
    return dizionario

def leggiTesto(filename):
    paroleUniche = set()
    with open(filename) as file:
        for riga in file:
            parole = riga.strip().split()
            for parola in parole:
                parola = parola.strip(string.punctuation)
                paroleUniche.add(parola)
                
    return paroleUniche
            
def controllaTesto(filename, dizionario):
    with open(filename) as file:
        for riga in file:
            parole = riga.strip().split()
            for parola in parole:
                parola = parola.strip(string.punctuation)
                # controlla se corretta o meno
                if parola.lower() not in dizionario:
                    print(parola) 


def main():
    FILE_DIZIONARIO = 'words'
    FILE_TESTO = 'alice30.txt'
    
    dizionario = leggiDizionario(FILE_DIZIONARIO)
    testo = leggiTesto(FILE_TESTO)
    
    controllaTesto(FILE_TESTO, dizionario)
    '''
    paroleSbagliate = testo.difference(dizionario)
    
    for parola in sorted(paroleSbagliate):
        print(parola)
    '''

main()