'''
rucerca di tutte le occorrenze che verificano una proprietà
'''

soglia = 10
insieme = [1, 4, 6, -4, -40, 12, 4, 6, 24, 18]

indiciTrovati = []
for (indice, elemento) in enumerate(insieme):
    # verifica propetà
    if elemento < soglia:
        indiciTrovati.append(indice)

if indiciTrovati != []:
    print(indiciTrovati)
else:
    print("nessun dato trovato")