'''
1. leggere dati
    lista di tuple (label,value)
2. leggere cfg
    crea cfg di defulat
    per ogni chiave in cfg
        se max_bar_length -> assegna il valore intero
        esle assegna valore a chiave
3. stampare i dati
    - normalizzare i dati
        trova maxval
        per ogni coppia (label, value)
            len = round((value / maxval) * max_bar_lenght)
            memorizza (label, len, value)

    verifica se ordinare
    stampa titolo se presente
    per ogni elemento
        barra = bar_char * len
        se stampa val -> str_val = valore else str_val = ''
        stampa etichetta, barra str_val
)'''


import csv
from operator import itemgetter

def leggiDati(filename):
    dati = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            (label, value) = (row['label'], float(row['value']))
            dati.append((label,value))

    return dati

def leggiCfg(filename):
    cfg = {
        'max_bar_length': 50,
        'bar_char': '*',
        'show_values': 'true',
        'sort': '',
        'title': ''
    }

    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            parti = line.strip().split('=')
            (key,value) = (parti[0], parti[1])
            cfg[key] = value
            if key == 'max_bar_length':
                cfg[key] = int(value)

    return cfg

def main():
    dati = leggiDati('dati.csv')
    cfg = leggiCfg('config2.txt')

    norm = []
    maxTuple = max(dati, key = itemgetter(1))
    maxVal = maxTuple[1]

    for (label, value) in dati:
        len = round( (value/maxVal) * cfg['max_bar_length'] )
        norm.append( (label, len, value) )

    # ordinamento
    if cfg['sort'] == 'asc':
        norm.sort(reverse = False, key = itemgetter(2))
    elif cfg['sort'] == 'desc':
        norm.sort(reverse = True, key = itemgetter(2))

    # gestione titolo
    if cfg['title'] != '':
        print(cfg['title'])

    for (label, len, value) in norm:
        strVal = ''
        if cfg['show_values'] == 'true':
            strVal = str(value)

        barra = cfg['bar_char'] * len
        print(f'{label:20s}|{barra} {strVal}')

main()
