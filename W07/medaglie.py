RIGHE = 4
COLONNE = 3

medaglie = []
for i in range(RIGHE):
    riga = [0] * COLONNE
    medaglie.append(riga)



medaglie = [
    [0, 1, 0],
    [1, 4, 7],
    [4, 0, 5],
    [0, 0, 1]
]

righe = len(medaglie)
colonne = len(medaglie[0])

for r in range(righe):
    # stampa la r-esima riga
    for c in range(colonne):
        #tsampare elemnto (r,c)
        print(f'{medaglie[r][c]:4}', end = '')

    print()

for r in range(righe):
    print(f'Nazione {r}: medaglie = {sum(medaglie[r])}')

for c in range(colonne):
    totale = 0
    for r in range(righe):
        totale += medaglie[r][c]

    print(f'Medgalie {c} = {totale}')