'''
input:
file con atleti, ompetizione e tempi

output:
per ogni competizione:
    numero atleti entro 10% tempo medio
    lista codici atleti con media ultime 3 prove in 3% TM
    totale atleti selezionati in tutte le competizioni al punto 1

ALGORITMO
1. leggi i dati, calcola per ogni competizione lista atleti, media tempi
    crea un dizionario (cod.comp: (lista atleti, t medio))
    atleta -> cod, media, last
1.5 totale selzionati = 0
2. per ogni competizione
    filtra i dati con regola 10% e aggiorna totale selzionati
3. per ogni competizione
    filtra dati su regola 3%
4. stampa totale selzionati punto 1

prove = {}
per ogni atleta
    leggi cod.atleta, cod.competizione, tempi
    vcalola media, last
    aggiungi a prova[cod.competizione] l'atleta (media, lst)
per ogni competizione
    tempo media = media tempi atleti



'''
def leggiAtleti(filename):
    # lettura dati...
    prove = {}
    with open(filename, 'r') as file:
        for line in file:
            (codice, gara, tempi) = line.strip().split(';')
            if gara not in prove:
                prove[gara] = {'media' : 0.0, 'atleti' : []}

            valTempi = [float(valore)  for valore in tempi.split(',')]

            atleta = {'codice' : codice,
                        'media' : sum(valTempi) / len(valTempi),
                        'last3' : sum(valTempi[-3:]) / 3 }
            
            prove[gara]['atleti'].append(atleta)
            prove[gara]['media'] += atleta['media']

    for gara in prove:
        prove[gara]['media'] /= len(prove[gara]['atleti'])

    return prove

def delta(time, rif):
    return abs((time - rif) / rif)

def main():
    prove = leggiAtleti('atleti.txt')
    #print(prove)

    sel = 0
    tot = 0
    # per ogni competizione calcola num atleti in 10% e 3%
    for gara in sorted(prove):
        atleti = prove[gara]['atleti']
        mediaGara = prove[gara]['media']
        tabella = [5, 10, 20, 40]

        cont10 = 0
        lista3 = []

        for atleta in atleti:
            if delta(atleta['media'], mediaGara) < 0.1:
                cont10 += 1
            if delta(atleta['last3'], mediaGara) < 0.03:
                lista3.append(atleta['codice'])

        print(f'Gli atleti per la gara {tabella[int(gara)]}km sono {cont10}')
        print(f'Gli atleti nel 3% sono {lista3}\n')

        sel += cont10
        tot += len(atleti)

    print(f'In totlae gli atleti selezioni sono stati {sel} su {tot} (sel/tot*100:.2f)')

main()