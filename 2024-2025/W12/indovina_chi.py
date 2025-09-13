'''
I/O
elenco personaggi
elenco domande

output
- elenco personaggi filtrti ad ogni domanda
- risutato finale

SD: lista di dizionari

leggi elenco di personaggi
per ogni domanda nel file
    filtarti = []
    per ogni personaggio
        se ha la cratteristica della domanda
            aggiungi personaggio a filtrati
    personaggi = filtrati

se il numero di personaggi rimanenti è 1
    giocatore ha vinto
altrimenti ha perso
'''

import csv

def leggiPersonaggi(filename):
    personaggi = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, delimiter = ';')
        for personaggio in reader:
            personaggi.append(personaggio)

    return personaggi

def stampaPersonaggi(frase, elenco):
    print(frase)
    for elemento in elenco:
        print(elemento)

def main():
    personaggi = leggiPersonaggi('personaggi.txt')
    # gioco
    stampaPersonaggi('Personaggi del gioco:', personaggi)

    with open('domande2.txt', 'r') as file:
        mossa = 1
        for line in file:
            (chiave, valore) = line.strip().split('=')
            print(f'Mossa {mossa} - domanda: {chiave} - {valore}')
            filtrati = []
            for p in personaggi:
                if p[chiave] == valore:
                    filtrati.append(p)

            stampaPersonaggi('Personaggi rimanenti:', filtrati)
            personaggi = filtrati
            mossa += 1

    if len(personaggi) == 1:
        print('Hai vinto!!!')
    else:
        print('Hai perso...')

main()