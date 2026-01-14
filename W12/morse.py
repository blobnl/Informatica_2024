'''
leggi file dizionario e crea m2a a2m

per ogni riga file configurazione
    estrai comando e file
    se comando == c --> codifica file usando a2m
    se comando == d --> decodifica file usando m2a

codifica file:
risultato = ''
per ogni carattere in file
    se il carattere è in a2m
        decodifica il carattere e aggiungilo a risultato

decpodifica:
risultato = ''
per ogni riga del file
    estrai codici morse
    per ogni codice
        se codice in m2a -> decodifica codice e aggiungi a risultato



'''
def creaDizionari(filename):
    a2m = {}
    m2a = {}
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split()
            (ascii, morse) = (parti[0], parti[1])
            a2m[ascii] = morse
            m2a[morse] = ascii

    return (a2m, m2a)


def main():
    (a2m, m2a) = creaDizionari('morse.txt')
    # lettura file configurazione
    with open('comandi.txt', 'r') as file:
        for line in file:
            parti = line.strip().split()
            (comando, filename) = (parti[0], parti[1])
            if comando == 'c':
                risultato = codifica(filename, a2m)
                print(f'Codifica del file {filename}:\n{risultato}')
            elif comando == 'd':
                risultato = decodifica(filename, m2a)
                print(f'Deodifica del file {filename}:\n{risultato}')
            else:
                print(f'Errore nel file: {comando} -> comando non riconosciuto')


def codifica(filename, diz):
    risultato = ''
    with open(filename, 'r') as file:
        testo = file.read().strip()
        testo = testo.upper()
        for carattere in testo:
            if carattere in diz:
                risultato += diz[carattere] + ' '

    return risultato

def decodifica(filename, diz):
    risultato = ''
    with open(filename, 'r') as file:
        for line in file:
            codici = line.strip().split()
            for codice in codici:
                if codice in diz:
                    risultato += diz[codice]

    return risultato

main()