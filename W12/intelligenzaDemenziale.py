'''
-leggi libro e memroizza coppie parola, 5 parole succ + freqyuenti
- finchè utente non inserisce riga vuota
    leggi parola iniziale (se non prsente in elenco, una a c aso)
    genera un numero casuale N di parole del testo
    per ogni parola (fino a N)
        prendi a cas un successore
        stampalo
        parola = successore
'''

import string
from operator import itemgetter
import random

def leggiLibro(filename):
    coppie = {}

    # leggi file, normalizza e rimuovi punteggiatura
    with open(filename, 'r', encoding = 'utf-8') as file:
        libro = file.read().lower()

        for carattere in string.punctuation:
            libro = libro.replace(carattere, ' ')

    # dividi in parole
    parole = libro.strip().split()

    # per ogni coppia di parole
    for i in range(len(parole) - 1):
        (parola, successiva) = (parole[i], parole[i+1])
        if parola not in coppie:
            coppie[parola] = {successiva : 1}
        else:
            if successiva in coppie[parola]:
                coppie[parola][successiva] += 1
            else:
                coppie[parola][successiva] = 1

    for (parola, successori) in coppie.items():
        opzioni = sorted(successori.items(), reverse = True, key = itemgetter(1))
        coppie[parola] = opzioni[:5]

    return coppie


def main():
    coppie = leggiLibro('promessisposi.txt')
    finito = False

    while not finito:
        start = input('Parola: ')
        if start == '':
            finito = True
        else:
            frase = creaFrase(start, coppie, random.randint(5, 50))
            print(frase)

def parolaRandom(coppie):
    parole = list(coppie.keys())
    return parole[random.randint(0, len(parole) - 1)]

def creaFrase(start, coppie, lunghezza):
    if start not in coppie:
        start = parolaRandom(coppie)

    frase = start + ' '
    for i in range(lunghezza):
        # cerca prossima
        opzioni = coppie[start]
        idx = random.randint(0, len(opzioni) - 1)
        prossima = opzioni[idx][0]

        # aggiorna frase e parola corrente
        frase += prossima + ' '
        start = prossima

    return frase


main()