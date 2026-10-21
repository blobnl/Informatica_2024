'''
creazione one-line di liste/contenitori a partire da contenitori...

Sintassi:
versione base:
[
    espressione(elemento)
    for elemento in contenitore
]

con selezione elementi del contenitore 
[
    espressione(elemento)
    for elemento in contenitore
    if condizione(elemento)
]

con più contenitori (lavora su tuple di valori)

[
    espressione(el1, el2)
    for el1 in contenitore1
    for el2 in contenitore2
    if condizione(el1, el2)
]

'''