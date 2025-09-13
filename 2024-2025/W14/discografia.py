'''
input
- lenco artisti
- per ogni artista, elenco ei brani

output
- per ogni anno in ordine di anno
    elenco canzoni

elemco = {}
per ogin artista
    eggi codice, file
    per ogni canzone in file
        aggiungi in elenco[anno] titolo e codice artista

stmapa elenco
'''

def leggiDB(filename):
    elenco = {}
    with open(filename, 'r') as file:
        for line in file:
            (codice, fileArtista) = line.strip().split(';')
            with open(fileArtista, 'r') as elencoBrani:
                for brano in elencoBrani:
                    (anno, titolo) = brano.strip().split(';')
                    if anno not in elenco:
                        elenco[anno] = [(titolo, codice)]
                    else:
                        elenco[anno].append((titolo, codice))

    return elenco

def main():
    elenco = leggiDB('artisti.txt')
    for anno in sorted(elenco):
        lista = elenco[anno]
        print(f'{anno}:')
        for brano in lista:
            print(f'{brano[0]:40s}{brano[1]}')
main()