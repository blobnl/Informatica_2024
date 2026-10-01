'''
data la lunghezza del muro e della piastrella, e che la fila parte da
nera e finisce con nera, calcolare:
- numero piastrelle per riga
- sapzio rimanente ai bordi (simmetrico)

ALGORITMO:
numeroP = largMuro // larghP
se numeroP è pari
    decrementa numeroP
    
stampa numroP
sapzioLati = (lungMuro - numP * lrghP) / 2

'''

LARGHEZZA_MURO = 200
LARGHEZZA_PIASTRELLA = 6

numPiatsrelle = LARGHEZZA_MURO // LARGHEZZA_PIASTRELLA
if numPiatsrelle % 2 == 0:
    numPiatsrelle = numPiatsrelle - 1
    #numPiatsrelle -= 1
    
print("Piastrelle =", numPiatsrelle)
spazio = (LARGHEZZA_MURO - numPiatsrelle * LARGHEZZA_PIASTRELLA) / 2
print("Spazio ai lati:", spazio)
    