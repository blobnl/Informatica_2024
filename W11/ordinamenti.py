'''
leggere dati studenti, memorizzare mat nome cognome e ordinare per camèpo secondo scelta utente
'''


import operator
import csv

def leggiElenco(filename):
    elenco = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for studente in reader:
            record = {'matricola': studente['MATRICOLA'],
                        'nome': studente['NOME'],
                        'cognome': studente['COGNOME']}
            elenco.append(record)

    return elenco

def scegliFunzione():
    print('1. ordina per matricola')
    print('2. ordina per cognome')
    print('3. ordina per nome')
    print('4. esci')

    return int(input('inserire scelta: '))


def main():
    '''
    1. leggere elenco studenti
    2. fincheè non viene inserito uscita
        ordina per campo e stampa
    '''
    elenco = leggiElenco('14BHDWZ_2026.csv')
    
    finito = False
    while not finito:
        val = scegliFunzione()
        if val == 4:
            finito = True
        else:
            scelte = ['', 'matricola', 'cognome', 'nome']
            chiave = scelte[val]
            elenco.sort(key = operator.itemgetter(chiave))
            for studente in elenco[:10]:
                print(studente)



main()