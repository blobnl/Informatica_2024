import string
from operator import itemgetter
from random import randint

def leggiTesto(filename):
    coppie = {}
    with open(filename, 'r', encoding = 'utf-8') as file:
        libro = file.read().lower()
        for char in string.punctuation:
            libro = libro.replace(char, ' ')

    # dividi in parole
    parole = libro.strip().split()

    # per ogni coppia di parole...
    for i in range(len(parole)-1):
        (parola, successiva) = (parole[i], parole[i+1])
        # aggiornare elenco coppie
        if parola not in coppie:
            coppie[parola] = {successiva : 1}
        else:
            if successiva in coppie[parola]:
                coppie[parola][successiva] += 1
            else:
                coppie[parola][successiva] = 1

    for parola in coppie:
        opzioni = sorted(coppie[parola].items(), key = itemgetter(1),
                         reverse = True)
        coppie[parola] = [item[0] for item in opzioni[:5]]

    return coppie

def creaFrase(parola, coppie, lunghezza):
    if parola not in coppie:
        parole = list(coppie.keys())
        parola = parole[randint(0, len(parole) - 1)]

    frase = parola
    for i in range(lunghezza):
        # seleziona succesore casuale
        opzioni = coppie[parola]
        successiva = opzioni[randint(0, len(opzioni) - 1)]
        frase += ' ' + successiva
        parola = successiva

    return frase


def main():
    coppie = leggiTesto('promessisposi.txt')

    #generazione frasi
    finito = False
    while not finito:
        parola = input('Parola iniziale: ')
        if parola == '':
            finito = True
            continue

        frase = creaFrase(parola, coppie, randint(5,50))
        print(frase)
    
main()