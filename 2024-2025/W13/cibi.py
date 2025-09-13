'''
INPUT
-> file della ricetta (ingredienti e qtà)
+ istruzioni preparazione

OUTPUT
- lista ingredienti
- numero ingredienti
- costo ricetta
- calorie ricetta

ALGORITMO
1. estrarre gli ingredienti dal file della ricetta
    sezIngredienti = False
    ingredienti = []
    per ogni linea del file
        se la linea contiene Ingredienti
            metti sezIngredienti a True
            continua la lettura
        se la linea contiene Procedimento
            metti sezIngredeinti a False
            termina la lettura
        se sono in sezIngredienti
            estrai nome e quantità e memorizza in ingredienti

2. stampare elenco ingredienti

3. calcolare costo e calorie
    leggere l'elenco dei cibi -> dizionario
    costo = 0, calorie = 0
    per ogni ingrediente della ricetta
        aggiorna il costo -> costo/kg ingrediente * (grammi/1000)
        aggiorna le calorie -> calorie/kg inghrediente * (grammi/1000)

'''

def leggiRicetta(filename):
    sezIngredienti = False
    ingredienti = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()

                if 'Ingredienti' in line:
                    sezIngredienti = True
                    continue
                if 'Procedimento' in line:
                    sezIngredienti = False
                    break
                if sezIngredienti and len(line) != 0:
                    parts = line.split(';')
                    ingrediente = {'nome' : parts[0], 'quantita' : float(parts[1])}
                    ingredienti.append(ingrediente)

    except:
        print('Errore nella lettura del file')

    return ingredienti

def leggiElencoCibi(filename):
    cibi = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                cibi[parts[0]] = {'costo' : float(parts[1]), 'calorie': float(parts[2])}
    except:
        print('Errore in lettura elenco dei cibi')

    return cibi

def main():
    ingredienti = leggiRicetta('fusilli_alle_olive.txt')
    
    print('Ingredienti:')
    for i in ingredienti:
        print(f"{i['nome']:20} - {i['quantita']:.1f}")

    print(f'\nNumero ingredienti: {len(ingredienti)}')
    cibi = leggiElencoCibi('cibi.txt')
    costo = 0
    calorie = 0

    for i in ingredienti:
        cibo = cibi[i['nome']]
        costo += cibo['costo'] * i['quantita'] / 1000
        calorie += cibo['calorie'] * i['quantita'] / 1000

    print(f'Costo ricetta: {costo:.2f}\nCalorie ricetta: {calorie:.2f}')

main()